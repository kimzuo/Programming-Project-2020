#Import area
import tkinter
import re
import tkinter.messagebox
import random

#GUI


#Main Program
class Question:     
    def __init__(self, question, answer, dummies):
        self.question = question
        self.answer = answer
        self.dummies = dummies
        self.set_answers()
         
    def set_answers(self):
        self.answers = self.dummies
        self.answers.insert(random.randrange(len(self.dummies) + 1), self.answer)

class Quiz:
    def __init__(self):
        self.questions = [Question('',
                        '',
                        []),
                        Question('',
                        '',
                        [])]

    def take_quiz(self):
        for q in self.questions:
            print( q.question )
            for i in range(len(q.answers)):
                print("\t" + str(i ) + "\t" + q.answers[i])
            print()
            self.process_answer(q)
            
    def process_answer(self,q):
        user_answer = -1
        while not 0 <= user_answer < len(q.answers):
            a = input("Please type the number of your answer here: ")
            try:
                user_answer = int(a)
                if not 0 <= user_answer < len(q.answers):
                     print("\nThat was out of range\n")
                elif user_answer == q.answers.index(q.answer):
                    print("\nWell Done!!\n")
                else:
                    print("\nIncorrect, the answer is " + q.answer + "\n")
            except ValueError:
                print("\nThat was not a sensible input. Integers only please.\n")

if __name__ == "__main__":
    text_quiz = Quiz()
    text_quiz.take_quiz()
Quiz.mainloop
