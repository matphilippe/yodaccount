class Category:
    _DEF_NAME = "testN"
    _DEF_DESCR = "testD"

    def __init__(self, name = _DEF_NAME, description = _DEF_DESCR,):
        self.name = name
        self.description = description

    def __repr__(self):
        vars = self.__dict__.keys()
        n = len(vars)
        values = tuple([getattr(self, x) for x in vars])
        format = ""
        if n > 1: format += "%r"
        for n in range(1, n):
            format += ", %r"
        return (self.__class__.__name__ + "(" + format + ")") % values

class CategoriesManager:

    def __init__(self):
        self.categories = {}
        self.nextCatID = 0

    def addCategory(self, category):
        self.categories[self.nextCatID] = category
        self.nextCatID += 1

    def getCategories(self):
        return (self.categories)

    def __repr__(self):
        return repr(self.categories)

if __name__ == "__main__":

    catMan = CategoriesManager()
    for t in range(10):
        catMan.addCategory(Category())
    print(catMan.getCategories())
