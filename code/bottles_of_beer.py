'''
This is a song for people with a lot of time on their hands!
'''

def print_verse(n):
   print(n,'bottles of beer on the wall')
   print(n,'bottles of beer')
   print('Take one down, pass it around')
   print(n-1,'bottles of beer on the wall')
   print()
def print_song(k):
    print(k,'Bottles of Beer Song')
    print()
    for i in range(k,0,-1):
        print_verse(i)

print_song(100)
