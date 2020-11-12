from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# 메인 홈페이지
@app.route('/')
def home():
    return render_template('band_prac.html')

# MENU-HOME
# @app.route('/', methods=['GET'])
# def goto_home_page():
#     return render_template("band_prac.html")

# 메인->악기
@app.route('/drum', methods=['GET'])
def show_drum_page():
    return render_template("band_drum.html")

@app.route('/piano', methods=['GET'])
def show_piano_page():
    return render_template("band_piano.html")

@app.route('/guitar', methods=['GET'])
def show_guitar_page():
    return render_template("band_guitar.html")

@app.route('/bass', methods=['GET'])
def show_bass_page():
    return render_template("band_bass.html")

@app.route('/vocal', methods=['GET'])
def show_vocal_page():
    return render_template("band_vocal.html")

@app.route('/band', methods=['GET'])
def show_band_page():
    return render_template("band_band.html")

# 영상 업로드 페이지
@app.route('/register_drum', methods=['GET'])
def register_drum_page():
    return render_template("video_regist.html")

@app.route('/register_piano', methods=['GET'])
def register_piano_page():
    return render_template("video_regist_piano.html")

@app.route('/register_guitar', methods=['GET'])
def register_guitar_page():
    return render_template("video_regist_guitar.html")

@app.route('/register_bass', methods=['GET'])
def register_bass_page():
    return render_template("video_regist_bass.html")

@app.route('/register_vocal', methods=['GET'])
def register_vocal_page():
    return render_template("video_regist_vocal.html")

@app.route('/register_band', methods=['GET'])
def register_band_page():
    return render_template("video_regist_band.html")




if __name__ == '__main__':
    app.run('127.0.0.1', port=5050, debug=True)