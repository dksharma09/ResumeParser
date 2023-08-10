from flask import Flask, render_template, request
import os
import logging
import time
import datetime

app = Flask(__name__)

fileName = str(time.time())
logging.basicConfig(filename=f'logs/{fileName}.log', encoding='utf-8', level=logging.DEBUG)
@app.route('/')
def homePage() :
    logging.info(f'{datetime.datetime.now()} : Homepage opened')
    return render_template('index.html')

@app.route('/submittedsuccessfully', methods=['GET', 'POST'])
def fileParsing() :
    logging.info(f'{datetime.datetime.now()} : Form filled Successfully')
    if request.method == 'POST' :
        fullName = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        resume = request.files['resume']
        
        if resume :
            filename = os.path.join(r'C:\Users\dushy\OneDrive\Documents\DK Projects\Resume Parser\ImportedFiles', resume.filename)
            resume.save(filename)
            try :
                f = open(filename)
                content = f.read()
                print(content)
                f.close()
            except Exception as e :
                print(e)
            
        else :
            return 'Resume not uploaded.'
        # print(fullName, email, phone, resumeName)
        return render_template('output.html', fullName=fullName, email=email, phone=phone, resumeName=resume.filename)
        
        


if __name__ == '__main__' :
    app.run(debug=True)