# `list`

Endpoints for retrieving information about lists.

### `GET /lists`

##### Description

Get an array of all known lists.

##### Request Parameters

None

##### Example Request/Response

```
GET http://api.tasks.example.com/lists

{
  "lists": [
    {
      "_id": "7L6jLexePAPiPJeTY",
      "archived": false,
      "boardId": "5iujYNEatccbyfpmo",
      "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
      "title": "In Progress",
      "updatedAt": "Tue, 03 Jan 2017 23:07:46 GMT"
    },
    {
      "_id": "SuwiPwZhd2DJnP8ZC",
      "archived": false,
      "boardId": "5iujYNEatccbyfpmo",
      "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
      "title": "Done",
      "updatedAt": "Tue, 03 Jan 2017 23:07:46 GMT"
    },
    ...
  ],
  "message": null,
  "success": true
}
```

### `GET /list/:list_id`

##### Description

Get details for a single list.

##### Request Parameters

|**Parameter**|**Description**|**Type**|
|---|---|---|
|`list_id`|ID of the list for which details should be retrieved.|`string`|

##### Example Request/Response

```
GET http://api.tasks.example.com/list/7L6jLexePAPiPJeTY

{
  "list": {
    "_id": "7L6jLexePAPiPJeTY",
    "archived": false,
    "boardId": "5iujYNEatccbyfpmo",
    "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
    "title": "In Progress",
    "updatedAt": "Tue, 03 Jan 2017 23:07:46 GMT"
  },
  "message": null,
  "success": true
}
```

### `GET /list/:list_id/cards`

##### Description

Get all known cards for a single list.

##### Request Parameters

|**Parameter**|**Description**|**Type**|
|---|---|---|
|`list_id`|ID of the list for which details should be retrieved.|`string`|

##### Example Request/Response

```
GET http://api.tasks.example.com/list/7L6jLexePAPiPJeTY/cards

{
  "cards": [
    {
      "_id": "22STmitmz3EtFBvY6",
      "archived": false,
      "boardId": "92zFkhfdqiv6NT5LH",
      "createdAt": "Tue, 03 Jan 2017 23:08:41 GMT",
      "dateLastActivity": "Tue, 03 Jan 2017 23:08:41 GMT",
      "labelIds": [
        "8kt8fq"
      ],
      "listId": "Tsy4B2gWYPenxHu6Z",
      "sort": 65536,
      "title": "310 api",
      "userId": "EpTgyK5Gd9riCGdK8"
    },
    {
      "_id": "2X2iuLPLjzc4DJXBc",
      "archived": false,
      "boardId": "92zFkhfdqiv6NT5LH",
      "createdAt": "Tue, 03 Jan 2017 23:08:41 GMT",
      "dateLastActivity": "Tue, 03 Jan 2017 23:08:41 GMT",
      "labelIds": [
        "8kt8fq"
      ],
      "listId": "Tsy4B2gWYPenxHu6Z",
      "sort": 49152,
      "title": "310 feedback",
      "userId": "EpTgyK5Gd9riCGdK8"
    },
    ...
  ],
  "message": null,
  "success": true
}
```
