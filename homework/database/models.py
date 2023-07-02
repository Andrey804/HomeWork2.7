from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base


class Group(Base):

    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10))
    student = relationship('Student')


class Teacher(Base):

    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    subject = relationship('Subject')


class Subject(Base):

    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    teacher_id = Column('teacher_id', ForeignKey('teachers.id'))
    score = relationship('Score')


class Student(Base):

    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    group_id = Column('group_id', ForeignKey('groups.id'))
    score = relationship('Score')


class Score(Base):

    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column('student_id', ForeignKey('students.id'))
    subject_id = Column('subject_id', ForeignKey('subjects.id'))
    score = Column(Integer)
    score_date = Column(Date, default=datetime.now().date())

