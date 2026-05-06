# Sorting Microservice

## Description

The Sorting Microservice takes a JSON object containing a list of fitness activities and a sorting type, sorts the activities by either distance or date, and returns the sorted activity list as a JSON object.

This microservice can be used in applications related to running, hiking, cycling, walking, or other fitness tracking systems.

---

## How to REQUEST Data

Request data by sending a JSON object with:
- a list of activities
- a sorting type

Send the request to:

```text
POST /sort
```

### Example Call

```javascript
fetch('http://localhost:3002/sort', {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        sortBy: "distance",
        activities: [
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

## Supported Sorting Types

```text
distance
date
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