


def facto(x):
	if x<2:
		return 1
	return x * facto(x-1)


somme = 0
cent_str = str(facto(100))
for c in cent_str:
	somme += int(c)
print(f"La somme des chiffres qui forment le factoriel 100 est {somme}")
