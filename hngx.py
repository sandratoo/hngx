from flask import Flask,jsonify,request
import datetime

app = Flask(__name__)

@app.route('/details/', methods=['GET'])
def get_details():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    day = 'Saturday'
    utc_time = datetime.datetime.now()
    file_URL = 'https://github.com/sandratoo/hngx/blob/main/hngx.py'
    source_code_URL = 'https://github.com/sandratoo/hngx.git'
    

    return jsonify({'slack_name':slack_name,'track':track, 'day':day,"utc_time": utc_time,'status_code': 200, "github_repo_url": source_code_URL,"github_file_url": file_URL})

if __name__ == ("__main__"):
    app.run(debug=True)