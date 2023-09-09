from flask import Flask,jsonify,request
import datetime

app = Flask(__name__)

@app.route('/details/', methods=['GET'])
def get_details():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    day = 'Saturday'
    utc_time = datetime.datetime.now()
    file_URL = ''
    source_code_URL = ''
    status_code = 200

    return jsonify({'slack_name':slack_name,'track':track, 'day':day,"utc_time": utc_time})

if __name__ == ("__main__"):
    app.run(debug=True)