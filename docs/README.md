# API Documentation

## Overview

`wekan-api` provides a RESTful, HTTP API. All API responses are `Content-Type: application/json`. Further, every API response is of the same shape:

```
{
  "success": bool (Whether the request was successful),
  "message": string|null (An English-language explanation of how the request was processed; usually an explanation of an error),
  ...
}
```

Additional keys in the response depend on the endpoint. For example, an endpoint that returns an array of cards will likely have an additional key `cards` of type `array`.

Whenever a request is unsuccessful (i.e. `success` is `false`), the response will also have a key `failure` of type `string` which is a unique failure code for the encountered error type.

## Requests and Responses

Simply issue an HTTP request of the specified verb to the endpoint specified. Parameters are usually included in the URI itself.

The following is an example of a valid request using `curl`:

```bash
$ curl -X GET http://api.tasks.example.com/card/vYX8sHjZsfaodWCEa
```

An example valid response:

```
{
  "card": {
    "_id": "vYX8sHjZsfaodWCEa",
    "archived": false,
    "boardId": "5iujYNEatccbyfpmo",
    "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
    "dateLastActivity": "Tue, 03 Jan 2017 23:07:46 GMT",
    "labelIds": [],
    "listId": "SuwiPwZhd2DJnP8ZC",
    "sort": 2048,
    "title": "linkr: support authenticated shortens",
    "userId": "EpTgyK5Gd9riCGdK8"
  },
  "message": null,
  "success": true
}
```

## Endpoint Documentation

Each document type has a separate markdown file in this directory detailing all available endpoints for that category.
