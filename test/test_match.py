import main


def test_match_case_1(monkeypatch):
    s = main.Session("Barbara")

    # create monkeypatched input
    bot_answers = ["P", "4", "11"]
    def bot_response(self):
        return bot_answers.pop(0)
    
    monkeypatch.setattr('builtins.input', bot_response)
    
    s.play_all()
