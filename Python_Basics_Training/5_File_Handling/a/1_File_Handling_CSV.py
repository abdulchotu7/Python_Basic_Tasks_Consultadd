import csv

input_file = "Python_Basics_Training/5_File_Handling/a/Student_score.csv"
output_file = "Python_Basics_Training/5_File_Handling/a/output.csv"

rows = []

with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)  
    header.append("Total Score")  
    rows.append(header)

    for row in reader:
        total = sum(map(int, row[2:]))  
        row.append(total)  
        rows.append(row)
    row.pop()
print(rows)
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print(f"Updated CSV file saved as: {output_file}")
