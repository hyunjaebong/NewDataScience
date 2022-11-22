class DatePro:
    content = "날짜 처리 클래스"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def  display(self):
        print("%d-%d-%d"%(self.year, self.month, self.day))

    @classmethod
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")

date = DatePro(1995, 10, 25)
print(date.content)
print(date.year)
date.display()

print(DatePro.content)
DatePro.date_string('19951025')