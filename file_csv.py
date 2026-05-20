import csv

with open("test2.csv", "w", newline="") as file:
    X = csv.writer(file)
    X.writerow(["Date", "Category", "Amount"])
    X.writerow(["2024-01-01", "Food", "10.50"])
