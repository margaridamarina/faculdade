import csv

with open('gabarito.csv') as f:

    DictReader_obj = csv.DictReader(f)

    for item in DictReader_obj:

        print(dict(item))

with open('respostas.csv') as f:

    DictReader_obj = csv.DictReader(f)

    for item in DictReader_obj:

        print(dict(item))