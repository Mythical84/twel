import copy

class Memory:
    def __init__(self):
        self.memory = {}
        self.temp_memory = []

    def get_value(self, name, filename):
        if len(self.temp_memory) > 0 and name in self.temp_memory[len(self.temp_memory)-1]:
            return self.temp_memory[len(self.temp_memory)-1][name]
        elif name in global_memory.keys():
            return global_memory[name]
        return self.memory[filename][name]
    
    def remove_value(self, name, filename):
        del self.memory[filename][name]

    def value_in(self, value, filename):
        return value in self.memory[filename]
    
    def add_value(self, name, values, filename):
        if len(self.temp_memory) > 0 and name in self.temp_memory[len(self.temp_memory)-1]: 
            self.temp_memory[len(self.temp_memory)-1][name] = values
        self.memory[filename][name] = values

    def add_temp_memory(self, name, values, filename):
        args = self.memory[filename][name]['args']
        self.temp_memory.append({})
        for i in range(0, len(args)):
            self.temp_memory[-1][args[i]] = values[i]

    def close_temp_memory(self):
        self.temp_memory.pop()

    def register_file(self, filename):
        if not filename == 'stdlib':
            self.memory[filename] = copy.copy(self.memory['stdlib'])
        else:
            self.memory[filename] = {}

global_memory = {}
memory = Memory()