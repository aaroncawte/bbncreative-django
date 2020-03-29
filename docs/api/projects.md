# Show List of Projects

Shows a list of all projects and metadata.

**URL** : `/api/projects/`

**URL Parameters** : `is_complete` where a boolean value filters on the completion status

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data**: `{}`

## Success Response

**Condition** : If zero projects exist.

**Code** : `200 OK`

**Content example**

```json
[]
```

### Or

**Condition** : If one or more projects exist.

**Code** : `200 OK`

**Content example**

```json
[
    {
        "id": 1,
        "name": "New Project",
        "shortName": "New Project",
        "description": "[Project Bio]",
        "slug": "new-project",
        "progress": {
            "complete": true,
            "date": "2020-03-29"
        },
        "clientName": "New Client",
        "images": {
            "icon": "http://domain:port/media/example.png",
            "hero": "http://domain:port/media/example.jpg"
        },
        "colors": {
            "primary": "455a64",
            "secondary": "234234"
        },
        "callToAction": {
            "label": "Go to Website",
            "url": "https://bbncreative.co"
        }
    }
]
```
