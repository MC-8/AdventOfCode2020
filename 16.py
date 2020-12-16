from utils import *

rules = {}
my_ticket = []
nearby_tickets = []
with open('16.in','r') as fp:
    line = fp.readline()
    
    # Start by extracting rules
    ex = "(.+): (\d+)-(\d+) or (\d+)-(\d+)"
    while (line!="\n"):
        match = re.findall(ex, line)[0]
        rules[match[0]]=(range(int(match[1]),int(match[2])+1), range(int(match[3]),int(match[4])+1))
        line = fp.readline()
    
    # Scan my ticket
    line = fp.readline() # "your ticket"
    line = fp.readline()
    my_ticket = [int(x) for x in line.split(',')]
    # Scan nearby tickets
    line = fp.readline() # '\n'
    line = fp.readline() # "nearby tickets"
    line = fp.readline() # first ticket
    while (line):
        nearby_tickets.append([int(x) for x in line.split(',')])
        line = fp.readline()
    
def one(nearby_tickets):
    errors = 0
    for ticket in nearby_tickets:
        for number in ticket:
            valid_number = False
            # Check ranges
            for _, rule_ranges in rules.items():
                if number in rule_ranges[0] or number in rule_ranges[1]:
                    valid_number = True
                    break
            if not valid_number:
                errors += number
                break
    return errors

def purge_tickets(ticket_list, rules):
    nl = []
    valid = False
    for ticket in ticket_list:
        for number in ticket:
            valid = False
            # Check ranges
            for _, rule_ranges in rules.items():
                if number in rule_ranges[0] or number in rule_ranges[1]:
                    valid = True
                    break
            if not valid:
                break
        if valid: 
            nl.append(ticket)
    return(nl)
    
def two(valid_tickets):
    # Scan one field at the time. Find rule that applies to all.
    field_rule = {}
    rule_map = {}
    for field_number in range(len(valid_tickets[0])):
        rules_names = set(rules.keys())
        for ticket in valid_tickets:
            for rule_name, rule_ranges in rules.items():
                if not(ticket[field_number] in rule_ranges[0] or ticket[field_number] in rule_ranges[1]):
                    # Not the right rule for this field
                    rules_names-={rule_name}
        rule_map[field_number] = rules_names
    
    # Since multiple rules may apply to one field, make sure we identify unique
    # rules (that is only one rule applies to a given field), and exclude that for subsequent checks
    # This way we find the field with only one rule, then the field with 2 rules (of which one is already done).
    # And repeat
    done_rules = set()
    while len(field_rule)<len(valid_tickets[0]):
        for field_number in range(len(rule_map)):
            # Only one matching name
            if len(found_field:=(rule_map[field_number]-done_rules))==1:
                done_rules|=found_field
                field_rule[field_number] = found_field.pop()
                break
    # All found. Now calculate the solution. That is multiply all (6) fields
    # that start with the word "departure"
    sol = 1
    for field_idx, field_nr in enumerate(my_ticket):
        if "departure" in field_rule[field_idx]:
            sol*=field_nr
    return sol
    
    
if __name__ == "__main__":
    print(f"{one(nearby_tickets) = }") # 25984
    valid_tickets = purge_tickets(nearby_tickets, rules)
    print(f"{two(valid_tickets) = }") # 1265347500049
