import random
from copy import deepcopy
from BFS import *

def minimizeDFA(fileName):

    DFA = Simplify_DFA(fileName)
    state_graph1 = {
        'states': DFA.states,
        'start_states': DFA.state_start,
        'end_states': DFA.state_final,
        'transitions': DFA.tran,
        'alphabet': DFA.alphabet,
    }
    # print(DFA.state_final)

    def hopcroft_algorithm(G):
        alphabet = set(G['alphabet'])
        start_state = '0'
        end_states = set(G['end_states'])
        new_end_states = []
        states = set(G['states'])
        transitions = G['transitions']
        not_end_states = states - end_states

        def get_source_set(target_set, char):
            source_set = set()
            for state in states:
                try:
                    if transitions[state][char] in target_set:
                        source_set.update(state)
                except KeyError:
                    pass
            return source_set


        if len(not_end_states) == 0:
            P = [end_states]
            W = [end_states]
        else:
            P = [end_states, not_end_states]
            W = [end_states, not_end_states]

        while W:

            A = random.choice(W)
            W.remove(A)

            for char in alphabet:
                X = get_source_set(A, char)
                P_temp = []

                for Y in P:
                    S = X & Y
                    S1 = Y - X

                    if len(S) and len(S1):
                        P_temp.append(S)
                        P_temp.append(S1)

                        if Y in W:
                            W.remove(Y)
                            W.append(S)
                            W.append(S1)
                        else:
                            if len(S) <= len(S1):
                                W.append(S)
                            else:
                                W.append(S1)
                    else:
                        P_temp.append(Y)
                P = deepcopy(P_temp)

        tran = {}
        for x in P:
            tran[str(P.index(x))] = {}
            for letter in alphabet:
                tran[str(P.index(x))][letter] = 'null'

        total_states = []
        for x in P:
            total_states.append(str(P.index(x)))
            if len(set(DFA.state_start) & set(x)) > 0:
                start_state = str(P.index(x))
            if len(set(DFA.state_final) & set(x)) > 0:
                new_end_states.append(str(P.index(x)))
            for state in x:
                for letter in alphabet:
                    temp = transitions[str(state)][letter]
                    for z in P:
                        if temp in z:
                            tran[str(P.index(x))][letter] = str(P.index(z))



        print('states: ', total_states)
        print('alphabet: ', alphabet)
        print('transitions: ', tran)
        print('start state: ', start_state)
        print('end states: ', new_end_states)

        return total_states, alphabet, start_state \
              ,new_end_states,tran
    return hopcroft_algorithm(state_graph1)


