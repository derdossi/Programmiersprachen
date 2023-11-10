
bl = 4000

kv = bl * 0.146 * 0.5
rv = bl * 0.186 * 0.5
av = bl * 0.034 * 0.5
pv = bl * 0.026 * 0.5

if bl > 5000:
    lohnsteuer = bl * 0.35
elif bl > 4000:
    lohnsteuer = bl * 0.30
elif bl > 3000:
    lohnsteuer = bl * 0.25
elif bl <= 3000:
    lohnsteuer = bl * 0.20

kirchensteuer = lohnsteuer * 0.08

nettolohn = bl - (kv + rv + av + pv + lohnsteuer + kirchensteuer)

print(nettolohn)
