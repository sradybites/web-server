# Show a Player

Show Player at specified URL.

**URL** : `/api/players/<int:player_id>/`

**Method** : `GET`

**Auth required** : TBD

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Condition** : User can see the Player.

**Code** : `200 OK`

**Content** : In this example, the User can see the Player at `/api/players/1/`:

```json
{
    "success": true,
    "data": {
        "username": "sradybites",
        "name": "Srady Bites",
        "guild": {
            "name": "Garlic Parmesan",
            "members": [
                {
                    "username": "sradybites",
                    "name": "Srady Bites"
                }
            ]
        },
        "match_hist": [
            {
                "status": 0,
                "winner": null
            }
        ]
    }
}
```

## Failure Responses

**Condition** : Player at specified URL does not exist.

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "success": false,
    "error": "Player not found"
}
```