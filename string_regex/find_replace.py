# Find replace

line = "the quick brown fox jumped over a lazzy dog"
print line.find('fox')
print line.index('fox')

print line.find('bear')
try:
	print line.index('bear')
except ValueError as e : 
	print type(e)
	print "not done because of ", e
else : 
	print "done"
finally : 
	print "cleaning up"
