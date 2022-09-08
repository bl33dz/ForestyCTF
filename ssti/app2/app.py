from flask import Flask, request, render_template_string

app = Flask(__name__)
app.config['SECRET_KEY'] = "ForestyCTF{ssti_is_easy_right?_ac2ae6}"

@app.route("/", methods=['GET', 'POST'])
def index():
    name = "Guest"
    if request.method == "POST":
        name = request.form.get('name')
    template = '<html><body>\
    <form action="/" method="post">\
      <label>Name:</label>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><p>Hello %s! </p></body></html>' % name
    return render_template_string(template)

if __name__=="__main__":
	app.run("0.0.0.0",port = 5000,debug=False)
