#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
    return (result)
