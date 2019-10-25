def count():
    for char in string:
        if char in string:
            if char not in list_name:
                if char != NULL:
                    list_name.insert(0,char)
                    print(char,"=",string.count(char))
            #elif char in list_name:
            #    continue

NULL =' '
list_name = []
string = input("Enter the string :")
count()
