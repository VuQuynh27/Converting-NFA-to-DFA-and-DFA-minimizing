import Data as dt
class Automaton(object):
    def __init__(self, states=None, alphabet=None, tran=None, state_start=None, state_final=None):
        self.state_start = state_start
        self.state_final = state_final
        self.states = states
        self.alphabet = alphabet
        self.tran = tran

    # automation data frame
    def automatonForm(self):
        automaton = {
            'state_start': self.state_start,
            'state_final': self.state_final,
            'states': self.states,
            'alphabet': self.alphabet,
            'tran': self.tran
        }
        return automaton
    def printAutomation(self):
        print(self.states)
        print(self.alphabet)
        print(self.tran)
        print(self.state_start)
        print(self.state_final)

# Input data in otomat
def automatonData():
    ndftData = dt.ndfInput()
    automaton = Automaton()
    for i in ndftData:
        if i == 'state_start':
            automaton.state_start = ndftData[i]
        elif i == 'state_final':
            automaton.state_final = ndftData[i]
        elif i == 'states':
            automaton.states = ndftData[i]
        elif i == 'alphabet':
            automaton.alphabet = ndftData[i]
        elif i == 'tran':
            automaton.tran = ndftData[i]
    return automaton

