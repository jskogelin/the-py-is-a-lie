## The Py Is a Lie
Python based backend faker.

Reads pylie.json to understand what data to return from its routes

A route is described as:
```json
{
  "base": "http://localhost:8080",
  "routes": {
    "/my/route": {
      "range": [40, 70],
      "data": {
        "id": "__id__",
        "name": "__fullname__",
        "type": "just some string"
      }
    }
  }
}
```

## Todo
* Tests
* Everything else
