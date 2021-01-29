import os, random, string

from sqlalchemy import create_engine  # database engine
from sqlalchemy import Column, String, Integer, ForeignKey  # SQLAlchemy datatypes
from sqlalchemy.orm import relationship  # SQLAlchemy relationships

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.orm import sessionmaker

DB_NAME = 'UNIVERSITY_DB'

class Staff(Base):
    __tablename__ = 'Staff'
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)

    hr_records = relationship('HR_record')
    exams = relationship('Exam')

class Faculty(Base):
    __tablename__ = 'Faculty'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

class FGroup(Base):
    __tablename__ = 'FGroup'
    id = Column('id', Integer, primary_key=True)
    number = Column('number', Integer)
    faculty_id = Column('faculty_id', Integer,
        ForeignKey('Faculty.id'))

class Student(Base):
    __tablename__ = 'Student'
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    group_id = Column('group_id', Integer,
        ForeignKey('FGroup.id'))

class Exam(Base):
    __tablename__ = 'Exam'
    id = Column('id', Integer, primary_key=True)
    discipline = Column('discipline', String)
    staff_id = Column('staff_id', Integer,
        ForeignKey('Staff.id'))

class Exam_record(Base):
    __tablename__  = 'Exam_record'
    id = Column('id', Integer, primary_key=True)
    date = Column('date', String)
    grade = Column('grade', Integer)
    student_id = Column('student_id', Integer,
        ForeignKey('Student.id'))
    exam_id = Column('exam_id', Integer,
        ForeignKey('Exam.id'))

class HR_record(Base):
    __tablename__ = 'HR_record'
    id = Column('id', Integer, primary_key=True)
    position = Column('position', String)
    staff_id = Column('staff_id', Integer,
        ForeignKey('Staff.id'))
    faculty_id = Column('faculty_id', Integer,
        ForeignKey('Faculty.id'))