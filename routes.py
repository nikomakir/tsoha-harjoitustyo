from flask import render_template, request, redirect
from app import app
import users
import stats
import places


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Tunnuksen tulee olla 1-20 merkkiä pitkä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat toisistaan")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli")

        if not users.register(username, password1, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

        return redirect("/")

@app.route("/search", methods=["GET"])
def search():
    query = request.form["query"]
    if len(query) < 1 or len(query) > 20:
        return render_template("error.html", message="Hakusanan tulee olla 1-20 merkkiä pitkä")

    result = stats.find_all_by_word(query)
    if not result:
        return render_template("error.html", message="Hakusanalla ei löytynyt tuloksia")

    return render_template("/search", places=result)

@app.route("/info/<int:place_id>")
def info(place_id):
    information = places.get_place_info(place_id)
    groups = places.get_groups(place_id)
    return render_template("info.html", name=information[0], groups=groups,
                           address=information[1], hours=information[3:],
                           description=information[2], id=place_id)

@app.route("/post_review/<int:place_id>", methods=["GET", "POST"])
def post_review(place_id):
    if request.method == "GET":
        users.require_role(1)
        return render_template("post_review.html", id=place_id)
    if request.method == "POST":
        users.require_role(1)
        users.check_csrf()

        stars = int(request.form["stars"])
        if stars < 1 or stars > 5:
            return render_template("error.html", message="Virheellinen tähtimäärä")

        comment = request.form["comment"]
        if len(comment) > 1000:
            return render_template("error.html", message="Liian pitkä kommentti")
        if comment == "":
            comment = "-"
        places.add_review(place_id, users.user_id(), stars, comment)
        return redirect("/reviews/"+str(place_id))

@app.route("/reviews/<int:place_id>")
def reviews(place_id):
    results = places.get_reviews(place_id)
    return render_template("reviews.html", reviews=results)

@app.route("/list")
def place_list():
    ranking = stats.place_rankings()
    return render_template("list.html", rankings=ranking)

@app.route("/add_place", methods=["GET", "POST"])
def add_place():
    if request.method == "GET":
        users.require_role(2)
        return render_template("add_place.html")

    if request.method == "POST":
        users.require_role(2)
        users.check_csrf()

        name = request.form["name"]
        if len(name) < 1 or len(name) > 20:
            return render_template("error.html", message="Nimen tulee olla 1-20 merkkiä pitkä")
        address = request.form["address"]
        if len(address) < 1 or len(address) > 20:
            return render_template("error.html", message="Osoite tulee olla 1-20 merkkiä pitkä")
        description = request.form["description"]
        if len(description) > 1000:
            return render_template("error.html", message="Kuvaus on liian pitkä")

        monday_hours = request.form["open_mon"] + "-" + request.form["close_mon"]
        tuesday_hours = request.form["open_tue"] + "-" + request.form["close_tue"]
        wednesday_hours = request.form["open_wed"] + "-" + request.form["close_wed"]
        thursday_hours = request.form["open_thu"] + "-" + request.form["close_thu"]
        friday_hours = request.form["open_fri"] + "-" + request.form["close_fri"]
        saturday_hours = request.form["open_sat"] + "-" + request.form["close_sat"]
        sunday_hours = request.form["open_sun"] + "-" + request.form["close_sun"]

        place_id = places.add_place(name, address, description, monday_hours, tuesday_hours,
                         wednesday_hours, thursday_hours, friday_hours,
                         saturday_hours, sunday_hours)

        return redirect("/info/"+str(place_id))

@app.route("/add_group", methods=["GET", "POST"])
def add_group():
    if request.method == "GET":
        users.require_role(2)
        return render_template("add_group.html")
    if request.method == "POST":
        users.require_role(2)
        users.check_csrf()
        group_name = request.form["groupname"]
        if len(group_name) < 1 or len(group_name) > 20:
            return render_template("error.html", message="Nimen pituus tulee olla 1-20 merkkiä")
        if not places.create_groupname(group_name):
            return render_template("error.html", message="Samanniminen ryhmä on jo olemassa")
        return redirect("/")
