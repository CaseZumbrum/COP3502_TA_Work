# # 5! = 5 * 4 * 3 * 2 * 1
# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)


# def mystery(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     return mystery(num - 1) + mystery(num - 2)


# if __name__ == "__main__":
#     print(mystery(1000))


board = [["x", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


board[0][2] = "o"
for i in reversed(board):
    for j in i:
        print(j, end=" ")
    print()
