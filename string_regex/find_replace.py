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

print line.rfind('a')
print line.endswith('dog')
print line.startswith('fox')

print line.replace('brown', 'red')
print line
print line.replace('o','--')

print line.partition('fox')
print line.split()

haiku = """matsushima-ya
 aah matsushima-ya
 matsushima-ya"""
splitlines = haiku.splitlines()
print splitlines

print "--".join(['1', '2', '3'])

print "\n".join(splitlines)



