class Quiz:
    def __init__(self, questions):
        self._questions = questions
        self._current_question = None
        self._score = {}
        pass

    def ask(self):
        for question in self._questions:
            self._current_question = question
            yield question

    def answer(self, answer):
        result = self._questions[self._current_question][answer]
        if result in self._score:
            self._score[result] += 1
        else:
            self._score[result] = 1

    def score(self):
        return self._score
