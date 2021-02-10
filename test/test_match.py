import main
from match import Match


def test_match_case_1(monkeypatch):
    s = main.Session('Barbara', 'db.csv')
    # create monkeypatched input
    bot_answers = ["P", "9", "11", "y"]   # ok
    # bot_answers = ["P", "6", "8", "9", "11", "y"]  # no!

    def bot_response(self):
        return bot_answers.pop(0)
    monkeypatch.setattr('builtins.input', bot_response)

    s.play_all()


def test_involved_pages():
    m = Match(1, 'Eva', 'db.csv')
    query = m.involved_pages(1)
    assert type(query) == dict
    assert query['actual_page']['page'] == 1
    assert query['childs'][0]['page'] == 2

    query = m.involved_pages(2)
    assert query['actual_page']['page'] == 2
    assert query['childs'][2]['page'] == 9


def test_many_choices(monkeypatch):
    m = Match(1, 'Lily', 'db_many_choices.csv')
    # create monkeypatched input
    bot_answers = ["p"]   # ok

    def bot_response(self):
        return bot_answers.pop(0)
        
    monkeypatch.setattr('builtins.input', bot_response)
    m.play_one()
