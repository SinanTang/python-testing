"""
== Unit Testing in Python ==
- write the skeleton of your function or class to be tested, but before fill in any actual methods, go to the next step;
- write up your unit test class first, it should inherit from unittest.TestCase;
- call unittest before starting to work on the real code, all (or most) test methods should fail;
- define the methods in the function/class, and then run the test again - all should pass this time!

- then write new tests to test unexpected use cases, bad input values & boundary cases.
- improve your current implementation based on test results.
"""

import unittest

class Stack:
	def __init__(self):
		self.stack = []
	def push(self, item):
		# pass
		self.stack.append(item)
	def pop(self):
		# pass
		# handle empty pops
		if not self.stack:
			raise IndexError('Cannot pop from empty stack')
		return self.stack.pop()
	def peek(self):
		# pass
		return self.stack[-1]
	def is_empty(self):
		# pass
		if len(self.stack) > 0:
			return False
		return True


# class StackTests(unittest.TestCase):
# 	def setUp(self):
# 		self.stack = Stack()
# 	def tearDown(self):
# 		del self.stack
# 	def test_is_empty(self):
# 		self.assertTrue(self.stack.is_empty())
# 	def test_push(self):
# 		self.stack.push(100)
# 		self.assertFalse(self.stack.is_empty())
# 	def test_peek(self):
# 		self.stack.push('test')
# 		self.assertEqual(self.stack.peek(), 'test')
# 	def test_pop(self):
# 		self.stack.push(10.1)
# 		self.stack.pop()
# 		self.assertTrue(self.stack.is_empty())
# 	def test_pop_value(self):
# 		self.stack.push('test_value')
# 		value = self.stack.pop()
# 		self.assertEqual(value, 'test_value')


class StackTests(unittest.TestCase):
	"""
	tests unexpected use cases, bad input values & boundary cases
	e.g. popping from empty list
	"""
	def setUp(self):
		self.stack = Stack()
	def tearDown(self):
		del self.stack
	def test_empty_pop(self):
		with self.assertRaises(IndexError):
			self.stack.pop()


if __name__ == '__main__':
	unittest.main()