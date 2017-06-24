import forecastio

api_key = 'df81a794c85818fc1e3dd5140d394986'
lat = 38.958631
lng = -77.357003
forecast = forecastio.load_forecast(api_key, lat, lng)

daily = forecast.daily()
print (daily.summary)