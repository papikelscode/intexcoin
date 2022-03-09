
from flask import Flask, render_template, request, redirect, url_for,jsonify
# from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from werkzeug.security  import generate_password_hash, check_password_hash
from  flask_login import UserMixin, LoginManager, login_required, login_user, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os
#from flask_migrate import Migrate, MigrateCommand
#from flask_script import Manager
#from sys import argv

from flask_mail import Mail
from random import randint
from datetime import datetime
#from flask_marshmallow import Marshmallow







#Position all of this after the db and app have been initialised


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname((__file__)))
database = "app.db"
con = sqlite3.connect(os.path.join(basedir,database))
mail = Mail(app)
app.config['SECRET_KEY'] = "jhkxhiuydu"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['MAIL_SERVER'] = 'intexcoin.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'info@intexcoin.com'
app.config['MAIL_SERVER'] = 'server148.web-hosting.com'

db = SQLAlchemy(app)

#migrate = Migrate(app, db,render_as_batch=True)
#manager = Manager(app)
#manager.add_command('db', MigrateCommand)




class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    fullname = db.Column(db.String(500))
    password = db.Column(db.String(500))
    userwallet = db.Column(db.String(500),unique=True)
    balance = db.Column(db.Integer,default=000)
    profit = db.Column(db.Integer,default=000)
    referID = db.Column(db.String(500),unique=True)
    verified = db.Column(db.Boolean,default=False)
    transactions = db.relationship('Transactions', backref='users', lazy=True)
    payments = db.relationship('Payments', backref='users', lazy=True)


    def check_password(self, password):
        return check_password_hash(self.password, password)
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')


    def create(self, username='',  email='', fullname='', password='',referID=''):
        self.username	 = username
        self.email	 = email
        self.fullname 	 = fullname
        self.referID = referID
        self.password= generate_password_hash(password, method='sha256')


    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()


