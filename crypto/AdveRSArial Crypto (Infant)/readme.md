# [AdveRSArial Crypto (Infant)](https://hackropole.fr/fr/challenges/crypto/fcsc2024-crypto-adversarial-crypto-1/)

## Énoncé

Je viens de suivre un cours sur RSA mais je crois que j’ai oublié quelque chose. Il me semble que le prof parlait de deux trucs, mais je ne sais plus exactement quoi. Vous pouvez m’aider ?

## Solution

Il s'agit d'une mauvaise implémentation du chiffrement RSA. Au lieu d'avoir deux nombres premiers distincts, un seul nombre premier est utilisé. 


On a donc `n = p` et `q = 1`. Or cela implique que `phi(n) = 0`. Néanmoins, il faut savoir que `phi(n)` (la valeur de l'indicatrice d'Euler en n) représente le nombre d'entiers inférieurs à `n` et premiers avec `n`. Ainsi `phi(n) = n - 1`.

On peut alors calculer la clé privée `d`:
```py
d = pow(e, -1, phi)
```

On peut alors déchiffrer le message chiffré `c`:
```py
m = pow(c, d, n)
```

Le script de solution est [solv.py](./solv.py).

## Flag

Le flag est le message déchiffré.

