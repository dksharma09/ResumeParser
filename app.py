from flask import Flask, render_template, request
import os
import logging
import time
import datetime

app = Flask(__name__)

try :
    fileName = str(time.time())
    logging.basicConfig(filename=f'LogsAPI/{fileName}.log', encoding='utf-8', level=logging.DEBUG)
except FileExistsError as e :
    print(f'Error : {e}')
except Exception as e :
    print(f'Error : {e}')
    
@app.route('/')
def homePage() :
    logging.info(f'{datetime.datetime.now()} : Homepage opened')
    return render_template('index.html')

@app.route('/submittedsuccessfully', methods=['GET', 'POST'])
def fileParsing() :
    logging.info(f'{datetime.datetime.now()} : Form filled Successfully')
    if request.method == 'POST' :
        try : 
            fullName = request.form.get('full_name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            resume = request.files['resume']
        except Exception as e :
            logging.error(f'{datetime.datetime.now()} - Unable to read data from form and Error = {e}')
        
        if resume :
            try :
                # file = resume.read()
                # print(file)
                filename = os.path.join(r'ImportedFiles', resume.filename)
                resume.save(filename)
            except FileExistsError as e :
                logging.error(f'{datetime.datetime.now()} - Unable to save the file and Error = {e}')
            try :
                file_path = f'ImportedFiles\\{resume.filename}'
                with open(file_path, 'r', encoding='iso-8859-1') as f:
                    content = f.read()
                    # print(content)
            except Exception as e :
                print(e)
                logging.error(f'{datetime.datetime.now()} - Unable to read the file and Error = {e}')
            
        else :
            return 'Resume not uploaded.'
        # print(fullName, email, phone, resumeName)
        return render_template('output.html', fullName=fullName, email=email, phone=phone, resumeName=resume.filename)
        
if __name__ == '__main__' :
    app.run(debug=True)