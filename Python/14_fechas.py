import time

seconds = time.time()
print('numero de ticks desde las 12:00 del 1 de enero de 1970 ', seconds)


#hora local
local_time = time.localtime()
print(local_time)

#hora local reseteada

asctime = time.asctime(local_time)
print(asctime)

#Formato fecha españa
date_format = '%d-%b-%Y a las %H:%M:%S'
date_formatted = time.strftime(date_format, time.gmtime(seconds))
print(date_formatted)