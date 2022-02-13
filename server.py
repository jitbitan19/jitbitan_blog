from flask import Flask, render_template, request
import requests
import smtplib

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", data_list=data)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact_page():
    if request.method == "POST":
        user_data = request.form
        print(user_data["user_name"])
        print(user_data["user_email"])
        print(user_data["user_ph"])
        print(user_data["user_msg"])

        def send_email(data):
            with smtplib.SMTP("smtp.google.com") as connection:
                connection.starttls()
                connection.login(
                    user="forlearningpython3@gmail.com",
                    password="Jitbitan19@"
                )
                connection.sendmail(
                    from_addr="forlearningpython3@gmail.com",
                    to_addrs="privatespace.n19@gmail.com",
                    msg=f"Subject: New User on our blog page\n\n"
                        f"Name: {data[0]}\n"
                        f"Email: {data[1]}\n"
                        f"Phone No.: {data[2]}\n"
                        f"Message: {data[3]}"
                )

        send_email(user_data)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post_id=<post_id>')
def posts(post_id):
    return render_template("post.html", post=data[int(post_id) - 1])


@app.route('/testing')
def html_forms():
    return render_template("form.html")


@app.route('/form-entry', methods=["POST"])
def receive_data():
    name = request.form["user_name"]
    email = request.form["user_email"]
    ph_no = request.form["user_ph"]
    msg = request.form["user_msg"]

    return "<h1>Submitted</h1>"


# @app.route('/login', methods=["POST"])
# def receive_data():
#     username = request.form["username"]
#     password = request.form["password"]
#     return f"<h1>Username: {username}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
