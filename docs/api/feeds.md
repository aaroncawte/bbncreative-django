# Show List of Feeds

Shows a list of all feeds and metadata.

**URL** : `/api/feeds/`

**URL Parameters** :
- `permanent` where a boolean value filters permanent feeds
- `protected` where a boolean value filters protected feeds

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data**: `{}`

## Success Response

**Condition** : If zero feeds exist.

**Code** : `200 OK`

**Content example**

```json
[]
```

### Or

**Condition** : If one or more feeds exist.

**Code** : `200 OK`

**Content example**

```json
[
    {
        "id": 1,
        "name": "Regular Feed",
        "shortName": "Regular Feed",
        "description": "Sample feed with no special properties to test the bbncreative API",
        "slug": "regular-feed",
        "lastUpdated": "2020-02-29T12:25:10.437185Z",
        "icon": {
            "faName": "regular"
        },
        "protected": false,
        "permanent": false,
        "images": {
            "hero": null
        },
        "colors": {
            "primary": "e8185f",
            "secondary": "ff1a36"
        }
    }
]
```
