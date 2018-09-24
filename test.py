from account import *
from category import *
from structure import *
import csvInterface
import random
import string

def randomString(minLen = 1, maxLen = 6):
    len = random.randint(minLen, maxLen)
    result = ''
    for i in range(len):
        result += random.choice(string.ascii_uppercase + string.digits)
    return result

def createRandomAccount():
    return Account(randomString(), randomString(), randomString())

def createRandomCategory():
    return Category(randomString(), randomString())


if __name__ == "__main__":
    for t in range(10):
        print(randomString())

    numberOfAccounts = 7
    numberOfCategories = 15

    structure = Structure()
    print(structure)

    for t in range(numberOfAccounts):
        structure.addAccount(createRandomAccount())

    for t in range(numberOfCategories):
        structure.addCategory(createRandomCategory())

    print(structure)
    getAllTransfers(structure)

    fileName = "test.csv"
    csvInterface.saveCategories(fileName, structure.regularCategoryMananager)
