from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Madlibs from WEEK_1:

# ---Upchallenge0(PrintColor):
# import sys
# def print_colored(text, color, end=' '):
#     colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
#     reset = '\x1b[0m'
#     sys.stdout.write(colors.get(color, '') + text + reset + end)
# ---Upchallenge1(Datetime): 
# import datetime
# CurrDate = datetime.datetime.now()
# DateTimeStr = CurrDate.strftime('%d-%m-%y')
# ---MadLib by cass
# print_colored('----MadLibs----\n', color= 'red')
# ---User input vvv
# noun = input('Enter a noun: ')
# verb = input('Enter a verb: ')
# verb2 = input('Give me a better one: ')
# noun2 = input('Now give me a NOUN: ')
# adjective = input('I NEED an adjective: ')
# adjective2 = input('Anotha 1: ')
# adverb = input('I lie. I want adverbs more(ugly sobbing):')
# adverb2 = input('Got any DECENT(not like the other one u just entered... yikes), adverbs: ')
# Feel = input('how do u feel so far(i totally care bestie): ')
# ---finished Product vvv
# print_colored('\n--------Finished product--------\n', color= 'red')
# print(f'In a surprising turn of events on {DateTimeStr}, {noun} transformed into a {verb} battleground for \nWorld War III, leaving behind a trail of destruction and chaos with everyone {verb2} in its wake.\nThe once {adverb} {adjective} land now echoed with the sounds of {adverb2} and {adjective2}. \nAs the dust settled,\nthe protagonist found themselves grappling with overwhelming emotions and deep-seated trauma.\nThey felt {Feel}, Seeking solace and {noun2},\n they embarked on a journey of intensive therapy to confront their clinical depression and make sense\nof the turmoil that had engulfed their beloved {noun}.')
# ---The end






# Madlib.html
@app.route('/madlib')
def fill_in_the_blank():
    myUrl= url_for('Completed')
    return render_template('madlib.html', url = myUrl)













# Completed.html(Cass)
@app.route('/Completed')
def Fill_In_Blanks():
    # get: var = request.form.get('name')
    
    # fill 

    return render_template('Completed.html')

# End

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80 ,debug = True)