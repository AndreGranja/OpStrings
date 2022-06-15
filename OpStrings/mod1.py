def maxLen(str1, str2):
    if len(str1) > len(str2):
        tam = len(str1)
    else:
        tam = len(str2)
    return tam

def minString(str1, str2):
    if len(str1) < len(str2):
        a = str1
    else:
        a = str2
    return a
