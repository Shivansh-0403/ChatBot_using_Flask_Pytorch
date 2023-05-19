@app.get("/")
def index_get():
    return render_template("base1.html")