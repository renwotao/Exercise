#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	图形界面
	
	Python 支持多种图形界面的第三方库，包括：
	 TK
	 wxWidgets
	 Qt
	 GTK

	Python 自带的库是支持 Tk 的 Tkinter，使用 Tkinter，无需安装任何抱，就亏直接使用。
'''

'''
	Tkinter
	
	Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；

	Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；

	Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
'''
from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()
	
'''
	在 GUI 中，每个 Button，Label，输入框等，都是一个 Widget。
	Frame 则是可以容纳其他 Widget 的 Widget，所有的 Widget 组合起来就是一棵树。
	pack() 方法把 Widget 加入到父容器中，并实现布局。pack() 是最简单的布局，
	grid() 可以实现更复杂的布局。
	
'''
app = Application()

# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()


'''
	输入文本
'''
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text='hello', command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()


