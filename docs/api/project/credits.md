# Show List of Credits

Shows a list of credits for the given project.

**URL** : `/api/project/{project}/credits`

**URL Parameters** :

- `project` where an integer value corresponds to a Project ID

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data**: `{}`

## Success Response

**Condition** : If zero credits exist for the given project.

**Code** : `200 OK`

**Content example**

```json
[]
```

### Or

**Condition** : If one or more credits exist for the given project.

**Code** : `200 OK`

**Content example**

```json
[
    {
        "action": "A credit",
        "collaborator": {
            "name": "Human Name",
            "url": "https://bbncreative.co",
            "twitter": "@bbncreative"
        }
    }
]
```

## Error Responses

**Condition** : If the given project does not exist.

**Code** : `404 Not Found`

**Content example**

```json
{
    "detail": "Not found."
}
```
