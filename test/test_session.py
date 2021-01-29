import main


def test_session_abort(monkeypatch):
    s = main.Session("Alan")

    # create monkeypatched input
    bot_answers = ["A", "y"]
    def bot_response(self):
        return bot_answers.pop(0)
    
    monkeypatch.setattr('builtins.input', bot_response)
    
    s.play_all()
