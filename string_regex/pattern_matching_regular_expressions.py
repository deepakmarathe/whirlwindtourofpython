# Pattern matching, regular expressions

# the strings are to be enclosed in double quotes " "

import re

line = "the quick brown fox jumped over a lazzy dog"

regex =  re.compile('\s+')

print regex.split(line)

for s in ["   ", "abc  ", "  abc"]:
	if regex.match(s):
		print repr(s), "matches"
	else : 
		print repr(s), "does not match"

regex = re.compile('fox')
match = regex.search(line)
print match.start()

# returns a new string
print regex.sub('BEAR', line)
# the original line is not changed.
print line

