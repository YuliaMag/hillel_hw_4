sentences = "Hello all. Here's pretty cold and hot. Choose yourself."

list_1 = sentences.split(". ")

str_1 = list_1[0]
str_2 = list_1[1]
str_3 = list_1[2]

ll1 = len(str_1.split(" "))
ll2 = len(str_2.split(" "))
ll3 = len(str_3.split(" "))

final_l = [ll1, ll2, ll3]

print(final_l)





