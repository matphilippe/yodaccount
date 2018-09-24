import csv
import account
import category

def saveCategories(fileName, categoriesManager):
    f = open(fileName, 'w')
    fieldnames = ['ID', 'name', 'description']
    writer = csv.DictWriter(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames = fieldnames)

    writer.writeheader()
    categories = categoriesManager.getCategories()
    for k in categories:
        writer.writerow({'ID' : repr(k), 'name': categories[k].name, 'description': categories[k].description})
