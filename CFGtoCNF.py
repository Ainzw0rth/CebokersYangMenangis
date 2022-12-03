from FA import isVariable
from grammar_reader import is_terminal
import sys

# referensi : https://www.youtube.com/watch?v=7G0PwGrdlH8&ab_channel=Education4u

def CFG_to_CNF(CFG):
    # STEP 2 : JADIKAN SEBAGAI NORMAL FORM
    ada = True
    sys.stdout = open("CFGtoCNF.txt", "w")

    while ada:
        satuElemen = {}
        ada = False
        
        for key, value in CFG.items():
            for rule in value:
                if len(rule) == 1 and not is_terminal(rule[0]):
                    ada = True
                    if key not in satuElemen.keys():
                        satuElemen[key] = [[rule[0]]]
                    else:
                        satuElemen[key].append([rule[0]])

        for keySatuElemen, valueSatuElemen in satuElemen.items():
            for rule_unit in valueSatuElemen:
                for key, value in CFG.items():
                    if len(rule_unit) == 1 and key == rule_unit[0]:
                        if keySatuElemen not in CFG.keys():
                            CFG[keySatuElemen] = value
                        else:
                            for rule in value:
                                if rule not in CFG[keySatuElemen]:
                                    CFG[keySatuElemen].append(rule)
    
        for keySatuElemen, valueSatuElemen in satuElemen.items():
            for rule_unit in valueSatuElemen:
                if len(rule_unit) == 1:
                    CFG[keySatuElemen].remove(rule_unit)

    print("====================== STEP 1 ===========================")
    for key, value in CFG.items():
        print(key, value)

    # STEP 3: ganti rules yang memiliki 3 atau lebih elemen
    RulesBaru = {}
    del_productions = {}

    i = 0
    for key, value in CFG.items():
        for rule in value:
            temp = key
            temp_rule = [r for r in rule]
            while len(temp_rule) > 2:
                ruleTambahan  = f"Y{i}"
                if temp not in RulesBaru.keys():
                    RulesBaru[temp] = [[temp_rule[0], ruleTambahan ]]
                else:
                    RulesBaru[temp].append([temp_rule[0], ruleTambahan ])
                temp = ruleTambahan 
                temp_rule.remove(temp_rule[0])
                i += 1

            if temp not in RulesBaru.keys():
                RulesBaru[temp] = [temp_rule]
            else:
                RulesBaru[temp].append(temp_rule)
            
            if key not in del_productions.keys():
                del_productions[key] = [rule]
            else:
                del_productions[key].append(rule)

    for new_head, new_body in RulesBaru.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    print("====================== STEP 3 ===========================")
    for key, value in CFG.items():
        print(key, value)

    # STEP 4: ganti elemen yang terminal jadi variable rules baru
    RulesBaru = {}
    RulesLama = {}

    i = 0
    for head, body in CFG.items():
        for rule in body:
            temp = []
            ada = False
            for r in rule:
                temp.append(r)

            for x in range(len(rule)):
                if len(rule) == 1:
                    ada = False
                    break
                if is_terminal(rule[x]):
                    ada = True
                    simbolbaruX = f"X{i}"
                    i += 1
                    RulesBaru[simbolbaruX] = [[rule[x]]]
                    temp[x] = simbolbaruX

            if ada:
                if head not in RulesBaru.keys():
                    RulesBaru[head] = [temp]
                else:
                    RulesBaru[head].append(temp)

                if head not in RulesLama.keys():
                    RulesLama[head] = [rule]
                else:
                    RulesLama[head].append(rule)

    for new_head, new_body in RulesBaru.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    print("====================== RULES LAMA ===========================")
    for key, value in RulesLama.items():
        print(key, value)
    for del_head, del_body in RulesLama.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    print("====================== RULES BARU ===========================")
    for key, value in RulesBaru.items():
        print(key, value)

    print("====================== STEP 4 ===========================")
    for key, value in CFG.items():
        print(key, value)

    return CFG