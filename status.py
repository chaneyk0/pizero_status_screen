#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from flask import Flask, jsonify, make_response, request, render_template
from datetime import datetime
mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__)
#app.config['SERVER_NAME']= 'status.local'

hacking_loop = False



def switchClear() : 
    global hacking_loop 
    mylcd.lcd_clear() 
    hacking_loop = False 
    sleep(1)

    
def currentTime():
    dateraw=datetime.now()
    timeFormat=dateraw.strftime("%-I:%M %p")
    return timeFormat

    
def switchAvailable() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("Available", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchBusy() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("Busy", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchAway() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("Away", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchMeeting() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("In a meeting", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchPhone() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("On the phone", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchSleepy() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("Feeling sleepy", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchErrands() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("Running errands", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)    
    
def switchFeymood() :
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string("Taken by a fey", 1)
    mylcd.lcd_display_string("mood as of "+cT, 2)
    sleep(1)
    
def switchHacking() :
    global hacking_loop
    switchClear()
    hacking_loop = True
    mylcd.lcd_display_string("Hacking", 1)
    
    while hacking_loop :    
        for i in range(4):
            display_string = "Mainframe" + "." * i
            display_string = display_string.ljust(16)
            mylcd.lcd_display_string(display_string, 2) 
            sleep(1)

def display_on_lcd(text):
    cT=currentTime()
    switchClear()
    mylcd.lcd_display_string(text, 1)  
    mylcd.lcd_display_string("as of "+cT, 2)
    
# API switchAvailable
@app.route('/api/available', methods=['GET'])
def apiAvailable() :
    switchAvailable()
    return jsonify({})
    
# API switchFeymood
@app.route('/api/feymood', methods=['GET'])
def apiFeymood() :
    switchFeymood()
    return jsonify({})
    
# API SwitchHacking
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

@app.route('/update_custom_status', methods=['POST'])
def update_custom_status():
    custom_status = request.form['customStatus']
    display_on_lcd(custom_status)
    return 'Status Updated'

    
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
