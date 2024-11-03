from flask import Flask,render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

#@app.route("/<username>")
#def hello_world(username):
    #return render_template("index.html", username=username)


@app.route("/<page>")
def portfolio(page):
    return render_template(page)

@app.route("/")
def home():
    return render_template("index.html")


# # #@app.route("/about.html")
# # def about():
# #     return render_template("about.html")

# # #@app.route("/contact.html")
# # def contact():
# #     return render_template("contact.html")

# # #@app.route("/works.html")
# # def works():
# #     return render_template("works.html")

# # #@app.route("/submit.html")
# def submit():
#     return render_template("submit.html")

# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route("/submit_form", methods= ["POST","GET"])
def asunmit():
    if request.method =="POST":
        data = request.form.to_dict()
        print(data)
        add_data_csv(data)
        return redirect("submit.html")    
    else:
        return "better luck next time"


def add_data(data):
    with open("database.txt", mode="a") as fy:
     email = data["email"]
     subject= data["subject"]
     message= data["message"]
     fy.write(f"Email-{email} \nSubject-{subject} \nMessage-{message}\n\n")

def add_data_csv(data):
    with open("database2.csv", mode="a",newline= "") as fy:
     email = data["email"]
     subject= data["subject"]
     message= data["message"]
     csv_writer = csv.writer(fy)
     csv_writer.writerow([email,subject,message])





