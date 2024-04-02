import time 
def count_down(a):
    while a :
        mins,secs = divmod(a,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end = "\r")
        time.sleep(1)
        a -= 1
    print ("time is over!!")
     
     
a = input("Enter the time:")

count_down(int(a))
                
    