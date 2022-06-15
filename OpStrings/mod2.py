def meanString(str1, str2):
    listOfStrings = []
    listOfStrings.append(len(str1))
    listOfStrings.append(len(str2))
    average = sum(listOfStrings) / len(listOfStrings)
    return average