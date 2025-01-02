# 16.	Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER
#       >= 30         >=90                Hot and Humid
#       >= 30         < 90                 Hot
#       <30           >= 90               Cool and Humid
#       <30           <90                 Cool


temperature = int(input("Enter the temperature in degree celsius :"))
humidity = int(input("Enter the humidity in % :"))
if(temperature>=30 and humidity>=90):
    print("Weather is hot and humid.")
elif(temperature>=30 and humidity<90) :
    print("Weather is hot ")
elif(temperature<30 and humidity>=90):
    print("Weather is cool and humid")
elif(temperature<30 and humidity<90):
    print("Weather is cool")
else:
    print("enter valid values ")