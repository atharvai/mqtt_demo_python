# Demo for MQTT Demo for Python Meetup

[Slides](https://docs.google.com/presentation/d/1Gmd3j4cvd-x6t3hNhPFckMBAaviJp3-Bn1sErjlPDO0/edit?usp=sharing)

Steps to run

# Publish and Subscribe 

- start subscriber for `demo_topic`
- publish message to `demo_topic`

# Ephemeral topic
Let's watch demo_topic data disappear

- stop subscriber
- publish message
- start subscribe

# Retaining topic

- stop subscriber
- publish multiple messages
- start subscriber

# Hierarchy of topics

## Subscribing to all topics

- stop all subscribers
- start subscriber for all topics
- publish multiple messages

Subsribe to all topics

`#`

## Publishing to hierarchy topics

- stop all subscribers
- subscribe to `home/living_room/light`
- publish message to `home/living_room/light`
- publish message to `home/living_room/tv`

## Wildcards `+`

- subscribe to `home/living_room/+`
- publish message to `home/living_room/light`
- subscribe to `home/+/light`
- publish to `home/living_room/light` and `home/bedroom/light`

# Setup
Start mosquitto

```mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf```

Subscribe to Topic

```mosquitto_sub -h localhost -p 1883 -t demo_topic -v```

Publish message

```mosquitto_pub -h localhost -p 1883 -t demo_topic -m "test"```
