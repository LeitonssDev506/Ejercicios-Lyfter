

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"}
]


groups = {}

for employee in employees:
    department = employee.get('department')
    name = employee.get('name')

    if department not in groups:
        groups[department] = [name]
    else:
        groups[department].append(name)


print(groups)