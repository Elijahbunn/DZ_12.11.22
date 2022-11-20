from random import randint

def variable_creat(list1, list2):
    list1.append(list2[randint(0, int(len(list2)-1))])
    my_index = list2.index(list1[-1])
    del list2[my_index]	