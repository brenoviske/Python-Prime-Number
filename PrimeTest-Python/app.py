from flask import Flask, render_template,request # Importing tools that i will need it
app = Flask(__name__)# Creating flask application

@app.route('/', methods = ['GET','POST'])
def homepage():
    result = ''
    if request.method == 'POST':
        try:
            Number = int(request.form.get('Number'))
            if Number <= 1:
                result = 'The number must be grater than one'
            else:
                divisor = 0
                for i in range (1, Number+1 ):
                    if Number % i == 0 : divisor+=1
                if divisor == 2 :
                    result = f'The number {Number} is prime'
                else:
                    result = f'The number {Number} is not prime'
        except ValueError:
            return 'There was an error, please try it again'
    return render_template('index.html',result = result)



if __name__ == '__main__': app.run(debug=True,port=5600)




