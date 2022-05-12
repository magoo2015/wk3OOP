class AlarmClock:

    def __init__(self):
        self.current_time = "0630"
        self.alarm_on = True
        self.alarm_time = "0900"

    def change_current_time(self, new_time):
        self.current_time = new_time
        print(self.current_time)
    
    
    def alarm_on_or_off(self, alarm_setting):
        self.alarm_on = alarm_setting
        return self.alarm_on

    
    def set_current_alarm_time(self, new_alarm_time):
        self.alarm_time = new_alarm_time
        print(self.alarm_time)


    
