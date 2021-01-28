import pytest
import main

# test_session = main.Session("Bot")
test_match = main.Match(1, "Bot")

def test_generic():
    # print("ciao")
    # print(test_match.db)
    assert test_match.pseudo_query(2)  == [3, 6, 9]


# testcase.play_all()

#     # print("Program End")