class Employee:
    def __init__(self, name, itemsSold = 0, managerName = None):
        self.name = name
        self.itemsSold = itemsSold
        self.managerName = managerName
        self.manager = None
        self.subordinates = []

class EmployeeHeirachy:
    def __init__(self, head):
        self.root = head

    def addEmployee(self, employee):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.name == employee.managerName:
                node.subordinates.append(employee)
                employee.manager = node
                break
            for person in node.subordinates:
                queue.append(person)
        node = employee
        increasedItem = employee.itemsSold
        node = node.manager
        while node:
            node.itemsSold += increasedItem
            node = node.manager

    def printHeirachy(self):
        stack = [(self.root, 0)]
        while stack:
            node, indentation = stack.pop()
            print indentation * ' ' + node.name + ' ' + str(node.itemsSold)
            for person in node.subordinates:
                stack.append((person, indentation+1))

employeeList = ['Ferris,Eve,1', 'Alice,,5', 'Bob,Alice,3', 'Carol,Bob,2', \
    'David,Bob,3', 'Eve,Alice,2']
dic = {}
for line in employeeList:
    lineTuple = line.split(',')
    if lineTuple[1] == '':
        CEO = lineTuple[0]
        CEOSold = int(lineTuple[2])
        if CEO not in dic:
            dic[CEO] = []
        # employeeMap = EmployeeHeirachy(Employee(lineTuple[0], int(lineTuple[2])))
    else:
        if lineTuple[1] not in dic:
            dic[lineTuple[1]] = [(lineTuple[0], lineTuple[1], int(lineTuple[2]))]
        else:
            dic[lineTuple[1]].append((lineTuple[0], lineTuple[1], int(lineTuple[2])))
        # employeeMap.addEmployee(Employee(lineTuple[0], int(lineTuple[2]), lineTuple[1]))

employeeMap = EmployeeHeirachy(Employee(CEO, CEOSold))
queue = dic[CEO]
while queue:
    person, manager, sold = queue.pop(0)
    employeeMap.addEmployee(Employee(person, sold, manager))
    if person in dic:
        for subordinate in dic[person]:
            queue.append(subordinate)
employeeMap.printHeirachy()
