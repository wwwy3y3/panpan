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
		return repr((self.key, self.items, self.coef))

class Machine(object):
	"""the machine"""
	def __init__(self, capacity):
		self.times= 0
		self.day= 0 # start from day0
		self.orders= []
		self.leftOrders= [] # order not finish
		self.capacity= capacity
		self.capacityLeft= capacity

	def take(self, item, order):
		if self.capacityLeft <= 0:
			raise error("capacity over")

		# item= {a: 2}
		item["key"]= order.key
		
		# add item in orders
		# if not init a list yet, init one
		if len(self.orders) <= self.day:
			self.orders.append([])

		# if over capacity
		for key,val in item.iteritems():
			if self.capacityLeft - val < 0:
				item[key] -= self.capacity
				self.leftOrders.append(item) # push to tomorrow's work

		# append
		self.orders[self.day].append(item)

		# add order time in machine
		# in order to check how many orders it done
		for val in item.values():
			self.times += val
			order.times -= val # order times need to be cut


	def shut(self):
		self.day += 1

	def start(self):
		self.times= 0
		self.capacityLeft= self.capacity
		# get job done yesterday
		if len(self.leftOrders) > 0:
			self.take(self.leftOrders.pop())

	def __repr__(self):
		string= 'machine orders\n'
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