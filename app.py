
from distutils.log import set_verbosity
import time
from flask import Flask, abort, jsonify, redirect, render_template, request, session, url_for
from werkzeug import exceptions as Err
from tinydb import TinyDB, Query
from tinydb.operations import add
from utilities import convertImageToBase64Blob
import uuid

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0;
app.config["SECRET_KEY"] = "192b9bdd22ab9ed4d12e236123456FE9993ec15f71bbf5dc987d54727823bcbf"
print("MODE: -> ", app.config["ENV"])

userDB = TinyDB("db.json");
USER = Query();

storeDB = TinyDB("store_db.json");
PRODUCT = Query();

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
		return render_template("hello_world.html");


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
   session.pop('userID', None);
   return redirect(url_for('hello_world'));


@app.route('/product/add', methods=['POST', 'GET'])
def add_product():
	has_session = "userID" in session;

	if not has_session: return redirect(url_for("user_login"));

	if request.method == 'POST':
		user_store_object = {}
		product_object = {};

		product_object["name"] = request.form.get("product_name");
		product_object["description"] = request.form.get("product_desc");
		product_object["price"] = request.form.get("product_price");
		product_object["imageBlob"] = convertImageToBase64Blob(request.files["product_image"].stream);
		product_object["productID"] = str(uuid.uuid4());
		product_object["timestamp"] = time.time();
		product_object["ownerID"] = session.get("userID");
		# product_object["paymentLink"] = ();


		# user_store_object["ownerID"] = session.get("userID");
		# user_store_object["products"] = [product_object];

		storeDB.insert( product_object );
		print("========= Product Added!! successfully!! ==========");
		link = product_object["productID"];
		# return redirect(url_for('product_store'));
		return render_template("product_success.html", link = link );

	elif request.method == "GET":
		return render_template("add_product.html");


@app.route('/product/<productID>')
def product_detail(productID):

	product_detail = storeDB.get(PRODUCT.ownerID == session.get("userID") and PRODUCT.entryID == productID);
	return jsonify(product_detail);
	

@app.route('/instapay/<link>')
def product_instapay(link):
	return 'Product Detail For' + link;


@app.route('/store', methods=['GET'])
def product_store():
	has_session = "userID" in session;

	if request.method == 'GET':
		if not has_session: return redirect(url_for("user_login"));

		user_store = storeDB.search(PRODUCT.ownerID == session.get("userID"));
		print("Product ======> ", user_store)
		return render_template("product_store.html", user_store = user_store);
	else:
		abort(404);


@app.route('/signup', methods = ['POST', 'GET'])
def create_user():
	if request.method == "POST":
		userID = request.form.get("phone_no");
		user_passwd = request.form.get("passwd");
		user_passwd_conf = request.form.get("passwd_confirm");

		if user_passwd != user_passwd_conf:
			return render_template("sign_up.html");
		if userDB.get(USER.phoneNo == userID):
			return render_template("sign_up.html");
		else:

			# accountDetails = createNewUserAndVirtualAccount();

			userDB.insert( {
				"id" : str(uuid.uuid4()),
				"phoneNo" : userID,
				"passwd" : user_passwd
				"balance" : 0,
				# "walletAddress" : accountDetails;
			} );

			session["userID"] = userID;
			return redirect(url_for('dashboard'));
	elif request.method == "GET":
		return render_template("sign_up.html");
	else:
		abort(404);
	# return "Sign Up Page";


@app.route('/sell', methods=['POST', 'GET'])
def sell():
	print(url_for("dashboard"), "=====referrer====", request.referrer.split("/")[-1].strip())
	has_session = "userID" in session;
	if not has_session: return redirect(url_for("user_login"));

	if request.method == "GET" and '/' + request.referrer.split("/")[-1].strip() == url_for("dashboard"):
		return render_template("sell_modal.html");
	else:
		abort(404);


@app.route('/send', methods=[ 'GET'])
def send_money():
	has_session = "userID" in session;
	if not has_session: return redirect(url_for("user_login"));

	if request.method == "GET":
		return render_template("send_money.html");
	else:
		abort(404);

@app.route('/transfer', methods=[ 'GET'])
def wallet_funds_transfer():
	has_session = "userID" in session;
	if not has_session: return redirect(url_for("user_login"));

	if request.method == "GET":
		return render_template("wallet_funds_transfer.html");
	else:
		abort(404);


@app.route('/wallet_to_wallet', methods=['POST'])
def wallet_to_wallet_transfer():
	has_session = "userID" in session;
	if not has_session: return redirect(url_for("user_login"));

	if request.method == "POST":
		try:
			phone_number_as_account_number = request.form.get("telephone");
			amount_to_send = float(request.form.get("amount"));

			sender = userDB.get(USER.phoneNo == session.get("userID"));
			# if sender.get("")

		except:
			abort(404)
	if request.method == "GET":




if __name__ == '__main__':
	app.run(port=5000)
