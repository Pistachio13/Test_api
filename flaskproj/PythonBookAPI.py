from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/PythonBook")
def my_python_book():
    return jsonify(Book_name="One-stop python",ISBN="978-616-207-772-5",price=225)

if __name__ == "__main__":
    app.run()