# Implementation of moving average filter in Arm Thumb assembler
# Author: Peter Hinch
# 15th Feb 2015
# Updated to reflect support for sdiv instruction
# Timing: 27uS on MicroPython board (independent of data)

# Function arguments:
# r0 is an integer scratchpad array. Must be of length 3 greater than
# the number of values to be averaged.
# On entry array[0] must hold the array length, other elements must be zero
# r1 holds new data value

# Return value: the current moving average

# array[0] is array length, array[1] is the current sum, array[2] the insertion point
# r2 holds the length of the coefficient array
# Pointers (byte addresses)
# r3 start of ring buffer
# r4 insertion point (post increment)
# r5 last location of ring buffer
# Other registers
# r7 temporary store for result

class avg_filiter():
	def __init__(self,cache_data):
		self.cache = cache_data
		self.len = len(cache_data)
		self.cache[0] = self.len
		self.sum = 0
		for item in cache_data[3:]:
			self.sum += item
		self.cache[1] = self.sum
		
	def avg(self,new_data):
		self.cache[1] = self.cache[1] - self.cache[3]
		self.cache[1] = self.cache[1] + new_data
		self.cache[3:-1] = self.cache[4:]
		self.cache[-1] = new_data
		return self.cache[1]//(self.len - 3)
