# Show Embedded Assets

Shows a list of embedded assets for the given feed.

**URL** : `/api/feed/{feed}/assets/embedded/`

**URL Parameters** :

- `feed` where an integer value corresponds to a Feed ID

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data**: `{}`

## Success Response

**Condition** : If zero embedded assets exist for the given feed.

**Code** : `200 OK`

**Content example**

```json
[]
```

### Or

**Condition** : If one or more embedded assets exist for the given feed.

**Code** : `200 OK`

**Content example**

```json
[
    {
        "id": 1,
        "parent": 2,
        "created_at": "2020-03-11T23:16:29.607315Z",
        "title": "Asset Title",
        "body": "Asset Body Text",
        "importance": 0,
        "content": {
            "code": "<iframe width=\"560\" height=\"315\" src=\"{content_source}\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>",
            "ratio": "VL"
        }
    }
]
```

## Error Responses

**Condition** : If the given feed does not exist.

**Code** : `404 Not Found`

**Content example**

```json
{
    "detail": "Not found."
}
```
