# Employee Management REST API (Python Flask)

A simple CRUD REST API that manages an in-memory employee dataset (IDs 401-406).

## Setup & Run
```
pip install -r requirements.txt
python app.py
```
Server starts at http://127.0.0.1:5000

## Endpoints
| # | Method | URL | Body (JSON) | Success |
|---|--------|-----|-------------|---------|
| 1 | GET | /employees | - | 200 |
| 2 | GET | /employees/<id> | - | 200 (404 if missing) |
| 3 | POST | /employees | id, name, designation | 201 (400 / 409 on error) |
| 4 | PUT | /employees/<id> | name, designation | 200 (404 / 400 on error) |
| 5 | DELETE | /employees/<id> | - | 200 (404 if missing) |

## Testing with Postman
1. Import `employee_api.postman_collection.json` (File > Import), or create requests manually.
2. For POST and PUT choose Body > raw > JSON.
3. Send each of the five requests and take screenshots of the request and response
   (save them in the `screenshots/` folder).

Sample POST body:
```
{ "id": 407, "name": "Lakshmi", "designation": "Tester" }
```
Sample PUT body (URL: /employees/401):
```
{ "name": "Arun Kumar", "designation": "Senior Manager" }
```

## Note
Data is stored in a Python list, so changes reset when the server restarts.
