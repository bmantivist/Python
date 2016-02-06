seconds = 3097.7193288803
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

s = "%i:%02i:%02i" % (hours, minutes, seconds)
print s