from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def show_landing_page():
    return render_template("landing-page.html")

@app.route("/search", methods=['POST'])
def form_submit():
    #request is to receive input from the user
    user_query = request.form['search_query'] # matches name attribute of query string input (HTML)
    redirect_url = url_for('.search_imdb', query_string=user_query)  # match search_imdb function name (Python flask)
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

        #requests is to call an api 
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template("search-result.html", data=data)
    except:
        return render_template("error404.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")