'''
Concept:
A class should have only one reason to change, meaning it should have only one 
job or responsibility.

Real world situation: 
Chef needs to only cook, not do the ordering, billing, etc.

In Practice: 
A class do only one job. e.g. If a class do processing, it should do only 
porcessing, not handle data storage, logging, error handling etc.

Example: 
If we have a class to process multiple jobs, then it should be split for 
each job.
'''


'''
CostProcessing calss violates the single responsibility principle becuase the 
class do both processing and saving the cost.
'''
class CostProcessing:
    def __init__(self, cost) -> None:
        self.cost = cost

    def process_cost(self):
        print(f'Processing cost: {self.cost}')

    def save_to_database(self):
        print(f'Saving cost to database: {self.cost}')

'''
Fix the violation by creating a separate class for cost processing.
'''

class CostProcessor:
    def __init__(self, cost) -> None:
        self.cost = cost

    def process_cost(self):
        print(f'Processing cost: {self.cost}')


class CostStorage:
    def __init__(self, cost) -> None:
        self.cost = cost

    def save_to_database(self):
        print(f'Saving cost to database: {self.cost}')