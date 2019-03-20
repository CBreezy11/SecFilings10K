from flask import Flask, request, render_template
import sec_final



app = Flask("__name__")

@app.route('/')
def index():
    return "We are working"

@app.route('/get10ksite', methods=['POST', 'GET'])
def get10ksite():
    if request.method == 'POST':
        company = request.form.get('company')
        launch.main(company)
        return render_template('{}.html'.format(company))

    else:
        return '''<form method='POST'>
                    company: <input type="text" name="company"><br>
                    <imput type="submit" value="submit:><br>
                </form>''' 

launch = sec_final.Get10k()
if __name__ == '__main__':
    app.run(host="0.0.0.0")

