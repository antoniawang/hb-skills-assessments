from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application_page():
    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application():
	last_name = request.form.get("lastname")
	first_name = request.form.get("firstname")
	min_salary = request.form.get("salary")
	job_title = request.form.get("position")
	return render_template("application.html",
    	lastname=last_name, firstname=first_name, salary=min_salary, position=job_title)


if __name__ == "__main__":
    app.run(debug=True)