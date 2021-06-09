import pika

params = pika.URLParameters('amqps://pkljeoiv:EUjMfKklDRjog0FHJuVZgVhH96uXDciP@beaver.rmq.cloudamqp.com/pkljeoiv')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')