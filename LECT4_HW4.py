
email = str(input("Email Address: "))
if "@" not in email:
    print(False)
elif "." not in email:
    print(False)
elif "@" in email[0]:
    print(False)
elif "." in email[0]:
    print(False)
elif "@" in email[-1]:
    print(False)
elif "." in email[-1]:
    print(False)
#elif TODO
else:
    print(True)




