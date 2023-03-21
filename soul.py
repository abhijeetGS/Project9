from flask import Flask  #From module flask import class Flask

app = Flask(__name__)   #Create an app object of class Flask

@app.route("/")
def hello_world():
  return "Hello, Binod!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)