import copy
from itertools import permutations

def incode_computer(data, phase_input):
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
            op_value = int(phase_input.pop(0))
            if first_parameter_mode == 0:
                data[data[pos+1]] = op_value
            if first_parameter_mode == 1:
                data[pos+1] = op_value
            pos += 2
        if opcode == 4:
            if first_parameter_mode == 0:
                return data[data[pos+1]]
            if first_parameter_mode == 1:
                return data[pos+1]
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

phase_setting = [1,0,4,3,2]

data = [int(z) for z in open('day05_input.txt').read().split(',')]

final_amplifier_output = []
for combination in permutations(phase_setting, len(phase_setting)):
    intial_amp_out = 0
    for val in combination:
        intial_amp_out = incode_computer(data, [val, intial_amp_out])
    final_amplifier_output.append(intial_amp_out)
print max(final_amplifier_output)
