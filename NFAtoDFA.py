from ReadNFA import *

NFA = readNFA(input())
print(NFA.states)
print(NFA.alphabet)
print(NFA.tran)
print(NFA.state_start)
print(NFA.state_final)
print(NFA.tran['0']['$'])


def getEpsilonTrans(state):
    for key in NFA.tran:
        value = NFA.tran[key]
        if NFA.tran[key][value]:
            return NFA.tran[key][value]

    return []


for x in NFA.states:
    eps = {x}
    queue = []
    queue.extend(NFA.tran[x]['$'])
    queue.append(x)
    eps.update(queue)

    while queue:
        currentState = queue.pop()
        queue += [x for x in getEpsilonTrans(currentState) if x not in eps]
        eps.update(queue)

    print(eps)
