import csv
import pprint
import random

with open('tem_and_hum.csv', 'a') as f:
    writer = csv.writer(f)
    for i in range(31):
        for j in range(24):
            for k in range(4):
                min = 15 * (k + 1)
                random_ten = random.randint(10, 22)
                random_hum = random.randint(10, 60)
                date = '2021-11-' + str(i + 1) + '-' + str(j + 1) + '-' + str(min) + '-' + str(random_ten) + '-' + str(random_hum)
                writer.writerow([date])