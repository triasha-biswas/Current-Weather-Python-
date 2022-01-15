import urllib.request,urllib.error,urllib.parse
import json
import ssl
import datetime

#Service URL and API key
serviceurl="http://api.openweathermap.org/data/2.5/weather?"
api_key="ea94075d83b5e822581e9f4f0d1aa7cf"

#Ignore SSl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#conversion: Kelvin to celsius
def ktoc(t):
    c=t-273.15
    cf="{:.2f}".format(c)
    return cf

while True:
    address=input("Enter location:")
    if len(address)<1: break
    url=serviceurl+urllib.parse.urlencode({'q': address, 'appid': api_key})

    uh=urllib.request.urlopen(url,context=ctx)
    data=uh.read().decode()
    js=json.loads(data)

    lat=js['coord']['lat']
    long=js['coord']['lon']
    w_main=js['weather'][0]['main']
    w_desc=js['weather'][0]['description']
    temp=js['main']['temp']
    a=ktoc(temp)
    fl=js['main']['feels_like']
    b=ktoc(fl)
    tempmin=js['main']['temp_min']
    c=ktoc(tempmin)
    tempmax=js['main']['temp_max']
    d=ktoc(tempmax)
    pressure=js['main']['pressure']
    humidity=js['main']['humidity']
    wind=js['wind']['speed']
    clouds=js['clouds']['all']
    sunrise=js['sys']['sunrise']
    sunset=js['sys']['sunset']
    time=js['dt']


    print('COORDINATES')
    print('Latitude: ',lat,'° N',sep='')
    print('Longitude: ',long,'° E',sep='')
    print()
    print('WEATHER CONDITIONS')
    print('Main:',w_main)
    print('Description:',w_desc)
    print()
    print('Temperature: ',a,'° C',sep='')
    print('Feels like: ',b,'° C',sep='')
    print('Minimum temperature: ',c,'° C',sep='')
    print('Maximum temperature: ',d,'° C',sep='')
    print()
    print('Pressure: ',pressure,'hPa')
    print('Humidity: ',humidity,'%',sep='')
    print('Wind speed: ',wind,'m/sec',sep='')
    print('Cloudiness: ',clouds,'%',sep='')
    print()
    print("Sunrise:",datetime.datetime.fromtimestamp(int(sunrise)).strftime('%Y-%m-%d %H:%M:%S'),"IST")
    print("Sunset:",datetime.datetime.fromtimestamp(int(sunset)).strftime('%Y-%m-%d %H:%M:%S'),"IST")
    print("Time of data calculation:",datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S'),"IST")
    print()