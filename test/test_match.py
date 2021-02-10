import main
from match import Match

# def test_match_case_1(monkeypatch):
#     s = main.Session("Barbara")

#     # create monkeypatched input
#     bot_answers = ["P", "4", "11"]

#     def bot_response(self):
#         return bot_answers.pop(0)

#     monkeypatch.setattr('builtins.input', bot_response)

#     s.play_all()


def test_involved_pages():
    m = Match(1, 'Eva')
    query = m.involved_pages(1)
    assert type(query) == dict
    assert query['actual_page']['page'] == 1
    assert query['childs'][0]['page'] == 2

    query = m.involved_pages(2)
    assert query['actual_page']['page'] == 2
    assert query['childs'][2]['page'] == 9