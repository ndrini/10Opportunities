import os
import csv

separator = '\n'*2 + '_____' + '\n'

def custom_path(script_dir, file_name) -> str:
    parent_dir = os.path.split(script_dir)[0]
    file_path = os.path.join(parent_dir, file_name)
    return file_path


def guess_type(x):
    # credits
    # https://stackoverflow.com/questions/19080007/
    # csv-reader-and-dictreader-turn-numeric-fields-into-strings
    
    try: 
        if x == "True":
            x = True
        elif x == "False":
            x = False
        else: 
            x = int(x)
        return x
    except: 
        return x
    
    # attempt_fns = [int,
    #                bool,
    #                float,
    #                ]
    # for fn in attempt_fns:
    #     try:
            
    #         # update boolean check!!!  
    #         # if ... 

    #         return fn(x)
    #     except (ValueError, SyntaxError):
    #         pass
    # return x


def read_db(file_name) -> list:
    result = []
    try:
        with open(file_name) as f:
            reader = csv.DictReader(f)
            for line in reader:
                # print("Not typed data\t: ", line)
                for key in line:
                    line[key] = guess_type(line[key])
                result.append(line)
                # print("Typed data\t: ", line)

    except OSError:
        print("\t*** No database file!")

    return result
