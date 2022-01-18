from cgitb import html
from flask import Flask
from data import pets

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Adopt a Pet!</h1>
                <p>Browse through the links below to find your new furry friend:</p>
                <ul>
                    <li><a href="/animals/dogs">Dogs</a></li>
                    <li><a href="/animals/cats">Cats</a></li>
                    <li><a href="/animals/rabbits">Rabbits</a></li>
                </ul>
            """

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = "<h1>List of {}</h1>".format(pet_type)
    html += "<ul>"

    count = 0
    for pet in pets[pet_type]:
        count = count+1
        html += "<li><a href=/animals/{}/{}>{n}</a> </li>".format(pet_type,count,n = pet["name"])

    html += "</ul>"


    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    
    pet_id = pet_id -1
    pet = pets [pet_type][pet_id]

    print ("{}", pet)
    return  '<h1> {} </h1> <br> <img src={} alt{}> <p>{}</p> <ul> <li>Breed: {} </li> <li>Age: {} </li>'.format(pet["name"],pet["url"],pet["name"], pet["description"], pet["breed"], pet["age"])

if __name__ == "__main__":
    app.run()