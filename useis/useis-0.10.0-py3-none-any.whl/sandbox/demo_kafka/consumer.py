from confluent_kafka import Consumer
import sys


conf = {'bootstrap.servers': "localhost:29092",
        'group.id': 'test',
        'auto.offset.reset': 'smallest'}

c = Consumer(conf)

running = True


def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                print('error')
                # if msg.error().code() == #KafkaError._PARTITION_EOF:
                #     # End of partition event
                #     sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                #                      (msg.topic(), msg.partition(), msg.offset()))
                # elif msg.error():
                #     print(msg.error())
                #     # raise KafkaException(msg.error())
            else:
                print(msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


def shutdown():
    running = False


basic_consume_loop(c, ['test'])
