import json
import requests

person = {
    "firstNane":"seha Latif",
    "lastName":"Muhammad"
}

string_person = json.dumps(person)

print(type(string_person))

dic_person = json.loads(string_person)

print(type(dic_person))


res = requests.get("https://jsonplaceholder.typicode.com/todos")

todos = res.json()

for todo in todos:
    print(todo["completed"])




