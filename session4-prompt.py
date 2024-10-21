import sys

class animal:
    def __init__(self, name, armlength, leglength, numeyes, tail, fur):
        self.name = name
        self.armlength = armlength
        self.leglength = leglength
        self.numeyes = numeyes
        self.tail = tail
        self.fur = fur
    
    def animal_info(self):
        print(f"The animal is a {self.name}.")
        print(f"Arm length: {self.armlength}ft")
        print(f'Leg Length: {self.leglength}ft')
        print(f'Number of Eyes: {self.numeyes}')
        print(f'Tail: {self.tail}')
        print(f'Fur: {self.fur}')

bear = animal("Polar Bear", 3.8, 3.8, 2, True, True)

bear.animal_info()