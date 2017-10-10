# Lambda functions 

add = lambda x, y: x + y

# The above lambda function is roughly equivalent to function below
def add(x, y):
	return x + y

print "add(2, 3) : ", add(2, 3)

# sort the datasets by suppying key function that returns the key from an item.
print "sorted([1, 10, 5]) ", sorted([1, 10, 5])

data = [
	{'first': 'Guido', 'last': 'van rossum' , 'YOB': 1956 }, 
	{'first': 'Grace', 'last': 'Hopper', 'YOB': 1906}, 
	{'first': 'Alan', 'last': 'Turing', 'YOB': 1912} 
	]

print "data as is, not sorted : ", data
print

sorted_data = sorted(data, key = lambda item: item['first'])
print "sorted data based on first name : ", sorted_data
print

sorted_data = sorted(data, key = lambda item: item['YOB'])
print "sorted data based on YOB : ", sorted_data
print

