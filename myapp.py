from flask import Flask, render_template;

app = Flask(__name__)

@app.route("/index")
def home():
	# Looping
	hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
	# Conditional
	ujian = "lulus" # Jika lulus saya akan senang, jika tidak lulus saya sedih
	return render_template("index.html", hari=hari, ujian=ujian)

	if __name__ == "__main__":
		app.run(debug=True)