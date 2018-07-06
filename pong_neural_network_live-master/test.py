import random

import matplotlib .pyplot as plt

IntegerMin = 1

IntegerMax = 100000

OriginalRandomInteger = random.randint(IntegerMin, IntegerMax)

MachineGuessing = random.randint(IntegerMin, IntegerMax)

MachineGuessingShadow = MachineGuessing

Counter = 0

print(OriginalRandomInteger,MachineGuessing)

print (Counter + 1)

while MachineGuessing != OriginalRandomInteger:

    if MachineGuessing == OriginalRandomInteger:

        exit()

        print (OriginalRandomInteger,MachineGuessing)

    elif MachineGuessing > OriginalRandomInteger:

        MachineGuessing = random.randint(OriginalRandomInteger, MachineGuessingShadow-1)

        MachineGuessingShadow = MachineGuessing

        Counter = Counter+1

        print (OriginalRandomInteger,MachineGuessing)

        print (Counter+1)

    else:

        MachineGuessing = random.randint(MachineGuessingShadow+1, OriginalRandomInteger)

        Counter = Counter+1

        MachineGuessingShadow = MachineGuessing

        print (OriginalRandomInteger,MachineGuessing)

        print (Counter+1)