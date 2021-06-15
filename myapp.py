from flask import Flask;

app = Flask(__name__)

@app.route("/index")
def home():
	return "Halo ini raffli"

	if __name__ == "__main__":
		app.run(debug=True)