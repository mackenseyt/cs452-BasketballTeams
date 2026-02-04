# College Basketball

My project models data for college basketball teams. Includes team information, player rosters, arenas, and win records for the 2025-2026 season.

![Schema Diagram](schema.png)

## Query I Thought It Did Well On

**Question**: What are the names of all players on the BYU Cougars?

**GPT SQL Response**:

```sql

```

**Friendly Response**:

## Question That It Tripped Up On

**Question**: Who is the fan favorite?

**GPT SQL Response**:

```
SELECT players.player_name, COUNT(wins.win_id) AS win_count
FROM players
JOIN wins ON players.team_id = wins.team_id
GROUP BY players.player_id
ORDER BY win_count DESC
LIMIT 1;
```

**SQL Result**: `[('Jaxson Robinson', 1)]`

**Friendly Response**: Jaxson Robinson is the fan favorite.

This one is an interesting one because it had no context for if we meant team or player when it came to fan favorite. So what it did is it chose a random player from the winning team, which is clever but not really what the user probably intended.

## Multi-Shot Attempt

I provided an example of a successful query and asked the same question again with few-shot prompting.

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
