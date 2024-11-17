from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.Add_Zimmer import Add_Zimmer
from models.Delete_Zimmer import Delete_Zimmer
from models.Get_All_Zimmers import get_all_zimers
from models.Get_LandLords import get_LandLords
from models.Get_Zimmer_by_Land_name import get_all_zimers_by_land_name
from models.Login import Is_landLord
from models.Specific_Zimmer import specific_Zimmer
from models.Update_Zimmer import Update_Zimmer
from models.sorting_functions.sorting_Zimmers import sort_by_name_zim, sort_by_Location, sort_by_price_asc, sort_by_price_desc
from models.sorting_functions.sorting_landlords import sort_by_name_Land, sort_by_Phone_Land

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='Template')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Login Page - Route and function
@app.route('/Login.html')
def login():
    return render_template('Login.html')  # Assuming you have a login.html template

# Handling Login Form Submission
@app.route('/Login.html', methods=['POST'])
def login_post():
    name_land = request.form['username']
    password = request.form['password']

    if Is_landLord(name_land, password):
        # Store the username in session and mark it as permanent
        session['User_name'] = name_land
        session.permanent = True
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password. Please try again.', 'error')
        return render_template('Login.html')

# The Home Page
@app.route('/', methods=['GET', 'POST'])
def root():
    session.pop('User_name', None)
    if request.method == 'POST' and 'logout' in request.form:
        session.pop('User_name', None)
    zimers_list = get_all_zimers()
    user_name = session.get('User_name', None)
    return render_template('index.html', zimers_list=zimers_list, user_name=user_name)

@app.route('/index.html')
def home():
    zimers_list = get_all_zimers()
    user_name = session.get('User_name', None)
    return render_template('index.html', zimers_list=zimers_list, user_name=user_name)


# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# The about page
@app.route('/about.html')
def page_about():
    LandLords = get_LandLords()

    return render_template('about.html', Land_list=LandLords)


# The add-Zimmer page
@app.route('/add-Zimmer.html', methods=['GET', 'POST'])
def add_zimmer():
    if request.method == 'POST':

        NameZim = request.form['NameZim']
        LocationZim = request.form['LocationZim']
        Area = request.form['Area']
        IsPool = request.form['IsPool']
        IsJacuzzi = request.form['IsJacuzzi']
        MidweekPrice = request.form['MidweekPrice']
        EndWeekPrice = request.form['EndWeekPrice']
        TypeZim = request.form['TypeZim']
        NumRoom = request.form['NumRoom']
        GeneralSpecific = request.form['GeneralSpecific']
        PhoneLand = request.form['PhoneLand']
        NameLand = request.form['NameLand']
        EmailLand = request.form['EmailLand']
        ImageURL = request.form['ImageURL']


        Add_Zimmer(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, PhoneLand, NameLand, EmailLand)

        return redirect(url_for('root'))

    return render_template('add-Zimmer.html')

# The account page
@app.route('/account.html', methods=['GET', 'POST'])
def account():
    if request.method == 'GET':
        if 'User_name' in session:
            user_name = session['User_name']
            user_zimers = get_all_zimers_by_land_name(user_name)
            return render_template('account.html', user_name=user_name, user_zimers=user_zimers)
        else:
            flash('Please log in to access your account.', 'error')
            return redirect(url_for('login'))
    else:
        if 'User_name' in session:
            zimmer_name = request.form.get('zimmer_name')
            if zimmer_name:
                Delete_Zimmer(zimmer_name)
                flash('Zimmer deleted successfully!', 'success')
            else:
                flash('Zimmer name not provided.', 'error')
        else:
            flash('Please log in to delete a Zimmer.', 'error')
        return redirect(url_for('account'))


@app.route('/Update.html', methods=['GET', 'POST'])
def update_zimmer():
    if request.method == 'POST':
        NameZim = request.form['NameZim']
        LocationZim = request.form['LocationZim']
        Area = request.form['Area']
        IsPool = request.form['IsPool']
        IsJacuzzi = request.form['IsJacuzzi']
        MidweekPrice = request.form['MidweekPrice']
        EndWeekPrice = request.form['EndWeekPrice']
        TypeZim = request.form['TypeZim']
        NumRoom = request.form['NumRoom']
        GeneralSpecific = request.form['GeneralSpecific']
        ImageURL = request.form['ImageURL']
        NameZimmer = request.form['NameZimmer']

        Update_Zimmer(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, ImageURL, NameZimmer)

        return redirect(url_for('account'))

    return render_template('Update.html')


# The property-agents page
@app.route('/property-agent.html')
def landLords():
    try:
        name_Land = request.args.get('nameLand')
        Phone_Land = request.args.get('PhoneLand')

        if name_Land:
            LandLords = sort_by_name_Land(name_Land)
        elif Phone_Land:
            LandLords = sort_by_Phone_Land(Phone_Land)
        else:
            LandLords = get_LandLords()

        return render_template('property-agent.html', Land_list=LandLords)
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred", 500



# The property-list page
@app.route('/property-list.html', methods=['GET'])
def property_list():
    try:
        name_zim = request.args.get('nameZim')
        area = request.args.get('area')
        price_order = request.args.get('priceOrder')

        if name_zim:
            zimers = sort_by_name_zim(name_zim)
        elif area and area != "choose Area":
            zimers = sort_by_Location(area)
        elif price_order and price_order != "search by price":
            if price_order == 'asc':
                zimers = sort_by_price_asc()
            else:
                zimers = sort_by_price_desc()
        else:
            zimers = get_all_zimers()

        print(f"zimers: {zimers}")  # הדפסת הצימרים ללוגים
        return render_template('property-list.html', zimers_list=zimers)
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred", 500

@app.route('/zimmer/<int:id>', methods=['GET'])
def Specific_Zimmer_By_ID(id):
    try:
        zimer = specific_Zimmer(id)  # פונקציה שתשלוף את הצימר מהמסד נתונים לפי id
        if zimer:
            return render_template('Specific_Zimmer.html', zimer=zimer)
        else:
            return "Zimmer not found", 404
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred", 500


# The property-type page
@app.route('/property-type.html')
def teacher_post_fun_task():
    return render_template('property-type.html')

if __name__ == '__main__':
    app.run(port=2024, debug=True)
