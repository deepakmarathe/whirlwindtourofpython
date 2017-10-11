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

email = re.compile('\w+@\w+\.[a-z]{3}')
text = "To email Guido, try guido@python.org or the older address guido@google.com"
print email.findall(text)
print email.sub('--@--.--', text)

# Regular expressions can sometimes be unforgiving, that it drops part of the email address because of the dot
print email.findall('barack.obama@whitehouse.gov')

