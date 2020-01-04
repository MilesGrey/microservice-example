from flask import Flask, jsonify
from py_eureka_client import eureka_client

app = Flask(__name__)
eureka_client.init_registry_client(
        eureka_server='http://localhost:8761/eureka/',
        app_name='movie-info-service',
        instance_port=5000
    )


@app.route('/movies/<int:movieId>')
def hello_world(movieId):
    return jsonify({
        'movieId': movieId,
        'name': 'Test name'
    })


if __name__ == '__main__':
    app.run()
