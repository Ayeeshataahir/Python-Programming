#Exercise 6.1
s='X-DSPAM-confidence:0.8475'
i=s.find(':')
name=s[i+1:]
i=float(i)
print (name)

