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
    

class StudentExam(object):
    """Store a student, exam and score"""

    def __init__(self, student, exam, score):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        """Administers the exam and assigns score to StudentExam"""

        self.score = self.exam.administer()
        print(f"Your score is {self.score:.2f}%.")

class Quiz(Exam):
    """Quiz class similmar to exam that that returns 1(passed) or 0(failed)"""
    
    def administer(self):
        """Administer a quiz"""

        score = super(Quiz, self).administer() ##how does this work?
    
        if score >= 0.5:
            return 1
        else:
            return 0

class StudentQuiz(object):
    """Quiz belonging to a particular student. Contains quiz score."""

    def __init__(self, student, quiz):
        self.quiz = quiz
        self.student = student
        self.score = None

    def take_test(self):
        """Administers the quiz and assigns score to StudentExam"""

        self.score = self.quiz.administer()
        
        if score == 1:
            print("You have passed")
        else:
            print("Oh dear, failed.")



def example():
    """Usage of all the above classes and methods"""

    exam1 = Exam('pop quiz')

    set1 = Question('Who is the Queen of Pop', 'Madonna')
    set2 = Question('Who is the King of Pop', 'Elvis')
    set3 = Question('Who is the Queen of Rap?', 'Nicki')

    exam1.add_question(set1)
    exam1.add_question(set2)
    exam1.add_question(set3)

    student = Student('Jasmine', 'Debugger', '1010 Computer Street')

    jasmine_popquiz = StudentExam(student, exam)

    jasmine_popquiz.take_test()















