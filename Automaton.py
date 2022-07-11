class Automaton(object):
    def __init__(self, states, alphabet, tran, state_start, state_final):
        self.states = states
        self.alphabet = alphabet
        self.tran = tran
        self.state_start = state_start
        self.state_final = state_final

    # hàm chạy xâu
    def process(self, w):
        ReadSymbols = 0
        CurrentState = self.state_start
        for ReadSymbols in range(0, len(w)):
            if w[ReadSymbols] not in self.alphabet:
                print('Xâu không phải là xâu nhị phân!')
                exit()
            CurrentState = self.tran[CurrentState][w[ReadSymbols]]


        if CurrentState in self.state_final:
            print('YES')
        else:
            print('NO')

    # hàm in ra thuộc tính của Automaton
    def __printAutomaton__(self):
        print(self.states)
        print(self.alphabet)
        print(self.tran)
        print(self.state_start)
        print(self.state_final)
