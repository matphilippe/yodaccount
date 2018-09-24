class Account:
    _DEF_NAME = "test"
    _DEF_DESCR = "test"
    _DEF_IBAN = "IBAN"

    def __init__(self, iban = _DEF_IBAN,  description = _DEF_DESCR, name = _DEF_NAME):
        self.name = name
        self.description = description
        self.iban = iban

    def __repr__(self):
        vars = self.__dict__.keys()
        n = len(vars)
        values = tuple([getattr(self, x) for x in vars])
        format = ""
        if n > 1: format += "%r"
        for n in range(1, n):
            format += ", %r"
        return (self.__class__.__name__ + "(" + format + ")") % values


class AccountsManager:

    def __init__(self):
        self.accounts = {}
        self.nextAccountID = 0

    def addAccount(self, account):
        self.accounts[self.nextAccountID] = account
        self.nextAccountID += 1
        return self.nextAccountID - 1

    def getAccounts(self):
        return (self.accounts)

    def __repr__(self):
        return repr(self.accounts)
        
if __name__ == "__main__":

    acMan = AccountsManager()
    for t in range(10):
        acMan.addAccount(Account())
    print(acMan.getAccounts())
