import pika
import time


# 双向传输
# 返回时，再建立一个queue，把结果发送新的queue里
# 为了服务端返回的queue不写死，在客户端给服务端发指令的的时候，同时带一条消息说，你结果返回给哪个queue
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(
        exchange='',  # 把执行结果发回给客户端
        routing_key=props.reply_to,  # 客户端要求返回想用的queue
        # 返回客户端发过来的correction_id 为了让客户端验证消息一致性
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 任务完成，告诉客户端


# if __name__ == '__main__':
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')  # 声明一个rpc_queue ,

# 若存在多个consumer每个consumer的负载可能不同，有些处理的快有些处理的慢
# RabbitMQ并不管这些，只是简单的以round-robin的方式分配message
# 这可能造成某些consumer积压很多任务处理不完而一些consumer长期处于饥饿状态
# 可以使用prefetch_count=1的basic_qos方法可告知RabbitMQ只有在consumer处理并确认了上一个message后才分配新的message给他
# 否则分给另一个空闲的consumer
channel.basic_qos(prefetch_count=1)

# 在rpc_queue里收消息,收到消息就调用on_request
channel.basic_consume(on_request, queue='rpc_queue')
print(" [x] Awaiting RPC requests")
channel.start_consuming()
