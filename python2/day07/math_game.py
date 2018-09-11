# 案例1:简单的加减法数学游戏
# 1.  随机生成两个100以内的数字
# 2.  随机选择加法或是减法
# 3.  总是使用大的数字减去小的数字
# 4.  如果用户答错三次,程序给出正确答案

from  random  import  randint,choice

# def add(x,y):           ##运用匿名函数优化，def  exam():下cmds改为
#     result=x+ y
#
# def  sub(x,y):
#     result=x- y

def  exam():
    # cmds={'+': add,'-': sub }
    cmds={'+':lambda x,y: x+y, '-':lambda x,y: x-y}
    nums=[randint(1,100) for i in range(2)]       #[20,10]随机两个数
    nums.sort(reverse=True)       ##相当于nums.sort ’默认升序排序‘ ,再nums.reverse()  ‘反转’
    op=choice('+-')
    result=cmds[op](*nums)
    prompt='%s %s %s =' % (nums[0],op,nums[1])
    #answer=int(input(prompt))
    counter=0

    while counter<3:
        try:
            answer=int(input(prompt))
        except:
            print()
            continue

        if answer ==result:
            print('Very good!!!')
            break
        else:
            print('Wrong Answer!')

        counter+=1
    else:
        print('The answer:')
        print('%s %s' %(prompt,result))

if __name__ == '__main__':
    while True:
        exam()
        try:
            yn=input('continue(y/n)?').strip()[0]
        except IndexError:                          ##enter
            continue
        except  (KeyboardInterrupt,EOFError):       ##ctrl+c   ctrl+d
            yn='n'

        if yn in 'Nn':
            print('\nBye-bye')
            break
