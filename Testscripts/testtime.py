milliseconds = 65600000
hours, milliseconds = divmod(milliseconds, 3600000)
minutes, milliseconds = divmod(milliseconds, 60000)
seconds = float(milliseconds) / 1000

s = "%i:%02i:%02i" % (hours, minutes, seconds)
print s