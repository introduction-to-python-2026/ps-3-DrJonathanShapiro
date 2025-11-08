def move(my_list, direction):
    my_list = my_list.copy() 
    index_of_one = my_list.index(1)

    if my_list[0] == 1 and direction == 'left':
        return my_list
    if my_list[-1] == 1 and direction == 'right':
        return my_list

    if direction == 'right':
        my_list[index_of_one], my_list[index_of_one + 1] = 0, 1
    elif direction == 'left':
        my_list[index_of_one], my_list[index_of_one - 1] = 0, 1

    return my_list



