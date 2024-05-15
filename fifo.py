


from queue import Queue 

# Function to find page faults using FIFO 
def pageFaults(pages, n, capacity): 
	
	s = set() 
	
	indexes = Queue() 

	page_faults = 0
	for i in range(n):  
		if (len(s) < capacity): 
			if (pages[i] not in s): 
				s.add(pages[i]) 

				page_faults += 1
 
				indexes.put(pages[i]) 

		else: 
			if (pages[i] not in s): 
				
				val = indexes.queue[0] 

				indexes.get() 

				s.remove(val) 

				s.add(pages[i]) 

				indexes.put(pages[i]) 

				page_faults += 1

	return page_faults 

# Example usage:
if __name__ == '__main__': 
	capacity = int(input("Enter the capacity of the page table: ")) 
	pages = list(map(int, input("Enter the page references : ").split())) 
	n = len(pages) 
	print("Total Page Faults:", pageFaults(pages, n, capacity)) 

