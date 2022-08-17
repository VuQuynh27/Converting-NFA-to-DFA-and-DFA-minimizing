# download thư viện beautifulsoup4: pip install beautifulsoup4
# download lxml parser: pip install lxml
import utils as jf
import os
from eNfatoDfa import *
def CreateFile():
  total_states, alphabet, start_state,new_end_states,tran = returnDfa()
  test = jf.Jflap("DFANotMini")
  test.create_file(os.getcwd())
  for i in total_states:
    if i in start_state:
      test.add_state(i, initial=True)
    elif i in new_end_states:
      test.add_state(i, final=True)
    else:
      test.add_state(i)
  sigma = [i for i in alphabet]
  test.create_sigma(sigma)
  for start_states, trans in tran.items():
    for alphabet, end_states in trans.items():
      test.add_transition_by_name(start_states,end_states, alphabet)