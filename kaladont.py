pocetna_rec = raw_input('Unesite rec: ')
nastavak = pocetna_rec [-2:]

igranje = True
while igranje == True:

	pocetna_rec += raw_input('Unesite rec: %s' %(nastavak))
	nastavak = pocetna_rec [-2:]

	if nastavak != 'ka':
		igranje = True
	else:
		print 'Izgubili ste!'
		igranje = False
