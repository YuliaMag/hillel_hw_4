
email = input("Email Address: ")

if "@" not in email:
    print(False)
# testatest.com

elif "." not in email:
    print(False)
# test@testdotcom

elif "@" == email[0]:
    print(False)
# @test.test

elif "." in email[-1]:
    print(False)
# test@test.

elif email.count("@") > 1: # if I put "!= 2" then 3 "@" will be valid input
    print(False)
# test@test@test.com

elif email.count(".") > 1: # if I put "!= 2" then 3 "." will be valid input
    print(False)
# test@test.test.com

elif email.find("@") > email.find("."):
    print(False)
# test.test@com

elif not email.isalnum():
    if email.find("@") or email.find("."):
        pass
    else:
        print(False)
    print(False)
# )*(^&*%^$%$##%^$^%
# #$%@&*(.% -- I missed this one

else:
    print("True")
# test@test.com




