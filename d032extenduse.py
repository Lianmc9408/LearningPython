#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-11 上午8:54

class School(object):
	def __init__(self, name, addr):
		self.name = name
		self.addr = addr
		self.students = []
		self.teachers = []

	def enroll(self, stu_obj):
		print('为学生%s办理注册手续' % stu_obj.name)
		self.students.append(stu_obj)

	def hire(self, staff_obj):
		print('招聘%s老师' % staff_obj.name)
		self.teachers.append(staff_obj)


class SchoolMember(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def tell(self):
		pass


class Teacher(SchoolMember):
	def __init__(self, name, age, sex, salary, course):
		super().__init__(name, age, sex)
		self.salary = salary
		self.course = course

	def tell(self):
		print('''-------info of Teacher:%s-------
					Name:%s
					Age :%s
					Sex :%s
					Salary:%s
					course:%s
				''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

	def teach(self):
		print('%s is teaching course [%s]' % (self.name, self.course))


class Student(SchoolMember):
	def __init__(self, name, age, sex, stu_id, grade):
		super().__init__(name, age, sex)
		self.stu_id = stu_id
		self.grade = grade

	def tell(self):
		print('''-------info of Teacher:%s-------
					Name:%s
					Age :%s
					Sex :%s
					Stuid:%s
					Grade:%s
				''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

	def pay_tuition(self, amount):
		print('%s has paid tution for $%s' % (self.name, amount))


school = School('asdasd', 'China')

t1 = Teacher('qwe', 30, 'm', 20, 'math')
t2 = Teacher('zxc', 11, 'f', 22, 'tt')

s1 = Student('cc', 33, 'mf', 123, '301')
s2 = Student('dd', 11, 'f', 234, '401')

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)

school.teachers[0].teach()

for stu in school.students:
	stu.pay_tuition(500)
