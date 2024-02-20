import grpc
import pubsub_pb2
import pubsub_pb2_grpc
import time
import threading

def publisher_thread():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pubsub_pb2_grpc.PubSubStub(channel)
    counter = 0
    while True:
        # message = pubsub_pb2.Message(name='client_a', data='client_a_test')
        print(f"Publishing {counter}")
        response = stub.Publish(pubsub_pb2.Message(name='client_a', data=f"client_a received {str(counter)}"))
        time.sleep(0.1)
        counter += 1

def subscribe(name):
    channel = grpc.insecure_channel('localhost:50051')
    stub = pubsub_pb2_grpc.PubSubStub(channel)
    response = stub.Subscribe(pubsub_pb2.SubscribeRequest(name=name))
    try:
        for message in response:
            # if message.data != "":
            print(f"Received message: {message.data}")
    except grpc.RpcError as e:
        print(f"Error in subscribe: {e.details()}")

if __name__ == '__main__':
    th_a = threading.Thread(target=subscribe, args=('client_a', ))
    th_b = threading.Thread(target=subscribe, args=('client_b', ))
    
    th_a.start()
    th_b.start()

    # time.sleep(5)

    th_p = threading.Thread(target=publisher_thread)
    th_p.start()

    while True:
        time.sleep(1)

