# NOTES

?? : 
*	```py
	# Creazione di un DataFrame fittizio con errori
	data = {
		'Nome': ['Alice', 'Bob', 'Charlie', 'David', np.nan, 'Eve'],
		'Età': [25, 30, 22, np.nan, 35, 28],
		'Punteggio': [85, 92, 78, 64, 99, 88],
		'Sesso': ['F', 'M', 'M', 'M', 'M', 'F'],
		'Indirizzo': ['123 Main St', '456 Elm St', np.nan, '789 Oak St', '555 Pine St', '999 Maple St'],
		'Nazionalità': ['USA', 'Canada', 'UK', 'USA', 'Germany', 'France']
	}

	df = pd.DataFrame(data)


	# 7. Categorizzare automaticamente le nazionalità
	df['Nazionalità'] = df['Nazionalità'].astype('category').cat.codes
	```
	