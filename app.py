# -*- coding = utf-8 -*-
# @Time : 2022/3/27 22:00
# @Author : Luna
# @File : app.py
# @Software: PyCharm
#@github:sky18

from flask import Flask,render_template,request
import datetime


app = Flask(__name__)

#路由解析，通过用户访问的路径，匹配相应的解析
@app.route('/')
def hello_world():
    return render_template("index.html")

# @app.route("/index")
# def hello():
#     return "您好"

# #通过访问路径，获取用户的字符串参数
# @app.route("/user/<name>")
# def welcome(name):
#     return "您好,%s"%name
#
# #路由的路径不能重复，用户通过唯一路径来访问特定的函数
# @app.route("/user/<int:id>")
# def welcome2(id):
#     return "您好,%d 号的会员"%id
#
#
# #返回给用户渲染后的网页
# # @app.route("/")
# # def index2():
# #     return render_template("temp.html")
#
# #向页面传递一些变量
# @app.route("/")
# def index2():
#     time = datetime.date.today()  #普通变量
#     name = ["小张","小王","小刘"]  #列表类型
#     task = {"任务":"打扫卫生","时间":"3小时"}
#     return render_template("temp.html",var = time,list = name,task = task)
#
# #表单提交
# @app.route('/test/register')
# def register():
#     return render_template("test/register.html")
#
# #接收表达提交的路由，需要指定method为POST
# @app.route('/result',methods=['POST','GET'])
# def result():
#     if request.method == "POST":
#         result = request.form
#         return render_template("test/result.html",result=result)
#     # else:
#     #     result = ""


if __name__ == '__main__':
    app.run(debug=True)