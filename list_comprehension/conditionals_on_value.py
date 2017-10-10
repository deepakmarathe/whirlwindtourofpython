val = -10

print val if val >= 0 else -val

print [ val if val % 2 else -val for val in range(20) if val % 3 ] 

