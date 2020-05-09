# Create a Guild

Create a Guild.

**URL** : `/api/guilds/`

**Method** : `POST`

**Auth required** : TBD

**Permissions required** : None

**Data constraints**

Provide name of Guild to be created.

```json
{
    "name": "[unicode 15 chars max]"
}
```

**Data example** All fields must be sent.

```json
{
    "name": "The Boys"
}
```

## Success Response

**Condition** : If everything is OK and a Guild didn't exist with this name.

**Code** : `201 CREATED`

**Content example**

```json
{
    "success": true,
    "data": {
        "name": "The Boys",
        "members": []
    }
}
```

## Error Responses

**Condition** : If Guild already exists with given name.

**Code** : `422 UNPROCESSABLE ENTITY`

**Content** :
```json
{
    "success": false,
    "error": "Guild name taken"
}
```

### Or

**Condition** : If name does not meet data constraints.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "success": false,
    "error": "Invalid name"
}
```