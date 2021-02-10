from usefull import read_db, separator
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

    def __init__(self, initial_page, player, db) -> None:
        ''' adquire info from Session obj '''
        self.page = initial_page      # TODO rename initial_page
        self.player_name = player
        # with open(r"db.yaml") as f:
        #     db = safe_load(f)
        self.db = read_db(db)

    def involved_pages(self, actual_page_number) -> dict:
        ''' return a dict with necessary info to
            have a choice: 
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
        ''' Return user valid selection, based on available choices 
            depending on the actual page
        '''
        good_choice = False
        while not good_choice:
            selected_page = input(
                "Scrivi la tua scelta or 'exit' to abort ")  # type str
            # abort match
            if selected_page == 'exit':
                return None
            print("You selected page number ", selected_page)

            # prevent NameError in case of no choice at all or ValueError
            try:
                int(selected_page)
            except:
                print(separator, "NOT valid choice!")
                continue

            # 20. assess the user's choice
            if (int(selected_page) in
                    [i['page'] for i in self.actual_page_info['childs']]):
                good_choice = True
                print("This is a valid choice!")  # , good_choice)
                # select a case to logout!
                self.history.append(selected_page)
                return int(selected_page)

    def play_one(self) -> None:
        ''' Match develpment based on a specific case'''
        # 10. User welcome and introduction
        # print("Hello again, " + self.player_name + "!")
        print("\nSTART: Let's play the match case number " +
              str(self.page) + ".")
        self.actual_page_info = self.involved_pages(self.page)
        print("\n\n The case title is: ",
              self.actual_page_info['actual_page']['msg_pre'])
        initial_check = input(
            "Play 'P' or any other char to Abort: ").lower()

        # 20. Play the match
        if initial_check == 'p':
            # TODO: insert Abort for the match
            while not self.actual_page_info['actual_page']['end']:
                # todo: simplify with
                #     choice = self.actual_page_info['actual_page']['choice']
                #     msg_pre = self.actual_page_info['actual_page']['msg_pre'])

                # 20.2 avoid title info duplication
                # if not (self.page == 1):
                if not (self.page in
                        [i['page'] for i in self.involved_pages(0)['childs']]):
                    print(separator,
                          self.actual_page_info['actual_page']['msg_pre'])

                # 20.4 avoid user input if linked page
                if not self.actual_page_info['actual_page']['choice']:
                    print(separator,
                          self.actual_page_info['actual_page']['msg_actual'])

                    if self.actual_page_info['childs']:
                        print(self.actual_page_info['childs'][0]['msg_pre'])
                        # update actual page
                        self.page = self.actual_page_info['childs'][0]['page']
                        self.actual_page_info = self.involved_pages(self.page)
                        sleep(1)
                        print(
                            self.actual_page_info['actual_page']['msg_actual'])

                    if self.actual_page_info['actual_page']['goto']:
                        print(
                            self.actual_page_info['actual_page']['msg_actual'])
                        sleep(2)
                        self.actual_page_info = self.involved_pages(
                            self.actual_page_info['actual_page']['goto']
                        )
                        self.page == self.\
                            actual_page_info['actual_page']['goto']

                    # BUG do not check for end==True

                    continue
                # or allow the choice
                else:
                    # print all children possibilities
                    print(" **** Possibilities")
                    for p in self.actual_page_info['childs']:
                        print('choice: ', p['page'], '->', p['msg_pre'])

                    # update page
                    self.page = self.read_and_pass_answer()
                    # last page check
                    if self.page == None:
                        print(separator, "The case (this match) is over")
                        print('The path has been: \n')
                        for n in self.history:
                            print(n, end=" ")
                        return

                    # 20.8 update page and continue
                    self.actual_page_info = self.involved_pages(self.page)
                    # self.page already updated

                    sleep(1)

                    # go to check
                    if self.actual_page_info['actual_page']['goto']:
                        print(
                            self.actual_page_info['actual_page']['msg_actual'])
                        sleep(2)
                        self.actual_page_info = self.involved_pages(
                            self.actual_page_info['actual_page']['goto']
                        )
                        self.page == self.\
                            actual_page_info['actual_page']['goto']

            return
        # 30. or exit this match (and go back to session for another case)
        else:
            return
