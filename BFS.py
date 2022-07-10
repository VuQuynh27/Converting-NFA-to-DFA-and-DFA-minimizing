#Chương trình in ra các trạng thái có thể đến được từ
# trạng thái bắt đầu của 1 DFA với file input jff.

from ReadFile import *
from Graph import *
from Automaton import *

def Simplify_DFA(fileName):

	# tạo đồ thị g
	g = Graph()
	#fileName = input('Hãy nhập vào địa chỉ chứa automaton: ')
	DFA = readFile(fileName)
	srt = 0

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

	for x in states:
		state_id = x.get('id')
		if x.initial:
			srt = int(state_id)
	# print(_states)

	# print(_state_start)
	# print(_state_final)

	transitions = bs_data.find_all('transition')

	for x in transitions:
		bs_from = x.find('from')
		bs_to = x.find('to')
		g.addEdge(int(bs_from.get_text()), int(bs_to.get_text()))

	#print('Danh sách các trạng thái có thể tới được từ trạng thái bắt đầu: ')
	g.BFS(srt)
	#print(g.reachable_states)
	states_minimum = g.reachable_states
	#print(states_minimum)

	all_states = [int(x) for x in DFA.states]
	DFA.states = states_minimum
	print('Danh sách các trạng thái có thể tới được từ trạng thái bắt đầu: ',DFA.states)

	for x in all_states:
		if x not in DFA.states:
			del DFA.tran[str(x)]

	#print(DFA.tran)
	return Automaton(DFA.states, DFA.alphabet, DFA.tran, DFA.state_start, DFA.state_final)

