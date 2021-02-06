# main logic structure

class Session():
    case_all = [1,2,3,4,5]  
    game_over = False

    def __init__(self, player_name):
        self.player_name = player_name

    def play_all(self):
        while self.case_all: # and not self.game_over: 
            # todo: ask for new match or game_over 
            m = Match(self.case_all[0], self.player_name)
            print("Playing", self.case_all[0])
            m.play_one()
            # removed played case from list 
            self.case_all = self.case_all[1:]
            print("case_all: ", self.case_all)
            ## here Abort result 


class Match(): 
    def __init__(self, case_number, player) -> None:
        self.case_number = case_number
        self.player_name = player
    
    def play_one(self) -> None:
        print("Hello, " + self.player_name + "!")
        print("Let's play the match case number " + 
            str(self.case_number) + ".")
        result = input("Play 'P' or Abort 'A': ")
        ## here Abort input 
        if result == "P":
            for i in range(5):
                print("play ...") 
            return  
        else: 
            return

s1 = Session("Paul")
s1.play_all()
print("end")
    