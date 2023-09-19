# # a = [5, 4, 3, 2, 1]


# # for i in range(1, 4, 1):
# #     # print("Lista: ")
# #     for j in range(i, 0, -1):
# #         if a[i] < a[j]:
# #             aux = a[i]
# #             a[i] = a[j]
# #             a[j] = aux
# #     # for n in range(5):
# #     #     print(a[n], ' ', end="")
# #     # print
# # for k in range(4):
# #     print(a[k], end="")


# ## do GPT:
# a = [5, 4, 3, 2, 1]

# for i in range(1, len(a)):
#     chave = a[i]
#     j = i - 1
#     while j >= 0 and chave < a[j]:
#         a[j + 1] = a[j]
#         j -= 1
#     a[j + 1] = chave

# for k in range(len(a)):
#     print(a[k], end="")
