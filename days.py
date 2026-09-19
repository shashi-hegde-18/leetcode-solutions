class Solution:
    def whichWeekDay(self, day):
      
        days = ["Invalid", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

        print(days[day] if 1 <= day <= 7 else "Invalid")