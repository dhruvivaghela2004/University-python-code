#create a class university which is acting as a parent class for 2 of the classes  cllg1 and cllg 2 and also perform constructor chaining and method chaining in the example and method chaining in child classes

#class
class University():
    UNIVERSITY_name='ABC University'
    HEAD='Dr. XYZ'
    
    #constructor
    def __init__(self,uid,name,mailid,contactnumber):
        self.UID=uid
        self.NAME=name
        self.MAILID=mailid
        self.CONTACTNUMBER=contactnumber
    
    def display(self):
        print(self.UID,self.NAME,self.MAILID,self.CONTACTNUMBER)
        
    @classmethod
    def displaycls(cls):
        print(cls.UNIVERSITY_name,cls.HEAD)    
    
class Cllg1(University):
    DEAN='Dr. PQR'
    CONTACTNUMBER=1234567890
    
    def __init__(self,uid,name,mailid,contactnumber,department,dob):
        super().__init__(uid,name,mailid,contactnumber)
        self.DEPARTMENT=department
        self.DOB=dob
        
    def display(self):
        super().display()
        print(self.DEPARTMENT,self.DOB)
        
    @classmethod
    def displaycls(cls):
        super().displaycls()
        print(cls.DEAN,cls.CONTACTNUMBER)    
        
        
class Cllg2(University):
    DEAN='Dr. PQR'
    CONTACTNUMBER=1234567890
    FACULTY='Dr. ABC'
    
    def __init__(self,uid,name,mailid,contactnumber,department,dob,years_of_experience):
        super().__init__(uid,name,mailid,contactnumber)
        self.DEPARTMENT=department
        self.DOB=dob
        self.YEARS_OF_EXPERIENCE=years_of_experience
        
    def display(self):
        super().display()
        print(self.DEPARTMENT,self.DOB,self.YEARS_OF_EXPERIENCE)
        
    @classmethod
    def displaycls(cls):
        super().displaycls()
        print(cls.DEAN,cls.CONTACTNUMBER,cls.FACULTY)          
        
        
University.displaycls()
c0=University(100,'University','university@gmail.com',1234567890)
c0.display()

c1=Cllg1(101,'Alice','alice@gmail.com',9876543210,'IT','08th may 2004')#object creation for cllg1 class
c1.display()
Cllg1.displaycls()  

c2=Cllg2(102,'Bob','bob@gmail.com',9876543211,'CSE','08th june 2004',15)#object creation for cllg2 class
c2.display()
Cllg2.displaycls()  

