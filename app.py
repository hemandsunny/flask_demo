from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return '<marquee><p style="margin-top:45vh;text-align:center;font-size:5vw;">HELLO FROM FLASK</p></marquee>'

if __name__=='__main__':
    app.run()