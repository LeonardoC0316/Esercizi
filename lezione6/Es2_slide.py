class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    def printinfo(self):
        print(self.name, self.studyProgram, self.age, self.gender)

leonardo = Student("Leonardo", "Math", 21, "Male")
alessio = Student("Alessio", "Ita", 24, "Male")
mirko = Student("Mirko", "Story", 26, "Male")

Student.printinfo(leonardo)
