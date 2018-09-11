# 案例7:记账程序
# 1.  假设在记账时,有一万元钱
# 2.  无论是开销还是收入都要进行记账
# 3.  记账内容包括时间、金额和说明等
# 4.  记账数据要求永久存储

#想好账本文件格式：
#时间  收入   支出   余额    说明
#余额文件，原位覆盖加减

#1、尝试写
# import  pickle
# import  time
# import  os
#
# def save(wallet,record):
#
#     amount=int(input('收入：'))
#     comment=input('说明：')
#     date=time.strftime('%Y-%m-%d')
#
#     with open(wallet,'wb') as fobj:
#         balance=pickle.load(fobj) +amount
#     with open(wallet,'wb') as fobj:
#         pickle.dump(wallet,fobj)
#     with open(record,'a')  as fobj:
#         fobj.write('%-12s%-8s%-8s%-10s%-20s\n' % (date, '', amount, balance, comment))
#
# def cost(wallet,record):
#
#     amount=int(input('收入：'))
#     comment=input('说明：')
#     date=time.strftime('%Y-%m-%d')
#
#     with open(wallet,'wb') as fobj:
#         balance=pickle.load(fobj) -amount
#     with open(wallet,'wb') as fobj:
#         pickle.dump(wallet,fobj)
#     with open(record,'a')  as fobj:
#         fobj.write('%-12s%-8s%-8s%-10s%-20s\n' % (date, amount,'', balance, comment))
#
# def view(wallet,record):
#     print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'cost', 'save', 'balace', 'comment'))
#     with open(record) as fobj:
#         for line in fobj:
#             print(line, end='')
#     with open(wallet, 'rb') as fobj:
#         balance = pickle.load(fobj)
#     print("Latest Balance: %d" % balance)
#
# def show_medu():
#     cmds={'0':save,'1':cost,'2':view,'3':exit}
#     info='''(0)save
#     （1）cost
#     （2）view
#      (3)exit
#     选择（0/1/2/3）'''
#     choice=input('input your choine0/1/2/3:')
#     wallet='wallet.data'
#     record='/tmp/item.txt'
#     if not os.path.exists(wallet):
#         with   open(wallet,'wb') as fobj:
#             pickle.dump(10000,fobj)
#
#     while  True:
#         if choice not in '0123':
#             print('重试')
#
#
#         cmds[choice](wallet,record)
#
# if __name__ == '__main__':
#      show_medu()


##2、老师讲解：
import  os
import  time
import  pickle as p

def save_money(record,wallet):
    amount=int(input('amount:'))
    comment=input('comment:')
    date=time.strftime('%Y-%m-%d')

    with open(wallet,'rb')as fobj:
        balance=p.load(fobj) + amount
    with open(wallet,'wb')as  fobj:
        p.dump(balance,fobj)
    with open(record,'a')as fobj:
        fobj.write(
            '%-15s%-8s%-8s%-10s%-20s\n' %(date,amount,'',balance,comment)
        )

def cost_money(record,wallet):
    amount=int(input('amount:'))
    comment=input('comment:')
    date=time.strftime('%Y-%m-%d')

    with open(wallet,'rb')as fobj:
        balance=p.load(fobj) - amount
    with open(wallet,'wb')as  fobj:
        p.dump(balance,fobj)
    with open(record,'a')as fobj:
        fobj.write(
            '%-15s%-8s%-8s%-10s%-20s\n' %(date,'',amount,balance,comment)
        )

def  query_money(record,wallet):
    print('%-15s%-8s%-8s%-10s%-20s' %\
          ('date', 'cost', 'save', 'balace', 'comment'))
    with open(record) as fobj:
        for line in fobj:
            print(line, end='')
    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj)
        print("\033[34;1mLatest Balance: %d\033[0m" % balance)

def  show_menu():
    record='record.txt'
    wallet='wallet.data'
    if not os.path.exists(wallet):
        with   open(wallet,'wb')as fobj:
            p.dump(10000,fobj)

    cmds = {'0': save_money, '1': cost_money, '2': query_money}

    prompt='''(0)save_money
(1)cost_money
(2)query_money
(3)exit
    please input your choine(0/1/2/3):'''
    while True:
        try:
            choice = input(prompt).strip()[0]
        except  IndexError:
            continue
        except  (KeyboardInterrupt,EOFError):
            print('\nBye-bye')
            choice='3'          ##=3时，break

        if  choice  not in '0123':
            print('Invalid  input. Try again!!!' )
            continue

        if choice =='3':
            break

        cmds[choice](record,wallet)

if __name__ == '__main__':
    show_menu()





































