#Задача - написать программу заменяющую слово из строки на номер слова в приложенном файле

# with open("russian.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()

a = [1,2,3,4,5,6,7,8,9,0]
f = open("russian.txt",'w')
f.writelines("%s\n" % i for i in a)
f.close()
open("russian.txt").read()
print(open("russian.txt").read())