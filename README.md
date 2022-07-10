# DFA READER

Author: Vu Thi Diem Quynh 20197100

## ***Description***:

* This program reads data of an Automaton from a JFF file and generates the corresponding Deterministic Finite Automaton.
Then it determines whether a given string is accepted or not by the DFA.

* Language: Python

## ***Modules***:

* Automaton: a class-based module that represents a Deterministic Finite Automaton. Has as class attributes a list of states, a list of alphabets, a string for the initial state and a list final states, and a transition table represented as a nested dictionary. Has methods for processing a string and a print method.
* ReadFile: a functional-based module that contains functions for reading a jff file given its name, and returns an instance of an Automaton given the information.

## ***How to run this program***

* Download beautifulsoup4, a Python library for pulling data out of HTML and XML files.
* Download lxml parser that provides a very simple and powerful API for parsing XML and HTML.