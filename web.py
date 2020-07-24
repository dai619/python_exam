from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    title="python_exam"
    return render_template("index.html",title=title)
@app.route('/hzau')
def hzau():
    return render_template("hzau.html")

if __name__=='__main__':
    app.run(host="127.0.0.1",port=8082)