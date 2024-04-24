
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
elif email.count("@") > 1:
    print(False)
elif email.count(".") > 1:
    print(False)
elif email.find("@") > email.find("."):
    print(False)
elif not email.isalnum():
    if email.__contains__("@") or email.__contains__("."):
        print(True)
    else:
        print(False)
else:
    print("True")





