import paho.mqtt.client as mqtt

if __name__ == '__main__':
    client = mqtt.Client()

    client.connect("localhost", 1883, 60)

    topic = 'home/bedroom/light'
    client.publish(topic,
                   payload='on',
                   # retain=False
                   )
