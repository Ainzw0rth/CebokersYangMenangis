TERMINAL_SYMBOLS = [
    'ENTER', ';', '//', '/*', 
    '*/', '(', ')', '{', '}', 
    '[', ']', ',', '.', ':', 
    '=', 'DO', 'WHILE', 'BREAK', 
    'CONTINUE', 'FOR', 'IN', 'OF', 
    'DELETE', 'SWITCH', 'CASE', 'DEFAULT', 
    'IF', 'ELSE', 'RETURN', 'ASYNC', 
    'AWAIT', 'FUNCTION_C', 'VAR', 'LET', 
    'CONST', 'TRY', 'CATCH', 'FINALLY', 
    'THROW', 'TRUE', 'FALSE', 'NULL', 'COMMENT', 'EXPRESSION', 
    'DEFS', 'VAR_NAME', 'FUNCTION_CALL', 'EPSILON', 
    'NUMBER', 'STRING'
    ]

def is_terminal(x):
    return x in TERMINAL_SYMBOLS


START_SYMBOL = "START"


def cfg_from_file(filepath):
    # I.S. filepath adalah path ke file txt yang berisi CFG
    # F.S. Mengembalikan CFG dalam G = (V, X, R, S)
    #      V adalah set of variables/non-terminal symbols
    #      X adalah set of terminal symbols
    #      R adalah set of production rules
    #      S adalah start symbol
    
    # Persiapkan variabel yang akan digunakan
    V = []
    X = TERMINAL_SYMBOLS
    R = {}
    S = START_SYMBOL 

    file = open(filepath, 'r')
    line = file.readline()
    while line != "@":
        if (line[0] != "#" and line != "" and line != "\n"):
            production, rules = line.split(" -> ")
            if production not in V and production not in X:
                V.append(production)
            rules = rules.replace("\n", "")
            if production not in R.keys():
                R[production] = [rules.split(" ")]
                # R[production] = R[production].split(" ")
            else:
                inputted_rules = rules.split(" ")
                if "" in inputted_rules:
                    inputted_rules.remove("")
                R[production].append(inputted_rules)
            
        line = file.readline()
    
    file.close()
    return (V, X, R, S)