email = input("Email Address: ")

s = "! # $ % ^ & * ( ) _ + = - / , < > ?"
l_n = s.split(" ")

for x in l_n:
    if ((x in email) or (email.count("@") != 1 or email.count(".") != 1) or ("@" == email[0] or "." == email[-1]) or
            (email.find("@") > email.find(".")) or (email.find(".") == email.find("@") + 1)):
        print(False)
        break
    else:
        print(True)
        break

# TC "True":
# test@test.com

# TCs "False":
# test.test@com
# test@@test@com
# test.test.com
# testtestcom
# ^%&!#$%^&*()_+><?
# ^%&test
# &*^@(*&.%$ ---!! failed, gives True!!!
# @test.
# @test
# test.
# test.@test
# test@.test ---- !!! the case I missed before
