from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    collection.insert_one({
        "name": item_name,
        "description": item_desc
    })

    return "Item saved successfully"

if __name__ == "__main__":
    app.run(debug=True)