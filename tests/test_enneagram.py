import pytest
from enneagram.quiz import Quiz


@pytest.mark.parametrize(
    "questions",
    [
        {
            "foobar": {"1": "achiever", "2": "peacemaker"},
            "bazboo": {"1": "peacemaker", "2": "achiever"},
        }
    ],
)
def test_enneagram_quiz_reports_results(questions):
    quiz = Quiz(questions)
    asked_questions = []
    for question in quiz.ask():
        asked_questions.append(question)
        quiz.answer("1")

    assert set(asked_questions) == set(question for question in questions)
    assert quiz.score() == {"achiever": 1, "peacemaker": 1}
