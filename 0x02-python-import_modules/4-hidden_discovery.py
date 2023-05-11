#!/usr/bin/python3
# mikiashailu
if __name__ == "__main__":
    import hidden_4

    people = dir(hidden_4)
    for name in people:
        if name[:2] != "__":
            print(name)
