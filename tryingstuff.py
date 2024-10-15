from dataclasses import dataclass
#This is meaningless and shouldn't be marked, but it was just for me to remind myself how to use dataclasses

@dataclass 
class Penguin:
    name: str
    weight: float
    colour: str
    
    def set_colour(self,newcolour):
        self.colour = newcolour
        return Penguin(self.name,self.weight,self.colour)

    def __repr__(self):
        return f'{self.name} is a {self.colour} penguin weighing {self.weight} kg'

    

p = Penguin('Penny', 10, 'black')

p.set_colour('blue')

print(p)