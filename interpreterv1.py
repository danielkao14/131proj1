from logging.config import _RootLoggerConfiguration
from intbase import InterpreterBase, Enum
import re

class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, input=None, trace_output=False):
        super().__init__(console_output, input)   # call InterpreterBase’s constructor
        self.variable_dict = {}
        self.func_dict = {}
        self.terminated = None
        self.ip = 0
        self.program_statements = [][]
        self.line_indents = []
    
    def tokenize_input(self, program):
        line_indents = [0] * len(program)
        for index, line in enumerate(program): #store number of left indents in each line
            counter = 0
            i = 0
            while line[i] == " ":
                counter += 1
                i += 1
            if(line[i] == "#"): #'remove' full comment lines in code
                line_indents[index] = -1
                continue
            line_indents[index] = counter
        self.line_indents = line_indents
    
        #tokenize the inputs
        #first remove the comments
        program_tokens = []*len(program)
        for line in enumerate(program):
           program_tokens.append(line.split())
        return(program_tokens)

    def record_func_line(self, program_name, ip):
        self.func_dict[program_name] = ip + 1
    
    def run(self, program):
        self.program_statements = self.tokenize_inpt(program)
        self.terminated = False
        while(not self.terminated):
            for index, token in enumerate(self.program_statements[self.ip]):
                if(token == super().FUNC_DEF): 
                    self.record_func_line(self.program_statements[self.ip][index+1], self.ip)
                    self.ip += 1
                    continue
                if(token == super().ASSIGN_DEF):
                    self.variable_dict[token] = self.program_statements[self.ip][index+1]


    