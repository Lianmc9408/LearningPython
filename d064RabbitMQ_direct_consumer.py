import pika
import sys

# direct 有选择的接收消息
# 接收者可以过滤消息，只收我想要的消息

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 获取运行脚本所有的参数
# python d064RabbitMQ_direct_consumer.py info warning
severities = sys.argv[1:]  # 如上例可以得到[info, warning]

if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)
# 循环列表去绑定
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

# 运行接收端，指定接收级别的参数，例：
# python d064RabbitMQ_direct_consumer.py info warning
# python d064RabbitMQ_direct_consumer.py warning error
