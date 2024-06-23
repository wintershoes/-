import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request, jsonify
import os
from abc import ABC, abstractmethod
from sqlalchemy.inspection import inspect
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import json
from flask_cors import CORS
from datetime import datetime
from flask import request, jsonify
import pytz
import base64
from sqlalchemy import CheckConstraint

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app) #允许跨域名访问
# 配置 SQLAlchemy，指向本地 SQLite 数据库文件
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///" + os.path.join(basedir, 'database.sqlite')
# 用于指示是否追踪对象的修改并发送信号给 Flask 应用程序
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 设置 Flask 应用的密钥，用于保持客户端会话的安全
app.config["SECRET_KEY"] = "major"

db = SQLAlchemy(app)

# 定义数据库模型
from sqlalchemy import CheckConstraint

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)
    registration_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    role = db.Column(db.String(20), nullable=False)
    __table_args__ = (
        CheckConstraint("role IN ('student', 'teacher', 'admin')"),
    )

    reservations = db.relationship('Reservation', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    scores = db.relationship('Score', backref='user', lazy=True)

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    book_image = db.Column(db.LargeBinary)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    isbn = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    reservation_count = db.Column(db.Integer, default=0)
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    __table_args__ = (
        CheckConstraint("status IN ('available', 'reserved', 'borrowed', 'damaged')"),
    )

    reservations = db.relationship('Reservation', backref='book', lazy=True)
    reviews = db.relationship('Review', backref='book', lazy=True)

class Reservation(db.Model):
    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    reservation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False)
    book_location = db.Column(db.String(50), nullable=False)
    reservation_location = db.Column(db.String(50), nullable=False)
    __table_args__ = (
        CheckConstraint("status IN ('confirmed', 'cancelled', 'completed', 'failed')"),
    )

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5"),
    )

class Score(db.Model):
    score_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    points = db.Column(db.Integer, nullable=False)
    change_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    description = db.Column(db.String(255))

class Activity(db.Model):
    activity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    end_time = db.Column(db.TIMESTAMP, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(255))



if __name__ == '__main__':
    app.run(debug=True)