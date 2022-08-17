# Converting NFA to DFA and DFA minimizing

Author: Vu Thi Diem Quynh 20197100,Nguyen Van Manh 20195088, Ho Trung Cong 20194237

## ***Description***:

### This program:
* reads data of a NFA from a JFF file.
* converts NFA to DFA.
* simplify DFA.
* minimize DFA.

### Language: Python

## ***Modules***:

* Automaton: a class-based module that represents a Finite Automaton. Has a class attributes, a list of states, a list of alphabets, a string for the initial state and a list final states, and a transition table represented as a nested dictionary.
* ReadNfaFile: a functional-based module that contains functions for reading a jff file given its name, and returns an instance of a NFA given the information.
* Data:  a functional-based module that contains functions for Create automata from output of ReadNfaFile
* eNfatoDfa: a functional-based module that contains functions for converting NFA to complete DFA.
* ReadFile: a functional-based module that contains functions for reading a jff file given its name, and returns an instance of a DFA given the information.
* Graph: a class-based module that represents a unweighted directed graph and BFS function.
* BFS: a functional-based module that contains functions for traversing a DFA and simplifying it.
* utils:  a functional-based module that contains functions for Create jff File 
* MinimizeDFA: a functional-based module that contains functions for merging nondistingguishable states of DFA and modify its states, start states, final states, and transtions.

## ***To run this program***

* Download beautifulsoup4, a Python library for pulling data out of HTML and XML files.
* Download lxml parser that provides a very simple and powerful API for parsing XML and HTML.
* Run Main.py and input file Nfa name
