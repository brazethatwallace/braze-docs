---
nav_title: Liquid code
article_title: Générer du code Liquid avec BrazeAI
description: "Cet article explique le fonctionnement de l'assistant Liquid BrazeAI et comment l'utiliser pour générer des extraits de code Liquid pour vos envois de messages."
page_type: reference
page_order: 0.0
---

# Générer du code Liquid avec BrazeAI {#generate-liquid-code-with-brazeai}

> L'assistant BrazeAI<sup>TM</sup> Liquid est un assistant de chat alimenté par BrazeAI<sup>TM</sup> qui aide à générer le Liquid dont vous avez besoin pour personnaliser le contenu de vos messages.

## À propos de l'assistant Liquid BrazeAI<sup>TM</sup> {#about-the-brazeaitm-liquid-assistant}

L'assistant Liquid BrazeAI<sup>TM</sup> est conçu pour vous aider à écrire du code Liquid efficace et adapté à vos besoins marketing. Formée à la syntaxe Liquid et à la manière dont les marketeurs utilisent Liquid dans leurs messages, notre intelligence artificielle comprend les nuances de l'élaboration d'un contenu personnalisé.

De plus, en fournissant à l'assistant Liquid BrazeAI<sup>TM</sup> vos noms d'attributs personnalisés (tels que « favourite_color ») et vos types de données (tels que booléen et chaîne de caractères), notre assistant Liquid BrazeAI<sup>TM</sup> garantit que vos messages sont précisément ciblés et alignés sur vos objectifs. En outre, si vous créez des directives de marque, l'assistant Liquid BrazeAI<sup>TM</sup> peut les utiliser pour mieux personnaliser les résultats générés et adapter le contenu à la voix de votre propre marque. Les directives de marque que vous créez ne seront utilisées que pour personnaliser le contenu pour votre propre usage.

## Canaux pris en charge {#supported-channels}

Vous pouvez utiliser l'assistant Liquid BrazeAI<sup>TM</sup> lors de la création de :
- Messages SMS
- Notifications push
- Messages e-mail en HTML
- Canvas

{% alert note %}
L'assistant fonctionne avec les messages e-mail et non avec les modèles. Il est plus performant sur les messages e-mail déjà créés.
{% endalert %}

## Générer du code Liquid {#generating-liquid-code}

Pour lancer l'assistant Liquid BrazeAI<sup>TM</sup>, sélectionnez l'icône de l'assistant IA dans le composeur de messages.

