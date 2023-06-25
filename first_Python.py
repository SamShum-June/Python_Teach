# name = "samshum,"
# first = "Hello,"
# second = "My World!"
# print("Hello " + name);

# print(name + first + second)

# # print()




# chenji = 100
# raing = True
# if chenji==100 and raing:
#     print("I give you 1000 yuan")
# else:
#     print("you give me 100 yuan")




    
# def max_num(num1,num2,num3,num4):
#     if num1>=num2 and num1>=num3 and num1>=num4:
#         return num1
#     elif num2>=num1 and num2>=num3 and num2>=num4:
#         return num2
#     elif num3>=num1 and num3>=num2 and num3>=num4:
#         return num3
#     else:
#         return num4

# print(max_num(0,1,1,1111111))
 

# num1 = float(input("请输入第一个运算数字 "))
# op = input("运算符")
# num2 = float(input("请输入第二个运算数字 "))

# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("不支持此运算")


# dict={1:"cc",2:"bb"}
# print(dict[1])

# 猜数字游戏
# 1、谜底是一个数字
# 2、游戏要输入数字，
# 输入的数字如果大于谜底提示小一点，
# 如果输入的数字小于谜底那就提示大一点，
# 无限次数的猜直到猜到正确为止，
# 如果输入正确那就恭喜你完成游戏。
# def num():
#     if num < md:
#         print("请输入小一点的数字")
#     elif num > md:
#         print("请输入大一点的数字")
#     elif num == md:
#         print("恭喜你答对了")



# md1 = int(input("主持人1输入要猜的数字:"))
# op = input("换算符号")
# md2 = int(input("主持人2输入要猜的数字:"))

# if op =="+":
#     md = md1+md2
# elif op=="-":
#     md = md1-md2
# elif op=="*":
#     md = md1*md2
# elif op=="/":
#     md = md1/md2
# num = None

# #print(md())

# while md != num:
#     num = float(input("请你心中的数字："))
#     if num == md:
#         print("恭喜你猜对了")
#     elif num > md:
#         print("请输入小一点的数字")
#     elif num < md:
#         print("请输入大一点的数字")
        


# print(pow(2,6))

def power(base_num,pow_num):
    base = base_num
    for index in range(pow_num-1):
        base = base * base_num
    return base

print(power(4,2))

#print(index)

    
    
