import django
import json
import os
from confluent_kafka import Consumer
from dotenv import load_dotenv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

import core.listeners


load_dotenv()

KAFKA_SERVER = os.getenv('KAFKA_SERVER')
KAFKA_USERNAME = os.getenv('KAFKA_USERNAME')
KAFKA_PASSWORD = os.getenv('KAFKA_PASSWORD')



consumer = Consumer({
'bootstrap.servers':KAFKA_SERVER,
'security.protocol':'SASL_SSL',
'sasl.mechanisms':'PLAIN',
'sasl.username': KAFKA_USERNAME,
'sasl.password':KAFKA_PASSWORD,
'group.id':'notifications-group',
'auto.offset.reset':'earliest',

# Best practice for higher availability in librdkafka clients prior to 1.7
'session.timeout.ms':'45000',
})



consumer.subscribe(['notifications_topic'])

try:
    while True:
        # consumer polls the topic and prints any incoming messages
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f'Consumer error: {msg.error()}')
            continue
        
        print(msg.key().decode("utf-8"))
        # activate callback function
        getattr(core.listeners, msg.key().decode('utf-8'))(json.loads(msg.value()))
except KeyboardInterrupt:
    pass
finally:
    # closes the consumer connection
    consumer.close()