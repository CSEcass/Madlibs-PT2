from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Madlib.html
@app.route('/madlib')
def fill_in_the_blank():
    myUrl= url_for('Completed')
    return render_template('madlib.html', url = myUrl)













# Completed.html(Cass)
@app.route('/Completed')
def Fill_In_Blanks():

    # get
    
    # fill 

    return

# End

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80 ,debug = True)