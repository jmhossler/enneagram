from question import Question


class Enneagram:

    def __init__(self, name, log_file='results.txt', question_file='questions.txt'):
        self.name = name
        self.question_file = self._get_questions(question_file)
        self.log_file = log_file
        self.answers = []

    def take_quiz(self):
        for question in self.ask_question():
            print(question)

    def ask_question(self):
        for i in range(0,len(self.questions)):
            answer = input("{}. {}".format(i, self.questions[i].ask()))
            self.answers.append(self.questions[i].get_result(answer))
            yield i

    def _get_questions(self, filename):
        questions = []
        for line in open(filename,'r'):
            questions.append(Question(*line.split('|')))

        return questions
