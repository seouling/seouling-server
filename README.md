# seouling-server
서울 앱 공모전 서울링 서버

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
[/mypage](#mypage)<br/>

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

**request**
```
{
  "sns_token": String(Optional),
  "email": String(Optional),
  "password": String(Optional),
  "login_type": String,
  "nickname": String,
  "profile_picture": String(Optional)
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
  "username": String,
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
  "last_id": Integer
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
      "is_main": Boolean,
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
  "end_date": String
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
    "is_main": Boolean,
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
  "is_main": Boolean(Optional),
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
    "is_main": Boolean,
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
  "data": {
    "message": String
  }
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
  order: Integer(default 0)
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
{
  "type": "morning" / "after_noon" / "night"
}
```

**request**
```
{
  "add": List(spot ids),
  "delete": List(spot ids)
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
  "last_id": Integer
}
```

**request**
```
{
  "tag": [
    {
      "id": Integer,
      "selected": String
    },
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
      "scheme": String,
      "picture": String,
      "name": String
    },
    ...
  ],

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
  "last_id": Integer
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
      "scheme": String,
      "picture": String,
      "name": String
    },
    ...
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
    "id": Integer,
    "name": String,
    "content": String,
    "pictures": List(String),
    "like": Integer,
    "visitor": Integer
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
  "last_id": Integer
}
```

**response**
```
{
  "data": [
    {
      "author_name": String,  
      "author_picture": String,  
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
    "author_name": String,  
    "author_picture": String,  
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
  "data": [
    {
      "order": Number,
      "picture": String
    }
    ...
  ]
}
```

## /mypage
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
