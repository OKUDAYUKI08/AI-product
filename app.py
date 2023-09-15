from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def  index():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")
@app.route("/show",methods=['GET','POST'])
def show():
    if request.method=='GET':
        return render_template("show.html")
    if request.method=='POST':
        result=request.form['data1']
        return render_template("show.html",result=result)


if __name__=="__main__":
    app.run(debug=True)