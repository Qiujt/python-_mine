import  random
result=random.randint(1,10)
answer=int(input("guess the number:"))

if  answer > result:
    print("猜大了！")
elif answer < result:
    print("猜小了！")
else:
    print("猜对了！")

print(result)