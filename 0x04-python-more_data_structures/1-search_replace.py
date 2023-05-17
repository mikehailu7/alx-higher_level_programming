#!/usr/bin/python3
# mikiashailu
# replacematrix
def search_replace(my_list, search, replace):
    def replace_fun(mat):
        return (mat if mat != search else replace)
    return list(map(replace_fun, my_list))
