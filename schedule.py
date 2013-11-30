# input: 
# read from json
import json
import os
import copy
from lib import *
from pprint import pprint

json_data=open('text.json')
data = json.load(json_data)
#pprint(data)
json_data.close()

# init what i need
machines= [ Machine(item["capacity"],item["id"]) for item in data["machines"] ]
_machines= copy.deepcopy(machines)
times= data["time"]

# overide orders, units to time
#ori_orders= []
ori_orders= []
for item in data["orders"]:
	order= {}
	for key, val in item.items():
		if key != "deadline" and key != "key":
			order[key]= val*times[key]
		else:
			order[key]= val
	ori_orders.append(order)


# orders
orders= [ Order(**order) for order in ori_orders ]
_orders= copy.deepcopy(orders)
# sort by times/deadline
# orders= sorted(orders, key=lambda order: order.coef, reverse=True)
# pprint(orders)
# schedule
# while(orders not all done, orders legnth > 0)
#	sort orders remains
#	pop the items in orders
#	min machine take it
#	if capacity is over
#		leave it next day
#	machine day++, cut the times pass in orders
i=0
iters=0
iterFail= False
done= False
priority= {order.key: 1 for order in orders}
while orderLeft(orders):
	if iterFail:
		iters +=1
		print 'iter on',iters
		orders= copy.deepcopy(_orders)
		machines= copy.deepcopy(_machines)
		for key,val in priority.iteritems():
			orders[orders.index(key)].priority= val
		iterFail= False
		i=0
	while orderLeft(orders):
		i +=1
		#print 'day',i
		#for order in orders:
		#	print 'order',order.key,' ',order.times/order.deadline*order.priority
		orders= sorted(orders, key=lambda order: order.times/order.deadline*order.priority, reverse= True)
		#for order in orders:
			#print 'order',order.key,' ',order.times/order.deadline*order.priority
		#print orders
		for machine in machines:
			machine.start()

		for order in orders:
			if not capacityLeft(machines):
				break
			j=0
			while j < len(order.items):
				if not capacityLeft(machines):
					break
				#print 'in order{0}'.format(order)
				minM= min(machines, key= lambda machine: machine.times)
				minM.take(order.items.pop(), order)
				#order.items.remove(item)

		# end of day

		for order in orders:
			if len(order.items) >0:
				order.deadline -= 1
				if order.deadline == 0:
					priority[order.key] *= 10
					print 'multi 20 on ',order.key
					iterFail= True

		if iterFail:
			break

		for machine in machines:
			machine.shut()

pprint(machines)
# check if okay
	
#os.system("pause")
#raw_input("Press enter to continue")

# output
# listA: [[1,3], [3,5], [5,7]]
# listB: [[1,3], [3,5], [5,7]]
# listC: [[1,3], [3,5], [5,7]]
