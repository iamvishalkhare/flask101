from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
    message = "Hello world"
    return message
    
if __name__ == "__main__":
    app.run() 