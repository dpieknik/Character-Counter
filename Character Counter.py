# Using Dictionaries to remove duplicate characters and display information

# Test String can be replaced with external input or any alternate string

test_str = "aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbccccccccccccccccllllllllllllldddddddddddddaaaaaaaaabbbbbbbbbbb"

# Turns test_str into a list so it can be sorted and turned into a dictionary

mylist = list(test_str)
mylist.sort()
dict_unique = dict.fromkeys(mylist)

# Dictionary characteristic allows removal of duplicates, which are displaed in an alternate list

mylist_unique = list(dict_unique)
print(mylist_unique)

# Matches characters from dict to their count from initial list

def find_unique(mylist_unique, dict_unique, mylist):
  for i in range(len(mylist_unique)):
  
	# The prints are unnecessary for the function, but show what's going on in the code	
		
      print(mylist_unique[i])
      print(mylist.count(mylist_unique[i]))
      print(mylist_unique[i])
	  
	  # This is the only line required for this function
	  
      dict_unique[mylist_unique[i]] = mylist.count(mylist_unique[i])

# Display Results

find_unique(mylist_unique, dict_unique, mylist)
print(dict_unique)