
from flask import Flask, abort, redirect, render_template, request, session, url_for
from werkzeug import exceptions as Err
from tinydb import TinyDB, Query

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0;
app.config["SECRET_KEY"] = "192b9bdd22ab9ed4d12e236123456FE9993ec15f71bbf5dc987d54727823bcbf"
print("MODE: -> ", app.config["ENV"])

userDB = TinyDB("db.json");
USER = Query();
test_data = {
	"name" : "Tochukwu Gakudi",
	"phoneNo" : "+2348012345678",
	"password" : "gakudi"
}

# Conditionally inserts test data.
if not userDB.get(USER.phoneNo == test_data["phoneNo"]):
	userDB.insert(test_data);

# Prevent Caching
@app.after_request
def add_header(r):
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r

# Setup a default error handler
@app.errorhandler(Err.NotFound)
def handle_bad_request(e):
	# return 'Page not found!', 404
	print("e: -> ", e);
	# va = e
	return render_template("error/404.html", prev_page = request.referrer), 404


# Root route
@app.route("/")
def hello_world():
	print("hey!!!")
	if 'userID' in session:
		return redirect(url_for("dashboard"));
	else:
		return redirect(url_for("user_login"));

	# return "<p>Hello, World!</p>"


@app.route('/dashboard')
def dashboard():
	if 'userID' not in session:
		return redirect(url_for("user_login"));
	else:
		user = userDB.get(USER.phoneNo == session.get("userID"));
		user["userID"] = session.get("userID");
		return render_template("dashboard.html", user = user);


@app.route('/login', methods = ['GET', 'POST'])
def user_login():
	has_session = "userID" in session;

	if has_session: return redirect(url_for("dashboard"));

	if request.method == 'POST':
		user_no = request.form.get('phone_no');
		user_pass = request.form.get('passwd');
		# print(userDB.get(USER.phoneNo == user_no));
		# print(userDB.get(USER.password == user_pass));
		if userDB.get(USER.phoneNo == user_no) and userDB.get(USER.password == user_pass) :
			session["userID"] = user_no;
			return redirect(url_for("dashboard"));
		else:
			return render_template("sign_in.html");
	elif request.method == 'GET':
		return render_template("sign_in.html");
	else:
		abort(404);

# The application also contains a logout () view function that pops up the 'username' session variable.
# Therefore, the ' /' URL displays the start page again.

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('userID', None)
   return redirect(url_for('hello_world'));


@app.route('/product/add')
def add_product():
	return "add product";


@app.route('/api/v1/product/<link>')
def product_link(link):
	return 'Product Detail For' + link;


@app.route('/store')
def product_store():
	has_session = "userID" in session;

	if not has_session: return redirect(url_for("user_login"));



	
@app.route('/signup')
def create_user():
	return "Sign Up Page";




if __name__ == '__main__':
	app.run(port=5000)
