# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] ='hard to guess'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://chanst:cstdhr361@localhost:3306/info' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app) #实例化


class Role(db.Model):
    __tablename__ = 'people'  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # 定义列对象
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return '<Role {}> '.format(self.name)



def main():
    #user_role = Role(name='User')
    #db.session.add_all([user_role])  # 准备把对象写入数据库之前，先要将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称事物
    u = Role.query.filter_by(name='nihao').first()
    u.name = 'buhao'
    db.session.add(u)
    db.session.commit()

if __name__ == '__main__':
    main()