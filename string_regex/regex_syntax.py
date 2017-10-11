# Basics of regular expression syntax

import re

# Simple strings are matched directly
regex = re.compile('ion')
print regex.findall('great expectations')

# characters with special meanings
# . ^ $ * + ? { } [ ] \ | ( )

# Escaping special characters
regex = re.compile('\$')
print regex.findall(r"the cost is $100")

print "standard python strings : ", "a\tb\tc"
print "raw python strings : ", r"a\tb\tc"

# Special characters can match character groups
regex = re.compile('\w\s\w')
print regex.findall('the fox is 9 years old')

# \d 	match any digit
# \D	match any non-digit
# \s 	match any whitespace 
# \S 	match any non-whitespace
# \w 	match any alphanumeric character
# \W	match any non-alphanumeric character

# Square brackets match custom character groups
regex = re.compile('[aeiou]')
print regex.split('consequential')

regex = re.compile('[A-Z][0-9]')
print regex.findall('1043, G2,  H6')


# Wildcard match repeated characters
regex = re.compile(r"\w{3}")
print regex.findall('The quick brown fox')

regex = re.compile('\w+')
print regex.findall("The quick brown fox")

# Table of repitition markers
# ? 	Match 0 or 1 repetitions of proceeding
# * 	Match 0 or more repetitions of preceeding
# + 	match 1 or more repetitions of the preceeding
# {n}	Match n repetitions of the preceeding
# {m, n}	Match between m and n repetitions of proceeding

email2 = re.compile(r'[\w+.]+@\w+\.[a-z]{3}')
print email2.findall('barack.obama@whitehouse.gov')


# Paranthesis indicate groups to extract
email3 = re.compile('([\w+.]+)@(\w+)\.([a-z]{3})')
text ="To email Guido, try guido@python.org or the older address guido@google.com"
print email3.findall(text)

# We can even name the groups 
email4 = re.compile('(?P<name>[\w+.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})') 
print email4.findall('guido@python.org')



