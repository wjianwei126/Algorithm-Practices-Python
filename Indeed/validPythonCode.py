# Given a list of strings. Each string represents a line of python code
# return the line number of first invalid line. If no invalid line, return -1
# rules for validation:
# 1. No indentation in the first line
# 2. There must be more indentations in the next line of control statements(if, else, for, etc)
# 3. If a line is not a control statement, it should have the same indentation as the line above or any control statement above.

def isValidPython(codes):
    if not codes: return -1
    i = 0
    while i < len(codes) and isWhiteSpace(codes[i]):
        i += 1
    if i == len(codes):
        return -1

    if getIndentation(codes[i]) != 0:
        return i+1
    controlFlag = isControlStatement(codes[0])
    stack = [0]
    for i in range(1, len(codes)):
        if isWhiteSpace(codes[i]):
            continue

        indentation = getIndentation(codes[i])

        if controlFlag:
            if indentation <= stack[-1]:
                return i+1
            else:
                stack.append(indentation)
        else:
            if indentation > stack[-1]:
                return i+1
            else:
                while stack and stack[-1] != indentation:
                    stack.pop()
                if not stack:
                    return i+1
        controlFlag = isControlStatement(codes[i])
    return -1

def isWhiteSpace(line):
    payload = line.strip()
    return payload == ''


def getIndentation(line):
    i = 0
    for ch in line:
        if ch != ' ':
            break
        i += 1
    return i

def isControlStatement(line):
    controlWords = set(['if', 'else:', 'while', 'for', 'def', 'class'])
    words = line.strip().split(' ')
    for word in words:
        if word in controlWords:
            return True
    return False

codes = ['for i in range(1, len(codes)):',
         '  if isWhiteSpace(codes[i]):',
         '      continue',
         '',
         '  indentation = getIndentation(codes[i])',
         '  if controlFlag:',
         '      if indentation <= stack[-1]:',
         '          return i+1',
         '      else:',
         '          stack.append(indentation)',
         '  else:',
         '      if indentation > stack[-1]:',
         '          return i+1',
         '      else:',
         '          while stack and stack[-1] != indentation:',
         '              stack.pop()',
         '          if not stack:',
         '              return i+1',
         '  controlFlag = isControlStatement(codes[i])]']
print isValidPython(codes)
