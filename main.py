import math

def sigmoid(i):
    return 1/(1+math.exp(-i))

def meets_threshold(pw):
    return True in [c.isupper() for c in pw] and True in [c.islower() for c in pw] and True in [c.isdigit() for c in pw]

def password_rating(pw):
    return ((10*sigmoid(sum([4 for c in pw if ".?!&#,;:-_*".find(c) != -1]) 
                        + sum([2 for c in pw if c.isdigit()]) 
                        + sum([1 for c in pw if c.isupper()]) 
                        + sum([1 for c in pw if c.islower()])/math.exp(2*len(pw)))) - 5)*2
#Tests-------------------------
print "Testing meets_threshold()"
print meets_threshold("password")#false
print meets_threshold("Password")#false
print meets_threshold("12398")#false
print meets_threshold("12398dsd")#falses
print meets_threshold("Password123")#true

print "\nTesting password_rating()"
print password_rating("hello")
print password_rating("Hello")
print password_rating("HeLlO12")
print password_rating("HELlo&!")