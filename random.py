import random as rd


PoolToPick=[
    12501,
    12502,
    12504,
    12505,
    12506,
    12508,
    12509,
    12510,
    12511,
    12513,
    12514,
    12515,
    12516,
    12517,
    12521,
    12522,
    12523,
    12524,
    12525,
    12526,
    12527,
    12528,
    12529,
    12530,
    12531,
    12532,
    12533,
    12534,
    12535,
    12536,
    12537,
    12538,
    12540,
    12541,
    12542,
    12543,
    12544,
    12545,
    12546,
    12547,
    12548,
    12550,
    12552,
    12553,
    12554,
    12555,
    12556,
    12557,
    12558,
    12558,
    12559,
    12561,
    12562,
    12564,
    12568,
    12570,
    12571,
    12573
]
print(len(PoolToPick))
HasLaptop =[
    12501,
    12505,
    12506,
    12508,
    12509,
    12511,
    12514,
    12527,
    12529,
    12533,
    12534,
    12535,
    12536,
    12538,
    12540,
    12541,
    12542,
    12543,
    12544,
    12548,
    12550,
    12552,
    12556,
    12568,
    12570,
    12571
]
print(len(HasLaptop))
PreDefinedGirlLeaders=[
    12532,
    12535,
    12547,
    12552,
    12556,
    12561,
    12562,
    12571
]
PreDefinedBoyLeaders=[
    12526,
    12506
]
PreDefinedTeam1=[
    12571,
    12536,
    12509
]
PreDefinedTeam2=[
    12532,
    12543,
    #one more member to be added using rd.choice() from PoolToPick
]

'''
each team should have 3 members, one of them is the leader, and the other two are picked randomly from the pool of students.
each team should have at least one member who has a laptop.
Predefined Girls leaders' team should be formed first, then the predefined Boys leaders' team should be formed, and then the remaining teams should be formed.
no member should be in more than one team.
any remaining members who are not in any team should be listed as "Unassigned".
then print the list of teams along with their members and leader and the list of unassigned members.
'''