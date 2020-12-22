import time 

def example(seconds): 
	print("Starking task")
	for i in range(seconds):
		print(i)
		time.sleep(1)
	print("Task Complete")