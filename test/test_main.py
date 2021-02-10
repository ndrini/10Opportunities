import pytest
from match import Match

test_match = Match(1, "Bot")

'''
TODO: 
create moneypatch for allowing multiple case tests
 '''

# @pytest.fixture
# def childs_page_number_setup():
#     print("childs_page_number_setup")
#     test_match.childs_page_number = [456]


def test_data_fix(monkeypatch):
    def substitution():
        return [456]

    monkeypatch.setattr('main.Match.childs_page_number', substitution)
    # monkeypatch.setattr('Match.childs_page_number', substitution)

    print("---> test_match.childs_page_number ",
          test_match.childs_page_number)

    assert test_match.pseudo_query(2) == [3, 6, 9]


def test_data_fix_2():
    # def test_data_fix_2(childs_page_number_setup):
    print("test_match.childs_page_number ",
          test_match.childs_page_number)
    assert test_match.pseudo_query(1)[-1] == 2

# def test_data_dinamic():
#     # print("ciao")
#     # print(test_match.db)
#     x = 1
#     # assert test_match.pseudo_query(x+1) == [x+2, x+5, x+8]
#     # assert test_match.pseudo_query(x+2) == [x+3, x+4]
#     assert test_match.pseudo_query(x+3) == [x+11]
#     # assert test_match.pseudo_query(x+4) == [x+12]


# data = [(2, [3, 6, 9]),
#         (3, [4, 5]),
#         (4, [12]),
#         (5, [13]),
#     ]
# @pytest.mark.parametrize('page,out', data)
# def test_data_by_pattern(page, out):
#     # print("ciao")
#     # print(test_match.db)
#     # x = 1
#     # assert test_match.pseudo_query(x+1) == [x+2, x+5, x+8]
#     # assert test_match.pseudo_query(x+2) == [x+3, x+4]
#     # assert test_match.pseudo_query(x+3) == [x+11]
#     # assert test_match.pseudo_query(x+4) == [x+12]
#     assert test_match.pseudo_query(page) == out


# testcase.play_all()

#     # print("Program End")
