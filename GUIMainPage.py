import tkinter
from tkinter import messagebox
import time

Version = "v1.1"


class Mainpage(object):
    def __init__(self, lessions=None, master=None):
        self.second = 0
        self.root = tkinter.Tk()
        self.lessions = lessions
        self.root.geometry("500x313")
        self.root.title("四川大学抢课软件" + Version)
        try:
            # 运行代码时记得添加一个gif图片文件，不然是会出错的，只能是gif文件
            self.canvas = tkinter.Canvas(self.root, height=300, width=500)  # 创建画布，也就是图片在画面上的大小
            self.image_file = tkinter.PhotoImage(file='scu.jpg.gif')  # 加载图片文件
            self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上
            self.canvas.pack(side='top')  # 放置画布（为上端）
        except:
            pass
        finally:
            # 创建一个`label`名为`Account: `
            self.label_course = tkinter.Label(self.root, text='抢课的课程号:')
            # 创建一个`label`名为`Password: `
            self.label_list_id = tkinter.Label(self.root, text='课序号:')
            # 创建抢课信息显示窗口
            self.label_info = tkinter.Label(self.root, text='欢迎使用四川大学抢课软件' + Version)

            # 创建一个课程号输入框,并设置尺寸
            self.input_course = tkinter.Entry(self.root, width=30)
            # 创建一个课序号输入框,并设置尺寸
            self.input_list_id = tkinter.Entry(self.root, width=30)

            # 创建一个抢课系统的按钮
            self.do_button = tkinter.Button(self.root, command=self.take_lessions, text="Do it", width=10)
            # 创建一个停止系统的按钮,没有self.quit,不可以在函数这里加括号，否则就是执行
            self.siginUp_button = tkinter.Button(self.root, command=self.Quit, text="Sign up", width=10)
            # 创建一个新窗口
            self.newwindow_button = tkinter.Button(self.root, command=self.newwindow, text="new window", width=10)

            # 创建后一定要布局，否则root面板上不会显示
            self.label_course.place(x=60, y=150)
            self.label_list_id.place(x=60, y=175)
            self.label_info.place(x=60, y=200)
            self.input_course.place(x=135, y=150)
            self.input_list_id.place(x=135, y=175)
            self.do_button.place(x=140, y=235)
            self.siginUp_button.place(x=240, y=235)
            self.newwindow_button.place(x=340, y=235)

    def take_lessions(self):

        kch = self.input_course.get()
        kxh = self.input_list_id.get()
        # 输入为空，跳过这次查询
        if kch is None and kxh is None:
            return None
        result = self.lessions.scu_post_cour(kch, kxh)
        if result == 1:
            self.label_info['text'] = "选课成功"
        elif result == -1:
            # TODO: 加入延时重试
            self.second = 60
            self.label_info['text'] = "现在是非选课时段,将会在%.0f秒后重试" % self.second
            self.label_info.update()
            while self.second >= 0:
                time.sleep(0.1)
                self.second -= 0.1
                self.label_info['text'] = "现在是非选课时段,将会在%.0f秒后重试" % self.second
                self.label_info.update()
            self.take_lessions()
        else:
            self.label_info['text'] = "选课失败"

    def newwindow(self):
        Mainpage(self.lessions)

    def Quit(self):
        self.root.destroy()
