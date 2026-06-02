# Sorting Microservice

## Description

The Sorting Microservice takes a list of fitness activities including date and/or distance fields, sorts the activities by either distance or date, and returns the sorted activity list as a JSON object.

This microservice can be used in applications related to running, hiking, cycling, walking, or other fitness tracking systems.

---

## How to REQUEST Data

Request data by sending a JSON array containing items with one of the required fields (date or distance).

Send the request to:

```text
POST /sort/date
```
or:
```text
POST /sort/distance
```

### Example Call

```javascript
fetch('http://localhost:3002/sort/distance', {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        [
            {
                title: "Mountain Hike",
                distance: 12,
                date: "2026-04-01"
            },
            {
                title: "Morning Run",
                distance: 5,
                date: "2026-03-01"
            }
        ]
    })
});
```

---

## How to RECEIVE Data

Receive a JSON array containing the sorted activities.

### Example Response

```json
[
    {
        "title": "Morning Run",
        "distance": 5,
        "date": "2026-03-01"
    },
    {
        "title": "Mountain Hike",
        "distance": 12,
        "date": "2026-04-01"
    }
]
```

---

## Running the Microservice

Start the Flask server with:

```bash
python app.py
```

The microservice will run on:

```text
http://localhost:3002
```