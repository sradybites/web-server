# Delete User's Player

Delete the Player of the Authenticated User if they are Owner (authentication coming soon).

**URL** : `/api/accounts/:player_id/`

**URL Parameters** : `player_id=[integer]` where `player_id` is the ID of the Player in the
database.

**Method** : `DELETE`

**Auth required** : YES (UNDER CONSTRUCTION)

**Permissions required** : User is Player Owner

**Data** : `{}`

## Success Response

**Condition** : If the Player exists.

**Code** : `204 NO CONTENT`

**Content** : `{}`

## Error Responses

**Condition** : If there was no Player available to delete.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
    "success": false,
    "error": "Player not found"
}
```

### Or

**Condition** : Authorized User is not Owner of Account at URL.

**Code** : `403 FORBIDDEN`

**Content** : `{}`

###### Note: Authentication still TODO