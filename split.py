EVERYONE_ELSE = "Everyone (else)"

# classes 
class Item:

	def __init__(self, name, price, claimers):
		self.name = name
		self.price = price
		self.claimers = claimers

class Splitter:


	def split(self):
		self.__get_input()
		self.__check_claims()
		self.__calculate_base()
		self.__split()
		self.__round_and_finish()

	def __get_input(self):		
		self.total       = float(input("Enter total bill amount: "))
		self.num_sharers = int(input("Enter number of sharers: "))		

	def __check_claims(self):
		"""enter items that people are paying for separately"""

		self.claimed_items = []
		self.claimed_total = 0

		claimable = input("Are there any items to be claimed separately? (y/n): ")
		print()
		
		while(claimable.lower() == "y"):

			i_name     = input("Item name: ")
			i_price    = float(input("Item price: "))
			i_claimers = input("Enter all claimers (separated by spaces): ").split(" ")
			confirm    = input("Save item? (y/n): ")
			item       = Item(i_name, i_price, i_claimers)

			if confirm.lower() != "n":
				self.claimed_items.append(item)
				self.claimed_total += item.price

			claimable = input("Add another item? (y/n): ")
			print()		

	def __calculate_base(self):
		"""calculate base amount that everyone has to pay"""

		self.base_total          = self.total - self.claimed_total
		self.base_total_per_head = self.base_total / self.num_sharers

	def __split(self):
		"""calculate everyone's total share"""

		self.split = {}
		
		for item in self.claimed_items:	
			for claimer in item.claimers:			
				if(claimer in self.split):
					self.split[claimer] += item.price / len(item.claimers)
				else:			
					self.split[claimer] = item.price / len(item.claimers)

		for claimer in self.split:
			self.split[claimer] += self.base_total_per_head

		# if some people didn't participate in any claim
		if(len(self.split) < self.num_sharers):
			self.num_base_sharers = self.num_sharers - len(self.split)
			self.split[EVERYONE_ELSE] = self.base_total_per_head


	def __round_and_finish(self):
		"""round up final shares to two decimal places and print answer"""

		total_after_rounding = 0
		for claimer in self.split:
			if claimer == EVERYONE_ELSE:
				total_after_rounding += round(self.num_base_sharers * self.split[claimer], 2)
			else:
				total_after_rounding += round(self.split[claimer], 2)
			print("{} pays ${:.2f}".format(claimer, round(self.split[claimer], 2)))

		print("Total amount after rounding off = ${:.2f}\n".format(round(total_after_rounding, 2)))

if __name__ == '__main__':	
	splitter = Splitter()
	splitter.split()
