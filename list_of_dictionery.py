def hight_scores(students):
    for student in students:
        if student["score"] > 80:
            print(f"{student["name"]} scored {student["score"]}")

def analyze_age(students):
    for student in students:
        if student['age'] > 21:
            print(f"{student["name"]} age is {student["age"]}")
            
students = [
    {"name":"abbb", "age":12, "score":82},
    {"name":"rsss", "age":22, "score":70},
    {"name":"hggf", "age":23, "score":79},
    {"name":"rtrt", "age":12, "score":85}
]

print("---- students with score of grater than 80 ----")
hight_scores(students)

print("---- students with age of greater than 21 ----")
analyze_age(students)

sorted_students = sorted(students, key= lambda s: s["score"], reverse=True)

print("---- students with age of greater than 21 ----")
for student in sorted_students:
    print(f"{student["name"]} - {student["score"]}")