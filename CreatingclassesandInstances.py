class Students:

    def __init__(self,firstname,lastname,enrollment):
        self.firstname = firstname
        self.lastname = lastname
        self.enrollment = enrollment
    
    def getfullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

    def generate_emailid(self):
        email_id = self.firstname.lower()+'.'+self.lastname.lower()+'@hmritm.in'
        return email_id
    
student_1 = Students('Gyanender','Kumar',2513302720)
print(student_1.getfullname())
print(student_1.generate_emailid())
