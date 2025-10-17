from DataStructures.Tree import bst_node as bsn
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll


def new_map():
    
    retorno = {
        "root": None
    }
    
    return retorno

def insert_node(root, key, value):
    if root is None:
        return bsn.new_node(key, value)
    if key < bsn.get_key(root):
        root["left"] = insert_node(root["left"], key, value)
    elif key > bsn.get_key(root):
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value  
    
    return root

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def get(my_bst, key):
    current = my_bst["root"]
    while current is not None:
        current_key = bsn.get_key(current)
        if key == current_key:
            return bsn.get_value(current)
        elif key < current_key:
            current = current["left"]
        else:
            current = current["right"]
    return None

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])

def size(my_bst):
    return size_tree(my_bst["root"])

def contains(my_bst, key):
    return get(my_bst, key) is not None

def is_empty(my_bst):
    return size(my_bst) == 0

def key_set_tree(root, keys):
    pass

def keys_range(root, low_key, high_key, keys):
    if root is None:
        return
    current_key = bsn.get_key(root)
    if low_key < current_key:
        keys_range(root["left"], low_key, high_key, keys)
    if low_key <= current_key <= high_key:
        sll.add_last(keys, current_key)
    if current_key < high_key:
        keys_range(root["right"], low_key, high_key, keys)

def keys(my_bst, low_key, high_key):
    keys_list = sll.new_list()
    keys_range(my_bst["root"], low_key, high_key, keys_list)
    return keys_list