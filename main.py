from app import app
import routes
import os
  
if not os.path.exists("./audios"):
    os.makedirs("./audios")

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run()