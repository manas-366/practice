class student:
    def read_stud(self):
        print("id of current method=",id(self))


s1=student()
s2=student()
print("id of s1 data=",id(s1))
s1.read_stud()
print("id of s2 data=",id (s2))
s2.read_stud()
