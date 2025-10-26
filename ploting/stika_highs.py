import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/3924220.csv'  # تأكد من تصحيح اسم الملف هنا
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # قراءة الرأس (العناوين)
    
    dates,higts,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        try:
            high = int(row[5])
            low = int(row[6])
           
        except ValueError:
            print(f'missing data for {current_date}')
        else:
            lows.append(low)
            higts.append(high)
            dates.append(current_date)

#plot the hight temperatuares
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(dates, higts, c='red', alpha=0.5)
ax.plot(dates , lows, c='b', alpha=0.5)
plt.fill_between(dates, higts, lows, facecolor='blue', alpha=0.1)


#format plot
ax.set_title("Daily higt and low temperatuares , from 2024 to 2025 " , fontsize=14)
ax.set_xlabel('',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("temoerature(F)",fontsize=16)
plt.tick_params(axis='both', which='minor', labelsize = 40)

plt.show()
