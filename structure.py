
from account import *
from category import *

_IncomeCatName = "Income"
_TransferCatName = "Transfer"

class Structure:

    def __init__(self, accountsManager = AccountsManager(), categoriesManager = CategoriesManager()):
        self.regularCategoryMananager = categoriesManager
        self.transfertCategoryManager = CategoriesManager()
        self.incomeCategoryManager = CategoriesManager()
        accounts = accountsManager.getAccounts().values()
        self.accountManager = AccountsManager()
        for a in accounts:
            self.addAccount(a)

    def addAccount(self, account):
        accounts = self.accountManager.getAccounts()
        myId = self.accountManager.addAccount(account)
        otherIds = accounts.keys()
        for k in otherIds:
            self._makeTransferCategory(k, myId)
        self._makeIncomeCategory(myId)

    def addCategory(self, category):
        self.regularCategoryMananager.addCategory(category)

    def _makeIncomeCategory(self, accountID):
        cat = Category(_IncomeCatName, accountID)
        self.incomeCategoryManager.addCategory(cat)


    def _makeTransferCategory(self, accountID1, accountID2):
        cat = Category(_TransferCatName, tuple(sorted([accountID1, accountID2])))
        self.transfertCategoryManager.addCategory(cat)

    def __repr__(self):
        values = (self.accountManager, self.regularCategoryMananager)
        #values = (self.accountManager, self.regularCategoryMananager, self.transfertCategoryManager, self.incomeCategoryManager)
        n = len(values)
        format = ""
        if n > 1: format += "%r"
        for n in range(1, n):
            format += ", %r"
        return (self.__class__.__name__ + "(" + format + ")") % values

def getAllTransfers(allocMan):
    transferCats = allocMan.transfertCategoryManager.getCategories()
    print(transferCats)
