from flask import Flask, request, render_template, redirect
from users import User
app = Flask(__name__)

@app.route('/users')
def index():
    users = User.get_all()
    return render_template('/users.html', all_users=users)

# Add new user
@app.route('/users/new')
def add_user():
    return render_template('/create_user.html')

@app.route('/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/users')

# Display user
@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id" : id
    }
    user = User.get_one_user(data)
    return render_template('/user.html',id=id, user=user[0])

# Update user
@app.route('/users/<int:id>/edit')
def edit_form(id):
    data = {
        "id" : id
    }
    user = User.get_one_user(data)
    return render_template('/edit.html', id=id, user=user[0])

@app.route('/update', methods=['POST'])
def edit():
    User.update(request.form)
    return redirect('/users')

# Delete user
@app.route('/users/<int:id>/delete')
def delete(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect('/users')

if __name__=='__main__':
    app.run(debug=True)