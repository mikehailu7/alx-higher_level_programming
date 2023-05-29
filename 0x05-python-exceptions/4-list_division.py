#!/usr/bin/python3
# Author: Mikiashailu
# Divide a list
def list_division(lis_1, lis_2, l_len):
    n_lis = []
    for n in range(l_len):
        try:
            res = lis_1[n] / lis_2[n]
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            n_lis.append(res)
    return n_lis
