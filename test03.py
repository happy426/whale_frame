second = 61205.00
s = second % 60
minute = (second - s) / 60
m = minute % 60
hour = (minute - m) / 60
h = hour % 24
day = (hour - h) / 24
print(f"{int(day)}天{int(h)}时{int(m)}分{int(s)}秒")
