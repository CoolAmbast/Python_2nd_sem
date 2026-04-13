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

# Track used people (cannot be used again in any role)
used_people = set()

# Track leaders separately to prevent them from becoming members
all_leaders = set()

# Store teams
teams = []

def has_laptop_member(members_list):
    """Check if at least one member has a laptop"""
    return any(m in HasLaptop for m in members_list)

def get_members_with_laptop(pool):
    """Return list of members from pool who have laptops"""
    return [m for m in pool if m in HasLaptop]

def get_members_without_laptop(pool):
    """Return list of members from pool who don't have laptops"""
    return [m for m in pool if m not in HasLaptop]

# 1. Create PreDefinedTeam1
teams.append({"leader": 12571, "members": [12536, 12509]})
used_people.update([12571, 12536, 12509])
all_leaders.add(12571)

# 2. Create PreDefinedTeam2 with one random member
remaining_pool = [x for x in PoolToPick if x not in used_people and x not in all_leaders]
# Team2 already has 12543, check if it has laptop
team2_members = [12543]
if 12543 in HasLaptop:
    # Already has laptop, can pick any random member
    random_member = rd.choice(remaining_pool)
else:
    # Need to ensure at least one laptop member
    laptop_available = [x for x in remaining_pool if x in HasLaptop]
    if laptop_available:
        random_member = rd.choice(laptop_available)
    else:
        random_member = rd.choice(remaining_pool)

teams.append({"leader": 12532, "members": [12543, random_member]})
used_people.update([12532, 12543, random_member])
all_leaders.add(12532)

# 3. Form teams for remaining Girl Leaders
remaining_girl_leaders = [g for g in PreDefinedGirlLeaders if g not in used_people]

for leader in remaining_girl_leaders:
    if leader in used_people:
        continue
    
    # Find available members (not used yet and not leaders)
    available = [x for x in PoolToPick if x not in used_people and x not in all_leaders and x != leader]
    
    if len(available) < 2:
        break
    
    # Ensure at least one member has a laptop
    laptop_available = get_members_with_laptop(available)
    non_laptop_available = get_members_without_laptop(available)
    
    if len(laptop_available) >= 1:
        # Pick one laptop member
        laptop_member = rd.choice(laptop_available)
        # Pick second member from remaining (could be laptop or non-laptop)
        remaining_after_laptop = [x for x in available if x != laptop_member]
        second_member = rd.choice(remaining_after_laptop)
        chosen = [laptop_member, second_member]
    else:
        # No laptops available, just pick randomly (but this violates requirement)
        chosen = rd.sample(available, 2)
    
    teams.append({"leader": leader, "members": chosen})
    used_people.update([leader] + chosen)
    all_leaders.add(leader)

# 4. Form teams for Boy Leaders (12526 and 12506)
for leader in PreDefinedBoyLeaders:
    if leader in used_people:
        continue
    
    # Find available members (not used yet and not leaders)
    available = [x for x in PoolToPick if x not in used_people and x not in all_leaders and x != leader]
    
    if len(available) < 2:
        break
    
    # Ensure at least one member has a laptop
    laptop_available = get_members_with_laptop(available)
    non_laptop_available = get_members_without_laptop(available)
    
    if len(laptop_available) >= 1:
        laptop_member = rd.choice(laptop_available)
        remaining_after_laptop = [x for x in available if x != laptop_member]
        second_member = rd.choice(remaining_after_laptop)
        chosen = [laptop_member, second_member]
    else:
        chosen = rd.sample(available, 2)
    
    teams.append({"leader": leader, "members": chosen})
    used_people.update([leader] + chosen)
    all_leaders.add(leader)

# 5. Form remaining teams from leftover members
# Each team needs 1 leader (pick randomly) + 2 members
# Ensure each team has at least one laptop member
remaining_members = [x for x in PoolToPick if x not in used_people and x not in all_leaders]

while len(remaining_members) >= 3:
    # Pick a random leader from remaining members
    leader_idx = rd.randint(0, len(remaining_members) - 1)
    leader = remaining_members.pop(leader_idx)
    all_leaders.add(leader)
    
    # Ensure we have at least one laptop member available if needed
    laptop_available = [m for m in remaining_members if m in HasLaptop]
    non_laptop_available = [m for m in remaining_members if m not in HasLaptop]
    
    if len(laptop_available) >= 1:
        # Pick one laptop member
        laptop_member_idx = remaining_members.index(rd.choice(laptop_available))
        laptop_member = remaining_members.pop(laptop_member_idx)
        
        # Pick second member randomly
        second_member_idx = rd.randint(0, len(remaining_members) - 1)
        second_member = remaining_members.pop(second_member_idx)
        
        members = [laptop_member, second_member]
    else:
        # No laptops left, just pick two randomly
        member_indices = rd.sample(range(len(remaining_members)), 2)
        member_indices.sort(reverse=True)
        members = [remaining_members.pop(i) for i in member_indices]
    
    teams.append({"leader": leader, "members": members})
    used_people.update([leader] + members)

# 6. Unassigned members
unassigned = [x for x in PoolToPick if x not in used_people]

# 7. Print results
print("=" * 50)
print("TEAMS FORMED")
print("=" * 50)

all_leaders_list = list(all_leaders)
all_members = [m for team in teams for m in team["members"]]

for i, team in enumerate(teams, 1):
    leader = team["leader"]
    members = team["members"]
    has_laptop_status = []
    
    # Check if team meets laptop requirement
    team_has_laptop = any(m in HasLaptop for m in members)
    
    for m in [leader] + members:
        if m in HasLaptop:
            has_laptop_status.append(f"{m} (Has Laptop ✓)")
        else:
            has_laptop_status.append(f"{m}")
    
    print(f"\nTeam {i}:")
    print(f"  Leader: {leader}")
    print(f"  Members: {members[0]}, {members[1]}")
    print(f"  Laptop status: {', '.join(has_laptop_status)}")
    if not team_has_laptop:
        print(f"  ⚠️ WARNING: No laptop member in this team!")

print("\n" + "=" * 50)
print("VERIFICATION")
print("=" * 50)
print(f"Total people: {len(PoolToPick)}")
print(f"Total used: {len(used_people)}")
print(f"Total leaders: {len(all_leaders)}")
print(f"Total members: {len(all_members)}")
print(f"Leaders + Members: {len(all_leaders) + len(all_members)}")

# Check for any overlap between leaders and members
leader_member_overlap = set(all_leaders) & set(all_members)
if leader_member_overlap:
    print(f"❌ ERROR: These people are both leaders and members: {leader_member_overlap}")
else:
    print(f"✓ No overlap between leaders and members")

print("\n" + "=" * 50)
print("UNASSIGNED MEMBERS")
print("=" * 50)
if unassigned:
    print(", ".join(map(str, unassigned)))
    print(f"Total unassigned: {len(unassigned)}")
    laptop_unassigned = [u for u in unassigned if u in HasLaptop]
    if laptop_unassigned:
        print(f"Unassigned laptop owners: {', '.join(map(str, laptop_unassigned))}")
else:
    print("All members have been assigned to teams.")