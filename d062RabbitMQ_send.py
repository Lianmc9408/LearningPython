import pika
# http://blog.csdn.net/fgf00/article/details/52872730
# http://www.diggerplus.org/archives/3110
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()  # 声明一个管道

# 声明queue
channel.queue_declare(queue='hello')
# channel.queue_declare(queue='hello', durable=True)  durable参数为消息持久化，消费者和生产者都要写

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',  # queue名字
                      body='Hello World!',  # body,要发的内容
                      )
# channel.basic_publish(exchange='',
#                       routing_key='hello',  # queue名字
#                       body='Hello World!',  # body,要发的内容

#                       properties=pika.BasicProperties(
#                           delivery_mode=2,  # 让消息持久化，rabbitMQ挂掉重启后队列和队列内的消息都还在
#                       )

#                       )
print(" [x] Sent 'Hello World!'")
connection.close()

# 消息持久化要改生产者和消费者的channel.queue_declare(queue='hello', durable=True)
# 和生产者的channel.basic_publish增加properties=pika.BasicProperties(
#                           delivery_mode=2,  # 让消息持久化
#                       )