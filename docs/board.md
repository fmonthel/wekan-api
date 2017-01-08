# `board`

Endpoints for retrieving information about boards.

### `GET /boards`

##### Description

Get an array of all known boards.

##### Request Parameters

None

##### Example Request/Response

```
GET http://api.tasks.example.com/boards

{
  "boards": [
    {
      "_id": "5iujYNEatccbyfpmo",
      "archived": false,
      "color": "nephritis",
      "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
      "labels": [
        {
          "_id": "C8XAQJ",
          "color": "green"
        },
        {
          "_id": "8AL3cx",
          "color": "purple"
        },
        {
          "_id": "7guNSD",
          "color": "yellow"
        },
        {
          "_id": "5pFzQY",
          "color": "blue"
        },
        {
          "_id": "mzLpdo",
          "color": "orange"
        },
        {
          "_id": "qiYz4o",
          "color": "red"
        }
      ],
      "members": [
        {
          "isActive": true,
          "isAdmin": true,
          "userId": "EpTgyK5Gd9riCGdK8"
        }
      ],
      "modifiedAt": "Tue, 03 Jan 2017 23:34:17 GMT",
      "permission": "private",
      "slug": "personal",
      "stars": 1,
      "title": "Personal"
    },
    ...
  ],
  "message": null,
  "success": true
}
```

### `GET /board/:board_id`

##### Description

Get details for a single board.

##### Request Parameters

|**Parameter**|**Description**|**Type**|
|---|---|---|
|`board_id`|ID of the board for which details should be retrieved.|`string`|

##### Example Request/Response

```
GET http://api.tasks.example.com/board/5iujYNEatccbyfpmo

{
  "board": {
    "_id": "5iujYNEatccbyfpmo",
    "archived": false,
    "color": "nephritis",
    "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
    "labels": [
      {
        "_id": "C8XAQJ",
        "color": "green"
      },
      {
        "_id": "8AL3cx",
        "color": "purple"
      },
      {
        "_id": "7guNSD",
        "color": "yellow"
      },
      {
        "_id": "5pFzQY",
        "color": "blue"
      },
      {
        "_id": "mzLpdo",
        "color": "orange"
      },
      {
        "_id": "qiYz4o",
        "color": "red"
      }
    ],
    "members": [
      {
        "isActive": true,
        "isAdmin": true,
        "userId": "EpTgyK5Gd9riCGdK8"
      }
    ],
    "modifiedAt": "Tue, 03 Jan 2017 23:34:17 GMT",
    "permission": "private",
    "slug": "personal",
    "stars": 1,
    "title": "Personal"
  },
  "message": null,
  "success": true
}
```

### `GET /board/:board_id/lists`

##### Description

Get all known lists for a single board.

##### Request Parameters

|**Parameter**|**Description**|**Type**|
|---|---|---|
|`board_id`|ID of the board for which details should be retrieved.|`string`|

##### Example Request/Response

```
GET http://api.tasks.example.com/board/5iujYNEatccbyfpmo/lists

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
    {
      "_id": "efE2qm9LHxQ4FkC3s",
      "archived": false,
      "boardId": "5iujYNEatccbyfpmo",
      "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
      "title": "Backlog",
      "updatedAt": "Tue, 03 Jan 2017 23:07:46 GMT"
    }
  ],
  "message": null,
  "success": true
}
```

### `GET /board/:board_id/cards`

##### Description

Get all known cards for a single board.

##### Request Parameters

|**Parameter**|**Description**|**Type**|
|---|---|---|
|`board_id`|ID of the board for which details should be retrieved.|`string`|

##### Example Request/Response

```
GET http://api.tasks.example.com/board/5iujYNEatccbyfpmo/cards

{
  "cards": [
    {
      "_id": "DDD6zuTLEz43uxfaW",
      "archived": false,
      "boardId": "5iujYNEatccbyfpmo",
      "createdAt": "Tue, 03 Jan 2017 23:07:46 GMT",
      "dateLastActivity": "Tue, 03 Jan 2017 23:07:46 GMT",
      "labelIds": [],
      "listId": "SuwiPwZhd2DJnP8ZC",
      "sort": 32768,
      "title": "rejection emails",
      "userId": "EpTgyK5Gd9riCGdK8"
    },
    {
      "_id": "Dtkqr6Dqe3FbRxAkX",
      "archived": false,
      "boardId": "5iujYNEatccbyfpmo",
      "createdAt": "Sun, 08 Jan 2017 02:05:56 GMT",
      "dateLastActivity": "Sun, 08 Jan 2017 02:05:56 GMT",
      "labelIds": [],
      "listId": "efE2qm9LHxQ4FkC3s",
      "members": [],
      "sort": 524291,
      "title": "linkr: account interface should support changing password",
      "userId": "EpTgyK5Gd9riCGdK8"
    },
    ...
  ],
  "message": null,
  "success": true
}
```
