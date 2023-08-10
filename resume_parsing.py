import os
import logging
import time
import datetime


fileName = str(time.time())
logging.basicConfig(filename=f'LogsResumeParsing/{fileName}.log', encoding='utf-8', level=logging.DEBUG)

folderPath = r'C:\Users\dushy\OneDrive\Documents\DK Projects\Resume Parser\ImportedFiles'

fileList = os.listdir(folderPath)

for file in fileList :
    print(file)
    logging.info(f'{datetime.datetime.now()} : {file}')
    filePath = os.path.join(folderPath, file)
    print(filePath)
    with open(filePath, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"Content of {file}:")
        print(content)
        logging.info(f'{datetime.datetime.now()} : {content}')