import csv

myfile = 'student-Ai-CSV.csv'

def read_display_csv(myfile):
   with open(myfile, mode='r') as datafile:
      csv_reader = csv.reader(datafile)
      for row in csv_reader:
         print(row)
print(read_display_csv(myfile))

def total_number_of_records(myfile):
    total_records = sum(1 for row in open(myfile)) - 1
    print("Total records:", total_records)
total_number_of_records(myfile)

def list_of_column_names(myfile):
    with open(myfile, mode='r') as datafile:
        csv_reader = csv.reader(datafile, delimiter=',')
        header = next(csv_reader)
    print("List of column names:", header)
list_of_column_names(myfile)