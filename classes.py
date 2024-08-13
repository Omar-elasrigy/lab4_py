class Human:

    def __init__(self,name,age,gender,nationality):
        self.name=name
        self.age=age
        self.gender=gender
        self.nationality=nationality
    def works(self):
        print(self.name,"works")
    def run(self):
        if self.age<40:
            print(self.name,"has energy to run and has",self.age,"years")
        else:
            print(self.name,"has no energy to run and has",self.age,"years")
class Employee:
    total_employees=0
    company_name="Intel"

    def __init__(self,name,gender,salary):
        self.name=name
        self.gender=gender
        self.salary=salary
        Employee.total_employees +=1
    def works(self):
        print(self.name,"works")
    def run(self):
        if self.age<40:
            print(self.name,"has energy to run and has",self.age,"years")
        else:
            print(self.name,"has no energy to run and has",self.age,"years")
    def update_salary(self,new_salary):
        self.salary=new_salary
    @classmethod
    def get_company_name(cls):
        return cls.company_name
    @classmethod
    def set_company_name(cls,new_company_name):
        cls.company_name=new_company_name

# man=Human("Omar",24,"male","Egyptian")
# man.works()
# man.run()
emp=Employee("Omar","male",3000)
print(emp.get_company_name())
emp.set_company_name("Microsoft")
print(emp.get_company_name())
