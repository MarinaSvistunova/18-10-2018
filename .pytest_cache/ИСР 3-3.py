import csv

data = open('C:/Users/svmar/Desktop/Учеба/2 курс/Python/titanic.csv', 'r')
csv_file = open('C:/Users/svmar/Desktop/Учеба/2 курс/Python/Result.csv', 'w', newline='')

with csv_file:
  for line in data:
     reader = line.split(',')
     writer = csv.writer(csv_file, delimiter=',')
     writer.writerow(reader)
print("Done")

"""
import csv
list_results = open('C:/Users/svmar/Desktop/Учеба/2 курс/Python/titanic.csv', 'r')

with open('C:/Users/svmar/Desktop/Учеба/2 курс/Python/Result.csv', 'w') as result:
    reader = readline()
    writer = csv.writer(result)
    writer.writerows([c.strip().split(',') for c in r.split(',')] for r in list_results)

print("Done")
import csv
csv_file = open('C:/Users/svmar/Desktop/Учеба/2 курс/Python/d.csv', 'r')
with csv_file:
  reader = csv.DictReader(csvfile, delimiter=',')
for line in csv_file:
  print(line[0], line[1], line[2], line[3])"""