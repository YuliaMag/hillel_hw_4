#
# string_1 = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."
#
# list_1 = string_1.split()
# for elem in list_1:
#     if elem.__contains__("oo"):
#         print(elem.title(), end=" ")
#     elif elem.__contains__("OO"):
#         print(elem.title())
#
#
# list_1 = string_1.split()
#
# for elem in list_1:
#     if elem.count("oo"):
#         print(elem.title(), end=" ")
#     elif elem.count("OO"):
#         print(elem.title())
#
# for x in l_st:
#     if x.count("o") or x.count("O"):
#         print(x.title(), end=" ")


string_1 = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

l_st = string_1.split(" ")

for x in l_st:
    if x.count("o") == 2 or x.count("O") == 2:
        print(x.title(), end=" ")
