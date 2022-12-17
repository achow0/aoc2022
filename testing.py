"""
WARNING: SUPER SLOW BRUTE FORCE SOLUTION
I suggest against running this code. It took around 45 minutes to complete part 2.
"""

import sys
import re
#import functools
I = sys.stdin.read().splitlines()
pattern = re.compile(r"[A-Z0-9]+")

class Valve:
    def __init__(self,name,flow,*connected):
        self.name = name
        self.flow = int(flow)
        self.connected = connected

class gameState:
    def __init__(self,valves_state,curr_pos,flow,e_pos = None,you_opened = None):
        self.valves_state = valves_state
        self.curr_pos = curr_pos
        self.flow = flow
        self.e_pos = e_pos
        self.you_opened = you_opened

valves = {}

for i in I:
    find = pattern.findall(i)[1:]
    valves[find[0]] = Valve(*find)

possible_gs = [gameState({i:0 for i in valves},"AA",0)]
keep = 1000
for i in range(30):
    new_possible_gs = []
    for gs in possible_gs:
        if gs.valves_state[gs.curr_pos] == 0:
            new_valves_state = {key:gs.valves_state[key] if key != gs.curr_pos else 1 for key in gs.valves_state}
            new_flow = gs.flow + sum(valves[valve].flow for valve in gs.valves_state if gs.valves_state[valve])
            new_possible_gs += [gameState(new_valves_state,gs.curr_pos,new_flow)]
        for valve in valves[gs.curr_pos].connected:
            new_flow = gs.flow + sum(valves[valve].flow for valve in gs.valves_state if gs.valves_state[valve])
            new_possible_gs += [gameState(gs.valves_state,valve,new_flow)]
    possible_gs = sorted(new_possible_gs, key = lambda gs:gs.flow)[-keep:]

print(possible_gs[-1].flow)

keep = 450000
possible_gs = [gameState({i:0 for i in valves},"AA",0,"AA")]
for i in range(26):
    your_moves = []
    for gs in possible_gs:  # all possible moves for you
        if gs.valves_state[gs.curr_pos] == 0: # open valve
            new_valves_state = {key:gs.valves_state[key] if key != gs.curr_pos else 1 for key in gs.valves_state}
            your_moves += [gameState(new_valves_state,gs.curr_pos,gs.flow,gs.e_pos,gs.curr_pos)]
        for valve in valves[gs.curr_pos].connected: # move
            your_moves += [gameState(gs.valves_state,valve,gs.flow,gs.e_pos)]
    new_possible_gs = []
    for gs in your_moves: # all possible moves for elephant + you
        if gs.valves_state[gs.e_pos] == 0: # open valve
            new_valves_state = {key:gs.valves_state[key] if key != gs.e_pos else 1 for key in gs.valves_state}
            add_flow = sum(valves[v].flow for v in gs.valves_state if gs.valves_state[v] and v != gs.you_opened)
            new_flow = gs.flow + add_flow
            new_possible_gs += [gameState(new_valves_state,gs.curr_pos,new_flow,gs.e_pos)]
        for valve in valves[gs.e_pos].connected: # move
            add_flow = sum(valves[v].flow for v in gs.valves_state if gs.valves_state[v] and v != gs.you_opened)
            new_flow = gs.flow + add_flow
            new_possible_gs += [gameState(gs.valves_state,gs.curr_pos,new_flow,valve)]
    possible_gs = sorted(new_possible_gs, key = lambda gs:gs.flow)[-keep:]
print(possible_gs[-1].flow)
