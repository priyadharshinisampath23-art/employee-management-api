"""Quick automated check of all five operations (run: python test_api.py)."""
from app import app

c = app.test_client()
def show(title, r):
    print(f"\n{title}\nStatus: {r.status_code}\n{r.get_data(as_text=True).strip()}")

show("1. GET all",      c.get("/employees"))
show("2. GET one",      c.get("/employees/401"))
show("2b. GET missing", c.get("/employees/999"))
show("3. POST",         c.post("/employees", json={"id": 407, "name": "Lakshmi", "designation": "Tester"}))
show("3b. POST dup",    c.post("/employees", json={"id": 407, "name": "X", "designation": "Y"}))
show("4. PUT",          c.put("/employees/401", json={"name": "Arun Kumar", "designation": "Senior Manager"}))
show("5. DELETE",       c.delete("/employees/406"))
show("5b. DELETE again",c.delete("/employees/406"))
