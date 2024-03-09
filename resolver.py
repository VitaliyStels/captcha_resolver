import os
files = os.listdir('static/uploads')

def check_image():
    if len(files) > 0:
        for i in files:
            return f'{i} succeeded'


    