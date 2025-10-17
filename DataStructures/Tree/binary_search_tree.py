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
    retorno = sll.new_list()
    if root is not None:
        key_set_tree(root["left"], keys)
        sll.add_last(retorno, bsn.get_key(root))
        key_set_tree(root["right"], keys)
    return retorno

def key_set(my_bst):
    keys = sll.new_list()
    key_set_tree(my_bst["root"], keys)
    return keys

def value_set_tree(root, values):
    retorno = sll.new_list()
    if root is not None:
        value_set_tree(root["left"], values)
        sll.add_last(retorno, bsn.get_value(root))
        value_set_tree(root["right"], values)
    return retorno

def value_set(my_bst):
    values = sll.new_list()
    value_set_tree(my_bst["root"], values)
    return values