import os
from flask import Flask, request, render_template
import cv2
from numpy import outer
from effects import Effect
from PIL import Image
from base64 import encodebytes
from flask import send_file
import zipfile


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'database/')    
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)  # Storing the input image in database folder

        # Reading the input image and applying the transformation
        img = cv2.imread(f'./database/{filename}', 1)
        filter = Effect(img)
        f1 = filter.Sepia()
        f2 = filter.HDR()
        f3 = filter.Summer()
        f4 = filter.Winter()
        f5 = filter.Dark()
        f6 = filter.Sharp()
        
        # Storing the output filtered images in output folder
        cv2.imwrite('./output/Sepia.jpg', f1)
        cv2.imwrite('./output/HDR.jpg', f2)
        cv2.imwrite('./output/Summer.jpg', f3)
        cv2.imwrite('./output/Winter.jpg', f4)
        cv2.imwrite('./output/Dark.jpg', f5)
        cv2.imwrite('./output/Sharp.jpg', f6)
        
        # Zip of the output images
        zipf = zipfile.ZipFile('./Name.zip','w', zipfile.ZIP_DEFLATED)
        for root,dirs, files in os.walk('./output/'):
            for file in files:
                zipf.write('./output/'+file)     
        zipf.close()
        
        return send_file('./Name.zip',
            mimetype = 'zip',
            attachment_filename= 'Name.zip',
            as_attachment = True)


if __name__ == "__main__":
    app.run(port=4559, debug=True)
