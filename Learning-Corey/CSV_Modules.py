import csv

# with open('employee.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

# with open('new_employee.csv', 'w') as new_file:
#     csv_writer = csv.writer(new_file, delimiter='\t')

#     for line in csv_reader:
#         csv_writer.writerow(line)

# Using the Dictionary Reader/Writer
# with open('employee.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     # for line in csv_reader:
#     #     print(line)
#     # print(line['email'])

#     with open('new_employee.csv', 'w') as new_file:
#         fieldnames = ['firstname', 'lastname', 'email']

#         csv_writer = csv.DictWriter(
#             new_file, fieldnames=fieldnames, delimiter='\t')

#         csv_writer.writeheader()

#         for line in csv_reader:
#             csv_writer.writerow(line)


#Removing/Filter the columns
with open('employee.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #     print(line)
    # print(line['email'])

    with open('new_employee.csv', 'w') as new_file:
        fieldnames = ['firstname', 'lastname']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
