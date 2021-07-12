from flask import Blueprint, Response, request, jsonify,render_template, session
from flask_sqlalchemy import SQLAlchemy




simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/login')
def login():
    print(session["barcode"])
    return render_template("login.html")


@simple_page.route('/test')
def test():
    return render_template("test.html")


@simple_page.route('/add_barcode' ,methods = ["GET","POST"])
def add_barcode():
    if request.method == "POST":
        data = request.form
        
        print(data)
        return render_template("add_barcode.html")
    else:
        return render_template("add_barcode.html")




    # if me:
    #     pass
    #     pic = request.files['pic']
     

    #     img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    #     db.session.add(img)
    #     db.session.commit()

    # return 'Img Uploaded!', 200