import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect("localhost", 1883, 60)

    topic = 'home/bedroom/light'
    client.publish(topic,
                   payload='on',
                   # retain=False
                   )
