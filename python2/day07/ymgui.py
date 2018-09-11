##安装tkinter模块
#yum -y install tk-devel tcl-devel  sqlite-devel
#cd /opt/Python-3.6.1
#./configure  --prefix=/usr/local/  ;  make  ;make install
###验证：                  #弹出一个窗口
# >>> import tkinter
# >>> root  =tkinter.Tk()

#用偏函数：
import  tkinter
from  functools  import  partial

root=tkinter.Tk()
lb1=tkinter.Label(root,text='Hello World',font='Arial  15')
MyButten=partial(tkinter.Button,root,bg='blue',fg='white')
b1=MyButten(text='Butten 1')
b2=MyButten(text='Butten 2')
b3=MyButten(text='Butten 3',command=root.quit)
lb1.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()


#没有用偏函数
# b1=tkinter.Button(root,bg='blue',fg='white',text='Button 1')
# b2=tkinter.Button(root,bg='blue',fg='white',text='Button 2')
# b3=tkinter.Button(root,bg='blue',fg='white',text='Button 3')



