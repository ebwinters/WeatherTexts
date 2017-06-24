import schedule 
import time

def func():
	print ("Hey")


schedule.every(1).minutes.do(func)


while True:
	schedule.run_pending()
	time.sleep(60)