from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

# Madlib.html
@app.route('/madlib', methods=['GET','POST'])
def fill_in_the_blank():
    return render_template('madlib.html', url="/completed")

# Completed.html(Cass)
@app.route('/completed', methods=['GET', 'POST'])
def Fill_In_Blanks():
       if request.method == 'POST':
        date = request.form['date']
        noun = request.form['noun']
        verb = request.form['verb']
        verb2 = request.form['verb2']
        adverb = request.form['adverb']
        adjective = request.form['adjective']
        adverb2 = request.form['adverb2']
        adjective2 = request.form['adjective2']
        feeling = request.form['feeling']
        noun2 =request.form['noun2']
        symptom = request.form['symptom']
        return render_template('Completed.html', date=date, noun=noun, verb=verb, verb2=verb2, adverb=adverb, adjective=adjective,
                           adverb2=adverb2, adjective2=adjective2, feeling=feeling,  noun2=noun2, symptom=symptom)



# End

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80 ,debug = True)