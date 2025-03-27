import csv 

input_file="Python_Basics_Training/5_File_Handling/b/Student_data.csv"
def add_student(name, age, grade):
    with open(input_file,'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])

def delete_student(name):
    with open(input_file,'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open(input_file,'w',newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != name:
                writer.writerow(row)

def search_student(name):
    with open(input_file,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]==name:
                return row 

add_student("Alice", 20, 9)
add_student("Bob", 21, 8)
add_student("Charlie", 22, 7)
print(search_student("Alice"))
delete_student("Alice")
print(search_student("Alice"))
print(search_student("Bob"))
print(search_student("Charlie"))