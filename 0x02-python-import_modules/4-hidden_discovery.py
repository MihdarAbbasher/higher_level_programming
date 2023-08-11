#!/usr/bin/python3
if __name__ == "__main__":
    """Print var and functions in hidden_4 module"""
    import hidden_4

    names_in_module = dir(hidden_4)
    for x in names_in_module:
        if x[:2] != "__":
            print(x)

