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
		self.orders= []
		self.capacity= capacity

	def take(self, item, key):
		# item= {a: 2}
		item["key"]= key
		self.orders.append(item)
		for val in item.values():
			self.times += val

	def __repr__(self):
		return repr(self.orders)