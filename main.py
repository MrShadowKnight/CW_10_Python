# my_list = []

# for item in range(int(input("Start range: ")), int(input("End range: ")) + 1):
#     if item % 3 == 0 and item % 5 == 0:
#         my_list.append(item)
# print(my_list)


# start = int(input("Start range: "))
# end = int(input("End range: "))
# simpl_num = []
# for i in range(start, end + 1):
#     flag = True
#     for j in range(start, end + 1):
#         if j >= i:
#             break
#         elif j != 1 and i != j:
#             resuld = i % j
#             if resuld == 0:
#                 flag = False
#                 break
#     if flag:
#         simpl_num.append(i)
# print (simpl_num)