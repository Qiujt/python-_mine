# 案例2:编写酒店类
# 1.  用于计算住宿开销
# 2.  酒店有会员卡可以打九折
# 3.  每天早餐15元
# 4.  根据住宿天数返加总费用

class  Hotel:
    def __init__(self,basic=200,cf=1.0,br=15):
        self.basic=basic
        self.cutoff=cf
        self.br=br

    def calc(self,days=1):
        return  (self.basic * self.cutoff + self.br) *days

if __name__ == '__main__':
    stdroom=Hotel()
    print(stdroom.calc())
    print(stdroom.calc(2))
    bigbed=Hotel(basic=230,cf=0.9)
    print(bigbed.calc())
    print(bigbed.calc(2))