class Payments(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    paymentID = db.Column(db.String(500),unique=True)
    confirm = db.Column(db.Boolean,default=False)
    paymentwallet = db.Column(db.String(500))
    user = db.Column(db.Integer, db.ForeignKey(Users.id))





class Plan(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(255))
    plan_price = db.Column(db.String(255))
    plan_roi = db.Column(db.String(255))
    plan_rate = db.Column(db.String(255))
    isDanger = db.Column(db.Boolean,default=False)
    IsActive = db.Column(db.Boolean,default=False)
    isWarning = db.Column(db.Boolean,default=False)
    iSpricing = db.Column(db.Boolean,default=False)




class Subscription(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    paymentID = db.Column(db.String(500))
    confirm = db.Column(db.Boolean,default=False)
    users = db.Column(db.Integer)
    plan = db.Column(db.String(255))
    plan_price = db.Column(db.String(255))
    plan_roi = db.Column(db.String(255))
    plan_rate = db.Column(db.String(255))





class Transactions(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    txtype = db.Column(db.String(255))
    cost = db.Column(db.String(255))
    timestamp = db.Column(db.String(255),default=datetime.now())
    user = db.Column(db.Integer, db.ForeignKey(Users.id))




class Settings(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    walletName = db.Column(db.String(255), unique=True)
    walletaddress = db.Column(db.String(255), unique=True)

class Market(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    coinname = db.Column(db.String(255), unique=True)
    types    =   db.Column(db.String(255))



    
admin = Admin(app, name='administration', template_mode='bootstrap3')
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Settings, db.session))
admin.add_view(ModelView(Subscription, db.session))
admin.add_view(ModelView(Transactions, db.session))
admin.add_view(ModelView(Plan, db.session))
admin.add_view(ModelView(Market,db.session))



    



login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(app)
@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(user_id)

    

    







@app.route('/')
def index():
    plans = Plan.query.all()
    activeusers = randint(576, 6899)
    return render_template('index.html',plans=plans,activeusers=activeusers)

@app.route("/dashboard")
@login_required
def dashboard():
    siteSettings = Settings.query.all()
    userplan = Subscription.query.filter_by(users=current_user.id).all()
    txs = Transactions.query.filter_by(user=current_user.id).all()
    plan = Plan.query.all()
    total = current_user.profit + current_user.balance
    markets = Market.query.all()
    return render_template('dashboard.html',
                                siteSettings=siteSettings,
                                userplan=userplan,
                                txs=txs,
                                plan=plan,
                                total=total,
                                markets=markets)

@app.route("/withdraw",methods=['GET'])
def withdraw():
    if current_user.userwallet == None:
        return jsonify({'status':404,'msg':"You haven't set your withdrawal wallet, click wallet to set it and try again"})

    return jsonify({'status':200,'msg':"Your withdraw request has been sent, you will recieve your payment shortly, Thanks for investing with us"})

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/call.html")
def call():
    return render_template("call.html")
    
@app.route("/contactus")
def contact():
    return "Comming soon"

@app.route("/account")
def account():
    return render_template("/account.html")
    
@app.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    siteSettings = Settings.query.all()
    return render_template('profile.html',siteSettings=siteSettings)




@app.route("/signin",methods=['GET','POST'])
def signin():
    users = Users()
    if request.method == "POST":
        data = request.json
        userByusername = users.query.filter_by(username=data['username']).first()
        userByemail = users.query.filter_by(email=data['username']).first()
        mainUser = None
        if userByusername:
            mainUser = userByusername
        if userByemail:
            mainUser = userByemail
        if mainUser:
            if mainUser.check_password(data['password']):
                login_user(mainUser,remember=True,fresh=True)
                return jsonify({'status':200,'msg':'user authenticated'})
            return jsonify({"status":404,"msg":"Inavlid password provided!!!"})
        return jsonify({"status":404,"msg":"invalid email or username"})

    return render_template("signin.html")


@app.route("/signup",methods=['GET','POST'])
def signup():
    users = Users()
    if request.method == 'POST':
        data = request.json
        username = data['username']
        email = data['email']
        fname = data['fname']
        password = data['password']
        if users.query.filter_by(username=username).first():
            return jsonify({"status":404,"msg":"username already exist!!!"})
        if users.query.filter_by(email=email).first():
            return jsonify({"status":404,"msg":"email already exist!!!"})
        users.create(username=username,
                            email=email,
                            fullname=fname,
                            password=password,
                            referID=randint(456463276,7656562565))
        users.save()

        login_user(users)
        # return redirect(url_for("dashboard"))
        return jsonify({'status':200,"msg":"registration compelete!!!"})

    return render_template("signup.html")



@app.route("/subscribe",methods=['POST'])
@login_required
def subscribe():
    data = request.json
    print(data)
    userplan = Plan.query.filter_by(plan=data['plan']).first()
    new_subscription = Subscription(
            users=current_user.id,
            plan = userplan.plan,
            plan_price = userplan.plan_price,
            plan_roi = userplan.plan_roi,
            plan_rate = userplan.plan_rate)
    if current_user.balance < int(userplan.plan_price):
        return jsonify({'status':200,'msg':'insufficient balance.'})


    current_user.balance -= int(userplan.plan_price)
    new_transaction = Transactions(cost=userplan.plan_price,
                                        user=current_user.id,
                                        description='investment of '+str(userplan.plan_price),
                                        txtype='investment')
    db.session.add(new_transaction)
    db.session.add(new_subscription)
    db.session.commit()
    return jsonify({'status':200,'msg':'Your plan will be updated on your dashbaord as soon as we confirm your payment on the network, Thanks for investing with us.'})

@app.route('/payments',methods=['POST'])
def makepayment():
    data = request.json
    if Payments.query.filter_by(paymentID=data['paymentID']).first():
        return jsonify({'status':404,'msg':'payment already exist'})
    new_payment = Payments(
        paymentID=data['paymentID'],
        user = current_user.id,
        paymentwallet=data['walletid'])
    new_transaction = Transactions(description='Account funding',
                                    txtype='Payment Deposit',
                                    user=current_user.id)
    db.session.add(new_transaction)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'status':200,'msg':'payement submmited'})


@app.route('/addwallet',methods=['POST'])
def addwallet():
    da = request.json
    print(da)    
    current_user.userwallet = str(da['wallet'])
    db.session.commit()
    return jsonify({'status':200,'msg':'wallet added to your account'})

@app.route("/updatepassword",methods=['POST'])
def updatepassword():
    data = request.json
    if check_password_hash(current_user.password,data['currentpassword']):
        current_user.password = data['newpassword']
        Users.commit()
        return jsonify({'status':200,'msg':'password reset complete'})
    return jsonify({'status':404,'msg':'password not match'})
@app.route("/verify",methods=['POST'])
def verify():
    request.files['file']
    current_user.verified = True
    db.session.commit()
    return redirect(url_for('dashboard'))



@app.route('/markrttype/<types>')
def market_type(types):
    print(len(types))
    mk = Market.query.filter_by(types=types).all()
    coin = []
    for i in mk:
        coin.append(i.coinname)

    return jsonify(coin)




@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("signin"))

@app.route("/db")
def database():
    db.drop_all()
    db.create_all()
    return "Hello done!!!"
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
# if __name__ == '__main__':
#     manager.run()
#     app.run(host='127.0.0.1', port=8050, debug=True)
 
