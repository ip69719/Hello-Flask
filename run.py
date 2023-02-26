import os
# import json library
import json
# import Flask class
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

# create instance and store it in a variable
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        """
        page_title variable used to display page title.
        <h2>{{ page_title }}</h2>
        set data on server-side and get it to come through onto the 
        client-side.

        company=data This is assigning a new variable called 'company'
        that will be sent through to the HTML template, which is equal to the
        list of data it's loading from the JSON file.
        """
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
# The angle brackets will pass in data from the URL path into the view below
def about_member(member_name):
    """
    When user clicks on the title, or the name of one of the characters, the
    function brings user to a page that displays more information about that
    character.
    """
    # This takes member_name from above as an argument
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
