#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	SMTP 发送邮件
	
	SMTP 是发送邮件的协议，Python 内置对 SMTP 的支持，可以发送纯文本邮件，HTML 邮件以及带附件的邮件。
	
	Python 对 SMTP 支持有 smtplib 和 email 两个模块，email 负责构造邮件，smtplib负责发送邮件。
'''
from email.mime.text import MIMEText
'''
	构造 MIMEText 对象时，第一个参数就是邮件正文，第二个参数是 MIME 的 subtype，
	传入'plain' 表示纯文本，最终的 MIME 就是'text/plain'，最后一定要用 utf-8
编码保证多语言兼容性。
'''
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入 Email 地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址
to_addr = input('To: ')
# 输入 SMTP 服务器地址
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP 协议默认端口是 25
# 用 set_debuglevel(1) 打印出和 SMTP 服务器交互的所有信息
server.set_debuglevel(1)
# login方法用来登陆 SMTP 服务器
server.login(from_addr, password)
# sendmail() 方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个 str, as_string() 把 MIMEText 对象变成 str。
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


'''
	以上代码发送的邮件，有如下问题：
	1. 邮件没有主题；
	2. 收件人的名字没有显示为好友的名字，比如 Mr Green <green@examle.com>;
	3. 明明收到了邮件，却提示不在收件人中。

	这是因为邮件主题，如何显示发件人，收件人等信息并不是通过 SMTP 协议发给 MTA，
	而是包含在 MTA 的文本中，所以，必须把 From, To 和 Subject 添加到 MIMEText中，才是一封完整的邮件。
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 使用_format_addr() 来格式化一个邮件地址
# 注意不能简单传入 name <addr@example.com>，因为如果包含中文，需要通过 Header 对象进行编码
# Header 对象编码的文本，包含 utf-8 编码信息和 Base64 编码的文本。
# msg['To'] 接收的是字符串而不是list，如果有多个邮件地址，用，分隔即可。
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自 SMTP 的问候...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

'''
	发送 HTML 邮件
'''

msg = MIMEText('<html><body><h1>Hello</h1>'+
	'<p>send by <a href="http://www.python.org">Python</a>...</p>'+
	'</body></html>', 'html', 'utf-8')

#server.sendmail(from_addr, [to_addr], msg.as_string())
#server.quit()


'''
	发送附件
	
	带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身。
	
	1. 构造一个MIMEMultipart 对象代表邮件本身
	2. 然后在里面添加一个 MIMEText 作为邮件正文
	3. 再继续添加附件 MIMEBase 对象
'''

# 邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# 邮件正文是 MIMEText
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个 MIMEBase，从本地读取一个图片
with open('/home/Pictures/test.jpg', 'rb') as f:
	# 设置附件的 MIME 和文件名，这里是 png 卫星
	mime = MIMEBase('image', 'jpg', filename='test.jpg')
	# 加上必要的头信息
	mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	# 把附件的内容度进来
	mime.set_payload(f.read())
	# 用 Base64 编码
	encoder.encode_base64(mime)
	# 添加到 MIMEMultipart
	msg.attach(mime)

'''
	发送图片
	
	直接在HTML邮件正文中中嵌入图片时，邮件服务商都会自动屏蔽带有外链的图片，
	因为不知道这些链接是否指向恶意网站。

	要把图片嵌入到邮件正文中，只需按照发送附件的方式
	1. 先把邮件作为附件添加进去
	2. 然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了,
	   如果有多个图片，给它们依次编号，然后引用不同的cid:x即可
'''
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
	'<p><img src="cid:0"></p>' +
	'</body></html>', 'html', 'utf-8'))

'''
	同时支持 HTML 和 Plain 格式
'''
'''
	如果发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，
	但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？


	办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，
	就可以自动降级查看纯文本邮件。
'''
'''
msg = MIMEMultipart('alternative')
msg['From'] = ...
msg['To'] = ...
msg['Subject'] = ...

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...
'''


'''
	加密 SMTP

	使用标准的25端口连接SMTP服务器时，使用的是明文传输，
	发送邮件的整个过程可能会被窃听。要更安全地发送邮件，
	可以加密SMTP会话，实际上就是先创建SSL安全连接，
	然后再使用SMTP协议发送邮件。
'''
'''
	某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。
	如何通过Gmail提供的安全SMTP发送邮件。必须知道，Gmail的SMTP端口是587
'''
'''
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
...
'''


'''
	构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，
	就表示一个文本邮件对象，如果构造一个MIMEImage对象，
	就表示一个作为附件的图片，要把多个对象组合起来，
	就用MIMEMultipart对象，而MIMEBase可以表示任何对象。

它们的继承关系如下:
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''
