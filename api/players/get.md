# Show All Players

Show all Players. Includes their own Player profile if they have one.

**URL** : `/api/players/`

**Method** : `GET`

**Auth required** : TBD

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Condition** : User can not see any Players.

**Code** : `200 OK`

**Content** :
```json
{
    "success": true,
    "data": []
}
```

### OR

**Condition** : User can see one or more Players.

**Code** : `200 OK`

**Content** : In this example, the User can see two Players:

```json
{
    "success": true,
    "data": [
        {
            "username": "sradybites",
            "name": "Brady Sites",
            "guild": {
                "name": "Garlic Parmesan",
                "members": [
                    {
                        "username": "sradybites",
                        "name": "Brady sites"
                    }
                ]
            },
            "match_hist": [
                {
                    "status": 0,
                    "winner": null
                }
            ]
        },
        {
            "username": "byst0",
            "name": null,
            "guild": null,
            "match_hist": []
        }
    ]
}
```