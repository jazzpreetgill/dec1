from flask import Flask, redirect, url_for,render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is fail and marks is" + str(score)

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The result is pass</h1></body></html>"

#result checker
@app.route('/result/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

#result checker submit HTML form
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0 
    if request.method=='POST':
        DATA440=float(request.form['DATA440'])
        DATA480=float(request.form['DATA480'])
        ARTI440=float(request.form['ARTI440'])
        ETHI440=float(request.form['ETHI440'])
        total_score = (DATA440+DATA480+ARTI440+ETHI440)/4
    res=""
    if total_score>=50:
        res='success'
    else:
        res='fail'
    return redirect(url_for(res,score=total_score))

if __name__=='__main__':
    app.run(debug=True)