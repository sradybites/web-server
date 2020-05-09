# Update Player

Update the Player of the Authenticated User if and only if they are Owner (authentication coming soon).

**URL** : `/api/players/<int:id>/`

**Method** : `PUT`

**Auth required** : TBD

**Permissions required** : User is Account Owner

**Data constraints**

```json
{
    "new_name": "[unicode 15 chars max]",
}
```

**Data example** Partial data is allowed, but there is only one field.

```json
{
    "new_name": "Srady Bites",
}
```

## Success Responses

**Condition** : Update can be performed either fully or partially by the Owner
of the Player.

**Code** : `201 OK`

**Content example** : For the example above, when the 'new_name' is updated and
posted to `/api/players/1/`...

```json
{
    "success": true,
    "data": {
        "username": "sradybites",
        "name": "Srady Bites",
        ...
    }
}
```

## Error Response

**Condition** : Player's name already matches specified parameter.

**Code** : `400 BAD REQUEST`

**Content** :
```json
{
    "success": false,
    "error": "Choose a name different from your current one"
}
```