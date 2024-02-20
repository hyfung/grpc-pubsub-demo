import grpc
from concurrent import futures
import time
import pubsub_pb2
import pubsub_pb2_grpc
from pprint import pprint
import threading

def broadcast_to_subscribers():
    pass

class PubSubServicer(pubsub_pb2_grpc.PubSubServicer):
    def __init__(self):
        self.subscriptions = {}
        # {"client_a": _Context}

        self.message_queue = {}
        # {"client_a" : [], "client_b": []}

        status_thread = threading.Thread(target=self.print_status)
        status_thread.start()

    def print_status(self):
        while True:
            print("--- Subscriptions ---")
            pprint(self.subscriptions)
            print("--- Message Queue ---")
            pprint(self.message_queue)
            time.sleep(1)

    def Subscribe(self, request, context):
        if not request.name in self.subscriptions:
            self.subscriptions[request.name] = context
            self.message_queue[request.name] = []
            print(f"Client {request.name} subscribed")
        else:
            print(f"")
        
        while True:
            print(f"Serving {request.name}")
            time.sleep(0.1)
            if not context.is_active():
                print(f"Context {request.name} lost, deleting")
                del self.subscriptions[request.name]
                del self.message_queue[request.name]
                break
            else:
                while len(self.message_queue[request.name]) > 0:
                    response = pubsub_pb2.Message(data=self.message_queue[request.name].pop(0))
                    yield response
                response = pubsub_pb2.Message(data=f"Heartbeat for {request.name}")
                yield response

    def Publish(self, request, context):
        if not request.name in self.subscriptions:
            return pubsub_pb2.PublishResponse(status=pubsub_pb2.PublishResponseStatus.NOT_FOUND)
        else:
            self.message_queue[request.name].append(request.data)
            return pubsub_pb2.PublishResponse(status=pubsub_pb2.PublishResponseStatus.SUCCEED)
    
    def messages(self):
        # This method generates some example messages
        for i in range(1, 10):
            yield pubsub_pb2.Message(data=f"Message {i}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pubsub_pb2_grpc.add_PubSubServicer_to_server(PubSubServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
