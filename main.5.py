x = float(input('x->'))
y = float(input('y->'))
z = float(input('z->'))
print('#>------------<Menu>------------<#')
print(f'|   + : Show sum for {x} and {y}   |')
print(f'|   - : Show dif for {x} and {y}   |')
print(f'|   * : Show mul for {x} and {y}   |')
print(f'|   / : Show dif for {x} and {y}   |')
print(f'| avg : Show avg for {x} and {y}   |')
print(f'| min3 : between {x}, {y}, {z}      |')
print(f'| max3 : between {x}, {y}, {z}      |')
print(f'| avg3 : between {x}, {y}, {z}      |')
print('#>------------------------------<#')
action = input('action->')
if action == '+':
    print(f'{x} + {y} = {x + y}')
elif action == '-':
    print(f'{x} - {y} = {x - y}')
elif action == '*':
    print(f'{x} * {y} = {x * y}')
elif action == '/':
    if x == 0 or y == 0:
        print(f"Error! {x} or {x} is zero!")
    else:
        print(f'{x} / {y} = {x / y}')
elif action == 'avg':
    print(f'Avg = {(x+y)/2}')
elif action == 'avg3':
    print(f'Avg = {(x+y+z)/3}')
elif action == 'max3':
    if x >= y and x >= z:
        print(f'Max is {x}')
    elif y >= x and y >= z:
        print(f'Max is {y}')
    elif z >= x and z >= y:
        print(f'Max is {z}')
    else:
        print(f'All values is equil!')
elif action == 'min3':
    if x <= y and x <= z:
        print(f'Min is {x}')
    elif y <= x and y <= z:
        print(f'Min is {y}')
    elif z <= x and z <= y:
        print(f'Min is {z}')
    else:
        print(f'All values is equil!')
else:
    print('Command not found!')