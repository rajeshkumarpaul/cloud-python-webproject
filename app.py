from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id": 1,
        "title": "Think Python: How to Think Like a Computer Scientist 2nd Edition",
        "author": "Allen Downey",
        "status": "available"
    },
    {
        "id": 2,
        "title'": "Learning Pything, 5th Edition",
        "author": "Mark Lutx",
        "status": "available"
    },
    {
        "id": 3,
        "title'": "Python Cookbook, Third Edition",
        "author": "David Beazley",
        "status": "available"
    },
]

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Unable to find werkzeug.server.shutdown')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down'

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_title = request.form['title']
        new_author = request.form['author']
        new_status = request.form['status']
        new_id = books_list[-1]['id'] + 1

        new_book = {
            "id": new_id,
            "title'": new_title,
            "author": new_author,
            "status": new_status
        }

    books_list.append(new_book)
    return jsonify(books_list), 200

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8081, debug=True)


