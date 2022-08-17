def readFile(root):
        _alphabet = {'0', '1'}
        _states = []
        _states2 = []
        _state_final = []
        _state_start = 0
        _tran = []
        for automaton in root.findall('automaton'):  # Truy cập thuộc tính automaton
            for state in automaton.findall('state'):  # Truy cập thuộc tính state
                _name = state.get('name')  # Truy cập tên nút
                _states.append(_name)
                for child in state:
                    if child.tag.find('initial') == 0:  # tìm nút initial
                        _state_start = _name
                    if child.tag.find('final') == 0:  # tìm nút final
                        _state_final.append(_name)
        for i in _states:
            for j in _alphabet:
                _tran.append([i,j])
        for automaton in root.findall('automaton'):
            for transition in automaton.findall('transition'):
                _from = transition.find('from').text
                _read = transition.find('read').text
                if _read not in _alphabet:
                    _read = 'e'
                _to = transition.find('to').text
                if _read == 'e':
                  _tran.append([_states[int(_from)],_read,_states[int(_to)]])
                else:
                 k=0
                 while k< len(_tran):
                     if _tran[k][0] == _states[int(_from)] and _tran[k][1] == _read:
                           _tran[k].append(_states[int(_to)])
                     k+=1
        k = 0
        while k < len(_tran):
            while len(_tran[k])>3:
                _tran.append([_tran[k][0],_tran[k][1],_tran[k][3]])
                _tran[k].pop(3)
            k+=1
        return _tran, _state_start, _state_final
