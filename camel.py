

x=input("camelCase: ")

list_version=list(x)

print("snake_case: ", end="")

for uppercase in list_version:
    is_upper=uppercase.isupper()
    if is_upper:
        print("_"+ uppercase.lower(), sep="", end="")
    else:
        print(uppercase, end="")

print()







