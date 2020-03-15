'''
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
'''

import tkinter as tk
import random

 
class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('750x500')
        
        initface(self.root)        
                
class initface():
    def __init__(self,master):
        
        self.master = master
        self.master.config(bg='white')
        self.initface = tk.Frame(self.master,)
        self.initface.pack()
        w1 = tk.Message(self.initface,text = 'Welcom to the Quiz Master',width = 100)
        w1.pack()
        btn = tk.Button(self.initface,text='change',command=self.change)
        btn.pack()
        
    def change(self,):       
        self.initface.pack_forget()
        face1(self.master)      
 
class face1():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='blue')
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()
        btn_back = tk.Button(self.face1,text='back to base menu',command=self.back)
        btn_back.pack()
    
    def back(self):
        self.face1.pack_forget()
        initface(self.master)
            
if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()

