from flask import Flask,render_template,request

app=Flask(__name__)
app.config['SECRET_KEY']= 'mysecretkey'


from forms import UserInfoForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def show_enter():
    form=UserInfoForm(request.form)
    
    if request.method=='POST' and form.validate():
        return render_template('result.html',form=form)

    return render_template('form.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)