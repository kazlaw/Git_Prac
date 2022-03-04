import datetime

class Person:
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname=lname
        
        
    def Clockin(self):
        print(self.firstname , self.lastname + ' came in at ',datetime.datetime.now())

class Salary(Person):
    def __init__(self, fname,lname ,salo):
        super().__init__(fname,lname)
        self.salary =salo
        salo =int(input('Enter Amount Paid:'))

    def Report(self):
        print(self.firstname,self.lastname + f' was paid ${self.salary}')


test = Salary('Replace name','Replace name','')

test.Clockin()

print('And')

test.Report()
