#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from flask import Flask, jsonify, make_response, request, render_template
from datetime import datetime
mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__)
#app.config['SERVER_NAME']= 'status.local'

def currentTime():
    dateraw=datetime.now()
    timeFormat=dateraw.strftime("%-I:%M %p")
    return timeFormat
   
def switchAvailable() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Available", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchBusy() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Busy", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchAway() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Away", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchSleepy() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Sleepy", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchMeeting() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("In a meeting", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchPhone() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("On the phone", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchSleepy() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Feeling sleepy", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchErrands() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Running errands", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)    
    
def switchHacking() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Hacking the", 1)
    mylcd.lcd_display_string("Mainframe", 2)
    sleep(1)   
    
def switchClear() :
    mylcd.lcd_clear()
    sleep(1)
    
# API switchAvailable
@app.route('/api/available', methods=['GET'])
def apiavailable() :
    switchAvailable()
    return jsonify({})
    
# API switchHacking
@app.route('/api/hacking', methods=['GET'])
def apiHacking() :
    switchHacking()
    return jsonify({})
    
# API Busy
@app.route('/api/busy', methods=['GET'])
def apiBusy() :
    switchBusy()
    return jsonify({})

# API Errands
@app.route('/api/errands', methods=['GET'])
def apiErrands() :
    switchErrands()
    return jsonify({})
    
# API Away
@app.route('/api/away', methods=['GET'])
def apiAway() :
    switchAway()
    return jsonify({})
    
# API switchMeeting
@app.route('/api/meeting', methods=['GET'])
def apiMeeting() :
    switchMeeting()
    return jsonify({})
    
# API switchPhone
@app.route('/api/phone', methods=['GET'])
def apiPhone() :
    global globalLastCalledApi
    globalLastCalledApi = '/api/Phone'
    switchPhone()
    return jsonify({})
    
# API clear
@app.route('/api/clear', methods=['GET'])
def apiClear() :
    switchClear()
    return jsonify({})

# API sleepy
@app.route('/api/sleepy', methods=['GET'])
def apiSleepy() :
    switchSleepy()
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.route('/')
def index():
    #url_for('html', filename='lcd.html')
    return render_template('lcd.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    #app.run(host='192.168.0.198', port=5000)
