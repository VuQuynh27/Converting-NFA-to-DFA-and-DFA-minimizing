import copy as cp
import Automaton as at
# hàm nhiều trạng thái
def findTransMany(transitions):
    des_many_states = []
    for i in transitions:
        if len(i) > 3:
            des_many_states.append(i)
    return des_many_states
# hàm tìm hàm chuyển có e
def findTransEp(transitions):
    des_many_states = []
    for i in transitions:
        if i[1] == 'e':
            des_many_states.append(i)
    return des_many_states

# tìm nút chuyển tiếp
def getNextState(trans_i):
    next_state = []
    for i in range(2, len(trans_i)):
        next_state.append(trans_i[i])
    return next_state
# Lay trang thai bat dau
def getStartTranStates(trans):
    start_state_trans = []
    for i in trans:
        start_state_trans.append(i[0])
    start_state_trans.sort()
    return start_state_trans
# Tìm final mới
def newFinalState(finalState,new_states):
    newFinal=[]
    newFinal.append(finalState)
    for i in finalState:
        for j in new_states:
            if len(j)>1:
                for x in range(len(j)):
                    if i==j[x]:
                        newFinal.append(j)
    newFinal.sort(reverse=True)
    return newFinal
#Đổi Format final
def final(finalStates,states):
    new_states = newStates(states)[0]
    x=0
    while x < len(finalStates):
        for i in new_states:
          if finalStates[x]==new_states[i]:
              finalStates[x]=i
        x+=1
    return finalStates
# tim cac ε-closure(q_i)
def find_eq(states, transitions):
    ls_eq = dict()
    eps_trans = findTransEp(transitions)
    _get_start_trans = getStartTranStates(eps_trans)
    for i in states:
        if i not in _get_start_trans:
            ls_eq.update({i: [i]})
        else:
            res_eq = []
            next_state = [i]
            new_next = []
            j = 0
            while len(next_state) > 0:
                k = 0
                check_k = True
                if next_state[j] in _get_start_trans:
                    while check_k == True and k < len(eps_trans):
                        if next_state[j] == eps_trans[k][0]:
                            new_next = getNextState(eps_trans[k])
                            for gn in new_next:
                                if gn not in res_eq and gn not in next_state:
                                    res_eq.append(gn)
                                    next_state.append(gn)
                            check_k = False
                        else: k += 1
                next_state.pop(j)
            res_eq.append(i)
            res_eq.sort()
            ls_eq.update({i: res_eq})
    return ls_eq

# lay ra eq(i)
def get_eq(state, ls_eq):
    for i in ls_eq:
        if state == i:
            return ls_eq[i]

# Tìm hàm chuyển cho một trạng thái và một ký tự trong bảng chữ cái
def findTransNotAlpha(x, alphabet, transitions):
    listFind = []
    for i in range(len(transitions)):
        n = transitions[i]
        if x == n[0] and alphabet == n[1]:
            if len(n) < 3:
                pass
            else:
                for j in range(2, len(n)):
                    listFind.append(n[j])
    return listFind

# hàm tạo states mới 2^n
def newStates(states):
    x = len(states)
    temp_new_states2=[]
    new_dict=dict()
    new_states=[]
    for i in range(1 << x):
        temp_new_states2.append([states[j] for j in range(x) if (i & (1 << j))])
    count=0
    for i in temp_new_states2:
        new_dict.update({'q' + str(count): i})
        count += 1
    for j in new_dict:
      new_states.append(j)
    return new_dict,temp_new_states2,new_states
def unionTransState(list_states):
    list_union = []

    for i in list_states:
        list_union = list(set(list_union) | set(i))
    list_union.sort()
    return list_union

