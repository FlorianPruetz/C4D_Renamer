import c4d
# Put code on a Python Tag on a Null
#Renames children in object tree,
#via a Python Tag,
#continously,
#ignores grandchildren
def main():
    n= 0
    NewName = "NewName_"   # New Name, must be in ""
    obj = op.GetObject()
    obj = obj.GetDown()
    children =[]
    while True:
        if obj == None:
            break
        obj[c4d.ID_BASELIST_NAME]=  NewName + str(n)
        children.append(obj[c4d.ID_BASELIST_NAME])
        obj = obj.GetNext()
        n = n + 1

    #print(children) Just for Checking
    #print(n)
