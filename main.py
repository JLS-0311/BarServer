from flask import Flask, jsonify, request


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/API/carta', methods=['GET'])
        def get_carta():
            return self.get_carta()

        @self.app.route('/API/loginInfo', methods=['POST'])
        def login_info():
            return self.login_info()

    def get_carta(self):
        carta = {
            "entradas": ["Ensalada", "Sopa"],
            "platos_principales": ["Pasta", "Pollo"],
            "postres": ["Helado", "Tarta"]
        }
        return jsonify(carta)

    def login_info(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username == 'admin' and password == 'password':
            return jsonify({"status": "success", "message": "Login successful"}), 200
        else:
            return jsonify({"status": "fail", "message": "Invalid credentials"}), 401

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    server = Server()
    server.run()
