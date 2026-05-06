# Sorting Microservice

## Description

The Sorting Microservice takes a JSON object containing a list of races and a sorting type, sorts the races by either distance or date, and returns the sorted race list as a JSON object.

---

## How to REQUEST Data

Request data by sending a JSON object with:
- a list of races
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
        races: [
            {
                name: "10K Race",
                distance: 10,
                date: "2026-04-01"
            },
            {
                name: "5K Race",
                distance: 5,
                date: "2026-03-01"
            }
        ]
    })
});
```

---

## How to RECEIVE Data

Receive a JSON array containing the sorted races.

### Example Response

```json
[
    {
        "name": "5K Race",
        "distance": 5,
        "date": "2026-03-01"
    },
    {
        "name": "10K Race",
        "distance": 10,
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