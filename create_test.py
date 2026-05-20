import csv

with open("newtest.csv", "x", newline="") as file:
    A = csv.writer(file)
    A.writerow(["Name", "Age", "City"])
    A.writerow(["Alice", 30, "New York"])


    
print("CSV file created successfully.")

