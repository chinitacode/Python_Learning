'''
Variables
Next let's add variables to our interpreter.
Variables require an instruction for storing the value of a variable, STORE_NAME;
an instruction for retrieving it, LOAD_NAME;
and a mapping from variable names to values.

For now, we'll ignore namespaces and scoping,
so we can store the variable mapping on the interpreter object itself.

Finally, we'll have to make sure that what_to_execute has a list of the variable names,
in addition to its list of constants.

>>> def s():
...     a = 1
...     b = 2
...     print(a + b)
# a friendly compiler transforms `s` into:
    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names":   ["a", "b"] }

Our new implementation is below.
To keep track of what names are bound to what values,
we'll add an environment dictionary to the __init__ method.
We'll also add STORE_NAME and LOAD_NAME.
These methods first look up the variable name in question and then
use the dictionary to store or retrieve its value.

The arguments to an instruction can now mean two different things:
They can either be an index into the "numbers" list,
or they can be an index into the "names" list.
The interpreter knows which it should be by checking what instruction it's executing.
We'll break out this logic—and the mapping of instructions to what their arguments mean—into a separate method.
'''
class Interpreter():
    def __init__(self):
        self.stack = []
        self.environment = {}

    # store the name,value pair in the environment dictionary
    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val

    # search in environment the value according to the name and append the value into the stack
    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)

    def LOAD_VALUE(self,number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def parse_argument(self, instruction, argument, what_to_execute):
        """ Understand what the argument to each instruction means."""
        numbers = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']

        if instruction in numbers:
            argument = what_to_execute['numbers'][argument]

        elif instruction in names:
            argument = what_to_execute['names'][argument]
        return argument


    def run_code(self, what_to_execute):
        instructions = what_to_execute['instructions']

        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)

            if instruction == 'LOAD_VALUE':
                self.LOAD_VALUE(argument)
            elif instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            elif instruction == 'PRINT_ANSWER':
                self.PRINT_ANSWER()
            elif instruction == 'STORE_NAME':
                self.STORE_NAME(argument)
            elif instruction == 'LOAD_NAME':
                    self.LOAD_NAME(argument)

    '''
    [***Important Note***]
    Even with just five instructions, the run_code method is starting to get tedious.
    If we kept this structure, we'd need one branch of the if statement for each instruction.
    Here, we can make use of Python's dynamic method lookup.
    We'll always define a method called FOO to execute the instruction called FOO,
    so we can use Python's getattr function to look up the method on the fly
    instead of using the big if statement.
    The run_code method then looks like this:
    '''
    def execute(self, what_to_execute):
        instructions = what_to_execute['instructions']

        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)
            bytecode_method = getattr(self, instruction)
            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument)


if __name__ == '__main__':
    # implement a = 1, b = 2 and print a+b:
    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names":   ["a", "b"] }
    interpreter = Interpreter()
    interpreter.execute(what_to_execute)
