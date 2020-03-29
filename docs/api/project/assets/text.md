# Show Text Assets

Shows a list of text assets for the given project.

**URL** : `/api/project/{project}/assets/text/`

**URL Parameters** :

- `project` where an integer value corresponds to a Project ID

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data**: `{}`

## Success Response

**Condition** : If zero text assets exist for the given project.

**Code** : `200 OK`

**Content example**

```json
[]
```

### Or

**Condition** : If one or more text assets exist for the given project.

**Code** : `200 OK`

**Content example**

```json
[
    {
        "id": 1,
        "parent": 2,
        "created_at": "2020-02-09T17:19:46.936900Z",
        "title": "Placeholder asset",
        "body": "Text content goes here",
        "importance": 0
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
