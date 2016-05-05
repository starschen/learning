#encoding:utf8
epsilon=0.01
k=int(raw_input())
numGuesses=0
guess=k/2.0
while abs(guess*guess-k)>=epsilon:
    guess=guess-(guess**2-k)/(2*guess)
    numGuesses+=1
print 'numGuesses=',numGuesses
print 'Square root of',k,'is about',guess