![Composeur de messages avec l'assistant d'intelligence artificielle.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Vous pouvez choisir l'une des invites incluses ou saisir la vôtre dans la zone de texte.

{% tabs local %}
{% tab Utiliser l'activité de l'app %}
L'invite **Utiliser l'activité de l'app** génère du code Liquid pour vous aider à envoyer différents messages en fonction de la date de dernière utilisation de votre app. L'assistant peut vous poser des questions complémentaires afin de générer un résultat plus précis.

![Exemple de résultat de l'invite « Utiliser l'activité de l'app ».]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab Ajouter un compte à rebours %}
Cette invite génère du code Liquid qui envoie un message indiquant le temps restant avant qu'un événement ne se produise. Vous serez invité à fournir des détails sur la date et l'heure de l'événement.

![Exemple de résultat de l'invite « Ajouter un compte à rebours ».]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab Inspirez-moi %}
Cette invite apparaît lorsque votre zone de message contient du contenu. Elle génère une liste d'options parmi lesquelles vous pouvez choisir pour personnaliser votre message avec Liquid.

![Exemple de résultat de l'invite « Inspirez-moi ».]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab Améliorer mon Liquid %}
Cette invite apparaît lorsque votre composeur de messages contient du contenu. Sélectionnez-la lorsque vous souhaitez que l'assistant rende votre code plus efficace et plus facile à lire.

![Exemple de résultat de l'invite « Améliorer mon Liquid ».]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Pour générer votre code Liquid, sélectionnez **Update composer**.

![Fenêtre de l'assistant d'intelligence artificielle avec les invites fournies.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}

Vous pouvez générer un autre message en utilisant la même invite en sélectionnant **Regenerate**. Pour supprimer le message et revenir au précédent, sélectionnez **Undo update**.

## Attributs Liquid {#supported-attributes}

Les attributs suivants sont actuellement en version bêta pour l'assistant Liquid BrazeAI<sup>TM</sup> :

| Critère | Type de connaissance |
| - | - |
| Liquid (y compris les boucles `for`, les instructions `if`, les calculs mathématiques et autres) | Codage |
| Attributs utilisateur par défaut et standard | Attributs |
| Attributs personnalisés qui possèdent l'un de ces types de données : {::nomarkdown}<ul><li>Booléens</li><li>Nombres</li><li>Chaînes de caractères</li><li>Tableaux</li><li>Date</li></ul>{:/} | Attributs |
| Contenu connecté | Codage |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid attributes" }

## Bonnes pratiques {#best-practices}

Pour vous aider à rédiger des invites efficaces pour l'assistant Liquid BrazeAI<sup>TM</sup>, consultez nos bonnes pratiques :

### Utiliser le langage naturel {#use-natural-language}

L'assistant Liquid BrazeAI<sup>TM</sup> est formé pour comprendre le langage naturel. Discutez avec lui comme vous le feriez avec un collègue lorsque vous demandez de l'aide. Il est ainsi plus facile pour l'assistant de comprendre vos besoins et de vous fournir une assistance précise.

### Préciser le contexte {#give-context}

Fournir du contexte aide l'assistant Liquid BrazeAI<sup>TM</sup> à comprendre la situation globale de votre projet. Il est utile d'inclure des éléments de contexte tels que :

- Le nom de votre entreprise et votre secteur d'activité
- Une campagne sur laquelle vous travaillez, comme le Black Friday ou les promotions de fin d'année
- Votre objectif, tel que l'augmentation de votre taux de clics
- Les attributs personnalisés spécifiques que vous souhaitez inclure dans votre message

Inclure du contexte dans votre invite permet à l'assistant d'adapter ses réponses à vos besoins. Vous pouvez également inclure des détails de votre campagne, de votre brief de message ou de votre document de réflexion pour mettre l'assistant au courant.

### Être précis {#be-specific}

L'assistant Liquid BrazeAI<sup>TM</sup> peut poser des questions de suivi, mais fournir des détails dès le départ peut permettre d'obtenir des résultats plus précis plus rapidement. Pensez à inclure des détails tels que :

- Toute préférence ou exigence connue concernant le message
- Des instructions sur la manière de gérer certaines situations, telles que l'absence de réponse du destinataire du message ou les options de message de repli
- Lorsque vous demandez du code Liquid qui utilise du contenu connecté, la documentation de l'endpoint de l'API, un exemple de réponse de l'API, ou les deux

### Faire preuve de créativité {#get-creative}

Sortez des sentiers battus avec vos invites pour voir comment l'assistant Liquid BrazeAI<sup>TM</sup> peut améliorer votre communication. Expérimentez avec différentes invites et idées : la créativité peut déboucher sur des résultats plus engageants.

## Exemples d'invites {#example-prompts}

Voici quelques exemples pour vous aider à démarrer :

{% tabs local %}
{% tab Acquérir des connaissances %}
- Qu'est-ce que Liquid, et comment peut-il m'aider à améliorer la personnalisation de mes campagnes marketing dans Braze ?
- Quels types de données puis-je utiliser dans Liquid pour personnaliser mes messages marketing, tels que des informations démographiques ou des achats antérieurs ?
{% endtab %}

{% tab Personnaliser du contenu dynamique %}
- Crée un message qui affiche un contenu différent en fonction du statut de fidélité de mon client. Si nous ne connaissons pas son statut de fidélité, envoie un message de repli.
- Rédige un message dynamique indiquant le produit préféré d'un utilisateur et la date de son dernier achat. S'il n'y a pas de dernier achat, annule le message.
- Écris-moi du code Liquid pour encourager quelqu'un à cliquer sur mon message, avec un compte à rebours indiquant le temps restant. Si l'offre a expiré, interromps le message.
- Aide-moi à rédiger un message pour encourager les utilisateurs à revenir et à procéder au paiement s'il leur reste des articles dans leur panier.
- Écris du code Liquid pour personnaliser un message en fonction du pays d'un client. Je veux remplir le message avec le nom du pays. Si nous ne disposons d'aucune de ces informations, suggère-leur de cliquer sur un lien pour mettre à jour leur profil.
- Comment puis-je personnaliser un message de bienvenue avec le prénom d'un utilisateur et rédiger un texte différent en fonction du genre de l'utilisateur ?
- Écris du code Liquid pour afficher différents messages en fonction d'un attribut personnalisé, « CUSTOM_ATTRIBUTE_NAME », et de sa valeur. Il y a six options différentes que je pourrais envoyer. S'il n'y a pas de valeur pour l'attribut personnalisé, je veux envoyer un message substitutif.
{% endtab %}

{% tab Gérer les cas particuliers %}
- Peux-tu me donner des exemples d'utilisation de Liquid dans des campagnes marketing pour augmenter les taux d'engagement et de conversion ?
- Quels sont les cas d'utilisation courants de Liquid dans des SMS pour les soldes d'été, par exemple les rappels de panier abandonné ou les promotions personnalisées ?
{% endtab %}
{% endtabs %}

{% alert tip %}
Faites-nous savoir si vous avez eu des invites ou des expériences intéressantes en réservant une [session de feedback](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) avec nous.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}