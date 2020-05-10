# Remove Player from Guild

Authenticated User removes specified Player from Guild, if User is the Leader (authentication coming soon).

**URL** : `/api/guilds/:guild_id/members/`

**Method** : `DELETE`

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

**Code** : `204 NO CONTENT`

## Error Response

**Code** : `422 UNPROCESSABLE ENTITY`