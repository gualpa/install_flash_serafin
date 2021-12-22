# -*- coding: utf-8 -*-
"""   """
import sys
 
def load_file_to_listoflist(file, count_list):
    """
    """
    bandera = 1
    array = []
    with open(file, 'r') as _raw_file:
        _string_file = _raw_file.read()
        for _x in _string_file.split('\n'):
            _y = _x.strip()     
            if _y != '':
                new_line = []
                for list_elements in _y.split('\t'):
                    ###element = list_elements.strip()
                    element = []
                    for _x in list_elements.split(' '):
                        _y = _x.strip()
                        if _y != '':
                            element.append(_y)                 
                    ####filter(None, element)
                    #if element != '':
                    #    if bandera ==1:
                    #        print("-:",element,"-",len(element),"-",count_list,"..",len(list_elements),":-")
                    #        bandera = 0
                        ###new_line.append(element)
                new_line = element
                if len(new_line) != 0:
                    while len(new_line) < count_list:
                        new_line.append("")
                    array.append(new_line)
    return array

def write_file_with_list(file, list_of_list, index_list):
    """
    """
    array = []
    with open(file, 'w') as _raw_file:
        for line_write in list_of_list:
            line = ""
            for element in index_list:
                line_aux = line_write[element]
                if line_aux:
                    line = line + str(line_write[element]) + " "
                else:
                    line = line + "0"
            _raw_file.write(line)
            _raw_file.write("\n")


def find_argument(argv, arg_name, separator, arg_default):
    """Look for an argument in the argument list. If not found, return default.

    Arg:
       argv[] = arguments
       arg_name = look for arg_name
       separator = remove the separator in return
       arg_default = if it doesn't find it returns arg_default
    Return:
        argument
    """
    _arg = arg_default
    for _node in argv:
        _index_arg = _node.find(arg_name + separator)
        if _index_arg != -1:
            _arg = _node[(_index_arg + len(separator) + len(arg_name)):]
    return _arg