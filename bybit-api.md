## Bybit V5 - 公告 (Announcement) API 文档

### HTTP 请求

```
GET /v5/announcements/index
```

---

### 请求参数 (Query)

| 参数       | 必需    | 类型      | 说明                       |
| -------- | ----- | ------- | ------------------------ |
| `locale` | **是** | string  | 公告语言 (language symbol)   |
| `type`   | 否     | string  | 公告类型 (announcement type) |
| `tag`    | 否     | string  | 公告标签 (tag)               |
| `page`   | 否     | integer | 分页页码，默认 `1`              |
| `limit`  | 否     | integer | 每页数据条数限制，默认 `20`         |

---

### 响应参数 (Response)

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "total": 735,
    "list": [
      {
        "title": "New Listing: Arbitrum (ARB) — Deposit, Trade and Stake ARB …",
        "description": "Bybit is excited to announce …",
        "type": {
          "title": "New Listings",
          "key": "new_crypto"
        },
        "tags": ["Spot", "Spot Listings"],
        "url": "https://announcements.bybit.com/en-US/article/new-listing-arbitrum-arb-…",
        "dateTimestamp": 1679045608000,
        "startDateTimestamp": 1679045608000,
        "endDateTimestamp": 1679045608000,
        "publishTime": 1679045608000  // 注意：某些接口例子里有这个字段
      }
    ]
  },
  "retExtInfo": {},
  "time": 1679415136117
}
```

#### 响应字段说明

* `total` (`integer`) — 公告总条目数
* `list` (`array`) — 公告项列表，每个项目是一个对象，包含以下字段：

  | 字段                   | 类型            | 说明                                                                   |
  | -------------------- | ------------- | -------------------------------------------------------------------- |
  | `title`              | string        | 公告标题                                                                 |
  | `description`        | string        | 公告描述                                                                 |
  | `type`               | object        | 公告类型对象，包含：<br>- `title` (string)：公告类型名称<br>- `key` (string)：公告类型 key |
  | `tags`               | array<string> | 公告标签 (tags)                                                          |
  | `url`                | string        | 公告链接 (URL)                                                           |
  | `dateTimestamp`      | number        | 作者填写时间戳 (毫秒)                                                         |
  | `startDateTimestamp` | number *(可选)* | 事件开始时间戳 (毫秒)；仅当 `type.key == "latest_activities"` 时有效                |
  | `endDateTimestamp`   | number *(可选)* | 事件结束时间戳 (毫秒)；仅当 `type.key == "latest_activities"` 时有效                |
  | `publishTime`        | number        | 公告发布时间 (毫秒)                                                          |

---

### 请求示例

**HTTP 示例**（简单 GET 请求）：

```
GET /v5/announcements/index?locale=en-US&limit=1 HTTP/1.1  
Host: api.bybit.com  
```

---

### 响应示例

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "total": 735,
    "list": [
      {
        "title": "New Listing: Arbitrum (ARB) — Deposit, Trade and Stake ARB to Share a 400,000 USDT Prize Pool!",
        "description": "Bybit is excited to announce the listing of ARB on our trading platform!",
        "type": {
          "title": "New Listings",
          "key": "new_crypto"
        },
        "tags": [
          "Spot",
          "Spot Listings"
        ],
        "url": "https://announcements.bybit.com/en-US/article/new-listing-arbitrum-arb-deposit-trade-and-stake-arb-to-share-a-400-000-usdt-prize-pool--bltf662314c211a8616/",
        "dateTimestamp": 1679045608000,
        "startDateTimestamp": 1679045608000,
        "endDateTimestamp": 1679045608000
      }
    ]
  },
  "retExtInfo": {},
  "time": 1679415136117
}
```

---

### 错误码 / 返回说明

* `retCode` — 返回码 (0 表示成功)
* `retMsg` — 返回消息 (例如 `"OK"`)
* `time` — 响应时间戳 (ms)

