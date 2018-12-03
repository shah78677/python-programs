class Stack():
    def __init__(self):
        self.a = []
        self.top = -1

    def push(self, ele):
        self.a.append(ele)
        self.top += 1

    def pop(self):
        self.a.pop()
        self.top -= 1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
s = Stack()
exp = input('Please enter the paranthesis:')
for i in exp:
    if i == '(':
        s.push(1)
    elif i == ')':
        if s.isEmpty():
            s.push(1)
        else:
            s.pop()
            isBalanced = True
    else:
        if s.isEmpty():
            isBalanced = True
        else:
            isBalanced = False

if s.isEmpty():
    print('There are equal number of paranthesis')
else:
    print('There are unequal number of paranthesis')
