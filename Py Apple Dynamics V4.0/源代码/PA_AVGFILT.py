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
		

def avg(r0, r1):
    mov(r3, r0)
    add(r3, 12)         # r3 points to ring buffer start
    ldr(r2, [r0, 0])    # Element count
    sub(r2, 4)          # Offset in words to buffer end
    add(r2, r2, r2)
    add(r2, r2, r2)     # convert to bytes
    add(r5, r2, r3)     # r5 points to ring buffer end (last valid address)
    ldr(r4, [r0, 8])    # Current insertion point address
    cmp(r4, 0)          # If it's zero we need to initialise
    bne(INIT)
    mov(r4, r3)         # Initialise: point to buffer start
    label(INIT)
    ldr(r7, [r0, 4])    # get current sum
    ldr(r6, [r4, 0])
    sub(r7, r7, r6)     # deduct oldest value
    add(r7, r7, r1)     # add newest value
    str(r7, [r0, 4])    # put sum back
    str(r1, [r4, 0])    # put in buffer and post increment
    add(r4, 4)
    cmp(r4, r5)         # Check for buffer end
    ble(NOLOOP)
    mov(r4, r3)         # Incremented past end: point to start
    label(NOLOOP)
    str(r4, [r0, 8])    # Save the insertion point for next call
    ldr(r1, [r0, 0])    # Element count
    sub(r1, 3)          # No. of data points
    mov(r0, r7)         # The sum
    sdiv(r0, r0, r1)    # r0 = r0//r1


