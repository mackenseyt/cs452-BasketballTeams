# College Basketball

My project models data for college basketball teams. Includes team information, player rosters, arenas, and win records for the 2025-2026 season.

![Schema Diagram](schema.png)

## Query I Thought It Did Well On

**Question**: What are the names of all players on the BYU Cougars?

**GPT SQL Response**:

```sql
SELECT p.player_name
FROM players p
JOIN teams t ON p.team_id = t.team_id
WHERE t.name = 'BYU Cougars';
```

**Friendly Response**: Jaxson Robinson, Dallin Hall, Trevin Knell, Fousseyni Traore, Aly Khalifa

## Question That It Tripped Up On

**Question**:

**GPT SQL Response**:

```sql

```

**SQL Result**: ``

**Friendly Response**:

ksjdfhs

askdjf

## Multi-Shot Attempt

I provided an example of a successful query and asked the same question again with few-shot prompting.

**Question (multi-shot)**:

**SQL Result**: ``

**Friendly Response**:

**Question (multi-shot)**:

**SQL Result**: ``

**Friendly Response**:
zdskjfhsd

## Conclusion

For college basketball data queries, GPT-4 does very well at generating SQL for simple to moderately complex joins. The key finding is that result interpretation and friendly response generation improves significantly with few-shot examples.

Main strengths:

- Simple SELECT queries work reliably
- JOINs across multiple tables are handled well
- WHERE clauses and filtering work correctly

Main weaknesses:

- Without examples, friendly responses can be generic or incomplete
- Result interpretation requires better context
- Zero-shot prompting often misses relevant context

**Prompting strategies tested**: Zero-shot, Few-shot/Multi-shot
**Best approach found**: Few-shot examples improve both SQL quality and result interpretation
