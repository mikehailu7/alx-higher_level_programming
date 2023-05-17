#!/usr/bin/python3
# mikiasHailu
# bestscore
def best_score(library):
    if len(library) and library:
        max = list(library.keys())[0]
        for key in library:
            if library[key] > library[max]:
                max = key
        return max
    return None
