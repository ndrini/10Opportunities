from usefull import read_db
from time import sleep

choice_generic_text = "se ti trovassi in questa situazione quale \
di queste tre azioni del vostro protagonista sceglieresti?"


class Match():
    history = [0]  # pace list (or breadcrumb)
    parent_msg = "No message :-( "
    childs = []  # list of records of children
    # TODO: remove childs_page_number and user childs list
    childs_page_number = []  # list of integers of page
    childs_page_info = []   # list of str: number + msg
    actual_page_info = {} 

    # with open(r"db.yaml") as f:
    #     db = safe_load(f)
    db = read_db('db.csv')

    def __init__(self, initial_page, player) -> None:
        ''' adquire info from Session obj '''
        self.page = initial_page      # TODO rename initial_page
        self.player_name = player

    def involved_pages(self, actual_page_number) -> dict:
        ''' return a dict with: 
            'actual_page': actual_page_obj,
            'childs': [children_page_objs] '''
        result = {'childs': []}
        for page in self.db:
            if page['page'] == actual_page_number:
                result['actual_page'] = page
            if page['parent'] == actual_page_number:
                result['childs'].append(page)
        return result

    def find_only_child(self, parent_page) -> int:
        ''' in case of only possible child, due to a no_choice
        parent page '''
        for page in self.db:
            if page["parent"] == parent_page:
                if page["choice"] == True:
                    print("\n\n\n DB inconsistency: not only child!")
                return page["page"]

    def pseudo_query(self, page_number) -> list:
        ''' Show actual situation and possible next steps 
            TODO: split in 2 functions: 
                - one that show the situation 
                - one that show the future possibilities        
        '''
        # select the options child of page page_number

        for page in self.db:
            if page["page"] == page_number:
                self.parent_msg = page["msg_pre"]   # msg_pre,msg_actual
                if page["end"] == True:
                    # reached the last page
                    print(self.parent_msg)
                    return ["End"]
                # connected choice not shown !!!
                if page["choice"] == False:
                    return ["go_on"]

            if page["parent"] == page_number:
                self.childs.append(page)

        self.childs_page_number = [p["page"] for p in self.childs]
        ''' Show actual situation '''
        print("Your situation: ", self.parent_msg)
        ''' Show possible next steps '''

        # TODO:  nice_display_function
        self.childs_page_info = [str(p["page"]) + "  " + p["msg"]
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
            selected_page = input("Scrivi la tua scelta ")  # type str
            if not selected_page:
                selected_page = "0"
            print("selected_page: ", selected_page)
            print("good_choice: ", good_choice)

            # if (selected_page in child_page_number) or (selected_page == "e"):
            
            if (int(selected_page) in 
                [i['page'] for i in self.actual_page_info['childs']]):

            # if (int(selected_page) in self.childs_page_number):
                good_choice = True
                print("good_choice: ", good_choice)
                # select a case to logout!
                self.history.append(selected_page)
                ''' Check if this is the last possible step '''
                # necessary here?!?!?

                # for choice in self.db:
                #     if choice["page"] == int(selected_page):
                #         # ex. "level": "S1_4"
                #         if choice["level"][-1] == str(4):
                #             return None
                # self.childs = []
                # self.childs_page_number = []
                return int(selected_page)
            # TODO: explicit abort option
            # else:
            #     # manually Abort
            #     manually_abort = input ("do you want to exit?")
            #     if manually_abort = "y":
            #           return None

    def play_one(self) -> None:
        ''' '''

        # 10. user welcome and introduction
        # print("Hello, " + self.player_name + "!")
        print("\nSTART: Let's play the match case number " +
              str(self.page) + ".")
        self.actual_page_info = self.involved_pages(self.page)
        print (self.actual_page_info)
        print("\n\n The case Title is: ",
              self.actual_page_info['actual_page']['msg_pre'])

        initial_check = input("Play 'P' or Abort 'A': ")
        # next_pace = True
        if initial_check == "P":
            # TODO: insert Abort for the match 
            while not self.actual_page_info['actual_page']['end']:
                
                if not (self.page == 1):
                    print(self.actual_page_info['actual_page']['msg_pre'])

                if not self.actual_page_info['actual_page']['choice']: 
                    print(self.actual_page_info['actual_page']['msg_actual'])
                    print(self.actual_page_info['childs'][0]['msg_pre'])

                    # print("new page number", actual_page_info['childs'][0]['page'])
                    self.page = self.actual_page_info['childs'][0]['page']
                    # print ("self.page ", self.page )
                    self.actual_page_info = self.involved_pages(self.page)
                    # print(actual_page_info['actual_page']['page'])
                    sleep(1)
                    print(self.actual_page_info['actual_page']['msg_actual'])
                    
                    continue                    
                else:
                    # print all children possibilities

                    print(" **** Possibilities")
                    #  it should be necessary
                    # print(choice_generic_text)

                    for p in self.actual_page_info['childs']:
                        print('choice: ', p['page'], '->', p['msg_pre'])



                # result = self.pseudo_query(self.page)
                # # while loop exit
                # if result[0] == "End":
                #     print("The case (this match) is over")
                #     # not necessary: self.match_alive = False
                #     return
                # if result[0] == "go_on":
                #     next_pace = self.find_only_child(self.page)
                #     self.page = next_pace  # update page
                #     continue
                
                    # update page
                    self.page = self.read_and_pass_answer()
                    # last page check      
                    if self.page == None:
                        return
                    self.actual_page_info = self.involved_pages(self.page)
                    sleep(1)
            return
        else:
            return
