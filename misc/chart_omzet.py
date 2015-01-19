import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# Example data
def chart_omzet(tuple_nota, list_total, office, about):
	y_pos = np.arange(len(tuple_nota))
	error = np.random.rand(len(tuple_nota))

	plt.barh(y_pos, list_total, xerr=error, align='center', alpha=0.4)
	plt.yticks(y_pos, tuple_nota)
	plt.xlabel(office)
	plt.title(about)

	plt.show()


'''
tuple_nota = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
list_total = [23,56,54,23,21]
office = "PT. Percaya Diri"
chart_omzet(tuple_nota, list_total, office, "OMZET PENJUALAN")
'''
