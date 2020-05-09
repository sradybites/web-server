# Show All Guilds

Show all Guilds. Includes the Player's guild, if they have one.

**URL** : `/api/guilds/`

**Method** : `GET`

**Auth required** : TBD

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Condition** : User can not see any Guilds.

**Code** : `200 OK`

**Content** :
```json
{
    "success": true,
    "data": []
}
```

### OR

**Condition** : User can see one or more Guilds.

**Code** : `200 OK`

**Content** : In this example, the User can see one Guild:

```json
{
    "success": true,
    "data": [
        {
            "name": "Garlic Parmesan",
            "members": [
                {
                    "username": "sradybites",
                    "name": "Srady Bites"
                }
            ]
        }
    ]
}
```