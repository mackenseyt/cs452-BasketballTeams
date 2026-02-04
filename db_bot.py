import json
from openai import OpenAI
import os
import sqlite3
from time import time

print("Running db_bot.py!")

fdir = os.path.dirname(__file__)
def getPath(fname):
    return os.path.join(fdir, fname)

# SQLITE
sqliteDbPath = getPath("basketball.sqlite")
setupSqlPath = getPath("setup.sql")
setupSqlDataPath = getPath("setupData.sql")

# Erase previous db
if os.path.exists(sqliteDbPath):
    os.remove(sqliteDbPath)

sqliteCon = sqlite3.connect(sqliteDbPath)  # create new db
sqliteCursor = sqliteCon.cursor()
with (
        open(setupSqlPath) as setupSqlFile,
        open(setupSqlDataPath) as setupSqlDataFile
    ):

    setupSqlScript = setupSqlFile.read()
    setupSQlDataScript = setupSqlDataFile.read()

sqliteCursor.executescript(setupSqlScript)  # setup tables and keys
sqliteCursor.executescript(setupSQlDataScript)  # setup data

def runSql(query):
    result = sqliteCursor.execute(query).fetchall()
    return result

# OPENAI
configPath = getPath("config.json")
print(configPath)
with open(configPath) as configFile:
    config = json.load(configFile)

openAiClient = OpenAI(api_key=config["openaiKey"])
openAiClient.models.list()  # check if the key is valid (update in config.json)

def getChatGptResponse(content):
    stream = openAiClient.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )

    responseList = []
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            responseList.append(chunk.choices[0].delta.content)

    result = "".join(responseList)
    return result


# strategies
commonSqlOnlyRequest = " Give me a sqlite select statement that answers the question. Only respond with sqlite syntax. If there is an error do not explain it!"
strategies = {
    "zero_shot": setupSqlScript + commonSqlOnlyRequest,
    "single_domain_few_shot": (setupSqlScript +
                   " How many wins does each team have? " +
                   " \nSELECT t.name, w.win_count\nFROM teams t\nLEFT JOIN wins w ON t.team_id = w.team_id\nORDER BY w.win_count DESC;\n " +
                   commonSqlOnlyRequest)
}

questions = [
    "What are the names of all players on the BYU Cougars?",
    "Which team has the most wins this season?",
    "What arena does Purdue play in?",
    "Show me all teams and their win counts"
]

def sanitizeForJustSql(value):
    gptStartSqlMarker = "```sql"
    gptEndSqlMarker = "```"
    if gptStartSqlMarker in value:
        value = value.split(gptStartSqlMarker)[1]
    if gptEndSqlMarker in value:
        value = value.split(gptEndSqlMarker)[0]

    return value

for strategy in strategies:
    responses = {"strategy": strategy, "prompt_prefix": strategies[strategy]}
    questionResults = []
    print("########################################################################")
    print(f"Running strategy: {strategy}")
    # for question in questions:
    question = input("What would you like to know about the database?\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Question:")
    print(question)
    error = "None"
    sql_response = "None"
    query_raw_response = "None"
    friendly_response = "None"
    
    try:
        getSqlFromQuestionEngineeredPrompt = strategies[strategy] + " " + question
        sqlSyntaxResponse = getChatGptResponse(getSqlFromQuestionEngineeredPrompt)
        sqlSyntaxResponse = sanitizeForJustSql(sqlSyntaxResponse)
        sql_response = sqlSyntaxResponse
        print("SQL Syntax Response:")
        print(sqlSyntaxResponse)
        queryRawResponse = str(runSql(sqlSyntaxResponse))
        query_raw_response = queryRawResponse
        print("Query Raw Response:")
        print(queryRawResponse)
        friendlyResultsPrompt = "I asked a question \"" + question + "\" and the response was \"" + queryRawResponse + "\" Please, just give a concise response in a more friendly way? Please do not give any other suggestions or chatter."
        friendlyResponse = getChatGptResponse(friendlyResultsPrompt)
        friendly_response = friendlyResponse
        print("Friendly Response:")
        print(friendlyResponse)
    except Exception as err:
        error = str(err)
        print(err)

    questionResults.append({
        "question": question,
        "sql": sql_response,
        "queryRawResponse": query_raw_response,
        "friendlyResponse": friendly_response,
        "error": error
    })

    responses["questionResults"] = questionResults

    with open(getPath(f"response_{strategy}_{time()}.json"), "w") as outFile:
        json.dump(responses, outFile, indent=2)


sqliteCursor.close()
sqliteCon.close()
print("Done!")