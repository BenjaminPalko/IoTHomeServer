from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

@app.route("/") # for null input
@app.route("/<user>")
def index(user="nothing"):
    return render_template("user.html", user=user)

@app.route("/objects") 
def objectPassing():
    objects = ["object1", "object2", "object3"]
    return render_template("objectList.html", objects = objects)

@app.route("/prototype")
def reactHTML():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)
# # @This is a decorator - wrap a function and modify its behavior
# @app.route("/prototype") #Mapped a URL to return vaule ex/prototype
# def prototype():
#     return 'This is to test Flask'

# # Passing username into parameter
# @app.route("/profile/<username>")
# def profile(username):
#     return "Hey there %s" % username

# # Checking method type of your browsing, usually GET when youre just running the URL
# @app.route("/methodType", methods=['GET', 'POST'])
# def methodType():
#     if request.method == 'POST':
#         return "You are using POST"
#     else:
#         return "You are using GET"