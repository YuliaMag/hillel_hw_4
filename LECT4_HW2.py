# sentences = "Hello all. Here's pretty cold and hot. Choose yourself."
# list_1 = sentences.split(". ")
# str_1 = list_1[0]
# str_2 = list_1[1]
# str_3 = list_1[2]
# ll1 = len(str_1.split(" "))
# ll2 = len(str_2.split(" "))
# ll3 = len(str_3.split(" "))
# final_l = [ll1, ll2, ll3]
# print(final_l)


sentences = input("Enter text: ")

list_1 = sentences.split(". ")
l_final = []

for x in list_1:
    y = len(x.strip().split(" "))
    l_final.append(y)
print(l_final)


"""
for test: 
1) Hello all. Here's pretty cold and hot. Choose yourself.

2) Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. 
"""











