# smart_chicken

Bienvenue sur le projet SmartChicken, le poulailler connecté.

Depuis quelques temps, on assiste au développement d'une nouvelle espèce d'animaux de compagnie : les poules.
C'est sympa, pas trop de bruits (si le coq n'est pas là), ça pond des oeufs, et les oeufs c'est bon pour la santé, ce ne fait pas que cela, mais c'est bon aussi pour le jardin, il n'est pas nécessaire de les promener comme on le fait avec les toutous (bien que certains le fassent) et pour finir ça mange presque n'importe quoi. C'est d'ailleurs pour cette raison que certaines mairies fournissent des poules à leurs administrés. Réduction du volume des déchets ménagers, donc baisse des impôts locaux.
Bon les poules c'est bien mais il y a quand même quelques inconvénients, le plus dur, pour moi en tous cas, c'est de leur ouvrir la porte de leur poulailler au petit matin. Supportable en été, même si ça oblige à se lever tôt, cela devient carrément une corvée en hiver lorsque la température descend sous zéro.

Pour m'assister dans cette lutte environnementale, j'ai décidé d'automatiser l'ouverture / fermeture du poulailler. Et puisqu'on y est, ajoutons quelques fonctions :
- l'ouverture / fermeture automatique de la porte en fonction
    * d'une programmation horaire
    * de la luminosité
    * des heures de lever et coucher du soleil récupérées sur le site de weather.com ou météo France
    * d'un bouton d'ouverture / fermeture disposé à l'extérieur du poulailler pour une commande manuelle
- relevé des températures et hygrométrie intérieure / extérieure à l'aide de deux sondes DHT11
- caméra infra-rouge, dans un premier temps cela permet d'observer mes protégées, comme Secret Story mais en plus instructif, cela permet aussi de les compter et de vérifier qu'elles sont bien rentrées (1 poule Harco noire : Aglaë et 1 poule rousse : Sidonie), pour finir, en utilisant OpenCV il parait que l'on peut compter les oeufs et envoyer une alerte, à voir pour plus tard !
- haut-parleur pour diffusion de musique
- 1 sortie sur relais pour l'allumage / extinction d'une lampe
- 1 sortie sur relais pour option future (chauffage, distributeur de nourriture, ... ?)

Pour la partie mécanique, j'utilise des moteurs (il y deux portes) de four à micro-onde ou de volets roulants, couple énorme et vitesse de rotation faible. Quelques pièces imprimées en 3D (les pièces ont été conçues avec Google Sketchup) et quelques vis et boulons.

La partie commande associe un raspberry B+ sous Raspbian, une horloge RTC DS1307, une clé Wi-fi, des relais chinois, un haut-parleur pour la diffusion des MP3, une caméra sur nappe CSI (caméra officielle du Pi), des sondes DHT11, une LDR, une alim et quelques composants et nappes ...

Pour la partie logicielle, et c'est là que GitHub entre en scène, j'ai codé un serveur web en Flask. la version en cours permet de prendre le contrôle de la maquette via un navigateur web sur pc ou smartphone à partir du réseau local, et de commander l'ouverture / fermeture de la porte, l'allumage de la lampe et de consulter sur l'interface, les températures, hygrométrie ainsi que le luminosité.

Au niveau système, on utilise les bibliothèques pour l'horloge sur bus I2C, wiring-PI pour la gestion du GPIO, motion pour la caméra

Un dossier maquette, regroupe des photos (il manque la cam, sur une autre réalisation pour l'instant), les fichiers Sketchup d'un prototype utilisé pour coder (c'est plus pratique que d'aller dans le jardin pour rebooter le Pi !) et quelques docs.

Le dossier flask contient tout ce qui a put être codé pour l'instant.

TO DO :
- intégrer les mesures de T°, HR% et luminosité dans un beau graphique, par jour, semaine, mois.
- intégrer la récupération des heures de lever et coucher de soleil (http://www.weirdog.com/blog/php/php-xml-previsions-meteo.html ou autre API) 
- intégrer un player MP3 et un espace de stockage (pas plus d'une dizaine de titre : la danse des canards, Black poule de Laurent Voulzy, BO de Chicken Run, Chicken For Ever de McDo, ... )
- visualisation de la caméra
- interface définitive html, css et responsive
- documentation projet
- package pour install
- wps
- OpenCV

Il reste encore pas mal de choses à faire, et si vous voulez apporter votre grain(e de maïs) n'hésitez pas. Vous pouvez me contacter par mail : sebastien.begusseau@gmail.com