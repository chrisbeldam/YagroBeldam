import random
# Create Workers and their partners


class Workers:
    """ Class which controls the 3 pairs of workers """

    def __init__(self, worker_name, required_blocks, construction_time, worker_partner=None):
        self.worker_name = worker_name
        self.inventory = []  # Empty inventory for workers, will be populated later
        self.required_blocks = required_blocks
        self.construction_time = construction_time
        self.worker_partner = worker_partner  # opposite worker
        self.timeTick = construction_time  # works like a running clock

    # Main function to check pieces on belt and then assemble P Components
    def start_belt(self, position):
        # if inventory blocks is a suset of required blocks run the following
        if set(self.inventory).issubset(self.required_blocks):
            if self.timeTick <= 0:
                print(f'{self.worker_name} has completed a block')
                if position.value == '':
                    self.inventory = []
                    self.timeTick = self.construction_time
                    print(f'{self.worker_name} is placing P on conveyor')
                    position.value = 'P'
                else:
                    if self.worker_partner:
                        # allows the partner to check and pickup a block
                        self.worker_partner.start_belt(position)
            else:
                self.timeTick -= 1
                if self.worker_partner:
                    self.worker_partner.start_belt(position)
        else:
            if position.value in self.required_blocks and position.value not in self.inventory:
                # add component into inventory
                self.inventory.append(position.value)
                position.value = ''
            else:
                if self.worker_partner:
                    self.worker_partner.start_belt(position)


class Components:
    """ Class which generates the 3 blocks of A, B, "" at even chance """

    def __init__(self, blocks):
        self.blocks = blocks

    # Generate Items/Blocks
    def generate_new_blocks(self):
        # Returns a new block either A, B or ""
        return random.choice(self.blocks)

# Position on conveyorbelt (had to look up how to do this from an example)


class ConveyorPosition:
    """ Position on conveyorbelt, had to look up how to do the positioning """

    def __init__(self, value):
        self.value = value  # Value which represents conveyorbelt position


class Statistics:
    """ Class which keeps track of the statistics of which items got picked """

    def __init__(self):
        # Dictionary to track how many values of each occur and set beginning values at 0
        self.total_values = {'A': 0, 'B': 0, "P": 0}

    def tracker(self, tracked):
        if len(tracked.value) > 0:
            key = tracked.value[0]
            # adds one to data value for each block
            self.total_values[key] += 1

    def tracking_report(self):
        total_unpicked = (self.total_values['A'] + self.total_values['B'])
        print(f'Total A Blocks Generated: {self.total_values["A"]}')
        print(f'Total B Blocks Generated: {self.total_values["B"]}')
        print(f'Total Products Made: {self.total_values["P"]}')
        print(f'Total Unpicked Blocks: {total_unpicked}')  # Total unpicked

# Create Conveyor Belt


class ConveyorBelt:
    """ Class which controls the conveyorbelt and its functionality """
    # User determined length
    length = input(
        f'Please enter the length of the conveyorbelt (bigger than 0): ')
    # Fixing if people enter alphas instead of numbers for conveyorbelt length for some strange reason
    if length.isalpha():
        length = input(
            f'Please enter the length of the conveyorbelt (bigger than 0): ')
        length = int(length)
    else:
        length = int(length)
    while length <= 0:
        length = input(
            f'Please enter the length of the conveyorbelt (bigger than 0): ')
        length = int(length)
    stop_time = input(
        f'How many seconds would you like the workers to take to build P?: ')
    if stop_time.isalpha():
        stop_time = input(
            f'Please enter the time it takes workers to build (bigger than 0): ')
        stop_time = int(stop_time)
    else:
        stop_time = int(stop_time)
    while stop_time < 1:
        stop_time = input(
            f'Please enter the time it takes workers to build must be at least 1: ')
        stop_time = int(stop_time)

    def __init__(self, components, statistics, worker_positions):
        self.worker_positions = [ConveyorPosition('')] * worker_positions
        self.statistics = statistics
        self.components = components
        self.workers = ConveyorBelt.create_workers(self.worker_positions)

    def create_workers(worker_positions, stop_time=stop_time):
        workers = {}  # Create empty worker object
        # for each position create pairs of workers
        for w in range(len(worker_positions)):
            workers[w] = Workers(f'Worker {w}',
                                 ['A', 'B'],
                                 stop_time,
                                 Workers(f'Partner {w}',
                                         ['A', 'B'],
                                         stop_time))
        return workers

    def printbelt(self, belt):
        print(f'-----')
        print(belt, ' | '.join([pos.value for pos in self.worker_positions]))
        print(f'-----')

    def start_belt(self, length=length):
        # for each part of the length of the conveyor belt
        for part in range(length):
            # each position creates a new block and moves the position on
            self.worker_positions = [
                ConveyorPosition(self.components.generate_new_blocks())] + self.worker_positions[:-1]
            self.printbelt(f'Positon {part}:')
            # list each index, get value and loop
            for index, pos in enumerate(self.worker_positions):
                # for each position a worker tries to grab/build an object
                self.workers[index].start_belt(pos)
            self.statistics.tracker(self.worker_positions[-1])
        self.statistics.tracking_report()

    # Build conveyor belt process - move over blocks by 1 each time for 100 seconds


def runtime():
    """ run whole file """
    """ Restricting user input of worker pairs. Doesn't make sense for more workers than length of belt """
    worker_pairs = input(f'How Many Pairs of workers?: ')
    if worker_pairs.isalpha():
        worker_pairs = input(
            f'You need at least 1 pair of workers, please enter a number greater than 0: ')
        worker_pairs = int(worker_pairs)
    else:
        worker_pairs = int(worker_pairs)
        while int(ConveyorBelt.length) < int(worker_pairs):
            worker_pairs = int(
                input(f'There must not be more worker pairs than conveyor belt positions: '))
    while worker_pairs <= 0:
        worker_pairs = int(input(
            f'You need at least 1 pair of workers, please enter a number greater than 0: '))
    ConveyorBelt(Components(['A', 'B', '']),  # Call conveyorbelt class, call components class and add blocks
                 Statistics(),  # Call statitics class,
                 worker_positions=worker_pairs).start_belt()  # set "worker positions" equal to number of pairs.
    # Then start main conveyorbelt method


runtime()
