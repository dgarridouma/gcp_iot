import requests
import json
#import datetime
import random
import time
import json

#FUNCTION_URL='https://YOUR_FUNCTION_URL_HERE'
FUNCTION_URL='http://127.0.0.1:8080'
period = 10

def main():

    while True:
        msg=dict()
        msg['temperature']=random.randint(25,30)
        msg['humidity']=random.randint(50,100)
        msg['pressure']=random.randint(900,1100)
#        msg['when']=datetime.datetime.now()
        json_data=json.dumps(msg,default=str)
        print(str(msg['temperature'])+' '+str(msg['humidity'])+' '+str(msg['pressure']))

        newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(FUNCTION_URL,
                #         data=json.dumps(json_data), This is string
                         data=json_data,
                         headers=newHeaders)

        print("Status code: ", response.status_code)
        print(response.text)

        time.sleep(period)

if __name__ == '__main__':
    main()
