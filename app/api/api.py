from app.agent.manus import Manus
from flask import Flask, jsonify, request, render_template


class API:
    def __init__(self):
        self.app = Flask(__name__)
        self.add_routes()
        self.manus = Manus()

    def add_routes(self):
        # Define routes
        @self.app.route("/")
        def home():
            # Return simple HTML string instead of rendering a template
            return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Gretly Agent API</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    h1 { color: #333; }
                </style>
            </head>
            <body>
                <h1>Welcome to the Gretly Agent API</h1>
                <p>This is the API server for the Gretly agent.</p>
            </body>
            </html>
            """

        @self.app.route("/prompt", methods=["POST"])
        def promptAgent():
            try:
                data = request.json
                prompt = data.get("prompt")

                # Use asyncio.run which handles the event loop for us
                import asyncio

                response = asyncio.run(self.manus.run(prompt))

                return jsonify(response)
            except Exception as e:
                return jsonify({"error": str(e)}), 500

    def run(self):
        self.app.run(debug=True)
