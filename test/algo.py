
def exceedbyK(s, k): 
	
	# the new result will be stored in this
	newValue = "" 
	
	for i in range(len(s)): 
		
		val = ord(s[i]) 
		
		dup = k 
		
		if val + k>122: 
			k -= (122-val) 
			k = k % 26
			newValue += chr(96 + k) 
			
		else: 
			newValue += chr(val + k) 
		
		k = dup 
	
	print (newValue) 
			
# please give the string and a k-value to test here
str = "nikhil"
k = 4

exceedbyK(str, k) 
