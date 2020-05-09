# Create User's Player

Create a Player for the User.

**URL** : `/api/players/`

**Method** : `POST`

**Auth required** : TBD

**Permissions required** : None

**Data constraints**

Provide username of Player to be created.

```json
{
    "username": "[unicode 10 chars max]"
}
```

**Data example** All fields must be sent.

```json
{
    "username": "doglover01"
}
```

## Success Response

**Condition** : If everything is OK and a Player didn't exist with this username.

**Code** : `201 CREATED`

**Content example**

```json
{
    "success": true,
    "data": {
        "username": "doglover01",
        "name": null,
        "guild": null,
        "match_hist": []
    }
}
```

## Error Responses

**Condition** : If Player already exists with given username.

**Code** : `422 UNPROCESSABLE ENTITY`

**Content** :
```json
{
    "success": false,
    "error": "Username is taken"
}
```

### Or

**Condition** : If username does not meet data constraints.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "success": false,
    "error": "Invalid username"
}
```