# `card`

Endpoints for retrieving information about cards.

### `GET /cards`

##### Description

Get an array of all known cards.

##### Request Parameters

None

##### Example Request/Response

```
GET http://api.tasks.example.com/cards

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

### `GET /card/:card_id`

##### Description

Get details for a single card.

##### Request Parameters

|**Parameter**|**Description**|**Type**|
|---|---|---|
|`card_id`|ID of the card for which details should be retrieved.|`string`|

##### Example Request/Response

```
GET http://api.tasks.example.com/card/22STmitmz3EtFBvY6

{
  "card": {
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
  "message": null,
  "success": true
}
```
