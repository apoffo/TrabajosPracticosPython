import matplotlib.pyplot as plt


plt.plot([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],[6,6,6,6,6,6,6,6,6,6,8,10,11,13,14,15,15,15,13,11,10,9,8,7])
plt.fill_between([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],[6,6,6,6,6,6,6,6,6,6,8,10,11,13,14,15,15,15,13,11,10,9,8,7])
plt.title("Temperaturas por horas en Río Cuarto")
plt.xlabel("Horas")
plt.ylabel("T°")
plt.show()
