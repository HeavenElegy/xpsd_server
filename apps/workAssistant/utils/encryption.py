


skipIndex = [3, 6, 9]

def resolvePassword(passwordMD5):
    new = []
    for i in range(0, len(passwordMD5)):
        if i not in skipIndex:
            new.append(passwordMD5[i])
    return ''.join(new)