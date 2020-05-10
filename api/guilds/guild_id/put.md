# Update Guild

Update the Guild of the Authenticated User if and only if they are Leader (authentication coming soon).

**URL** : `/api/guilds/:guild_id/`

**Method** : `PUT`

**Auth required** : TBD

**Permissions required** : User is Guild Leader

**Data constraints**

```json
{
    "new_name": "[unicode 15 chars max]",
}
```

**Data example** Partial data is allowed, but there is only one field.

```json
{
    "new_name": "The Best Guild",
}
```

## Success Responses

**Condition** : Update can be performed either fully or partially by the Leader
of the Guild.

**Code** : `201 OK`

**Content example** : For the example above, when the 'new_name' is updated and
posted to `/api/guilds/1/`...

```json
{
    "success": true,
    "data": {
        "name": "The Best Guild",
        ...
    }
}
```

## Error Response

**Condition** : A Guild exists with that name already.

**Code** : `422 BAD REQUEST`

**Content** :
```json
{
    "success": false,
    "error": "Guild name already in use"
}
```