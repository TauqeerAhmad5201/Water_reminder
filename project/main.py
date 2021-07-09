'''The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.
'''
import time 
from plyer import notification 

if __name__=="__main__":
    while True:
        notification.notify(
        title = "Time to have water !! :D",
        message = "It's too hot in Delhi, staying hydrated is crucial to maintaining your body temperature.",
        # app_icon = "D:\Programming\Python\pythonProject1\WaterReminder\icon.ico",
        timeout = 5
        )
        time.sleep(1*60*30)

a = input()