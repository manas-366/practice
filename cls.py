class student:
    @classmethod
    def m1(cls):
        cls.school="sbhs"
        cls.address="bk road"
    @classmethod
    def m2(cls):
        cls.course="python"
        cls.faculty="ram"

    def m3(self):
        self.student1_name="manas"
        self.student1_class="10th"
        self.student_age="16"

    def m4(self):
        self.student2_name="rahul"
        self.student2_class="8th"
        self.student_age="14"

student.m1()
student.m2()
s1=student()
s2=student()
s1.m3()
s2.m4()
print(s1)
print(s2)
