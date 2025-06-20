import json

students = {
    "name": "anwar", "age": 24, "score": 85
}

json_str = json.dumps(students)
print(json_str)

json_data = '{"name": "Abdu", "age": 21, "score": 88}'

python_dict = json.loads(json_data)
print(python_dict["name"])

# Reading and writng json file

students2 = [
    {"name": "Abdu", "age": 21, "score": 88},
    {"name": "Sara", "age": 20, "score": 90}
]

with open("students.json", "w") as f:
    json.dump(students2, f, indent=4)
    
with open("students.json", "r") as f:
    data = json.load(f)

for student in data:
    print(student["name"], student["score"])
