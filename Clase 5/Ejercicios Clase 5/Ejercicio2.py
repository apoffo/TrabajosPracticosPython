import matplotlib.pyplot as plt

"""bar = plt.subplots()"""

# datos

y = [30,20,15,22,18,12,18,7,9,15,22,25]
meses = [1,2,3,4,5,6,7,8,9,10,11,12]

plt.bar(meses, y, color="red")
plt.title("Registro pluviométrico anual 2023")


plt.show()
