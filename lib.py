import copy

class Order(object):
	"""the order"""
	def __init__(self, **arg):
		self.items= []
		self.times= 0
		for key, val in arg.items():
			if key == "deadline": # deadline, not items
				self.deadline= val
			elif key == "key":
				self.key= val
			else:
				order= {}
				order[key]= val
				self.items.append(order)
				# add up sum time
				self.times += val
		self.coef= self.times/self.deadline # larger, need to be done earlier

	def __repr__(self):
		return repr((self.key, self.items, self.times/self.deadline))

class Machine(object):
	"""the machine"""
	def __init__(self, capacity,id):
		self.id= id
		self.times= 0
		self.day= 0 # start from day0
		self.orders= []
		self.leftOrders= [] # order not finish
		self.capacity= capacity
		self.capacityLeft= capacity

	def take(self, item, order):
		if self.capacityLeft <= 0:
			raise error("capacity over")

		#print 'machine {0} take {1} in order{2}, origin capacity {3}'.format(self.id,item,order.key,self.capacityLeft)
		# item= {a: 2}
		item["key"]= order.key
		
		# add item in orders
		# if not init a list yet, init one
		if len(self.orders) <= self.day:
			self.orders.append([])

		# if over capacity
		for key,val in item.iteritems():
			if self.capacityLeft - val < 0 and not key == 'key':
				leftItem= copy.deepcopy(item)
				item[key] = self.capacityLeft
				leftItem[key] -= self.capacityLeft
				self.leftOrders.append((leftItem, order)) # push to tomorrow's work
				#print 'over capacity, so split item to {0}, {1}'.format(item,leftItem)

		# append
		self.orders[self.day].append(item)

		# add order time in machine
		# in order to check how many orders it done
		for key,val in item.iteritems():
			if not key == 'key':
				self.times += val
				order.times -= val # order times need to be cut
				self.capacityLeft -= val
		#print 'machine {0}, capacity left {1}\n'.format(self.id,self.capacityLeft)

	def shut(self):
		self.day += 1

	def start(self):
		self.times= 0
		self.capacityLeft= self.capacity
		# get job done yesterday
		if len(self.leftOrders) > 0:
			order= self.leftOrders.pop()
			self.take(order[0], order[1])

	def __repr__(self):
		string= 'machine {0}\n'.format(self.id)
		i=0
		for dayOrders in self.orders:
			i +=1
			string += 'day'+ str(i) + '\n'
			for order in dayOrders:
				orderStr= 'order key: {0}, item: {1}, time: {2}\n'
				for key,val in order.iteritems():
					if key == 'key':
						orderKey= str(val)
					else:
						orderItem= key
						orderVal= str(val)
				string += orderStr.format(orderKey, orderItem, orderVal)
		return string

def orderLeft(orders):
	for order in orders:
		if len(order.items) > 0:
			return True
	return False

def capacityLeft(machines):
	for machine in machines:
		if machine.capacityLeft > 0:
			return True
	return False