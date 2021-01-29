from yaml import safe_load

''' levels
1 intro
2 3 choices
3 2 choces
4 solution'''

choice_generic_text = "se ti trovassi in questa situazione quale \
di queste tre azioni del vostro protagonista sceglieresti?"

# def t(string, languange = "it"):
#     if languange == "it": 


class Session():
    ''' it collects the player name, boosts the game in each possible case '''
    case_all = [1,20,30] # TODO: move to a dictionary  
    game_over = False

    def __init__(self, player_name):
        self.player_name = player_name

    def play_all(self):
        ''' cover one by one (no user chice) the possible cases '''
        # TODO: allow the user to select the desired case
        #       (function case_all_shuffle or select) 
        while self.case_all and not self.game_over: 
            # todo: ask for new match or game_over 
            m = Match(self.case_all[0], self.player_name)
            print("Playing", self.case_all[0])
            m.play_one()
            # removed played case from list 
            self.case_all = self.case_all[1:]
            print("case_all: ", self.case_all)
            ## here Abort result
            game_over_declar = input("Do you want do exit? Yes (y) or No (n)")
            if game_over_declar == "y":
                self.game_over = True
        if not self.case_all: 
            print("All possible cases Completed!") 


class Match(): 
    history = [0] # pace list (or breadcrumb)
    parent_msg = "No message :-( "
    childs = [] # list of records of children 
    # TODO: remove childs_page_number and user childs list
    childs_page_number = [] # list of integers of page 
    childs_page_info = []   # list of str: number + msg 
    match_alive = True

    with open(r"db.yaml") as f:
        db = safe_load(f)

    def __init__(self, case_number, player) -> None:
        ''' adquire info from Session obj '''
        self.case_number = case_number      # TODO rename case_initial_page
        self.player_name = player
    
    def play_one(self) -> None:
        ''' '''
        # print("Hello, " + self.player_name + "!")
        print("Let's play the match case number " + 
            str(self.case_number) + ".")
        initial_check = input("Play 'P' or Abort 'A': ")
        next_pace = True
        ## here Abort input 
        if initial_check == "P":
            # for i in range(5):
            #     print("play ...")
            while self.match_alive and next_pace: 
                self.pseudo_query(self.case_number)
                next_pace = self.read_and_pass_answer() 
                self.case_number = next_pace  # update page
            return  
        else: 
            return
    
    def pseudo_query(self, page_number) -> list:
        ''' Show actual situation and possible next steps '''
        # select the options child of page page_number

        for page in self.db: 
            if page["parent"] == page_number:
                self.childs.append(page)
            if page["page"] == page_number:
                self.parent_msg = page["msg"]
                
        self.childs_page_number = [p["page"] for p in self.childs]
        ''' Show actual situation '''
        print("Your situation: ", self.parent_msg)
        ''' Show possible next steps '''
        # TODO:  nice_display_function
        self.childs_page_info = [str(p["page"]) + "  " + p["msg"] \
            for p in self.childs]
        # prompt option
        print(self.player_name, ", ", choice_generic_text)
        print("Le scelte possibili sono ")
        for m in self.childs_page_info: 
            print("\t", m)
        
        return self.childs_page_number


    def read_and_pass_answer(self) -> int:
        ''' '''
        # selected_page = input(t("make your choice"))
        good_choice = False
        while not good_choice:     
            selected_page = input("Scrivi la tua scelta ") # type str
            if not selected_page:
                selected_page = "0"
            print ("selected_page: ", selected_page)
            print("good_choice: ", good_choice)

            # if (selected_page in child_page_number) or (selected_page == "e"):
            if (int(selected_page) in self.childs_page_number):
                good_choice = True
                # select a case to logout! 
                self.history.append(selected_page) 
                ''' Check if this is the last possible step '''
                for choice in db:
                    if choice["page"] == int(selected_page):
                        if choice["level"][-1] == str(4):  # ex. "level": "S1_4"
                            return None
                self.childs = [] 
                self.childs_page_number = []  
                return int(selected_page)
            # TODO: explicit abort option
            # else: 
            #     # manually Abort
            #     manually_abort = input ("do you want to exit?")
            #     if manually_abort = "y":
            #           return None  


if __name__ == "__main__":
    s1 = Session("John")
    s1.play_all()
    print("Program End")
    

# expertex 2, 6, 9 

# def valid_user_input(x):
#     try:
#         
#         return int(x) > 2
#     except ValueError:
#         return False

# maximum_number_input = input("Maximum Number: ")  # raw_input not available py3

# while valid_user_input(maximum_number_input):
#     maximum_number_input = input("Maximum Number: ")
#     print("You have successfully entered a valid number")

# pseudo_query(history[-1]):




