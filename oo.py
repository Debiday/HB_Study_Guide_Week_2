# Create your classes here

class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address 

class Question(object):
    """A question in an exam"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Print question to console and prompt user for answer"""
        user_answer = input(self.question + ">")

        if user_answer == self.correct_answer:
            return True
        else:
            return False

class Exam(object):
    """Exam class that can hold more than one question"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        """Adds question to the exam object/class"""
        self.questions.append(question)
    
    def administer(self):
        """Administer a test and return the score"""
        score = 0
    
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return (score/len(self.questions))*100
        










