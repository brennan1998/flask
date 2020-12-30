from flask import Flask,render_template,url_for , redirect, request
import requests


app = Flask(__name__)
app.config["DEBUG"] = True



@app.route("/")
def show_landing_page():
    name_length = len("brennan")
    return render_template("landing-page.html",name ="brennan", name_length= name_length)
@app.route("/search" , methods = ['POST'])
def search():
    return render_template("search-result.html")

@app.route("/error")
def show_error_page():
    return render_template("error404.html")

@app.route("/search", methods= ['POST'])
def form_submit():
    # User request has a form in it (search query is from the name of landing-page.html)
    user_query = request.form['search_query']
    
    #looking for the url where the function search_imdb is located at 
    redirect_url = url_for('.search_imdb', query_string = user_query)
    return redirect(redirect_url)

@app.route("/search/<query_string>", methods=['GET'])
def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q": query_string}

    headers = {
        'x-rapidapi-key': "7406ce2570msh2cdf4c78aab3a28p12fc39jsn3be65634f33e",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template("search-result.html")
    except:
        return render_template("error404.html", data=data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "5001")