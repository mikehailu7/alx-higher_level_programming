#!/usr/bin/python3
# MikiasHailu
def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        answer = (0, None)
        return answer
    else:
        result = (size, sentence[0:1])
        return result
