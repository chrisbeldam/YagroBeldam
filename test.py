import random

#Create Workers
#Create Conveyor Belt
#Generate Items/Blocks
#Build conveyor belt process - move over blocks by 1 each time for 100 seconds
#Worker functionality - pickup and build blocks

class Workers:
    """ Class which controls the 3 pairs of workers """
    def __init__(self, required_blocks, time):
        self.inventory = [] #Empty inventory for workers, will be populated later
        self.required_blocks = required_blocks 
        self.construction_time = construction_time 
    def start(self, stage): #Main function to check pieces on belt and then assemble P
        pass

class Components:
    """ Class which generates the 3 blocks of A, B, "" at even chance """
    def __init__(self, blocks):
        self.blocks = blocks # A, B, ""
    
    def new_blocks(self):
        return random.choice(self.blocks) # Returns a new block either A, B or ""


class ConveyorBelt:
    """ Class which controls the conveyorbelt and its functionality """
    def __init__(self):

class Statistics:
    """ Class which keeps track of the statistics of which items got picked """
    def __init__(self):
        self.totals = {'A':0, 'B':0, "P":0} #Dictionary to track how many values of each occur