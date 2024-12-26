
class Connection():
    def __init__(self, input0, input1, operation, result):
        self.input0 = input0
        self.input1 = input1
        self.operation = operation
        self.result = result
    def __repr__(self):
        return f'{self.input0} {self.operation} {self.input1} -> {self.result}'
def parse_input(input):
    initial_values = {}
    connections = []
    IVs = True
    for x in input:
        if len(x.strip()) > 0:
            if IVs:
                xs = x.split(':')
                initial_values[xs[0]] = int(xs[1])
                #print(initial_values)
            else:
                #print(x)
                xs = x.split(' -> ')
                result = xs[1].strip()
                xs2 = xs[0].split(' ')
                input0 = xs2[0].strip()
                operation = xs2[1].strip()
                input1 = xs2[2].strip()
                connections.append(Connection(input0, input1, operation, result))
        else:
            #print('here')
            IVs = False
    return initial_values, connections

def part1(input):
    values, connections = parse_input(input)
    #print(values, connections)
    
    def f(i0, op, i1):
        if op == 'AND':
            return int(values[i0]) & int(values[i1])
        elif op == 'OR':
            return int(values[i0]) | int(values[i1])
        elif op == 'XOR':
            return int(values[i0]) ^ int(values[i1])
        else:
            return NotImplementedError('Operation not known')
    while len(connections) > 0:
        #print(len(connections))
        #if len(connections) < 25:
        #   raise Exception
        con = connections.pop(0)
        if con.input0 in values and con.input1 in values:
            values[con.result] = f(con.input0, con.operation, con.input1)
        else:
            #raise NotImplementedError
            # Input currently carries no value, put at end of queue:
            connections.append(con)
            #print(connections)
    z_only = {k:v for k,v in values.items() if k[0] == 'z'}
    i = 0
    zstr = ''
    while True:
        try:
            #print(f'z{i:02d}')
            #print(z_only[f'z{i:02d}'])
            zstr = str(z_only[f'z{i:02d}']) + zstr
            i += 1
        except KeyError:
            return int(zstr, base=2)
if __name__ == '__main__':
    actual_input = open('c:/temp/day24_input.txt')
    #print(parse_input(sample_input))
    print('Part 1 answer is',part1(actual_input))