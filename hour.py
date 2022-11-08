"""
    Сделайте так, чтобы число секунд 
отображались в виде 
дни: часы: минуты: секунды.
365   24    60      60   
"""

sec = int(input("secund ->> "))

while(sec):
    days = sec //(24 * 3600)
    sec %= 24*3600
    hours = sec//3600
    sec%=3600
    minutes = sec//60
    sec%= 60

    print(days,":",hours,":",minutes,":",sec)



