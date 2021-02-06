import os

def custom_path(script_dir, file_name) -> str:
    parent_dir = os.path.split(script_dir)[0]
    file_path = os.path.join(parent_dir, file_name)
    return  file_path

def guess_type(x):
    # credits           
    # https://stackoverflow.com/questions/19080007/
    # csv-reader-and-dictreader-turn-numeric-fields-into-strings
    attempt_fns = [int,
                   bool, 
                   float,
                   lambda x: datetime.datetime.strptime(x, 
                                                    "%Y-%m-%d %H:%M:%S")
                   ]
    for fn in attempt_fns:
        try:
            return fn(x)
        except (ValueError, SyntaxError):
            pass
    return x
