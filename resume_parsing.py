import os
import logging
import time
import datetime
from PyPDF2 import PdfReader

fileName = str(time.time())
logging.basicConfig(filename=f'LogsResumeParsing/{fileName}.log', encoding='utf-8', level=logging.DEBUG)

folderPath = r'C:\Users\dushy\OneDrive\Documents\DK Projects\Resume Parser\ImportedFiles'

fileList = os.listdir(folderPath)

for file in fileList :
    # print(file)
    logging.info(f'{datetime.datetime.now()} : {file}')
    filePath = os.path.join(folderPath, file)
    reader = PdfReader(filePath)
    number_of_pages = len(reader.pages)
    logging.info(f'{datetime.datetime.now()} : Number of Pages = {number_of_pages}')
    page = reader.pages[0]
    text = page.extract_text()
    logging.info(f'{datetime.datetime.now()} : Content of the first Page = {text}')
    # print(filePath)
    # with open(filePath, 'r', encoding='utf-8') as f:
    #     content = f.read()
    #     print(f"Content of {file}:")
    #     print(content)
    #     logging.info(f'{datetime.datetime.now()} : {content}')