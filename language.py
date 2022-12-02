from FA import isNumber, isStringValid

STR_TO_GRAMMAR = {
# For Literals    
    "\n": "ENTER",
    ";" : ";",
    "(": "(",
    ")": ")",
    "{": "{",
    "}": "}",
    "[": "[",
    "]": "]",
    ",": ",",
    ".": ".",
    ":": ":",
    "=": "=",
    
# Loop Control
    "do": "DO",
    "while":"WHILE",
    "break": "BREAK",
    "continue": "CONTINUE",
    "for": "FOR",
    "in": "IN",
    "of": "OF",

# Delete
    "delete" : "DELETE",

# Conditional
    "switch" : "SWITCH",
    "case" : "CASE",
    "default" : "DEFAULT",
    "if" : "IF",
    "else" : "ELSE",


# Functions
    "return": "RETURN",
    "async": "ASYNC",
    "await": "AWAIT",
    "function": "FUNCTION_C",

# Variables Definition
    "var": "VAR",
    "let": "LET",
    "const": "CONST",

# Try Catch / Throw
    "try": "TRY",
    "catch": "CATCH",
    "finally": "FINALLY",
    "throw": "THROW",

# DATA TYPES
    "true": "TRUE",
    "false": "FALSE",
    "null": "NULL",

# CONSOLE
    "console.log": "CONSOLE",

# SPECIAL VALUES
    "@CMT_SINGLE": "COMMENT_STMT",
    "@CMT_MULTI": "COMMENT_STMT",
    "@EXP": "EXPRESSION",
    "@DEFS": "DEFS",
    "@VAR": "VAR_NAME",
    "@FCALL": "FUNCTION_CALL",
    "" : "EPSILON",
    "@NUM": "NUMBER",
    "@STR": "STRING",
}

def rearrange_string(string):
    #I.S. sebuah string
    #F.S. string yang sudah lebih rapih spacingnya

    NEED_SPACING = [
        "(", ")", "{", "}", "[", "]", ",", ".", ":", "=", "+", "-", "*", "/", "%", "^", "<", ">", "<=", ">=", "==", 
        "!=", "&&", "||", "!", "===", "!==", ">>", "<<", ">>>", "&", "|", "~", "&&=", "||=", "&=", "|=", 
        "^=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", ">>>=", "^=", "**", "**=", ";", "for", "in", "of", "while",
        "do", "break", "continue", "return", "async", "await", "function", "var", "let", "const", "try", "catch",
        "finally", "throw", "true", "false", "null", "CONSOLE", "\n"
    ]

    DONT_SPACE = [
        "//", "/*", "*/"
    ]

    i = 0
    while i < len(string) - 1:
        if string[i] in NEED_SPACING:
            j = i
            while string[i:j+1] in NEED_SPACING:
                j += 1
            
            if not string[i:j+1] in DONT_SPACE:
                string = string[:i] + " " + string[i:j] + " " + string[j:]
                i = j + 2
            else:
                i = j + 1
        else:
            i += 1

    return string

def remove_empty_str(list_of_str):
    # I.S. list of string
    # F.S. list of string yang sudah tidak ada string kosongnya
    i = 0
    while i < len(list_of_str):
        if list_of_str[i] == "":
            list_of_str.remove(list_of_str[i])
        else:
            i += 1

    return list_of_str

def get_variable_from_defs(string):
    # I.S. string yang berisi definisi variabel
    # F.S. list of string yang berisi nama variabel
    list_of_variable = []
    string = string.split(" ")
    string = remove_empty_str(string)
    for i in range(len(string)):
        if string[i] == "=":
            if string[i-1] not in list_of_variable:
                list_of_variable.append(string[i-1])
        if string[i] == ",":
            if string[i+1] not in list_of_variable:
                list_of_variable.append(string[i+1])
    
    return list_of_variable

