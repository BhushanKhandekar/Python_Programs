# String 
# Single ( ' ' )& Double ( " " ) Quotation Marks returns a string on single line only
# Triple ( ''' ''' ) Quotation Mark returns string on multiple lines

#print(" My name is Bhushan and I am living in Nagpur")

#print('My name is Bhushan and I am living in Nagpur')

#print('''My name is Bhushan and I am living in Nagpur''')




# String Slicing
# positive indexing is from 0 to n
# positive is from left to right
# negative indexing is from -1 to n
# negative indexing is from right to left

string = "My name is Bhushan."

print(string[1:5])
print(string[2:5])
print(string[-2:-5])    # No Output since direction is right to left
print(string[-5:-2])
print(string[3:-3])
print(string[:])           # Return string as it is
print(string[::-1])      # T9 reversed the string
print(string[3:-3:2]) 
print(string[::2])
print(string[-3:3:-2])    
print(string[3:-3:-2]) # No Output