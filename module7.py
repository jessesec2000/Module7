import sys
import datetime

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) == 4:
        store, item, cost, payment = data
        dt= datetime.datetime.today()
       
        print ("{0}\t{1}\t{2}".format(dt,item,cost))

     
   
from datetime import datetime, timedelta 

tday=datetime.today()
tdelta=timedelta(seconds=60)
tdeltay=timedelta(weeks=104)
print(tday-tdelta+tdeltay)


from datetime import timedelta 
d = timedelta(days=100, hours=10, minutes=13)
print(d)



from datetime import datetime 
datetime_object = datetime.now() 
print(datetime_object) 
print('Type :- ',type(datetime_object))

def metricsys (feet, inches, time_object):
    pass
metricsys(10,10, datetime_object)
