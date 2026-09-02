---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "Cet article de référence décrit le partenariat entre Braze et Copy Pastd, un générateur d'e-mails par glisser-déposer qui envoie des Content Blocks et des modèles alimentés par Liquid directement dans votre espace de travail Braze."
page_type: partner
search_tag: Partner
---

# Copy Pastd

> [Copy Pastd](https://copypastd.com/) propose Building Blocks, un générateur d'e-mails par glisser-déposer qui envoie des Content Blocks alimentés par Liquid et des modèles complets directement dans votre espace de travail Braze. Concevez une fois, synchronisez avec Braze et réutilisez les mêmes composants dans vos Campaigns, Canvas et flux déclenchés sans recréer le HTML à chaque fois.

_Cette intégration est maintenue par Copy Pastd._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Copy Pastd vous permet de créer des e-mails dans Building Blocks, un générateur d'e-mails hébergé qui produit un rendu natif Braze avec du Liquid propre, des références aux Content Blocks et des modèles qui s'intègrent directement dans n'importe quelle Campaign ou Canvas sans conversion.

Vous pouvez assembler un e-mail à partir de blocs réutilisables, l'envoyer vers Braze en un clic et avoir la certitude que les mêmes styles de marque, composants et contenus dynamiques s'affichent de manière cohérente à chaque envoi. Le résultat : moins de modèles codés à la main, moins de temps consacré à la création et à l'envoi d'e-mails, et une bibliothèque centralisée qui se met à jour partout dès qu'elle est modifiée.

## Prérequis {#prerequisites}

Les éléments suivants sont nécessaires pour utiliser cette intégration :

| Condition | Description |
| ----------- | ----------- |
| Compte Copy Pastd | Requis pour utiliser Building Blocks. Inscrivez-vous sur [copypastd.com](https://copypastd.com). Chaque client reçoit un espace de travail, une bibliothèque de feuilles de style, cinq sièges de générateur et une bibliothèque de blocs. |
| Clé API REST Braze pour les modèles d'e-mail | Une clé API avec les permissions `templates.email.create`, `templates.email.update` et `templates.email.list`.<br><br>Créez la clé dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Clé API REST Braze pour les Content Blocks | Une clé API avec les permissions `content_blocks.create`, `content_blocks.update`, `content_blocks.info` et `content_blocks.list`.<br><br>Créez la clé dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Clé API REST Braze pour les catalogues (facultatif) | Une clé API avec un accès en lecture à `catalogs.get`, `catalogs.get_item` et `catalogs.get_selections`. Requise uniquement si vous prévoyez de lier des blocs aux catalogues Braze. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. Building Blocks sélectionne automatiquement l'endpoint en fonction du cluster que vous choisissez. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Cas d'usage {#use-cases}

* **Création cohérente avec la marque à grande échelle.** Appliquez une feuille de style Building Blocks à chaque modèle : les couleurs, polices, styles de boutons et marges s'affichent de manière identique dans des centaines d'e-mails. Lorsque la marque évolue, mettez à jour la feuille de style une seule fois et resynchronisez pour déployer la modification dans tous vos e-mails en une seule opération.
* **Modèles de produits liés au contenu connecté et aux catalogues.** Associez les champs de blocs d'e-mail directement à vos endpoints de [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) et à vos [catalogues Braze]({{site.baseurl}}/user_guide/data/activation/catalogs) depuis le générateur. Réutilisez le même modèle pour de nouveaux lancements de produits, des collections saisonnières ou des actualisations de contenu sans toucher au Liquid.
* **Production d'e-mails en libre-service pour les marketeurs non techniques.** Composez un e-mail complet à partir de blocs approuvés, y compris la personnalisation et la logique Liquid, puis envoyez-le vers Braze pour révision sans avoir besoin d'un développeur pour écrire ou relire le HTML ou le Liquid.
* **En-têtes et pieds de page centralisés, mis à jour en un clic.** Créez un en-tête ou un pied de page une seule fois dans le générateur Building Blocks et envoyez-le vers Braze. Chaque modèle qui le référence reste synchronisé : un changement de logo, une mise à jour de mentions juridiques ou un nouveau lien vers les réseaux sociaux ne nécessite qu'une seule modification dans Building Blocks pour se propager à tous les e-mails déjà dans Braze.
* **Contenu centralisé pour tous les e-mails.** Créez un bloc hero, un pied de page ou une carte promotionnelle une seule fois en tant que bloc intelligent Building Blocks. Mettez-le à jour, synchronisez, et chaque e-mail déjà dans Braze qui le référence intègre la modification lors du prochain envoi. Les flux de bienvenue, les newsletters hebdomadaires et les parcours déclenchés restent à jour sans avoir à modifier chaque Campaign.
* **Modèles verrouillés pour le libre-service des contributeurs.** Créez des modèles, verrouillez les champs de votre choix, puis invitez d'autres équipes à composer leurs propres e-mails depuis une interface contributeur sans leur donner accès aux outils destinés aux utilisateurs.

## Intégration {#integration}

### Étape 1 : Connecter Building Blocks à Braze {#step-1-connect-building-blocks-to-braze}

{% alert note %}
La connexion de Building Blocks à Braze est une configuration unique. Une fois vos identifiants validés, Building Blocks les enregistre pour toutes les synchronisations et tous les envois de modèles futurs.
{% endalert %}

1. Connectez-vous à Building Blocks sur [blocks.copypastd.com](https://blocks.copypastd.com), ou sélectionnez **Login** sur [copypastd.com](https://copypastd.com).
2. Depuis le tableau de bord, sélectionnez **Set up your Braze connection**. (Cette pastille apparaît pour les administrateurs lors de la première connexion et jusqu'à ce que la configuration soit terminée. Vous pouvez également accéder à la page depuis **Team Settings** > **Connect** > **Braze API Keys**.)
3. Sélectionnez votre cluster Braze dans le menu déroulant. L'endpoint REST correspondant est automatiquement renseigné.
4. Collez votre clé API Templates, votre clé API Content Blocks et (facultativement) votre clé API Catalogs dans les champs correspondants.
5. Sélectionnez **Validate and save**. Building Blocks appelle Braze pour confirmer que les clés fonctionnent et que les périmètres d'autorisation sont corrects. Si quelque chose manque, une erreur en ligne vous indique quel périmètre est incorrect.

### Étape 2 : Synchroniser votre bibliothèque avec Braze {#step-2-sync-your-library-to-braze}

1. Une fois les clés validées, sélectionnez **Sync now** dans la fenêtre modale de configuration. (Vous pouvez également resynchroniser à tout moment depuis **Settings** > **Connect** > **Braze** > **Sync library**.) <br> Building Blocks envoie votre feuille de style et vos blocs dans votre espace de travail Braze sous forme de Content Blocks Braze. Ils apparaissent dans Braze avec des noms préfixés par `CP_` (par exemple, `CP_Hero_1`) ou `cp_` pour les feuilles de style (par exemple, `cp_default_style`).
2. Une fois la synchronisation terminée, vous pouvez envoyer des modèles individuels depuis le générateur en utilisant **Push to Braze**.

## Personnaliser les Building Blocks {#customize-building-blocks}

### Étape 1 : Configurer votre feuille de style {#step-1-set-up-your-stylesheet}

1. Dans Building Blocks, accédez à **Settings** > **Build** > **Stylesheets**.
2. Modifiez la feuille de style par défaut ou créez-en une nouvelle. Définissez votre palette de couleurs (24 couleurs nommées), vos polices (Google Fonts pris en charge), les styles de boutons, les styles de liens, les rayons et l'échelle de padding.
3. Sélectionnez **Save**. Building Blocks régénère le Liquid pour chaque bloc qui utilise cette feuille de style.
4. Sélectionnez **Sync now** pour envoyer les styles mis à jour dans votre espace de travail Braze.

### Étape 2 : Activer les endpoints de contenu connecté (facultatif) {#step-2-enable-connected-content-endpoints-optional}

1. Dans Building Blocks, accédez à **Settings** > **Connect** > **Connected Content endpoints**.
2. Ajoutez l'URL de l'endpoint, nommez-le et enregistrez. Building Blocks prend en charge un format de réponse Google Sheets en plus du format JSON standard.
3. Dans le générateur, liez n'importe quel champ de texte, d'image ou de lien à une variable de contenu connecté depuis le panneau **Personalize**. Le Liquid {% raw %}`{% connected_content %}`{% endraw %} correct est généré à l'exportation.

### Étape 3 : Lier aux catalogues Braze (facultatif) {#step-3-bind-to-braze-catalogs-optional}

1. Dans Building Blocks, accédez à **Settings** > **Connect** > **Catalogs**. Building Blocks lit votre liste de catalogues à l'aide de la clé API Catalogs.
2. Ouvrez un bloc compatible (par exemple, une grille de produits).
3. Sélectionnez un catalogue et une sélection, puis mappez les champs du bloc aux attributs des éléments du catalogue.
4. Envoyez le modèle. Building Blocks génère le Liquid {% raw %}`{% catalog_items %}`{% endraw %} et {% raw %}`{% catalog_selection_items %}`{% endraw %} correct pour que Braze résolve les valeurs au moment de l'envoi.

### Étape 4 : Ajouter vos attributs personnalisés Braze (facultatif) {#step-4-add-your-braze-custom-attributes-optional}

Building Blocks est fourni avec les attributs utilisateur Braze par défaut (`first_name`, `email`, `country`, etc.). Pour lier des blocs à vos propres attributs personnalisés, importez-les une seule fois dans Building Blocks et ils restent disponibles dans chaque menu déroulant **Personalize**.

1. Dans Building Blocks, accédez à **Team Settings** > **Connect** > **Custom Attributes**.
2. Importez vos attributs personnalisés en utilisant l'une des méthodes suivantes :
* **Import en masse (recommandé).** Dans Braze, accédez à **Data Settings** > **Custom Attributes** et sélectionnez **Export**. Chargez le fichier CSV dans Building Blocks.
* **Ajouter les attributs un par un.** Saisissez le nom de l'attribut (par exemple, `loyalty_tier`) et sélectionnez **Add**. Cette méthode est utile si vous n'ajoutez que quelques attributs ou si vous souhaitez ajouter un nouvel attribut entre deux exports Braze.

Après l'enregistrement, vos attributs personnalisés apparaissent dans le menu déroulant **Personalize** du générateur aux côtés des attributs par défaut. L'insertion d'un attribut génère le Liquid {% raw %}`{{custom_attribute.${name}}}`{% endraw %} correct à l'exportation, afin que Braze résolve la valeur par destinataire au moment de l'envoi.

## Utiliser l'intégration {#use-the-integration}

### Étape 1 : Envoyer un modèle vers Braze {#step-1-push-a-template-to-braze}

1. Ouvrez n'importe quel e-mail dans le générateur Building Blocks.
2. Sélectionnez **Push to Braze** dans la barre d'actions.
3. Sélectionnez l'espace de travail et confirmez. Building Blocks crée un modèle d'e-mail dans Braze avec le Liquid rendu.

Le modèle apparaît dans Braze sous **Modèles et médias** > **Modèles d'e-mail**, nommé d'après l'e-mail et la date sélectionnée dans les paramètres de l'e-mail.

### Étape 2 : Utiliser le modèle dans une Campaign ou un Canvas {#step-2-use-the-template-in-a-campaign-or-canvas}

1. Dans Braze, créez une nouvelle Campaign d'e-mail ou une étape Canvas.
2. Sélectionnez **Templates** et choisissez le modèle envoyé par Building Blocks.

Le modèle contient chaque référence Building Blocks (feuille de style, Content Blocks) sous forme de Liquid {% raw %}`{{content_blocks.${...}}}`{% endraw %} en direct or en ligne/en production/instantané, de sorte que les mises à jour dans Building Blocks se propagent sans avoir à réimporter le modèle.

### Étape 3 : Mettre à jour le contenu de manière centralisée {#step-3-update-content-centrally}

1. Dans Building Blocks, modifiez le bloc ou la feuille de style concerné(e).
2. Sélectionnez **Sync** pour renvoyer le Content Block mis à jour vers Braze.

Chaque e-mail dans Braze qui le référence (flux permanents, déclenchés ou de bienvenue) récupère la nouvelle version lors du prochain envoi. Vous n'avez pas besoin de modifier chaque Campaign.

### Étape 4 : Créer des pools de contenu {#step-4-build-content-pools}

Les pools de contenu sont des tables de lignes de contenu que les e-mails référencent au lieu de contenir du texte statique. Mettez à jour le pool dans Building Blocks, et chaque e-mail dans Braze qui l'utilise diffuse le nouveau contenu lors du prochain envoi. Utilisez les pools de contenu partout où un même élément de contenu doit rester à jour dans de nombreux e-mails, comme les newsletters hebdomadaires, les flux de bienvenue, les séquences de reconquête, les Campaigns saisonnières ou les parcours post-achat.

1. Dans Building Blocks, sélectionnez **Content** dans la navigation principale.
2. Sélectionnez **New Pool**. Donnez un nom qui décrit son contenu (par exemple, Offres hebdomadaires, Catalogue produits, Articles d'actualité).
3. Choisissez le type de bloc alimenté par le pool (par exemple, Hero, Grid, Card). Cela détermine les champs disponibles pour chaque ligne.
4. Ajoutez des lignes. Chaque ligne correspond à un élément de contenu. Remplissez les champs (titre, image, texte du CTA, lien du CTA, etc.).
5. Définissez l'ordre de priorité en faisant glisser les lignes vers le haut ou vers le bas. Activez ou désactivez chaque ligne, et définissez des dates de début et de fin optionnelles. Au moment de l'envoi, la ligne active de plus haute priorité dont les dates sont valides l'emporte.
6. Cliquez sur **Save**. Les blocs intelligents peuvent désormais référencer ce pool.

### Étape 5 : Utiliser les blocs intelligents pour afficher le contenu du pool dans vos e-mails {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

Un bloc intelligent est un bloc sur le canevas du générateur qui référence un ou plusieurs pools de contenu au lieu de contenir du contenu statique. Au moment de l'envoi, Braze affiche la ligne du pool qui a la priorité la plus élevée, qui est active et dont les dates sont valides. Le Liquid exporté fait le travail. Aucune configuration supplémentaire dans Braze n'est nécessaire.

1. Dans Building Blocks, faites glisser un bloc intelligent sur le canevas (tout type de bloc disposant d'un pool correspondant).
2. Dans le panneau de propriétés, ouvrez l'éditeur de cascade.
3. Ajoutez un ou plusieurs pools de contenu par ordre de priorité. Il s'agit de la cascade : le premier pool contenant une ligne active et valide en termes de dates est affiché. S'il n'a rien d'actif, le bloc intelligent passe au pool suivant, puis au suivant. Un schéma courant est Vente flash > Offres hebdomadaires > Favoris permanents, de sorte qu'il y a toujours quelque chose à afficher.
4. Envoyez le modèle vers Braze. Le Liquid exporté contient la cascade complète, de sorte que Braze évalue la priorité du pool et les dates à chaque envoi.

Désormais, vous mettez à jour le pool, pas l'e-mail. Les flux déclenchés, les newsletters permanentes et les Campaigns saisonnières restent tous à jour tant que le pool est à jour.

Retrouvez vos modèles Building Blocks importés dans Braze sous **Modèles et médias** > **Modèles d'e-mail**. Les feuilles de style et les blocs synchronisés apparaissent sous **Modèles et médias** > **Content Blocks**.

## Considérations {#considerations}

- **Une seule instance Braze par espace d'équipe Building Blocks.** Chaque équipe Building Blocks se connecte à une seule instance Braze. Les clients qui utilisent plusieurs espaces de travail (marques, régions ou environnements distincts) peuvent les ajouter à la même équipe, ce qui permet de partager des blocs.
- **Les permissions des clés API sont définies séparément.** Les clés de modèles et les clés de Content Blocks sont distinctes. La validation échoue rapidement si une clé ne dispose pas d'un scope requis, ce qui vous permet de savoir exactement quelle permission ajouter dans Braze.
- **Les noms de Content Blocks sont préfixés.** Building Blocks envoie les Content Blocks avec les préfixes `CP_` (blocs) et `cp_` (feuilles de style) afin d'éviter les conflits avec les Content Blocks créés directement dans Braze.
- **Les modifications de feuilles de style mettent à jour tous les e-mails.** Les feuilles de style sont rendues sous la forme d'un seul Content Block Braze référencé par chaque modèle. Une modification dans Building Blocks met à jour tous les e-mails dans Braze qui l'utilisent, y compris ceux déjà planifiés. Testez les modifications de feuilles de style dans un modèle brouillon avant de synchroniser.
- **La liaison au catalogue est en lecture seule.** Building Blocks lit les catalogues pour alimenter l'interface de liaison. Il n'écrit pas dans les catalogues Braze. Toute la gestion des catalogues se fait toujours dans le tableau de bord de Braze.
- **Limitations du débit et nouvelles tentatives.** Toutes les requêtes sortantes respectent les limitations du débit de Braze, avec des délais exponentiels, du jitter et la gestion de l'en-tête Retry-After. Un en-tête `User-Agent: partner-CopyPastd` est envoyé à chaque appel pour l'attribution partenaire.
- **Aucune donnée utilisateur n'est transmise.** Building Blocks est un outil de création de contenu. Il n'envoie pas d'attributs utilisateur, d'événements, d'achats ni de données de Segment à Braze, et il ne consomme pas de points de donnée Braze.

## Résolution des problèmes {#troubleshooting}

- **La validation de la clé API échoue.** Vérifiez que chaque clé dispose des permissions exactes indiquées dans les prérequis. Les portées des modèles et des Content Blocks sont vérifiées séparément. Si vous régénérez une clé dans Braze, collez la nouvelle valeur dans Building Blocks et relancez la validation.
- **Incohérence de l'endpoint REST.** Les clés des modèles et des Content Blocks doivent provenir du même espace de travail Braze, et l'endpoint REST doit correspondre au cluster. Le menu déroulant de Building Blocks configure cela automatiquement : vérifiez donc la sélection du cluster si la validation échoue.
- **L'envoi vers Braze renvoie une erreur.** Ouvrez **Settings** > **Build** > **Activity log** pour consulter la dernière tentative de synchronisation et la réponse renvoyée par Braze. La plupart des échecs sont liés aux permissions (portée manquante) ou aux quotas (limitation du débit, réessayée automatiquement).
- **Le Content Block ne se met pas à jour dans Braze.** Déclenchez une resynchronisation manuelle depuis **Settings** > **Connect** > **Braze** > **Sync library**. Building Blocks effectue une comparaison avant remplacement : les blocs inchangés sont donc ignorés.
- **Un modèle fait référence à un Content Block qui n'existe pas encore dans Braze.** Envoyez d'abord les dépendances (feuille de style, blocs intelligents) via **Sync library**, puis envoyez le modèle.
- **Pour tout autre problème.** Contactez Copy Pastd à l'adresse [help@copypastd.com](mailto:help@copypastd.com). Indiquez le nom de votre équipe et l'heure de l'action ayant échoué afin que Copy Pastd puisse retrouver l'entrée correspondante dans le journal d'activité.