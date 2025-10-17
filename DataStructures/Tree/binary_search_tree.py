from DataStructures.List import array_list as al

def value_set(my_bst):
    list = value_set_tree(my_bst["root"])
    if list is None:
        return None
    return list


def value_set_tree(root, key_list):
    if root is None:
        return key_list
    else:
        value_set_tree(root["left"], key_list)
        al.add_last(key_list, root["key"])
        value_set_tree(root["right"], key_list)
    return key_list