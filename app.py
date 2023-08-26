import flask
from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

target_datetime = datetime(2023, 12, 31, 23, 59, 59)

@app.route('/')
def countdown():
    current_datetime = datetime.now()
    time_left = target_datetime - current_datetime

    if time_left.total_seconds() <= 0:
        countdown_str = "This is the end"
    else:
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    
    return render_template('countdown.html', countdown=countdown_str)

if __name__ == '__main__':
    app.run(debug=True)
