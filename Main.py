# chạy cmd này tại terminal để download thư viện beautifulsoup4: pip install beautifulsoup4
# chạy cmd này tại terminal để download lxml parser: pip install lxml

from BFS import *

print('Hãy nhập vào địa chỉ file chứa Automaton: ')
link = input()

DFA = Simplify_DFA(link)
print(DFA.states)
print(DFA.alphabet)
print(DFA.state_start)
print(DFA.state_final)
print(DFA.tran)


