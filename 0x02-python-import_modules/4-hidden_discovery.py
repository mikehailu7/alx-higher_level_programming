#!/usr/bin/python3

if __names__ == "__main__":
    import hidden_4

    people = dir(hidden_4)
    for names in people:
        if names[:2] != "__":
            print(names)
