import pika
import os

class mpProducer(producer_interface):

    def __init__(self, routing_key: str, exchange_name: str):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        setUpRMQConnection()

    

    def setupRMQConnection(self):
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)
    

    def publishOrder(self, message: str):
        channel = connection.channel()
        exchange = channel.exchange_declare(exchange=self.exchange_name)
        channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message,
        )
        channel.close()
        connection.close()



