
# HW1.1
inp_str = input("Input string: ")

inp_str = inp_str.strip().lower()
rev_str = reversed(inp_str)

if list(inp_str) == list(rev_str):
    print(True)
else:
    print(False)


print("-------------------")
# HW1.2

n = input("Input string: ")
nn = n.strip().lower()

if nn == nn[::-1]:
    print(True)
else:
    print(False)

