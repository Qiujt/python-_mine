# 案例3:快速排序
# 1.  随机生成10个数字
# 2.  利用递归,实现快速排序

from random import  randint

def qsort(num_list):
    if len(num_list) <2:
        return num_list

    middle=num_list[0]         #自定义第一个数为中间数
    smaller=[]
    larger=[]
    for i in num_list[1:]:
        if i < middle:
            smaller.append(i)
        else:
            larger.append(i)

    return  qsort(smaller)+[middle]+qsort(larger)

if __name__ == '__main__':
    nums=[randint(1,100) for i in range(10)]
    print(nums)
    print(qsort(nums))
