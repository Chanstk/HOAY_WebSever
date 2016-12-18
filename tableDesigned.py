# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] ='hard to guess'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://chanst:cstdhr361@localhost:3306/HOAY' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app) #实例化

'''用户表'''
class User(db.Model):
    __tablename__ = 'User'  # 定义表名
    UserID = db.Column(db.Integer, primary_key=True)    #用户ID
    PassWord = db.Column(db.String(10)) #密码
    NickName = db.Column(db.String(10)) #昵称
    Sex = db.Column(db.Boolean) #性别 1为男 0为女
    Age = db.Column(db.Integer) #年龄
    ImagePath = db.Column(db.String(50)) #头像路径

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''用户位置表'''
class UserLocation(db.Model):
    __tablename__ = 'UserLocation'
    key = db.Column(db.Integer,primary_key=True)
    UserID = db.Column(db.Integer) #用户ID
    Longitude = db.Column(db.Float) #经度位置
    Altitude = db.Column(db.Float) #纬度位置
    time = db.Column(db.Time) #时间

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''相遇表'''
class Encounter(db.Model):
    __table__name = 'Encounter'
    EncounterID = db.Column(db.Integer, primary_key=True)
    UserID_1 = db.Column(db.Integer)   #用户1ID
    UserID_2 = db.Column(db.Integer)   #用户2ID
    MeetTime = db.Column(db.Time)   #相遇时间
    Longitude = db.Column(db.Float)  # 相遇经度位置
    Altitude = db.Column(db.Float)  # 相遇纬度位置
    State = db.Column(db.Boolean)   #0为正常模式，1为夜游模式

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''夜游表'''
class NightMode(db.Model):
    __tablename__ = 'NightMode'
    key = db.Column(db.Integer,primary_key=True)
    UserID = db.Column(db.Integer)  # 用户ID
    Identity = db.Column(db.Boolean)    #身份 0为鬼差，1为魂魄
    Grade = db.Column(db.Integer)   #等级
    State = db.Column(db.Integer)   #状态 0 为自由，1为被捕中， 2 为被关

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''捕捉表'''
class Caputure(db.Model):
    __tablename__ = 'Caputure'
    CatchID = db.Column(db.Integer, primary_key=True)  # 自增
    PredatorID = db.Column(db.Integer)  # 捕捉者ID
    PrisonerID = db.Column(db.Integer)  # 被捕者ID
    Grade = db.Column(db.Integer)   #等级
    State = db.Column(db.Integer)  #状态 0 为读条，1为成功， -1 为失败
    Longitude = db.Column(db.Float)  # 捕捉经度位置
    Altitude = db.Column(db.Float)  # 捕捉纬度位置

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''地雷表'''
class Mine(db.Model):
    __tablename__ = 'Mine'
    MineID = db.Column(db.Integer, primary_key=True)
    MineState = db.Column(db.Integer)   #地雷状态0未投放，1已投放未生效，2已投放已生效，3已爆炸
    OwnerID = db.Column(db.Integer)  #拥有者ID
    Longitude = db.Column(db.Float)  # 投放经度位置
    Altitude = db.Column(db.Float)  # 投放纬度位置
    SetTime = db.Column(db.Time)  # 投放时间
    ValidTime = db.Column(db.Time) #生效时间
    ExplodeID = db.Column(db.Integer) #被炸者ID

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''小纸条表'''
class Note(db.Model):
    __tablename__ = 'Note'
    NoteID = db.Column(db.Integer, primary_key=True) #小纸条ID
    OwnerID = db.Column(db.Integer)  # 拥有者ID
    Content = db.Column(db.String(150)) #小纸条内容
    State = db.Column(db.Integer) #初始为0，每次阅读+1
    SetTime = db.Column(db.Time)  # 投放时间
    EndTime = db.Column(db.Time)  # 无效时间
    Reader = db.Column(db.Integer) #可阅读人数
    Longitude = db.Column(db.Float)  # 投放经度位置
    Altitude = db.Column(db.Float)  # 投放纬度位置

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''小纸条回复表'''
class NoteReply(db.Model):
    __tablename__ = 'NoteReply'
    key = db.Column(db.Integer,primary_key=True)
    NoteID = db.Column(db.Integer)  # 小纸条ID
    PickerID = db.Column(db.Integer) #回复者ID
    Longitude = db.Column(db.Float)  # 捡到地点经度位置
    Altitude = db.Column(db.Float)  # 捡到地点纬度位置
    Time = db.Column(db.Time)  # 回复时间
    Content = db.Column(db.String(150))  # 回复内容

    def __repr__(self):
        return '<Role {}> '.format(self.name)


'''关系表'''
class Relation(db.Model):
    __tablename__ = 'Relation'
    UserID_1 = db.Column(db.Integer,primary_key=True)  # 用户1ID
    UserID_2 = db.Column(db.Integer,primary_key=True)  # 用户2ID
    FateValue = db.Column(db.Integer) #缘分值
    UnFateValue = db.Column(db.Integer) #孽缘值
    Follow = db.Column(db.Integer) #关注与否
    PhotoValue = db.Column(db.Integer) #碎片值

    def __repr__(self):
        return '<Role {}> '.format(self.name)

def main():
    db.create_all()
if __name__ == '__main__':
    main()