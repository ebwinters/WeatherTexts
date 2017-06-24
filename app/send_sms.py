from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
import forecastio
import schedule
import time

"""Get weather for curent day"""
api_key = 'df81a794c85818fc1e3dd5140d394986'
lat = 38.958631
lng = -77.357003
forecast = forecastio.load_forecast(api_key, lat, lng)
daily_summary = forecast.daily().summary


"""Set up function to create and send text"""
client = Client(account_sid, auth_token)
msg = 'Hi Ethan, here is a summary of the days weather:\n' + daily_summary
def send_text():
	text = client.messages.create(to=my_cell, from_=my_twilio, body=msg)
	print ('message sent')

"""schedule texts"""
schedule.every.day.at("08:00").do(send_text)

while True:
	schedule.run_pending()
	time.sleep(60)

