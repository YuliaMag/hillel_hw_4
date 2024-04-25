
string_1 = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

# list_1 = string_1.split()
# for elem in list_1:
#     if elem.__contains__("oo"):
#         print(elem.title(), end=" ")
#     elif elem.__contains__("OO"):
#         print(elem.title())
#

list_1 = string_1.split()
for elem in list_1:
    if elem.count("oo"):
        print(elem.title(), end=" ")
    elif elem.count("OO"):
        print(elem.title())
