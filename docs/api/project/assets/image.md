# Show Image Assets

Shows a list of image assets for the given project.

**URL** : `/api/project/{project}/assets/image/`

**URL Parameters** :

- `project` where an integer value corresponds to a Project ID

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data**: `{}`

## Success Response

**Condition** : If zero image assets exist for the given project.

**Code** : `200 OK`

**Content example**

```json
[]
```

### Or

**Condition** : If one or more image assets exist for the given project.

**Code** : `200 OK`

**Content example**

```json
[
    {
        "id": 2,
        "parent": 1,
        "created_at": "2020-01-05T19:28:24.045546Z",
        "title": "Asset Title",
        "body": "Asset Body Text",
        "importance": 0,
        "content": {
            "src": "http://domain:port/media/uuid/example.gif",
            "alt": "Alternative Text",
            "ratio": "W1"
        }
    },
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
