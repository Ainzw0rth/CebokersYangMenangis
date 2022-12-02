# variabel FA
def state0var(c):
    if ord(c) == 95:
        state = 1
    elif ord(c) == 36:
        state = 1
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 1
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 1
    else:
        state = 2

    return state

def state1var(c):
    if ord(c) == 95:
        state = 1
    elif ord(c) == 36:
        state = 1
    elif ord(c) >= 48 and ord(c) <= 57:
        state = 1
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 1
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 1
    else:
        state = 2

    return state

def state2var(c):
    state = 2

    return state

def isVariable(s):
    state = 0
    for i in range (len(s)):
        if (state == 0):
            state = state0var(s[i])
        if (state == 1):
            state = state1var(s[i])
        if (state == 2):
            state = state2var(s[i])
    if (state == 1):
        return True
    else :
        return False

# FA untuk angka
def statenumber0(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 2
    elif (ord(c) == 45):
        state = 1
    else:
        state = 4

    return state

def statenumber1(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 2
    else :
        state = 4

    return state

def statenumber2(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 2
    elif (ord(c) == 46):
        state = 3
    else :
        state = 4

    return state

def statenumber3(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 2
    else :
        state = 4

    return state

def statenumber4(c):
    return 4

def isNumber(s):
    state = 0
    for i in range (len(s)):
        if (state == 0):
            state = statenumber0(s[i])
        elif (state == 1):
            state = statenumber1(s[i])
        elif (state == 2):
            state = statenumber2(s[i])
        elif (state == 3):
            state = statenumber3(s[i])
        elif (state == 4):
            state = statenumber4(s[i])
    if (state == 2):
        return True
    else :
        return False

# FA untuk string
def stateString0(c):
    if (ord(c) == 34):
        state = 1
    elif (ord(c) == 39):
        state = 4
    else:
        state = 2
    return state

def stateString1(c):
    if (ord(c) == 34):
        state = 2
    else:
        state = 1
    return state

def stateString2(c):
    return 3

def stateString4(c):
    if (ord(c) == 34):
        state = 5
    else:
        state = 4

    return state

def stateString5(c):
    return 6

def isStringValid(s):
    state = 0
    for i in s:
        if (state == 0):
            stateString0(i)
        elif (state == 1):
            stateString1(i)
        elif (state == 2):
            stateString2(i)
        elif (state == 4):
            stateString4(i)
        elif (state == 5):
            stateString5(i)

    if (state == 2 or state == 5):
        return True
    else:
        return False

# FA untuk operasi
def startOperasional(c):
    if ord(c) == 95:
        state = 1
    elif ord(c) == 36:
        state = 1
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 1
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 1
    else: 
        # jika angka
        if ord(c) >= 48 and ord(c) <= 57:
            state = 4
        elif ord(c) == 46:
            state = 3
        else:
            state = 20 # dead state
        
    return state

def stateSatuOperasional(c):
    if ord(c) == 95:
        state = 1
    elif ord(c) == 36:
        state = 1
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 1
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 1
    else: 
        # jika angka
        if ord(c) >= 48 and ord(c) <= 57:
            state = 4
        elif ord(c) == 37 or ord(c) == 42 or ord(c) == 43 or ord(c) == 45 or ord(c) == 47:
            state = 17              # start state 2
        # jika operasi
        elif ord(c) >= 60 and ord(c) <= 62:
            state = 2
        else:
            state = 20 # dead state

    return state

def stateDuaOperasional(c):
    if ord(c) == 61:
        state = 17
    else:
        startStateDua(c)
    return state

def stateTigaOperasional(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        state = 4
    else:
        state = 20
    return state

def stateEmpatOperasional(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        state = 6
    elif ord(c) == 46:
        state = 5
    elif ord(c) == 37 or ord(c) == 42 or ord(c) == 43 or ord(c) == 45 or ord(c) == 47:
        state = 8
    elif ord(c) >= 60 and ord(c) <= 62:
        state = 8
    else:
        state = 20
    return state

def stateLimaOperasional(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        state = 6
    else:
        state = 20
    return state

def stateEnamOperasional(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        state = 6
    elif ord(c) == 37 or ord(c) == 42 or ord(c) == 43 or ord(c) == 45 or ord(c) == 47:
        state = 8
    elif ord(c) >= 60 and ord(c) <= 62:
        state = 8
    else:
        state = 20
    return state

def stateDelapanOperasional(c):
    if ord(c) == 61:
        state = 17
    else:
        state = startStateDua(c)
    return state

def startStateDua(c):
    if ord(c) == 95:
        state = 9
    elif ord(c) == 36:
        state = 9
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 9
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 9
    else: 
        # jika angka
        if ord(c) >= 48 and ord(c) <= 57:
            state = 9
        elif ord(c) == 46:
            state = 10
        else:
            state = 20 # dead state
        
    return state

def stateSepuluhOperasional(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 11
    elif ord(c) == 46:
        state = 12
    else:
        state = 20 # dead state

    return state

def stateSebelasOperasional(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 13
    elif ord(c) == 46:
        state = 12
    else:
        state = 20 # dead state

    return state

def stateDuabelasOperasional(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 9
    else:
        state = 20 # dead state

    return state

def stateTigabelasOperasional(c):
    if ord(c) >= 48 and ord(c) <= 57:
        state = 13
    else:
        state = 20 # dead state

    return state

def stateEmpatbelasOperasional(c):
    if ord(c) == 61:
        state = 17
    else:
        state = startStateDua(c)
    return state

def stateSembilanOperasional(c):
    if ord(c) == 95:
        state = 9
    elif ord(c) == 36:
        state = 9
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 9
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 9
    elif ord(c) == 37 or ord(c) == 42 or ord(c) == 43 or ord(c) == 45 or ord(c) == 47:
        state = 14
    elif ord(c) >= 60 and ord(c) <= 62:
        state = 14
    elif ord(c) >= 48 and ord(c) <= 57:
        state = 9
    else:
        state = 20 # dead state

    return state

def isOperasiValid(s):
    s.replace(" ", "")
    sum = s.count("+=") + s.count("-=") + s.count("/=") + s.count("*=") + s.count("==") + s.count("<=") + s.count(">=") + s.count("<") + s.count(">")
    if sum > 1:
        return False
    else:
        state = 0
        kurungbuka = False
        for i in s:
            if i == " ":
                continue
            elif s.count("(") != s.count(")"):
                return False
            elif i == "(":
                kurungbuka = True
                if ")" not in s:
                    return False
                else:
                    continue
            elif i == ")":
                if not kurungbuka:
                    return False
                else:
                    kurungbuka = False
                    continue
            else:
                if state == 0:
                    state = startOperasional(i)
                elif state == 1:
                    state = stateSatuOperasional(i)
                # waktu state == 2
                elif state == 2:
                    state = stateDuaOperasional(i)
                elif state == 3:
                    state = stateTigaOperasional(i)
                elif state == 4:
                    state = stateEmpatOperasional(i)
                elif state == 5:
                    state = stateLimaOperasional(i)
                elif state == 6:
                    state = stateEnamOperasional(i)
                elif state == 8:
                    state = stateDelapanOperasional(i)
                elif state == 9:
                    state = stateSembilanOperasional(i)
                elif state == 10:
                    state = stateSepuluhOperasional(i)
                elif state == 11:
                    state = stateSebelasOperasional(i)
                elif state == 12:
                    state = stateDuabelasOperasional(i)
                elif state == 13:
                    state = stateTigabelasOperasional(i)
                elif state == 14:
                    state = stateEmpatbelasOperasional(i)
                elif state == 17:
                    state = startStateDua(i)
        if state == 9:
            return True
        else:
            return False