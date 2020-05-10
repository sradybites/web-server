# Show a Guild

Show Guild at specified URL.

**URL** : `/api/players/:guild_id/`

**Method** : `GET`

**Auth required** : TBD

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Condition** : User can see the Guild.

**Code** : `200 OK`

**Content** : In this example, the User can see the Guild at `/api/guilds/1/`:

```json
{
    "success": true,
    "data": {
        "name": "Garlic Parmesan",
        "members": [
            {
                "username": "sradybites",
                "name": "Srady Bites"
            }
        ]
    }
}
```

## Failure Responses

**Condition** : Guild at specified URL does not exist.

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "success": false,
    "error": "Guild not found"
}
```