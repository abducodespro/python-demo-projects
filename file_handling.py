import csv


# txt files 
with open("hello.txt", "w") as file:
    file.write("hello to everyone\n")
    file.write("I am learing python")


with open("hello.txt", "r") as f:
    content = f.read()
    print(content)



# csv file 
students = [
    ["Name", "Age", "Score"],
    ["Abdu", 21, 88],
    ["Sara", 19, 92]
]

with open("student.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

with open("student.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)