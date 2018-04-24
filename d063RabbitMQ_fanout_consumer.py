import pika
import sys

# 前面的效果都是一对一发，如果做一个广播效果可不可以，这时候就要用到exchange了
# exchange必须精确的知道收到的消息要发给谁。exchange的类型决定了怎么处理，
# 类型有以下几种：
# fanout: 所有绑定到此exchange的queue都可以接收消息
# direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
# topic： 所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息


# fanout 纯广播、all
# 需要queue和exchange绑定，因为消费者不是和exchange直连的，消费者是连在queue上，
#       queue绑定在exchange上，消费者只会在queue里读消息

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
# 获取随机的queue名字
queue_name = result.method.queue
print("random queuename:", queue_name)

channel.queue_bind(exchange='logs',  # queue绑定到转发器上
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

# 注意：广播，是实时的，收不到就没了，消息不会存下来，类似收音机。
# 先启动consumer，再启动publish
