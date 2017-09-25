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
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
# 注意：这里是广播，不需要声明queue
channel.exchange_declare(exchange='logs',  # 声明广播管道
                         type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',  # 注意此处空，必须有,因为是广播，不需要queue
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
