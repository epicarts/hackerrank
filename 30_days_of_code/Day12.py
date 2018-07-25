#!/bin/python3


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	def __init__(self, firstName, lastName, idNumber, score):
        Person.__init__(self, firstName, lastName, idNumber)
        self.result_score = score

    def calculate(self):
        avr = 0
        for i in self.result_score:
            avr = avr + i

        avr = avr / len(self.result_score)

        if(90 <= avr <= 100):
            print('Grade: O')
            quit()
        elif(80 <= avr < 90):
            print('Grade: E')
            quit()
        elif(70 <= avr < 80):
            print('Grade: A')
            quit()
        elif(55 <= avr < 70):
            print('Grade: P')
            quit()
        elif(40 <= avr < 55):
            print('Grade: D')
            quit()
        else:
            print('Grade: T')
            quit()


line = input().split()

numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
