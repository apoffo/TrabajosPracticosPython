import matplotlib.pyplot as plt

#web https://www.foreca.es/Argentina/Cordoba-Province/R%C3%ADo-Cuarto/10-day-forecast?date=2023-06-28
# https://www.foreca.es/Argentina/Formosa-Province/Formosa/10-day-forecast?date=2023-07-02

horas =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
rio_cuarto =[6,6,6,6,6,6,6,6,6,6,8,10,11,13,14,15,15,15,13,11,10,9,8,7]
formosa = [19,18,18,17,17,16,16,16,16,18,20,23,25,27,28,28,28,27,25,23,21,20,20,19]
plt.plot(horas, rio_cuarto, label="Río Cuarto")
plt.plot(horas, formosa, label="Formosa")
plt.title("Temperaturas Extremas")
plt.xlabel("Horas")
plt.ylabel("T°")
plt.legend()

plt.show()