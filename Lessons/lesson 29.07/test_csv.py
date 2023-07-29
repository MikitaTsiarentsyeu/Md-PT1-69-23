with open("data.txt", 'r') as f:
    data = eval(f.read())

print(type(data))
print(data[0])

with open("res.csv", "w") as f:
    for car_info in data:
        f.write(','.join([str(x) for x in car_info])+"\n")

with open("res.csv", "r") as f:
    for line in f:
        print(line.split(','))

import csv

headlines = ["make", "model", "volume", "power", "year", "id"]

with open("res.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headlines)
    writer.writerows(data)

with open("res.csv", "r", newline='') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)

with open("res.csv", "r", newline='') as f:
    reader = csv.DictReader(f, headlines)
    for line in reader:
        print(type(line))

# with open("res.csv", "w", newline='') as f:
#     writer = csv.DictWriter(f, headlines)
#     writer.writeheader()
#     writer.writerow({"volume":"test volume", "power":"test power"})