# Xây dựng lại hàm chuyển
def updateTrans(newState, alphabet, transitions, ls_eq):
    new_ls_trans = []
    for i in newState:
        if len(i) > 0:
            new_tran = []
            for j in alphabet:
                next_tran_ij = []
                for k in i:
                    # Tim trang thai chuyen tiep cho trang thai bat dau la k thuoc eq(i) va j thuoc bang chu cai
                    _find_next_state_tran = findTransNotAlpha(k, j, transitions)
                    if len(_find_next_state_tran) > 0:
                        ep = get_eq(_find_next_state_tran[0], ls_eq)
                        next_tran_ij.append(ep)
                # Hop cac trang thai chuyen tiep
                union_trans = unionTransState(next_tran_ij)
                union_eq = []
                if len(union_trans) == 0:
                    union_eq = union_trans
                else:
                    _temp_union_trans = []
                    for k in union_trans:
                        _get_eq_k = get_eq(k, ls_eq)
                        _temp_union_trans.append(_get_eq_k)
                    union_eq = unionTransState(_temp_union_trans)
                # Them ham chuyen [i, j, res] vao bo ham chuyen moi
                if len(union_eq) == 0:
                    new_ls_trans.append([i, j])
                else:
                    _new_tran_ij = [i, j]
                    for k in union_eq:
                        _new_tran_ij.append(k)
                    new_ls_trans.append(_new_tran_ij)
    return new_ls_trans


#Format Transition
def formatTransi(new_ls_trans):
    new_trans = new_ls_trans.copy()
    a=findTransMany(new_ls_trans)
    for i in a:
        update = []
        for j in range(2, len(i)):
            update.append(i[j])
        temp_update = [i[0], i[1], update]
        check = True
        id_trans = 0
        while check == True and id_trans < len(new_trans):
            trans_i = new_trans[id_trans]
            if i == trans_i:
                new_trans[id_trans] = temp_update
                check = False
            else:
                id_trans += 1
    return new_trans
#Thay đổi tên nút
def changeNameStates(new_trans, new_states):
    new_trans=new_trans.copy()
    for i in new_trans:
        for j in new_states:
            if i[0] == new_states[j]:
                i[0] = j
            if len(i) > 2:
                if i[2] == new_states[j] or [i[2]]==new_states[j]:
                    i[2] = j
    for i in new_trans:
        if len(i)<3:
            i.append('q0')
    new_trans.append(['q0', '0', 'q0'])
    new_trans.append(['q0', '1', 'q0'])
    state = []
    nest={}
    for i in new_trans:
        if i[0] not in state:
            state.append(i[0])
    for i in state:
        nest[i] = {}
        for j in new_trans:
            if j[0] == i:
                temp = {j[1]: j[2]}
                nest[i].update(temp)
    return nest

def dfa(state_start, state_final, states, alphabet, tran):
    # create nfa
    _dfa = at.Automaton()
    # list epsilon
    ls_eq = find_eq(states, tran)
    # new alphabet
    alphabet = [i for i in alphabet if i != 'e']
    _dfa.alphabet = alphabet
    # new state
    dict_s=newStates(states)[0]
    states2 = newStates(states)[1]
    states3 = newStates(states)[2]
    _dfa.states = states3


    # new trans
    transitions = cp.deepcopy(tran)
    new_trans = updateTrans(states2, alphabet, transitions, ls_eq)
    new_trans=formatTransi(new_trans)
    new_trans=changeNameStates(new_trans,dict_s)
    _dfa.tran = new_trans

    # new start state
    startState = cp.deepcopy(state_start)
    a= get_eq(startState,ls_eq)
    for i in dict_s:
        if a == dict_s[i]:
            a=i
    _dfa.state_start = a

    # new final state
    finalStates = cp.deepcopy(state_final)
    new_final_state = newFinalState(finalStates,states2)
    new_final_state=final(new_final_state,states)
    _dfa.state_final = new_final_state
    return _dfa
def returnDfa():
    au=at.automatonData()
    print(newStates(au.states)[0])
    c = dfa(au.state_start, au.state_final, au.states, au.alphabet, au.tran)
    c.printAutomation()
    return c.states,c.alphabet,c.state_start,c.state_final,c.tran
