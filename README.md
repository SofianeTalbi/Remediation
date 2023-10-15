Travail Complémentaire De Remédiation
=======
Contexte
----------

Dans le cadre de mon rattrapage, il m'a été demandé de construire un dashboard dynamique permettant de présenter la diversité des solutions de production électrique des principaux pays européens (+UK) au cours des 10 dernières années dans l'environnement Python + Dash/Plotly.

Mon application devait récupérer des données open sources que l'on peut trouver sur le web. Mon dashboard devait afficher les données de façon optimale avec la mise en place de graphiques, de cartes etc.J'ai pris l'initiative également de fournir une documentation technique et fonctionnelle (voir ci dessous).

C’est donc ce que j'ai fait. J'ai récupéré mes données sur Kaggle à l'adresse https://www.kaggle.com/datasets/prateekmaj21/electricity-production-by-source-world/data. Ainsi, sur mon dashboard, vous pouvez visualiser les données à travers les graphiques en naviguant sur mon application.

Concernant la source de donnée, Les données proviennent de "Our World in Data". Ces données sont compilées par Our World in Data à partir de deux sources principales :
- BP Statistical Review of World Energy : https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html
- Ember : https://ember-climate.org/data/
Le fichier csv présente la production électrique des pays dans le monde par source en fonction des années et possède 11 colonnes et 6242 lignes:
- "Entity" (Nom du pays)
- "Code" (Code du pays)
- "Year" (Année)
- "Electricity from coal (TWh)" (Source)
- "Electricity from gas (TWh)" (Source)
- "Electricity from hydro (TWh)" (Source)
- "Electricity from other renewables (TWh)" (Source)
- "Electricity from solar (TWh)" (Source)
- "Electricity from oil (TWh)" (Source)
- "Electricity from wind (TWh)" (Source)
- "Electricity from nuclear (TWh)" (Source)

User guide
----------
-> Tout d'abord, il faut que vous cloniez le projet en effectuant la commande suivante sur votre terminal: 

        git clone https://github.com/SofianeTalbi/Remediation.git
	
-> Veuillez, avant de continuer, taper les commandes suivantes sur votre terminal:

pip install dash

pip install pandas

pip install pd

pip install dcc

pip install html

pip install Input

pip install Output

pip install plotly.express
				
-> Ensuite, toujours sur votre terminal, il faut que vous fassiez:

cd Remediation

-> Enfin vous pourrez lancer l'application Web en tapant toujours sur votre terminal:

python dashboard.py

-> Vous pouvez ensuite visualiser mon application en tapant sur votre moteur de recherche:

http://127.0.0.1:8050/

Developper Guide
----------

*Comment est organisé le code ?*

Le fichier principal est celui nommé dashboard.py. C'est celui qu'il faut lancer depuis le terminal et qui active l'application.

1. **Imports** : Les bibliothèques nécessaires sont importées au début du code pour pouvoir les utiliser dans la suite du programme.

2. **Chargement des données** : Les données sont chargées à partir d'un fichier CSV et les opérations de prétraitement sont effectuées pour filtrer les pays européens, les années spécifiques, et calculer des statistiques pertinentes.

3. **Configuration de l'application Dash** : L'application Dash est créée, et des options de personnalisation telles que les années, les sources d'énergie, et les icônes sont configurées.

4. **Mise en page de l'application Dash** : La mise en page de l'application Dash est définie avec des éléments HTML et des composants Dash. La mise en page est organisée en sections, chaque section contenant un titre, des graphiques, et des options de filtrage.

5. **Callbacks** : Des fonctions de rappel (callbacks) sont définies pour mettre à jour les graphiques en fonction des sélections de l'utilisateur. Ces fonctions de rappel prennent en compte les filtres, les années, et les sources d'énergie sélectionnés pour mettre à jour les graphiques en conséquence.

6. **Exécution de l'application** : Enfin, le code vérifie si le script est exécuté directement (et non importé en tant que module) et démarre l'application Dash en mode débogage.

le fichier style.css qui se trouve dans le dossier assets permet de gerer le visuel de mon application (marge + dropdown coloré + font) 

Rapport d'analyse
----------
*Conclusion*

Pour conclure, ce travail m'a permis d'en apprendre plus sur la diversité des solutions de production électrique des principaux pays européens (+UK) entre 2010 et 2020.

Ce que l'on sait maintenant:

1. **Production Électrique Par Source et Par Année** : Les graphiques montrent comment la production électrique varie au fil des années pour différentes sources d'énergie selon les pays. On peut voir que certains pays produisent bien plus d'électricité que d'autre. Par exemple l'Allemagne produit une bien plus grande quantité d'électricité en TWh que le Portugal.

2. **Répartition de la Production d'Électricité par Source** : Ces graphiques en camembert permettent de visualiser la répartition de la production d'électricité pour une source et pour une année donnée. On peut observer comment les pays européens répartissent leur production entre les différentes sources, montrant ainsi la diversité ou la prédominance de certaines sources. Par exemple, l'allemagne et la Pologne sont des grands producteurs d'électricité à partir du charbon. Chaque année, ils représentent à eux deux 50% de la production électrique total via charbon.

3. **Évolution de la Production par Source** : Les graphiques en ligne montrent comment la production d'une source d'énergie particulière a évolué de 2010 à 2020. Cela permet de voir si certains pays ont augmenté ou réduit leur dépendance à une source d'énergie spécifique. Par exemple, on peut voir que l'Italie voit sa production d'électricité via l'énergie solaire en constante augmentation depuis les années 2010.

4. **Comparaison de la Production Renouvelable et Non Renouvelable** : Le graphique de comparaison de la production d'électricité renouvelable et non renouvelable montre comment ces deux catégories de production varient au fil du temps pour différents pays. Cela met en évidence l'accent mis sur les énergies renouvelables dans certains pays. Par exemple le Royaume-Uni voit sa production électrique à partir d'énergie renouvelable égalé sa production électrique à partir d'énergie non renouvelable. Au contraire, certain pays comme la France ne semble pas vouloir produire plus d'électricité via les energies renouvelables que par les energies non renouvelable.

5. **Histogramme de la Production d'Électricité** : L'histogramme montre la production totale d'électricité par source pour une année donnée. Cela permet de voir quels pays privilégient certaines sources d'énergie et dans quelle mesure.

6. **Production Électrique Totale Par Source et Par Année** : Le graphique montre quelles sont les solutions qui produisent le plus d'électricité en fonction du temps. On peut voir par exemple que le nucléaire a toujours était la solution de production électrique la plus efficace depuis les années 2010

En résumé, les graphiques sur mon dashboard illustrent la diversité des sources d'énergie utilisées par les principaux pays européens et leur évolution au fil des années. Certains pays semblent avoir une production électrique plus diversifiée, tandis que d'autres restent fortement dépendants de sources spécifiques. La transition vers des sources d'énergie plus propres et renouvelables est également mise en évidence.

*Axe de développement*

Un axe de développement serait de réaliser le même travail mais sur l'ensemble des données que fournit le fichier csv et non pas seulement les pays européens ni en se restraignant aux 10 dernières années. Cela nous permettrait d'en savoir plus sur la diversité des solutions de production électrique dans le monde depuis les années 1985.

Contact
----------
Talbi Sofiane: talbi.sofiane@edu.esiee.fr

lien vers mon projet: https://github.com/SofianeTalbi/Remediation.git
