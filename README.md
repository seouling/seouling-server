# seouling-server
서울 앱 공모전 서울링 서버<br/>
API SERVER URL: https://seouling-server.herokuapp.com/<br/>
API Docs
-------------------
[/auth/token](#authtoken)<br/>
[/auth/signup](#authsignup)<br/>
[/auth/signin/email](#authsigninemail)<br/>
[/auth/signin/sns](#authsigninsns)<br/>
[/plan](#plan)<br/>
[/plan/{plan_id}](#planplan_id)<br/>
[/plan/{plan_id}/schedule](#planplan_idschedule)<br/>
[/schedule/{schedule_id}](#scheduleschedule_id)<br/>
[/tag](#tag)<br/>
[/spot/search/tag](#spotsearchtag)<br/>
[/spot/search/name](#spotsearchname)<br/>
[/spot/{spot_id}](#spotspot_id)<br/>
[/spot/{spot_id}/comment](#spotspot_idcomment)<br/>
[/myseoul](#myseoul)<br/>
[/me](#mypage)<br/>

## /auth/token
#### -POST
Check Token

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |

**request**
```
{
  "token": String
}
```

**response**
```
{
  "message": String
}
```

## /auth/signup
#### -POST
Sign up

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Language| ko/en |

**request**
```
{
  "sns_token": String(Optional),
  "email": String(Optional),
  "password": String(Optional),
  "login_type": String,
  "nickname": String,
  "profile_picture": String(Optional), 
}
```

**response**
```
{
  "data": {
    "id": Integer,
    "sns_token": String,
    "email": String,
    "password": String,
    "nickname": String,
    "profile_picture": String,
    "is_push": Boolean,
    "login_type": Integer,
    "last_login": String,
    "created_at": String
  }
}
```

## /auth/signin/email
#### -POST
login

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |

**request**
```
{
  "email": String,
  "password": String
}
```

**response**
```
{
  "token": String
}
```

## /auth/signin/sns
#### -POST
login from facebook / google

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |

**request**
```
{
  "sns_token": String,
  "type": String
}
```

**response**
```
{
  "token": String
}
```

## /plan
#### -GET
Get Plans

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
{
  "page": Integer
}
```

**response**
```
{
  data: [
    {
      "id": Integer,
      "scheme": String,
      "name": String,
      "picture": String,
      "created_date": String,
      "start_date": String,
      "end_date": String
    },
    ...
  ],

  "paging": {
    "after": String,
    "before": String
  }
}
```

#### -POST
Create Plans

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**request**
```
{
  "start_date": String,
  "end_date": String,
  "name": String
},
```

**response**
```
{
  data: {
    "id": Integer,
    "scheme": String,
    "name": String,
    "picture": String,
    "created_date": String,
    "start_date": String,
    "end_date": String
  }
}
```

## /plan/{plan_id}
#### -PUT
Edit Plans

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**request**
```
{
  "name": String(Optional),
  "start_date": String(Optional),
  "end_date": String(Optional),
},
```

**response**
```
{
  "data": {
    "id": Integer,
    "scheme": String,
    "name": String,
    "picture": String,
    "created_date": String,
    "start_date": String,
    "end_date": String
  },
}
```

#### -DELETE
Delete Plans

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**request**
```
```

**response**
```
{
  "message": String
}
```

## /plan/{plan_id}/schedule
#### -GET
Get Plan's schedule

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
{
}
```

**response**
```
{
  data: {
    "id": Integer,
    "date": String,
    "morning": [
      {
        "id": 2,
        "name": String,
        "subway": String,
        "picture": String
      },
      ...
    ]
    "after_noon": [
      {
        "id": 2,
        "name": String,
        "subway": String,
        "picture": String
      },
      ...
    ]
    "night": [
      {
        "id": 2,
        "name": String,
        "subway": String,
        "picture": String
      },
      ...
    ]
}
```

## /schedule/{schedule_id}
#### -PUT
Edit Plan's schedule

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```

```

**request**
```
{
  "type": "morning" / "after_noon" / "night",
  "add": List(Integer),
  "remove": List(Integer)
}
```

**response**
```
{
  "data": {
    "id": Integer,
    "date": String,
    "morning": [
      {
        "spot_id": Integer,
        "scheme": String,
        "picture": String,
        "name": String
      },
      ...
    ]
    "after_noon": [
      {
        "spot_id": Integer,
        "scheme": String,
        "picture": String,
        "name": String
      },
      ...
    ]
    "night": [
      {
        "spot_id": Integer,
        "scheme": String,
        "picture": String,
        "name": String
      },
      ...
    ]
  }
}
```

## /tag
#### -GET
Get tags

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
```

**response**
```
{
  "data": [
    {
      id: Integer,
      bundle: List(String)
    }
    ...
  ]
}
```

## /spot/search/tag
#### -POST
Search Spot from tag

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
{
  "page": Integer
}
```

**request**
```
{
  "tag": [
    Integer,
    ...
  ],
  "gu": [
    Integer,
    ...
  ]
}
```

**response**
```
{
  "data": [
    {
        "id": Integer,
        "name": String,
        "subway": String,
        "content": String
        "picture": String
     }
    ]

  "paging": {
    "after": String,
    "before": String
  }
}
```

## /spot/search/name
#### -POST
Search Spot from name

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
{
  "page": Integer
}
```

**request**
```
{
  "name": String
}
```

**response**
```
{
  "data": [
    {
        "id": Integer,
        "name": String,
        "subway": String,
        "content": String
        "picture": String
     }
    ],

  "paging": {
    "after": String,
    "before": String
  }
}
```

## /spot/{spot_id}
#### -GET
Get Spot

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
```

**response**
```
{
  "data": {
        "id": 1,
        "gu": "동대문구",
        "category": "엔터테인먼트",
        "name": "남산",
        "content": "내용",
        "operation": "12:00~13:00",
        "recommend_time": "12:00-13:00",
        "subway": "삼성",
        "line": "1/5",
        "phone": "01066555744",
        "homepage": "http://121212.com",
        "address": "서울",
        "pictures": [],
        "tags": [
            "친구끼리",
            "핫플레이스"
        ],
        "like": 0,
        "visitor": 1
    }
}
```

## /spot/{spot_id}/comment
#### -GET
Get Spot's message

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
{
  "page": Integer
}
```

**response**
```
{
  "data": [
    {
      "id": Integer,
      "author": User,
      "content": String,
      "created_date": String
    }
    ...
  ],

  "paging": {
    "after": String,
    "before": String
  }
}
```

#### -POST
Post Spot's message

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**request**
```
{
  "content": String
}
```

**response**
```
{
  "data": {
    "author": User,  
    "content": String,
    "created_date": String
  }
}
```

## /myseoul
#### -GET
Get MySeoul Info

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
```

**response**
```
{
    "data": {
        "checked": [
            {
                'id': Integer, 
                'name': String, 
                'gu': Integer, 
                'category': Integer
            }
        ],
        "not_checked": [
            Spot
        ],
        "amount_count": Integer,
        "visit_count": Integer
    }
}
```

## /me
#### -GET
Get my Info

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**param**
```
```

**response**
```
{
  "data": {
    "profile_picture": String,
    "nickname": String,
    "is_push": Boolean
  }
}
```

#### -PUT
Edit my Info

**header**

|Key|Value|
|---|-----|
|Content-Type| application/json |
|Authorization| Bearer token |

**request**
```
{
  "profile_picture": File(Optional),
  "nickname": String(Optional),
  "is_push": Boolean(Optional)
}
```

**response**
```
{
  "data": {
    "profile_picture": String,
    "nickname": String,
    "is_push": Boolean
  }
}
```
