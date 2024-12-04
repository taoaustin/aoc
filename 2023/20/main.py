import re
import math

class Gate:
    def __init__(self, name):
        self.name = name
        self.outputs = []

    def notify(self, signal):
        out_signals = []
        for gate in self.outputs:
            out_signals.append((gate, self.name, signal))
        return out_signals

    def add_input(self, gate):
        pass

    def add_output(self, gate):
        self.outputs.append(gate)

class FlipFlop(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.state = False

    def update(self, _, signal):
        if not signal:
            self.state = not self.state
            return self.notify(self.state)
        return []

class Conjunction(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.inputs = {}
    
    def update(self, source, signal):
        self.inputs[source] = signal
        if all(self.inputs.values()):
            return self.notify(False)
        else:
            return self.notify(True)

    def add_input(self, gate):
        if gate not in self.inputs:
            self.inputs[gate] = False

class Broadcaster(Gate):
    def __init__(self, name):
        super().__init__(name)


def parse_input():
    lines = [re.split(" -> ", line) for line in open("input.txt").read().splitlines()]
    all_gates = {}
    for line in lines:
        if line[0][0] == "%":
            all_gates[line[0][1::]] = FlipFlop(line[0][1::])
        elif line[0][0] == "&":
            all_gates[line[0][1::]] = Conjunction(line[0][1::])
        elif line[0] == "broadcaster":
            all_gates[line[0]] = Broadcaster(line[0])
    all_gates["rx"] = FlipFlop("rx")
    for line in lines:
        input_gate = line[0][1::] if line[0] != "broadcaster" else "broadcaster"
        output_gates = line[1].split(", ")
        for o_gate in output_gates:
            all_gates[o_gate].add_input(input_gate)
            all_gates[input_gate].add_output(all_gates[o_gate])
    return all_gates

def main():
    all_gates = parse_input()
    low_sig_count = 0
    high_sig_count = 0
    for _ in range(1000):
        q = []
        q += all_gates["broadcaster"].notify(False)
        while q:
            gate, source, signal = q.pop(0)
            if (signal): high_sig_count += 1
            else: low_sig_count += 1
            q += gate.update(source, signal)
        low_sig_count += 1 # for initial button press
    silver = low_sig_count * high_sig_count
    print(f"Part 1: {silver}")

    i = 1
    # didn't reset state, so was getting wrong answers which just-so-happens to be 1000 button presses off
    all_gates = parse_input()
    cycles = []
    while(True):
        q = []
        q += all_gates["broadcaster"].notify(False)
        while q:
            gate, source, signal = q.pop(0)
            q += gate.update(source, signal)
            if (gate.name == "nr" and signal):
                cycles.append(i)
        # input is constructed just so that the first 4 cycles are distinct, so this condition is sufficient
        if len(cycles) == 4:
            break
        i += 1
    gold = math.lcm(*cycles)
    print(f"Part 2: {gold}")
    

if __name__ == "__main__":
    main()
