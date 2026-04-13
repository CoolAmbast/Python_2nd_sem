import random as rd

PoolToPick = [
    12501, 12504, 12505, 12506, 12508, 12509, 12511,
    12514, 12515, 12516, 12517, 12521, 12522, 12523, 12525, 12526,
    12529, 12531, 12532, 12533, 12534, 12535, 12536,
    12537, 12540, 12541, 12542, 12543, 12544, 12545, 12546, 12547,
    12548, 12550, 12552, 12553, 12556, 12558, 12558,
    12559, 12561, 12562, 12568, 12571, 12573
]

HasLaptop = [
    12501, 12505, 12506, 12508, 12509, 12511, 12514, 12529, 12533,
    12534, 12535, 12536, 12540, 12541, 12542, 12543, 12544, 12548,
    12550, 12552, 12556, 12568, 12571
]

PreDefinedGirlLeaders = [
    12532, 12535, 12547, 12552, 12556, 12561, 12562, 12571
]

PreDefinedBoyLeaders = [
    12526, 12506
]

PreDefinedTeam1 = [12571, 12536, 12509]  # leader + 2 members
PreDefinedTeam2 = [12532, 12543]  # leader + 1 member, one more needed

# Track used members
used_members = set()

# Store teams
teams = []

# 1. Create PreDefinedTeam1
teams.append({"leader": 12571, "members": [12536, 12509]})
used_members.update([12571, 12536, 12509])

# 2. Create PreDefinedTeam2 with one random member
remaining_pool = [x for x in PoolToPick if x not in used_members]
random_member = rd.choice(remaining_pool)
teams.append({"leader": 12532, "members": [12543, random_member]})
used_members.update([12532, 12543, random_member])

# 3. Form teams for remaining Girl Leaders
remaining_girl_leaders = [g for g in PreDefinedGirlLeaders if g not in used_members]

for leader in remaining_girl_leaders:
    if leader in used_members:
        continue
    
    # Find available members (not used yet)
    available = [x for x in PoolToPick if x not in used_members and x != leader]
    
    if len(available) < 2:
        break  # Not enough members to form a team
    
    # Pick 2 random members
    chosen = rd.sample(available, 2)
    teams.append({"leader": leader, "members": chosen})
    used_members.update([leader] + chosen)

# 4. Form teams for Boy Leaders (12526 and 12506)
for leader in PreDefinedBoyLeaders:
    if leader in used_members:
        continue
    
    available = [x for x in PoolToPick if x not in used_members and x != leader]
    
    if len(available) < 2:
        break
    
    chosen = rd.sample(available, 2)
    teams.append({"leader": leader, "members": chosen})
    used_members.update([leader] + chosen)

# 5. Form remaining teams from leftover members
# Each team needs 1 leader (pick randomly) + 2 members
remaining_members = [x for x in PoolToPick if x not in used_members]

while len(remaining_members) >= 3:
    # Pick a random leader from remaining members
    leader_idx = rd.randint(0, len(remaining_members) - 1)
    leader = remaining_members.pop(leader_idx)
    
    # Pick 2 random members
    member_indices = rd.sample(range(len(remaining_members)), 2)
    member_indices.sort(reverse=True)  # To pop from end without index issues
    
    members = [remaining_members.pop(i) for i in member_indices]
    
    teams.append({"leader": leader, "members": members})
    used_members.update([leader] + members)

# 6. Unassigned members
unassigned = [x for x in PoolToPick if x not in used_members]

# 7. Print results
print("=" * 50)
print("TEAMS FORMED")
print("=" * 50)

for i, team in enumerate(teams, 1):
    leader = team["leader"]
    members = team["members"]
    has_laptop_status = []
    
    for m in [leader] + members:
        if m in HasLaptop:
            has_laptop_status.append(f"{m} (Has Laptop)")
        else:
            has_laptop_status.append(f"{m}")
    
    print(f"\nTeam {i}:")
    print(f"  Leader: {leader}")
    print(f"  Members: {members[0]}, {members[1]}")
    print(f"  Laptop status: {', '.join(has_laptop_status)}")

print("\n" + "=" * 50)
print("UNASSIGNED MEMBERS")
print("=" * 50)
if unassigned:
    print(", ".join(map(str, unassigned)))
    print(f"Total unassigned: {len(unassigned)}")
else:
    print("All members have been assigned to teams.")