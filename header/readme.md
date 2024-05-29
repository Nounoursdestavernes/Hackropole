# [Header](https://hackropole.fr/fr/challenges/web/fcsc2022-web-header/)

## Énoncé

Pour cette épreuve, vous devrez vous pencher sur une fonctionnalité essentielle du protocole HTTP.

## Solution

On commence par se rendre sur le site après avoir lancé le docker.

Vu le titre de l'épreuve, on fonce regarder les headers de la requête dans l'inspecteur de notre navigateur.

Il n'y a rien de spécial dans les headers de la requête, malheureusement.

On voit également qu'il y a un onglet ```source``` dans le menu du site. On peut supposer que ce lien nous permettra de voir le code source de la page.

On clique sur le lien et boom:

```js
const fs = require('fs');
const express = require('express');
const escape = require('escape-html')
var favicon = require('serve-favicon');
const app = express();

app.use(favicon('favicon.ico'));
app.set('view engine', 'ejs');
app.use(express.static('public'));

app.get('/', async (req, res) => {
    var verif = req.header("X-FCSC-2022");
    if (verif == "Can I get a flag, please?") {
        var flag = fs.readFileSync("flag.txt");
        res.status(200);
        res.render("pages/index", {
            type: "success",
            msg: "Here it is: " + flag,
        });
        return res.end();
    } else {
        res.status(200);
        res.render("pages/index", {
            type: "warning",
            msg: "No flag for you. Want a meme instead?",
        });
        return res.end();
    }
});

app.get('/source', async (req, res) => {
    const source = fs.readFileSync(__filename);
    res.render("pages/source", {
        source: escape(source),
    });
    return res.end();
});

app.listen(8000);
```

Le mot flag m'a sauté aux yeux (déformation professionnelle... faut que je fasse une pause...). On voit que si le header ```X-FCSC-2022``` est égal à ```Can I get a flag, please?```, alors on obtient le flag.

On va donc ajouter ce header à notre requête sur la page d'accueil.

La reponse de la requête contient bien le flag.


## Flag

Le flag est dans la réponse de la requête sur ```http://localhost:8000/``` après avoir ajouté le header ```X-FCSC-2022: Can I get a flag, please?```.