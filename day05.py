import copy
data = [int(z) for z in open('input.txt').read().split(',')]
#data = [int(z) for z in '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'.split(',')]
#data = [int(z) for z in '3,3,1108,-1,8,3,4,3,99'.split(',')]
def modify(opcode, x, y, pos):
    if opcode == 1:
        data[pos] = data[x]+data[y]
        return True
    if opcode == 2:
        data[pos] = data[x]*data[y]
        return True
    if opcode == 99:
        return False
pos = 0
while pos < len(data):
#   print 'position', pos
    def resolve_mode(data, mode, val):
        if mode == 0:
            return int(data[val])
        if mode == 1:
            return int(val)
    opcode = str(data[pos])
#   print "type", pos, opcode
    opcode = ''.join(['0'*(5-len(opcode)), opcode])
    third_param_mode = int(opcode[0])
    second_parameter = int(opcode[1])
    first_parameter_mode = int(opcode[2])
    opcode = int(opcode[3:])
    if opcode == 1:
        # 'addition'
        op_value = \
            resolve_mode(data, first_parameter_mode, data[pos+1]) + resolve_mode(data, second_parameter, data[pos+2])
        if third_param_mode == 0:
            data[data[pos+3]] = op_value
        if third_param_mode == 1:
            data[pos+3] = op_value
        pos += 4
    if opcode == 2:
        # 'multiply'
        op_value = \
            resolve_mode(data, first_parameter_mode, data[pos+1]) * resolve_mode(data, second_parameter, data[pos+2])
        if third_param_mode == 0:
            data[data[pos+3]] = op_value
        if third_param_mode == 1:
            data[pos+3] = op_value
        pos += 4
    if opcode == 3:
        op_value = int(raw_input('input: '))
        if first_parameter_mode == 0:
            data[data[pos+1]] = op_value
        if first_parameter_mode == 1:
            data[pos+1] = op_value
        pos += 2
    if opcode == 4:
        if first_parameter_mode == 0:
            print 'output:', data[data[pos+1]]
        if first_parameter_mode == 1:
            print 'output:', data[pos+1]
        exit(data)
    if opcode == 5:
        # 'jump-if-true'
        if resolve_mode(data, first_parameter_mode, data[pos+1]) != 0:
            pos = resolve_mode(data, second_parameter, data[pos+2])
        else:
            pos +=3
    if opcode == 6:
        # 'jump-if-false'
        if resolve_mode(data, first_parameter_mode, data[pos+1]) == 0:
            pos = resolve_mode(data, second_parameter, data[pos+2])
        else:
            pos +=3

    if opcode == 7:
        # 'less than'
        if third_param_mode == 0:
            op_value = data[data[pos+3]]
        if third_param_mode == 1:
            op_value = data[pos+3]
        if resolve_mode(data, first_parameter_mode, data[pos+1]) < resolve_mode(data, second_parameter, data[pos+2]):
            data[data[pos+3]] = 1
        else:
            #data[op_value] = 0
            data[data[pos+3]] = 0
        pos += 4

    if opcode == 8:
        # 'equal to'
        if third_param_mode == 0:
            op_value = data[data[pos+3]]
        if third_param_mode == 1:
            op_value = data[pos+3]
        if resolve_mode(data, first_parameter_mode, data[pos+1]) == resolve_mode(data, second_parameter, data[pos+2]):
            data[data[pos+3]] = 1
        else:
            data[data[pos+3]] = 0
        pos += 4

    if opcode == 99:
#       print ','.join([str(x) for x in data])
        exit('Got 99, exiting.')
    if opcode not in [1, 2, 3, 4, 5, 6, 7, 8, 99]:
#       print ','.join([str(x) for x in data])
        exit('invalid opcode')
