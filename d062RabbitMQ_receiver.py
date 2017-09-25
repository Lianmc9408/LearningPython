import pika
# http://blog.csdn.net/fgf00/article/details/52872730
# http://www.diggerplus.org/archives/3110
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')  # 生产者和消费者不知道谁先声明，最好都写，如果未写的一方先执行，报错
# channel.queue_declare(queue='hello', durable=True)  durable参数为消息持久化，消费者和生产者都要写

def callback(ch, method, properties, body):
    '''
    一定要声明这4个参数
    :param ch:  管道的内存对象地址，即管道对象
    :param method: 内容相关信息
    :param properties:
    :param body: 生产者发送的消息
    :return:
    '''
    print('', ch, method, properties)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # no_ack 为 false时需要手动确认

# channel.basic_qos(prefetch_count=1)  # 类似权重，按能力分发，如果有一个消息，就不在给你发
channel.basic_consume(callback,  # 消费者消息，如果收到消息，就调用callback方法处理消息
                      queue='hello',  # queue名字
                      # no_ack=True   # 处理完消息后是否给生产者发送一个确认，生产者接收到确认后才会把消息从队列删除
                                    # no_ack为Ture时生产者不接收消息确认，当消费者callback处理消息时程序中断
                                    #       生产者不会把消息发送给下一个消费者，发消息时直接把消息从队列删除
                                    # no_ack为False时生产者会接收消息确认，当消费者callback处理消息时程序中断
                                    #       生产者会把消息发送给下一个消费者，再把消息从队列删除
                                    # RabbitMQ判断消费者是否断开就是通过socket连接是否断开判断的
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 声明channel之后要start，start之后会一直收
