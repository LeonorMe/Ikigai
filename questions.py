import json
import random


class Questions():
    @property
    def qType(self):
        return self.__qtype
    
    @property
    def questions(self):
        return self.__all_questions
    
    def __init__(self, ikigai, language="EN"):
        self.__ikigai = ikigai
        self.__all_questions = self.__getQuestions()
        self.__qtype = None
        self.__language = language
        self.__ikigai_type = {
            "love" : self.__ikigai.love,
            "need" : self.__ikigai.need,
            "paid" : self.__ikigai.paid,
            "good" : self.__ikigai.good
        }
        
    def rndQuestion(self):
        qtype, question = random.choice(self.__all_questions)
        self.__qtype = qtype
        return question
    
    def saveAws(self, aws):
        self.__ikigai_type[self.qType].append(aws) 
    
    def __getQuestions(self):
        file = open("questions.json", "r")
        if self.__language == "EN":
            loaded = json.load(file)[0]
        elif self.__language == "PT":
            loaded = json.load(file)[1]
            
        print(loaded)
        

from ikigai import Ikigai 
q = Questions(Ikigai(), "PT")
q.questions