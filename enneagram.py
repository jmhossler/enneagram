from question import Question


class Enneagram:

    def __init__(self, name, log_file='results.txt', questions='questions.txt'):
        self.name = name
        self.questions = self._get_questions(questions)
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

    def _get_questions(self, fp):
        questions = []
        for line in open(fp,'r'):
            questions.append(Question(*line.split('|')))

        return questions
