from io import StringIO
import xml.etree.ElementTree as ET
from ReadNfaFile import *
def inputFile():
    print('Hãy nhập vào địa chỉ file Jflag: ')
    link1 = input()
    file_object = open(link1)  # demo.jff is file'name which located in the same folder as the project
    xml = file_object.read()
    xml_file = StringIO(xml)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    _tran, _state_start, _state_final = readFile(root)
    return _tran, _state_start, _state_final
def ndfInput():
    _tran, _state_start, _state_final=inputFile()
    state_start = _state_start
    state_final = _state_final
    states = []
    alphabet = []
    tran = _tran
    for i in tran:
        states.append(i[0])
        states = list(set(states))
        alphabet.append(i[1])
        alphabet=list(set(alphabet))
    ndftData = {
        'state_start': state_start,
        'state_final': state_final,
        'states': sorted(set(states)),
        'alphabet': sorted(set(alphabet)),
        'tran': tran
    }
    return ndftData



