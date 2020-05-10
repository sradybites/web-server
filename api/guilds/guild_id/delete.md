# Delete Guild

Delete the Guild.

**URL** : `/api/guilds/:guild_id/`

**URL Parameters** : `guild_id=[integer]` where `guild_id` is the ID of the Guild in the
database.

**Method** : `DELETE`

**Auth required** : YES (UNDER CONSTRUCTION)

**Permissions required** : User is Guild Leader

**Data** : `{}`

## Success Response

**Condition** : If the Guild exists.

**Code** : `204 NO CONTENT`

**Content** : `{}`

## Error Responses

**Condition** : If there was no Guild available to delete.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
    "success": false,
    "error": "Guild not found"
}
```

### Or

**Condition** : Authorized User is not Leader of Guild at URL.

**Code** : `403 FORBIDDEN`

**Content** : `{}`

###### Note: Authentication still TODO