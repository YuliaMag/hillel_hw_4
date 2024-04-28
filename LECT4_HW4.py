email = input("Email Address: ")
q = 0
w = 0
prev_chr = ""
s_end = len(email) - 1
res = True

for i in range(len(email)):
    if email[i].isalnum():
        prev_chr = email[i]
        continue
    if email[i] == "@" and q == 0 and 0 < i < s_end:
        q = 1
        prev_chr = email[i]
        continue
    if email[i] == "." and w == 0 and 0 < i < s_end and q == 1 and prev_chr != "@":
        w = 1
        prev_chr = email[i]
        continue
    res = False
    break

if q == 0 or w == 0:
    res = False

print(res)


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
