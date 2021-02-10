from match import Match

class Session():
    ''' it collects the player name, boosts the game in each possible case '''
    case_all = [1, 18,] # TODO: move to a dictionary  
    game_over = False

    def __init__(self, player_name):
        self.player_name = player_name

    def play_all(self):
        ''' cover one by one (no user chice) the 10 possible cases '''
        # TODO: allow the user to select the desired case
        #       (function case_all_shuffle or select) 
        while self.case_all and not self.game_over: 
            # todo: ask for new match or game_over 
            m = Match(self.case_all[0], self.player_name)
            print("Playing", self.case_all[0])

            # TODO: play_one should return 
            #       "exit" -> exit game
            #       "pass" -> pass to another case 
            #       "stop" -> froze the game
            #   
            m.play_one()
            # removed played case from list 
            self.case_all = self.case_all[1:]
            print("case_all: ", self.case_all)
            ## here Abort result
            game_over_declar = input("Do you want do exit? Yes (y) or No (n)")
            if game_over_declar == "y":
                self.game_over = True
        if not self.case_all: 
            print("\n *** All possible cases Completed! *** ") 

