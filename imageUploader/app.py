# Code based on pythonbuddy.com

from flask import Flask, render_template, request, jsonify, session, redirect
import os

# Configure Flask App
# Remember to change the SECRET_KEY!
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

# My code
UPLOAD_FOLDER = os.path.join('static','upload')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

image_path=os.path.join(UPLOAD_FOLDER)
# my code end

@app.route('/')
def index():
    """Display home page
        :return: index.html
    """
    session["count"] = 0
    images=[os.path.join(image_path,image) for image in os.listdir(image_path)]
    return render_template("index.html", len = len(images), user_image=images)

'''
BEGIN TASK 1
'''
# Should you use a GET or POST Request?
@app.route('/submit_image', methods=['POST','GET'])
# @app.route('/submit_image', methods=['GET'])
def submit_image():
    """Adds an image to our server and adds it to our webpage. 
        Automatically refreshes our webpage so that user can see the image appended
    """
    if(request.method=='POST'):

        if 'image_to_be_uploaded' not in request.files:
            return "no file found"

        uploaded_files = request.files['image_to_be_uploaded']
        filename = uploaded_files.filename
        uploaded_files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # How do we store images in our server?
        return redirect('/')

'''
END TASK 1
'''

if __name__ == '__main__':
   app.run(debug = True)