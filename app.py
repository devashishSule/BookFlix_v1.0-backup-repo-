from flask import Flask, render_template, request, url_for, redirect, session, g, jsonify
import os
from connect import *
from flask_mail import Mail,Message
import openai
import pickle

popular_df = pickle.load(open('popular.pkl','rb'))

API_KEY = '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'
openai.api_key = API_KEY
model='text-davinci-003'



app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sule.devashish@gmail.com'
app.config['MAIL_PASSWORD'] = 'eifqhvywfhnhenkb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db = client.BookFlix_db
user_info = db.user_info
user_pref = db.user_preferences

@app.route('/')
def index():
    return render_template('index.html')
     

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        # security_question = request.form['security']
        if firstName and lastName and email and username and password1 and password2 and password1 == password2:
    
                user_info.insert_one({
                    'firstName':firstName, 
                    'lastName':lastName,
                    'username':username, 
                    'email':email,
                    'password':password1
                    # 'security_question':security_question
                })
                msg = Message(
                    "BookFlix - Acknowledgement letter (Notification)",
                    sender='BookFlix.',
                    recipients=[email]
                )
                msg.body = "Thank You for creating an account in BookFlix. We will keep you updated."
                mail.send(msg)
                out_message = "Registration Successful."
                return jsonify({'message':out_message})
        else:
            return jsonify({'error':'Error Occured!!'})
            
    all_info = user_info.find()
    return render_template('./user/Actions/register.html', user_info=all_info)

@app.route('/login', methods=('GET', 'POST') )
def login():
    if request.method == "GET":
        session.pop('user',None)
        
    if request.method == "POST":
        session.pop('user',None)
        user_verification = user_info.find_one({
            'username':request.form['username'],
            'password':request.form['password']
        })
        # print(user_verification)
        if user_verification != None:
            session['user'] = request.form['username']
            return jsonify({'status':'/user_dashboard'})
        else:
            return jsonify({'error':'Error Occured!!'})
        
    return render_template('./user/Actions/login.html')               

@app.route('/user_dashboard', methods=('GET', 'POST'))
def user_dashboard():
   
        if g.user:
            user_data = user_info.find_one({
                'username':session['user']
            })
            if request.method == "POST":
                subject_info = user_pref.find_one({
                    'Course':request.form['Course'],
                    'Year':request.form['Year'],
                    'Semester':request.form['Semester']
                })
                # print(subject_info)
                subject = subject_info["Subjects"].split(', ')
                print(subject[0])
                print(subject[1])
                print(subject[2])
                print(subject[3])
                print(subject[4])
                response_from_db = [subject[0], subject[1], subject[2], subject[3], subject[4]]
                return jsonify({'answer':response_from_db})
                # all_info = user_pref.find()
            return render_template('./user/Dashboard/user/user_dashboard.html', 
                                   book_name = list(popular_df['Name of books'].values),
                                   book_author = list(popular_df['Author'].values),
                                   book_image = list(popular_df['Image-URL'].values),
                                   book_ratings = list(popular_df['Average ratings'].values),
                                   user = user_data)
        return redirect(url_for('index')) 
        
        

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
        
@app.route('/dropsession')
def dropsession():
    session.pop('user',None)
    return redirect('/')

@app.route('/forgetPassword', methods=('GET','POST'))
def forgetPassword():
    if request.method == "POST":
        verify_mail = user_info.find_one({
            'email':request.form['email']
        })
        print(verify_mail)
        email = verify_mail["email"]
        firstName = verify_mail["firstName"]
        username = verify_mail["username"]
        password = verify_mail["password"]
        # recovery = verify_mail["security_question"]
        # # print(recovery)
        
        msg = Message(
            "BookFlix - Recovery of Account (Alert)",
            sender='BookFlix.',
            recipients=[email]
        )
        msg.body = "Hello "+ firstName +",\n" + "username: " + username + "\n" + "password: " + password
        mail.send(msg)
         
    return render_template('./user/Actions/forgetPassword.html')

@app.route('/user_dashboard/chatbot', methods=('GET','POST'))
def chatbot():
   
   if request.method=="POST":
        question = request.form['question']
 
        response = openai.Completion.create(
            prompt=question,
            model=model,
            max_tokens = 2024,  
            temperature = 0,
            top_p=1,
            
        )
        
        # print(response)
        return jsonify({'answer':response})
   return render_template('./user/Actions/chatbot.html')
    


if __name__ == "__main__":
    app.run(debug=True)
    

