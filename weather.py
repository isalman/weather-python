import json, urllib
from sys import argv
from time import localtime, strftime, gmtime

def get_weather(city_name, appid):
    response = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" %(city_name, appid))
    weather = response.read()
    weather_json = json.loads(weather)
    
    if weather_json['cod'] == 200:
        wdescription = weather_json['weather'][0]['description'].capitalize()
        curr_temp = float(weather_json['main']['temp'])-273.3
        pressure = float(weather_json['main']['pressure'])
        humidity = float(weather_json['main']['humidity'])
        temp_min = float(weather_json['main']['temp_min'])-273.3
        temp_max = float(weather_json['main']['temp_max'])-273.3
        sea_level = float(weather_json['main']['sea_level'])
        grnd_level = float(weather_json['main']['grnd_level'])
        wind_speed = float(weather_json['wind']['speed'])
        wind_dir = float(weather_json['wind']['deg'])
        sunrise = strftime("%H:%M", localtime(int(weather_json['sys']['sunrise'])))
        sunset = strftime("%H:%M", localtime(int(weather_json['sys']['sunset'])))
        name = weather_json['name']
        country = weather_json['sys']['country']
        curr_time = strftime("%a, %d %b %Y, %H:%M:%S", gmtime())

        print '''
        ##############################################
                                                     
                 ## %s ##
               ##  Weather Report for %s,%s. ##
                                                     
                      **  %s  **
                                                     
            Temperature:            %.2f degree C    
            Max Temperature:        %.2f degree C    
            Min temperature:        %.2f degree C    
                                                     
            Pressure:               %.2f hPa         
            Sea Level:              %.2f hPa         
            Ground Level:           %.2f hPa         
                                                    
            Humidity:               %.2f %%          
                                                    
            Wind:                   %.2f m/s         
            Wind Direction:         %.2f degree      
                                                    
            Sunrise:                %s               
            Sunset:                 %s               
                                                    
        ##############################################
        '''%(curr_time, name, country, wdescription, curr_temp, temp_max, temp_min,
             pressure, sea_level, grnd_level, humidity, wind_speed, wind_dir, sunrise,
             sunset)
        
    else:
        print "\n[-]",weather_json['message']
        print """
[-] Usage: python weather.py <city_name> or <city_Name, country_code>

    Examples: python weather.py lahore
              python weather.py lahore,PK

              """
        exit()

        
def main():
    appid = '807a5769331d4af3f7fea717e5b6333b'
    if len(argv) == 2:
        script, city_name = argv
        get_weather(city_name, appid)
        
    else:
        print """
    [-] Usage: python weather.py <city_name> or <city_Name, country_code>

        Examples: python weather.py lahore
                  python weather.py lahore,PK

              """
        exit()
        
if __name__ == __main__:
    main()
