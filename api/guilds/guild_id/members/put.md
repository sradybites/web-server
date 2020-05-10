# Add Player to Guild

Authenticated User adds specified Player to Guild, if User is the Leader (authentication coming soon).

**URL** : `/api/guilds/:guild_id/members/`

**Method** : `PUT`

**Auth required** : TBD

**Permissions required** : User is Guild Leader

**Data constraints**

```json
{
    "player_id": "[integer]",
}
```

**Data example**

```json
{
    "player_id": "3",
}
```

## Success Responses

## Error Response