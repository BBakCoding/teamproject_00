from flask import Flask, render_template, send_file, request, jsonify
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.myproject

app = Flask('__name__')

# HTML을 불러온다.


@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/loginpage')
def Loginpage():
    return render_template('Login.html')


@app.route('/signup')
def Loginpage():
    return render_template('Login.html')

# join_us(POST) API


@app.route('/signup', methods=['POST'])
def save_info():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    pass_receive = request.form['pass_give']

    # if "" not in name_receive:
    #     return jsonify({'msg': '이름을 입력해주세요.})

    if "@" not in email_receive:
        return jsonify({'msg': '이메일을 입력해주세요.'})

    elif not (email_receive and pass_receive):
        return jsonify({'msg': '모두 입력해주세요'})

    elif '.' not in email_receive:
        return jsonify({'msg': '이메일을 완성해주세요'})

    # 위의 과정을 전부 정상으로 받아들여졌을때 서버에 저장
    else:
        doc = {
            'name': name_receive,
            'email': email_receive,
            'password': pass_receive
        }
    db.project01.insert_one(doc)
    return jsonify({'msg': '회원가입이 완료 되었습니다.'})

# login API


@app.route('/login', methods=['POST'])
def login():
    user_email_receive = request.form['user_email_give']
    user_pass_receive = request.form['user_pass_give']
    user_data = list(db.project01.find({}, {'_id': False}))

    if "@" and "." not in user_email_receive:
        return jsonify({"msg": "이메일을 확인해주세요"})
    elif not user_email_receive and user_pass_receive:
        return jsonify({'msg': '모두 입력해주세요'})
    else:
        for user in user_data:
            if user_email_receive == user['email'] and user_pass_receive == user['password']:
                return jsonify({'msg': '환영합니다.'})
            elif user_email_receive != user['email'] and user_pass_receive != user['password']:
                return jsonify({'msg': '입력하신 정보를 확인해주세요.'})
            elif user_email_receive == user['email'] and user_pass_receive != user['password']:
                return jsonify({'msg': '입력하신 정보를 확인해주세요.'})
            # elif user_email_receive != user['email'] and user_pass_receive == user['password']:
            #     return jsonify({'msg':'입력하신 정보를 확인해주세요.'})


if '__name__' == '__main__':
    app.run()
app.run(host='0.0.0.0', port=5000)
