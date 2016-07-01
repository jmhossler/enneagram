class Question:

    def __init__(self, question, answer1, answer2):
        self.question = question
        self.one = answer1
        self.two = answer2

    def ask(self):
        return self.question

    def get_result(self, answer):
        if int(answer) == 1:
            return self.one
        elif int(answer) == 2:
            return self.two
        else:
            raise Exception("Unrecognized answer\n")
