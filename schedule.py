# input: 
# orders
orders= [ 
{ 'a': 3, 'b': 2, deadline: 7 }, 
{ 'a': 5, 'b': 6, deadline: 8 }, 
{ 'a': 2, 'b': 2, deadline: 22 }
]

# resources: three parallel machines
machines= [
{capacity: 8},
{capacity: 8},
{capacity: 8}
]
# queue the orders

# schedule
# list per machine
# dispatcher
# algr:
# shorter accumelate time, will be dispatch job

# output
# listA: [[1,3], [3,5], [5,7]]
# listB: [[1,3], [3,5], [5,7]]
# listC: [[1,3], [3,5], [5,7]]