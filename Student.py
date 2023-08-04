class Student():

    def __init__(self):
        self.name = input("Enter the name of the student")
        self.rollno =input("Enter the rollno")
        print("Student",self.name,"created with roll number",self.rollno)
        self.sub1 = int(input("Enter Maths marks"))
        self.sub2 = int(input("Enter science marks"))
        self.sub3 = int(input("Enter English marks"))
        return

    def getmarks(self):
        self.total = self.sub1 + self.sub2 + self.sub3
        print(self.total)
        return





