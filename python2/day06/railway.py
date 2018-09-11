# 1.  在屏幕上打印20个#号
# 2.  符号@从20个#号穿过
# 3.  当@符号到达尾部,再从头开始import  time

import  sys
import  time

l=19
counter=0
print('#' * (l+1),   end=' ')  ##\r回车不换行，原位覆盖

while True:
    sys.stdout.flush()
    time.sleep(0.3)
    print('\r%s@%s' % ('#' * counter, '#' * (l - counter)), end='')
    counter += 1
    if counter > l:
        counter = 0
