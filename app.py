from flask import Flask
import os
from datetime import datetime
import platform

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to the Flask App</h1><p>Go to <a href="/htop">/htop</a> to see system information.</p>'

@app.route('/htop')
def htop():
    try:
        full_name = "Sayan Banerjee"
        username = os.environ.get('USER') or os.environ.get('USERNAME')
        ist_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        system_info = platform.uname()
        system_output = f"""
        System: {system_info.system}
        Node Name: {system_info.node}
        Release: {system_info.release}
        Version: {system_info.version}
        Machine: {system_info.machine}
        Processor: {system_info.processor}
        """

        return f"""
        <html>
            <head><title>HTop</title></head>
            <body>
                <h1>System Info</h1>
                <p>Name: {full_name}</p>
                <p>Username: {username}</p>
                <p>Server Time (IST): {ist_time}</p>
                <pre>{system_output}</pre>
            </body>
        </html>
        """
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  
