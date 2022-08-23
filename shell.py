from user.models import *
from datetime import datetime

l1 = Language.objects.create(name='Python', month_to_learn=6)
l2 = Language.objects.create(name='JavaScript', month_to_learn=6)
l3 = Language.objects.create(name='UX UI design', month_to_learn=6)

s1 = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
                            work_study_place='School №13', has_own_notebook=True, preferred_os='windows'
                            )
s2 = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',
                            work_study_place='TV', has_own_notebook=True, preferred_os='mac'
                            )
s3 = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312',
                            work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux'
                            )

m1 = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.comm', phone_number='0500545454',
                           main_work=None, experience='2021-10-23'
                           )
m2 = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
                           main_work='University of Fort Collins', experience='2010-09-18'
                           )

m2.course = Course.objects.create(name=l)
m2.students.set([s1, s2], through_defaults={'name': 'Python 21', 'language': l1,
                                            'date_started':'2022-08-01'})

m1.students.set(s3, through_defaults={'name': 'Python 21', 'language': l1,
                                      'date_started': '2022-08-01'})
