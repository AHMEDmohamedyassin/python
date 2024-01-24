import logging
import string
import random 

if (__name__ == "__main__") :       ## check if file is not opend as model
    print('file opened directly') 

###logging
logging.basicConfig(filename="log.log" ,
                    filemode="a" ,
                    format="%(asctime)s => %(name)s | %(levelname)s | %(message)s" ,
                    datefmt="%d %B %Y , %H:%M:%S")

mylogger = logging.getLogger('AHMED')
mylogger.warning('the warning message')
mylogger.error('the warning message')
mylogger.info('the warning message')
mylogger.critical('the warning message')


####random ###creating random text example
formingtext = string.ascii_lowercase + string.ascii_uppercase + string.digits
count = 11
theRandomText = ''
while count > 0 :
    count -= 1
    e = formingtext[random.randint(0 , len(formingtext) - 1 )]
    theRandomText = theRandomText + e

print(theRandomText)