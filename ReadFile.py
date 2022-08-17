from Automaton import *
from bs4 import BeautifulSoup

# hàm lấy data từ file jff chứa thông tin Automaton
def readFile(fileName):

    try:
        with open(fileName, 'r') as f:
            data = f.read()

        bs_data = BeautifulSoup(data, 'xml')
        # print(bs_data)
        GetType = bs_data.find('type')
        if not GetType:
            print('File không hợp lệ!')
            exit()
        TypeOfFile = GetType.get_text()
        if TypeOfFile != 'fa':
            print('File không hợp lệ!')
            exit()
        states = bs_data.find_all('state')
        # print(_states)
        _alphabet = {'0', '1'}
        _states = []
        _state_final = []
        _state_start = '0'
        _tran = {}

        for x in states:
            state_id = x.get('id')
            if state_id not in _states:
                _states.append(state_id)
            if x.final:
                _state_final.append(state_id)
            if x.initial:
                _state_start = state_id

        # dict tran{} biểu diễn transition table của Automaton
        for x in _states:
            _tran[x] = {}
            for letter in _alphabet:
                _tran[x][letter] = 'null'

        transitions = bs_data.find_all('transition')
        for x in transitions:
            bs_from = x.find('from')
            bs_read = x.find('read')
            bs_to = x.find('to')
            _tran[bs_from.get_text()][bs_read.get_text()] = bs_to.get_text()
        return Automaton(_states, _alphabet, _tran, _state_start, _state_final)
    except FileNotFoundError:
        print('File không hợp lệ!')
        exit()