def handle_special_value(string):
    # I.S. string
    # F.S. string yang special valuenya sudah dihandle
    #      special Value: COMMENT dan EXPRESSION
    #      mengembalikan string yang sudah dihandle dan list of extracted special value and variable 

    operator = [
        "+", "-", "*", "/", "%", "^", "<", ">", "<=", ">=", "==", "!=", "&&", "||", "!", "===", "!==", ">>", "<<", ">>>", "&", "|", "~", 
        "&&=", "||=", "&=", "|=", "^=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", ">>>=", "^=", "**", "**=", "="
    ]

    object_operator = ["."]

    defs = ["let", "var", "const"]
    exp_start = ["(", "[", "{", "true", "false", "null", "function", "async", "await", "try", "throw", "for", "while", "do", "if", "switch", "return", "break", "continue", "CONSOLE", ";"]
    exp_end = [")", "]", "}", ";", "else", "catch", "finally", "in", "of", "for", "while", "do", "if", "switch", "return", "break", "continue"]
    def_end = [";", "\n", ""]
    
    i = 0
    list_of_expression = []
    list_of_variable = []
    while i <= len(string) - 1:
        # Handle Comment
        if string[i] == "/" and string[i+1] == "/":
            j = i + 2
            while not string[j] == "\n" and j < len(string) - 1:
                j += 1
            string = string[:i] + " @CMT_SINGLE " + string[j-1:]
            i = j - 1
        elif string[i] == "/" and string[i+1] == "*":
            j = i + 2
            while not (string[j] == "*" and string[j+1] == "/" and j < len(string) - 1):
                j += 1
            string = string[:i] + " @CMT_MULTI " + string[j+2:]
            i = j -1
        else:
            if string[i] != " ":
                current_str = string[i]
                j = i + 1
                while j < len(string) and string[j] != " ": 
                    current_str += string[j]
                    j += 1

                # Handling Variables Definition
                if current_str in defs:
                    while string[j] not in def_end and j < len(string) - 1:
                        j += 1
                    list_of_variable += get_variable_from_defs(string[i:j])
                    string = string[:i] + " @DEFS " + string[j:]
                    i = i + 6

                # Handling Expression
                elif current_str in operator:
                    j_e = j
                    i_e = i - 1
                    successorWord = ""
                    while successorWord not in exp_end and j_e <= len(string) - 1:
                        successorWord = ""
                        j_s = j_e
                        while j_s < len(string) and string[j_s] == " ":
                            j_s += 1
                            j_e += 1
                        while j_e < len(string) and string[j_e] != " ":
                            successorWord += string[j_e]
                            j_e += 1
                    predecessorWord = ""
                    while predecessorWord not in exp_start and i_e >= 0:
                        predecessorWord = ""
                        i_s = i_e
                        while i_s >= 0 and string[i_s] == " " and i_s >= 0:
                            i_s -= 1
                            i_e -= 1
                        while i_e >= 0 and string[i_e] != " " and i_e > 0:
                            predecessorWord = string[i_e] + predecessorWord
                            i_e -= 1
                    list_of_expression.append(string[i_e+1:j_e])
                    string = string[:i_e+3] + " @EXP " + string[j_e-1:]
                    i = i_e + 9
                else:
                    i = j 
            else:
                while string[i] == " " and i < len(string):
                    i += 1

    i = 0                    
    while i <= len(string) - 1:
        if string[i] != " ":
            current_str = string[i]
            j = i + 1
            while j < len(string) and string[j] != " ": 
                current_str += string[j]
                j += 1
            # Handling Variable
            if current_str not in STR_TO_GRAMMAR.keys() and not current_str.startswith("@"):
                if isNumber(current_str):
                    string = string[:i] + " @NUM " + string[j:]
                elif isStringValid(current_str):
                    string = string[:i] + " @STR " + string[j:]
                else:
                    list_of_variable.append(current_str)
                    string = string[:i] + " @VAR " + string[j:]
                i = i + 5
            else:
                i = j 
        else:
            while string[i] == " ":
                i += 1
                if i == len(string):
                    break
                    
    return string, list_of_expression, list_of_variable


def string_to_grammar(string):
    converted_str = []
    expressions = []
    variables = []

    init_str = rearrange_string(string)
    init_str, expressions, variables = handle_special_value(init_str)
    init_str = init_str.split(" ")
    init_str = remove_empty_str(init_str)
    
    for i in range(len(init_str)):
        if len(init_str[i]) > 1 and init_str[i].endswith("\n"):
            init_str[i] = init_str[i][:-1]
            if init_str[i] in STR_TO_GRAMMAR.keys():
                converted_str.append(STR_TO_GRAMMAR[init_str[i]])
                converted_str.append(STR_TO_GRAMMAR["\n"])
                continue
        if init_str[i] in STR_TO_GRAMMAR.keys():
                converted_str.append(STR_TO_GRAMMAR[init_str[i]])
        else:
            converted_str.append(init_str[i])

    converted_str.append(STR_TO_GRAMMAR["\n"])
    # print(converted_str)
    return converted_str, expressions, variables