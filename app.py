from flask import Flask, render_template, json, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to User Database</h1>'

with open('data.json') as f:
    user = json.load(f)

@app.route('/<username>')
def userdata(username):
    # print(data)
    for current_user in user:
        # print(current_user)
        if current_user['Name'] == username:
            print(current_user['Name']+' '+current_user['Age'])
            return render_template('userTemplate.html', name=current_user['Name'], age=current_user['Age'], city=current_user['City'])
    return render_template('noUser.html')

if __name__ == '__main__':
    app.run(debug=True)

