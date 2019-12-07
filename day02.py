import copy
input_data = [int(z) for z in open('input.txt').read().split(',')]
def modify(opcode, x, y, pos):
    if opcode == 1:
        data[pos] = data[x]+data[y]
        return True
    if opcode == 2:
        data[pos] = data[x]*data[y]
        return True
    if opcode == 99:
        return False
i = 0
for x in range(99):
    for y in range(99):
        data = copy.copy(input_data)
        data[1] = x
        data[2] = y
        i = 0
        while True:
            opcode = data[i]
            in1 = data[i+1]
            in2 = data[i+2]
            pos = data[i+3]
            if not modify(opcode, in1, in2, pos):
                if data[0] == 19690720:
                    print 100*x+y
                else:
                    break
            i += 4
            if i+3>=len(data):
                break

