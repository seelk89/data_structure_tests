import csv
import random
import timeit

# Clearing file
f = open('comma_delimited_test.csv', 'w+')
f.close()

start = timeit.default_timer()
for i in range(1000):
    with open('comma_delimited_test.csv', 'a+', newline='') as f:
        fieldnames = ['column_1', 'column_2', 'column_3']
        file_writer = csv.DictWriter(f, fieldnames=fieldnames)

        rn = random.randint(1, 3)
        if rn == 1:
            file_writer.writerow({'column_{0}'.format(rn): '{0}'.format(i)})

        if rn == 2:
            file_writer.writerow({'column_{0}'.format(rn): '{0}'.format(i)})

        if rn == 3:
            file_writer.writerow({'column_{0}'.format(rn): '{0}'.format(i)})

        f.close()

print('Write time: ', (timeit.default_timer() - start) / 1000)

start = timeit.default_timer()
for i in range(1000):
    with open('comma_delimited_test.csv') as f:
        reader = csv.reader(f)

        # Loop through csv list
        for row in reader:
            for k in range(3):
                if str(i) == row[k]:
                    print('Column: {0} number: {1}'.format(k, row))

    f.close()

print('Read time: ', (timeit.default_timer() - start) / 1000)
