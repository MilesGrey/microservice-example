import py_eureka_client.eureka_client as eureka_client

your_rest_server_port = 9090
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server="http://localhost:8761/eureka",
                                app_name="your_app_name",
                                instance_port=your_rest_server_port)

while True:
    print('running')