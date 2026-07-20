---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "Cet article de référence décrit le partenariat entre Braze et Copy Pastd, un générateur d'e-mails par glisser-déposer qui envoie des Content Blocks et des modèles alimentés par Liquid directement dans votre espace de travail Braze."
page_type: partner
search_tag: Partner
---

# Copy Pastd

> [Copy Pastd](https://copypastd.com/) Building Blocks est un générateur d'e-mails par glisser-déposer qui envoie des Content Blocks alimentés par Liquid et des modèles complets directement dans votre espace de travail Braze. Concevez une fois, synchronisez avec Braze et réutilisez les mêmes composants dans vos Campaigns, Canvas et flux déclenchés sans recréer le HTML à chaque fois.

_Cette intégration est maintenue par Copy Pastd._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Copy Pastd vous permet de créer des e-mails dans Building Blocks, un générateur d'e-mails hébergé qui produit un contenu natif Braze avec du Liquid propre, des références aux Content Blocks et des modèles qui s'intègrent dans n'importe quelle Campaign ou Canvas sans conversion.

Vous pouvez assembler un e-mail à partir de blocs réutilisables, l'envoyer vers Braze en un clic et avoir la certitude que les mêmes styles de marque, composants et contenus dynamiques s'affichent de manière cohérente à chaque envoi. Le résultat : moins de modèles codés à la main, moins de temps consacré à la création et à l'envoi d'e-mails, et une bibliothèque centralisée qui se met à jour partout lorsqu'elle est modifiée.

## Conditions préalables {#prerequisites}

Les éléments suivants sont requis pour utiliser cette intégration :

| Condition | Description |
| ----------- | ----------- |
| Compte Copy Pastd | Requis pour utiliser Building Blocks. Inscrivez-vous sur [copypastd.com](https://copypastd.com). Chaque client reçoit un espace de travail, une bibliothèque de feuilles de style, cinq postes de générateur et une bibliothèque de blocs. |
| Clé API REST Braze pour les modèles d'e-mail | Une clé API avec les autorisations `templates.email.create`, `templates.email.update` et `templates.email.list`.<br><br>Créez la clé dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Clé API REST Braze pour les Content Blocks | Une clé API avec les autorisations `content_blocks.create`, `content_blocks.update`, `content_blocks.info` et `content_blocks.list`.<br><br>Créez la clé dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Clé API REST Braze pour les Catalogues (facultatif) | Une clé API avec un accès en lecture à `catalogs.get`, `catalogs.get_item` et `catalogs.get_selections`. Requis uniquement si vous prévoyez de lier des blocs aux Catalogues Braze. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. Building Blocks sélectionne automatiquement l'endpoint en fonction du cluster que vous choisissez. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'usage {#use-cases}

* **Création cohérente avec la marque à grande échelle.** Appliquez une feuille de style Building Blocks à chaque modèle : les couleurs, polices, styles de boutons et échelles de marge s'affichent de manière identique sur des centaines d'e-mails. Lorsque la marque évolue, mettez à jour la feuille de style une seule fois et resynchronisez pour déployer la mise à jour sur tous vos e-mails en une fois.
* **Contenu connecté et modèles de produits liés aux Catalogues.** Liez les champs de blocs d'e-mail directement à vos endpoints de [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) et aux [Catalogues Braze]({{site.baseurl}}/user_guide/data/activation/catalogs) depuis le générateur. Réutilisez le même modèle pour les lancements de nouveaux produits, les collections saisonnières ou les actualisations de contenu sans toucher au Liquid.
* **Production d'e-mails en libre-service pour les marketeurs non techniques.** Composez un e-mail complet à partir de blocs approuvés, y compris la personnalisation et la logique Liquid, et envoyez-le vers Braze pour révision sans avoir besoin d'un développeur pour écrire du HTML ou du Liquid, ni pour effectuer l'assurance qualité.
* **En-têtes et pieds de page centralisés, mis à jour en un clic.** Créez un en-tête ou un pied de page une seule fois dans le générateur Building Blocks et envoyez-le vers Braze. Chaque modèle qui le référence reste synchronisé, de sorte qu'un changement de logo, une modification de mentions légales ou un nouveau lien social ne nécessite qu'une seule mise à jour dans Building Blocks pour se propager à tous les e-mails déjà dans Braze.
* **Contenu centralisé pour tous les e-mails.** Créez un héros, un pied de page ou une carte promotionnelle une seule fois en tant que bloc intelligent Building Blocks. Mettez-le à jour, synchronisez, et chaque e-mail déjà dans Braze qui le référence récupère la modification lors du prochain envoi. Les flux de bienvenue, les newsletters hebdomadaires et les parcours déclenchés restent à jour sans modifier chaque Campaign.
* **Modèles verrouillés pour le libre-service des contributeurs.** Créez des modèles, verrouillez certains champs, puis invitez d'autres équipes à créer leurs propres e-mails depuis une interface contributeur sans leur donner accès aux outils destinés aux utilisateurs.

## Intégration {#integration}

### Étape 1 : Connecter Building Blocks à Braze {#step-1-connect-building-blocks-to-braze}

{% alert note %}
La connexion de Building Blocks à Braze est une configuration unique. Une fois vos identifiants validés, Building Blocks les enregistre pour toutes les synchronisations et envois de modèles futurs.
{% endalert %}

1. Connectez-vous à Building Blocks sur [blocks.copypastd.com](https://blocks.copypastd.com), ou sélectionnez **Login** sur [copypastd.com](https://copypastd.com).
2. Depuis le tableau de bord, sélectionnez **Set up your Braze connection**. (Cette pastille apparaît pour les administrateurs lors de la première connexion et jusqu'à ce que la configuration soit terminée. Vous pouvez également accéder à la page depuis **Team Settings** > **Connect** > **Braze API Keys**.)
3. Sélectionnez votre cluster Braze dans le menu déroulant. L'endpoint REST correspondant est renseigné automatiquement.
4. Collez votre clé API Templates, votre clé API Content Blocks et (facultativement) votre clé API Catalogs dans les champs correspondants.
5. Sélectionnez **Validate and save**. Building Blocks appelle Braze pour confirmer que les clés fonctionnent et que les portées d'autorisations sont correctes. Si quelque chose manque, une erreur en ligne vous indique quelle portée est incorrecte.

### Étape 2 : Synchroniser votre bibliothèque avec Braze {#step-2-sync-your-library-to-braze}

1. Une fois les clés validées, sélectionnez **Sync now** dans la fenêtre modale de configuration. (Vous pouvez également resynchroniser à tout moment depuis **Settings** > **Connect** > **Braze** > **Sync library**.) <br> Building Blocks envoie votre feuille de style et vos blocs dans votre espace de travail Braze sous forme de Content Blocks Braze. Ils apparaissent dans Braze avec des noms préfixés par `CP_` (par exemple, `CP_Hero_1`) ou `cp_` pour les feuilles de style (par exemple, `cp_default_style`).
2. Une fois la synchronisation terminée, vous pouvez envoyer des modèles individuels depuis le générateur en utilisant **Push to Braze**.

## Personnaliser Building Blocks {#customize-building-blocks}

### Étape 1 : Configurer votre feuille de style {#step-1-set-up-your-stylesheet}

1. Dans Building Blocks, accédez à **Settings** > **Build** > **Stylesheets**.
2. Modifiez la feuille de style par défaut ou créez-en une nouvelle. Définissez votre palette de couleurs (24 couleurs nommées), vos polices (Google Fonts pris en charge), vos styles de boutons, styles de liens, rayons et échelle de marge.
3. Sélectionnez **Save**. Building Blocks régénère le Liquid pour chaque bloc qui utilise cette feuille de style.
4. Sélectionnez **Sync now** pour envoyer les styles mis à jour dans votre espace de travail Braze.

### Étape 2 : Activer les endpoints de contenu connecté (facultatif) {#step-2-enable-connected-content-endpoints-optional}

1. Dans Building Blocks, accédez à **Settings** > **Connect** > **Connected Content endpoints**.
2. Ajoutez l'URL de l'endpoint, nommez-le et enregistrez. Building Blocks prend en charge un format de réponse Google Sheets en plus du format JSON standard.
3. Dans le générateur, liez n'importe quel champ texte, image ou lien à une variable de contenu connecté depuis le panneau **Personalize**. Le Liquid {% raw %}`{% connected_content %}`{% endraw %} correct est généré à l'exportation.

### Étape 3 : Lier aux Catalogues Braze (facultatif) {#step-3-bind-to-braze-catalogs-optional}

1. Dans Building Blocks, accédez à **Settings** > **Connect** > **Catalogs**. Building Blocks lit votre liste de catalogues à l'aide de la clé API Catalogs.
2. Ouvrez un bloc compatible (par exemple, une grille de produits).
3. Sélectionnez un catalogue et une sélection, puis associez les champs du bloc aux attributs des éléments du catalogue.
4. Envoyez le modèle. Building Blocks génère le Liquid {% raw %}`{% catalog_items %}`{% endraw %} et {% raw %}`{% catalog_selection_items %}`{% endraw %} correct pour que Braze le résolve au moment de l'envoi.

### Étape 4 : Ajouter vos attributs personnalisés Braze (facultatif) {#step-4-add-your-braze-custom-attributes-optional}

Building Blocks est livré avec les attributs utilisateur Braze par défaut (`first_name`, `email`, `country`, etc.). Pour lier des blocs à vos propres attributs personnalisés, importez-les une fois dans Building Blocks et ils restent disponibles dans chaque menu déroulant **Personalize**.

1. Dans Building Blocks, accédez à **Team Settings** > **Connect** > **Custom Attributes**.
2. Importez vos attributs personnalisés en utilisant l'une des méthodes suivantes :
* **Import en masse (recommandé).** Dans Braze, accédez à **Data Settings** > **Custom Attributes** et sélectionnez **Export**. Téléversez le CSV dans Building Blocks.
* **Ajouter les attributs un par un.** Saisissez le nom de l'attribut (par exemple, `loyalty_tier`) et sélectionnez **Add**. Cette méthode est utile si vous n'ajoutez que quelques attributs ou si vous souhaitez ajouter un nouvel attribut entre deux exports Braze.

Après l'enregistrement, vos attributs personnalisés apparaissent dans le menu déroulant **Personalize** du générateur aux côtés des attributs par défaut. L'insertion d'un attribut génère le Liquid {% raw %}`{{custom_attribute.${name}}}`{% endraw %} correct à l'exportation, de sorte que Braze résout la valeur par destinataire au moment de l'envoi.

## Utiliser l'intégration {#use-the-integration}

### Étape 1 : Envoyer un modèle vers Braze {#step-1-push-a-template-to-braze}

1. Ouvrez n'importe quel e-mail dans le générateur Building Blocks.
2. Sélectionnez **Push to Braze** dans la barre d'actions.
3. Sélectionnez l'espace de travail et confirmez. Building Blocks crée un modèle d'e-mail dans Braze avec le Liquid rendu.

Le modèle apparaît dans Braze sous **Modèles et médias** > **Modèles d'e-mail**, nommé d'après l'e-mail et la date sélectionnée dans les paramètres de l'e-mail.

### Étape 2 : Utiliser le modèle dans une Campaign ou un Canvas {#step-2-use-the-template-in-a-campaign-or-canvas}

1. Dans Braze, créez une nouvelle Campaign e-mail ou une étape du Canvas.
2. Sélectionnez **Templates** et choisissez le modèle envoyé par Building Blocks.

Le modèle contient chaque référence Building Blocks (feuille de style, Content Blocks) sous forme de Liquid {% raw %}`{{content_blocks.${...}}}`{% endraw %} actif, de sorte que les mises à jour dans Building Blocks se propagent sans réimporter le modèle.

### Étape 3 : Mettre à jour le contenu de manière centralisée {#step-3-update-content-centrally}

1. Dans Building Blocks, modifiez le bloc ou la feuille de style concerné.
2. Sélectionnez **Sync** pour renvoyer le Content Block mis à jour vers Braze.

Chaque e-mail dans Braze qui le référence (flux permanents, déclenchés, de bienvenue) récupère la nouvelle version lors du prochain envoi. Vous n'avez pas besoin de modifier chaque Campaign.

### Étape 4 : Créer des pools de contenu {#step-4-build-content-pools}

Les pools de contenu sont des tables de lignes de contenu que les e-mails référencent au lieu de contenir du texte statique. Mettez à jour le pool dans Building Blocks, et chaque e-mail dans Braze qui l'utilise affiche le nouveau contenu lors du prochain envoi. Utilisez les pools de contenu partout où un même contenu doit rester à jour dans de nombreux e-mails, comme les newsletters hebdomadaires, les flux de bienvenue, les séquences de reconquête, les campagnes saisonnières ou les parcours post-achat.

1. Dans Building Blocks, sélectionnez **Content** dans la navigation principale.
2. Sélectionnez **New Pool**. Donnez un nom qui décrit son contenu (par exemple, Offres hebdomadaires, Catalogue produits, Articles d'actualité).
3. Choisissez le type de bloc alimenté par le pool (par exemple, Hero, Grid, Card). Cela détermine les champs disponibles pour chaque ligne.
4. Ajoutez des lignes. Chaque ligne correspond à un élément de contenu. Remplissez les champs (titre, image, texte du CTA, lien du CTA, etc.).
5. Définissez l'ordre de priorité en faisant glisser les lignes vers le haut ou vers le bas. Activez ou désactivez chaque ligne, et définissez des dates de début et de fin facultatives. Au moment de l'envoi, la ligne active de plus haute priorité dont les dates sont valides l'emporte.
6. Cliquez sur **Save**. Les blocs intelligents peuvent désormais référencer ce pool.

### Étape 5 : Utiliser les blocs intelligents pour afficher le contenu du pool dans vos e-mails {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

Un bloc intelligent est un bloc sur le canevas du générateur qui référence un ou plusieurs pools de contenu au lieu de contenir du contenu statique. Au moment de l'envoi, Braze affiche la ligne du pool qui a la priorité la plus élevée, qui est active et dont les dates sont valides. Le Liquid exporté fait le travail. Aucune configuration supplémentaire dans Braze n'est nécessaire.

1. Dans Building Blocks, faites glisser un bloc intelligent sur le canevas (tout type de bloc ayant un pool correspondant).
2. Dans le panneau des propriétés, ouvrez l'éditeur de cascade.
3. Ajoutez un ou plusieurs pools de contenu par ordre de priorité. C'est la cascade : le premier pool avec une ligne active et dont les dates sont valides s'affiche. S'il n'a rien d'actif, le bloc intelligent passe au pool suivant, puis au suivant. Un schéma courant est Vente flash > Offres hebdomadaires > Favoris permanents, de sorte qu'il y a toujours quelque chose à afficher.
4. Envoyez le modèle vers Braze. Le Liquid exporté contient la cascade complète, de sorte que Braze évalue la priorité du pool et les dates à chaque envoi.

À partir de maintenant, vous mettez à jour le pool, pas l'e-mail. Les flux déclenchés, les newsletters permanentes et les campagnes saisonnières restent tous à jour tant que le pool est à jour.

Retrouvez vos modèles Building Blocks téléversés dans Braze sous **Modèles et médias** > **Modèles d'e-mail**. Les feuilles de style et blocs synchronisés apparaissent sous **Modèles et médias** > **Content Blocks**.

## Considérations {#considerations}

- **Une seule instance Braze par espace d'équipe Building Blocks.** Chaque équipe Building Blocks se connecte à une seule instance Braze. Les clients utilisant plusieurs espaces de travail (marques, régions ou environnements distincts) peuvent les ajouter à la même équipe, ce qui permet le partage de blocs.
- **Les autorisations des clés API sont séparées.** Les clés pour les modèles et les clés pour les Content Blocks sont distinctes. La validation échoue rapidement si une clé ne dispose pas d'une portée requise, de sorte que vous savez exactement quelle autorisation ajouter dans Braze.
- **Les noms des Content Blocks sont préfixés.** Building Blocks envoie les Content Blocks avec les préfixes `CP_` (blocs) et `cp_` (feuilles de style) pour éviter les collisions avec les Content Blocks créés directement dans Braze.
- **Les modifications de feuille de style mettent à jour chaque e-mail.** Les feuilles de style sont rendues sous forme d'un seul Content Block Braze référencé par chaque modèle. Une modification dans Building Blocks met à jour chaque e-mail dans Braze qui l'utilise, y compris ceux déjà planifiés. Testez les modifications de feuille de style dans un modèle brouillon avant de synchroniser.
- **La liaison aux Catalogues est en lecture seule.** Building Blocks lit les catalogues pour alimenter l'interface de liaison. Il n'écrit pas dans les Catalogues Braze. Toute la gestion des catalogues se fait toujours dans le tableau de bord de Braze.
- **Limites de débit et nouvelles tentatives.** Toutes les requêtes sortantes respectent les limites de débit de Braze, avec des délais exponentiels, du jitter et la gestion de Retry-After. Un en-tête `User-Agent: partner-CopyPastd` est envoyé à chaque appel pour l'attribution partenaire.
- **Aucune donnée utilisateur n'est transmise.** Building Blocks est un outil de création de contenu. Il n'envoie pas d'attributs utilisateur, d'événements, d'achats ou de données de segments vers Braze, et il ne consomme pas de points de donnée Braze.

## Résolution des problèmes {#troubleshooting}

- **La validation de la clé API échoue.** Vérifiez que chaque clé dispose des autorisations exactes listées dans les conditions préalables. Les portées des modèles et des Content Blocks sont vérifiées séparément. Si vous régénérez une clé dans Braze, collez la nouvelle valeur dans Building Blocks et revalidez.
- **Endpoint REST non concordant.** Les clés des modèles et des Content Blocks doivent provenir du même espace de travail Braze, et l'endpoint REST doit correspondre au cluster. Le menu déroulant de Building Blocks le configure pour vous ; vérifiez donc la sélection du cluster si la validation échoue.
- **L'envoi vers Braze renvoie une erreur.** Ouvrez **Settings** > **Build** > **Activity log** pour voir la dernière tentative de synchronisation et la réponse renvoyée par Braze. La plupart des échecs sont liés aux autorisations (portée manquante) ou aux quotas (limite de débit, nouvelle tentative automatique).
- **Le Content Block ne se met pas à jour dans Braze.** Déclenchez une resynchronisation manuelle depuis **Settings** > **Connect** > **Braze** > **Sync library**. Building Blocks effectue une comparaison et un remplacement, de sorte que les blocs inchangés sont ignorés.
- **Le modèle référence un Content Block qui n'existe pas encore dans Braze.** Envoyez d'abord les dépendances (feuille de style, blocs intelligents) en utilisant **Sync library**, puis envoyez le modèle.
- **Pour tout le reste.** Contactez Copy Pastd à [help@copypastd.com](mailto:help@copypastd.com). Incluez le nom de votre équipe et l'heure de l'action ayant échoué afin que Copy Pastd puisse consulter le journal d'activité correspondant.