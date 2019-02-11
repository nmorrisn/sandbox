# if __name__ == '__main__':
#     N = int(input())
#
# commands = []
# list = []
# for i in range(N):
#     commands.insert(i, str(input()))
#
# for j in commands:
#     words = j.split(" ")
#     if words[0] == "insert":
#         if len(words) < 2:
#             raise Exception('insert keyword must be followed by two integers')
#
#         list.insert(int(words[1]), int(words[2]))
#
#     elif words[0] == "print":
#         print(list)
#
#     elif words[0] == "remove":
#         list.remove(int(words[1]))
#
#     elif words[0] == "append":
#         list.append(int(words[1])
#
#     elif words[0] == "sort":
#         list.sort()
#
#     elif words[0] == "pop":
#         list.pop(len(list) - 1)
#
#     elif words[0] == "reverse":
#         list.reverse()
#
#     else:
#         print("Invalid command.")


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
# newList = student_marks[query_name]
#
# sum = 0
# for score in newList:
#     sum += score
#
# avg = 0.0
# avg = sum/len(newList)
#
# print ("%.2f" % avg)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    myList = list(arr)
    myMax = max(myList)
    for i in range(myList.count(myMax)):
        myList.remove(myMax)

    print(max(myList))
