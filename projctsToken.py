KeyWords = ['cout', 'cin', 'using', 'namespace', 'int', 'long', 'double','bool',
            'char', 'string', 'float', 'main', 'include', 'std', 'iostream', 'if', 'for']
Operaters = ['+', '-', '*', '^', '/', '=', '<', '>', '>>', '<<']
symbols = ['#', '(', ')', ';', '{', '}', '[', ']', ',', '%']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('cpp.cpp', 'r') as FileCpp:
    word = FileCpp.read()
Result = ""
tempWord = ""
i = 0
while i < len(word):
    if word[i] != "\n" and word[i] != " ":
        if word[i] in symbols:
            Result += word[i] + "           -->    Symbol\n"
            i += 1
        elif word[i:i + 2] in Operaters:
            Result += word[i:i + 2] + "           -->    Operator\n"
            i += 2
        elif word[i] in Operaters:
            Result += word[i] + "           -->    Operator\n"
            i += 1
        elif word[i] == '"':
            tempWord += word[i]
            i += 1
            while word[i] != '"':
                tempWord += word[i]
                i += 1
            tempWord += word[i]
            Result += tempWord + "           -->    Identifier\n"
            tempWord = ""
            i += 1
        else:
            while word[i] not in symbols and word[i]not in Operaters and word[i] != " ":
                tempWord += word[i]
                i += 1
            if tempWord in KeyWords:
                Result += tempWord + '           -->    Keyword\n'
            elif tempWord[0] in number:
                Result += tempWord+'           -->    Number\n'
            else:
                Result += tempWord + '           -->    Identifier\n'
            tempWord = ""
    else:
        i += 1
with open('result.txt', 'w') as resultfile:
    resultfile.write(Result)
