MQTT_HOSTNAME='YOUR_BROKER_IP'
MQTT_PORT=1883

import datetime
import random
import time
import paho.mqtt.client as mqtt
import json

period = 10


def on_connect(unused_client, unused_userdata, unused_flags, rc, properties):
    """Callback for when a device connects."""
    print('on_connect', mqtt.connack_string(rc))


def on_publish(unused_client, unused_userdata, unused_mid, rc, properties):
    """Paho callback when a message is sent to the broker."""
    print('on_publish')


def on_message(unused_client, unused_userdata, message):
    """Callback when the device receives a message on a subscription."""
    payload = str(message.payload,"utf-8")
    #print('Received message \'{}\' on topic \'{}\' with Qos {}'.format(
    #        payload, message.topic, str(message.qos)))
    if message.topic.endswith('command'):
        global period

        dict_command=json.loads(payload)
        period = int(dict_command['period'])
        print(dict_command['message'])


def main():

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(MQTT_HOSTNAME, MQTT_PORT, 60)

    client.loop_start()

    mqtt_topic='device1/data'
    while True:
        msg=dict()
        msg['temperature']=random.randint(25,30)
        msg['humidity']=random.randint(50,100)
        msg['pressure']=random.randint(900,1100)
        msg['when']=datetime.datetime.now()
        json_data=json.dumps(msg,default=str)
        print(str(msg['temperature'])+' '+str(msg['humidity'])+' '+str(msg['pressure']))
        
        client.publish(mqtt_topic, json_data, qos=1)
        time.sleep(period)

if __name__ == '__main__':
    main()
