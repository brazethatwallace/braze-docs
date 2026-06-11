---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "Cet article de référence présente le partenariat entre Braze et Movable Ink, une plateforme logicielle basée sur le cloud qui permet aux marketeurs numériques de créer des expériences visuelles convaincantes et uniques pour engager les clients."
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) est une plateforme logicielle basée sur le cloud qui permet aux marketeurs numériques de créer des expériences visuelles convaincantes et uniques pour engager les clients. La plateforme Movable Ink offre de précieuses options de personnalisation qui peuvent être facilement insérées dans vos Campaigns.

_Cette intégration est maintenue par Movable Ink._

## À propos de l'intégration {#about-the-integration}

Étendez vos capacités créatives en tirant parti des fonctionnalités de création intelligente de Movable Ink, telles que le sondage, le compte à rebours et le grattage. L'intégration de Movable Ink et de Braze permet une approche plus complète des messages dynamiques axés sur les données, en fournissant aux utilisateurs des éléments en temps réel sur les sujets qui comptent.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Movable Ink | Un compte Movable Ink est nécessaire pour bénéficier de ce partenariat. |
| Source de données | Vous devez connecter une source de données à Movable Ink. Cela peut se faire par le biais d'un fichier CSV, de l'importation d'un site web ou d'une API. Veillez à transmettre les données avec un identifiant commun entre Braze et Movable Ink (par exemple, `external_id`).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Cas d'utilisation {#use-cases}

- Récapitulatifs mensuels ou de fin d'année personnalisés.
- Personnalisez dynamiquement les images pour les e-mails, les notifications push ou les notifications riches en fonction du dernier comportement connu.<br>
	Par exemple :
	- Utilisation d'un message push riche pour créer dynamiquement un calendrier d'événements en tirant des données de l'API.
	- Utilisation du compte à rebours pour avertir les utilisateurs de l'imminence d'une grande vente (par exemple, le Black Friday, la Saint-Valentin ou des offres de fêtes).
	- Utilisation de la fonctionnalité de grattage comme un moyen amusant et interactif de distribuer des codes de promotion.

## Capacités Movable Ink prises en charge {#supported-movable-ink-capabilities}

Intelligent Creative propose de nombreuses offres dont les utilisateurs peuvent profiter. La liste suivante indique les capacités prises en charge.

| Capacité Movable Ink | Fonctionnalité | Notification push enrichie | Messages in-app / Content Cards / e-mail | Détails |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Creative Optimizer | Affichage du contenu des tests A/B | ✗ | ✔ | |
| Optimiser | ✗ | ✔* | * Vous devez utiliser la solution de création de liens profonds de Branch |
| Règles de ciblage | Date | ✔* | ✔ | * Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas |
| Jour de la semaine | ✔* | ✔ | * Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas |
| Heure de la journée | ✔* | ✔ | * Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas |
| Stories/Activités comportementales | | ✔* | ✔* | * L'identifiant unique de l'utilisateur utilisé pour Braze doit être lié à l'identifiant de votre ESP |
| Création de liens profonds dans l'application | | ✔* | ✔* | * Pour offrir une expérience fluide à vos clients, utilisez une solution de création de liens profonds établie via Branch ou une solution validée avec l'équipe Expérience client de Movable Ink. |
| Applications | Compte à rebours | ✔* | ✔ | * Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas |
| Sondage | ✗ | ✔* | * Après avoir voté, l'utilisateur quittera l'application pour accéder à une page d'accueil mobile |
| Grattage | ✔* | ✔* | * En cliquant, l'utilisateur quittera l'application pour accéder à l'expérience de grattage |
| Vidéo | ✔* | ✔* | * Uniquement les GIF animés, <br>Pour Android, Braze exige la [prise en charge du format GIF]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) dans l'implémentation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Supported Movable Ink capabilities" }

## Intégration {#integration}

### Étape 1 : Créer une source de données pour Movable Ink {#step-1-create-a-data-source-for-movable-ink}

Les clients devront créer une source de données qui peut être un CSV, une importation de site web ou une intégration API.

![Différentes options de sources de données apparaissent : chargement d'un CSV, site web ou intégration API.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV Data Source %}
- **Source de données CSV** : chaque ligne doit comporter au moins une colonne de segmentation et une colonne de contenu. Une fois votre fichier CSV téléchargé, sélectionnez les colonnes à utiliser pour le ciblage du contenu. [Exemple de fichier CSV]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Champs affichés en sélectionnant « CSV » comme source de données.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- **Source de données du site web** : chaque ligne doit comporter au moins une colonne de segmentation et une colonne de contenu. Une fois votre fichier CSV téléchargé, sélectionnez les colonnes à utiliser pour le ciblage du contenu.
  - Dans le cadre de ce processus, vous devez établir un mappage :
    - Quels champs seront utilisés comme Segments
    - Quels champs de données vous souhaitez voir personnalisés de manière dynamique dans la création (par exemple : attributs de l'utilisateur ou attributs personnalisés tels que le prénom, le nom, la ville, etc.)

![Champs affichés en sélectionnant « Website » comme source de données.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API Integrations %}
- **Intégrations API** : utilisez l'API de votre entreprise pour alimenter le contenu directement à partir d'une réponse d'API.

![Champs affichés en sélectionnant « API Integration » comme source de données.]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Étape 2 : Créer une Campaign sur la plateforme Movable Ink {#step-2-create-a-campaign-on-the-movable-ink-platform}

Depuis l'écran d'accueil de Movable Ink, créez une Campaign. Vous pouvez choisir entre un e-mail à partir de code HTML, un e-mail à partir d'une image ou un bloc pouvant être utilisé dans n'importe quel canal, y compris les notifications push, les messages in-app et les Content Cards (recommandé).

Nous vous suggérons également de jeter un coup d'œil aux différentes options de contenu disponibles par le biais des blocs.

![Aperçu de la plateforme Movable Ink lors de la création d'une nouvelle Campaign Movable Ink.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink dispose d'un éditeur convivial qui vous permet de glisser-déposer des éléments tels que du texte ou des images. Si vous avez rempli votre source de données, vous pouvez générer dynamiquement une image à l'aide des propriétés des données. En outre, vous pouvez également créer des solutions de repli dans ce flux pour les utilisateurs si la Campaign est envoyée et qu'un utilisateur ne correspond pas aux critères de personnalisation.

![L'éditeur de blocs Movable Ink affichant les différents éléments personnalisables.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Avant de terminer votre Campaign, veillez à prévisualiser les images dynamiques et à tester les paramètres de requête pour voir à quoi ressembleront les images lors de leur affichage. Une fois l'opération terminée, une URL dynamique sera générée et pourra être insérée dans Braze !

Pour plus d'informations sur l'utilisation de la plateforme Movable Ink, consultez le [centre d'assistance Movable Ink](https://support.movableink.com/).

### Étape 3 : Obtenir l'URL du contenu Movable Ink {#step-3-obtain-movable-ink-content-url}

Pour inclure le contenu Movable Ink dans les messages Braze, vous devez localiser l'URL source que Movable Ink vous a fournie.

Pour obtenir l'URL source, vous devez avoir configuré le contenu dans le tableau de bord Movable Ink, puis terminer et exporter votre contenu. Sur la page **Finish**, copiez l'URL source (`img src`) de la balise du contenu créatif.

![La page qui s'affiche une fois que vous avez terminé votre Campaign Movable Ink ; vous y trouverez l'URL de votre contenu.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Ensuite, dans la plateforme Braze, collez l'URL dans le champ approprié. Les champs appropriés pour votre canal de communication sont indiqués à l'étape 4. Enfin, remplacez toutes les balises de fusion (telles que {% raw %}`&mi_u=%%email%%`{% endraw %}) par la variable Liquid correspondante (telle que {% raw %}`&mi_u={{${email_address}}}`{% endraw %}).

### Étape 4 : Expérience Braze {#step-4-braze-experience}

{% tabs local %}
{% tab Email %}
Dans la plateforme Braze, collez votre balise créative dans le corps de votre e-mail.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Push notification %}

1. Dans la plateforme Braze :
	- Notification push Android : collez l'URL dans les champs **Push Icon Image** et **Expanded Notification Image**.<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- Notification push iOS : collez l'URL dans le champ de lien **Media** et indiquez le format de fichier que vous utilisez.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Notification push Web : collez l'URL dans les champs **Push Icon Image** et **Large Notification Image**.<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Pour vous assurer que les images ne sont pas mises en cache, placez des balises Liquid vides avant l'URL de l'image dans le message : <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}

{% endtab %}
{% tab In-app message %}

1. Dans la plateforme Braze, collez l'URL dans le champ **Rich Notification Media**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Fournissez une URL unique pour éviter la mise en cache. Pour confirmer que les images en temps réel de Movable Ink fonctionnent et ne seront pas affectées par la mise en cache, utilisez Liquid pour ajouter un horodatage à la fin de l'URL de l'image Movable Ink.

Pour ce faire, utilisez la syntaxe suivante, en remplaçant l'URL de l'image si nécessaire :
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Ce modèle prend l'heure actuelle (en secondes), l'ajoute à la fin de l'onglet image de Movable Ink (en tant que paramètre de requête), puis affiche le résultat final. Vous pouvez le prévisualiser à l'aide de l'onglet **Test** — celui-ci évalue le code et affiche un aperçu.

**3.** Enfin, réévaluez l'appartenance au segment. Pour ce faire, activez l'option `Re-evaluate audience membership and liquid at send-time` située à l'étape **Target Audiences** d'une Campaign. Si cette option n'est pas disponible, contactez votre gestionnaire de la satisfaction client ou l'assistance Braze. Cette option indiquera aux SDK de Braze de redemander la Campaign, en fournissant une URL unique à chaque fois qu'un message in-app est déclenché.

{% endtab %}
{% tab Content Card %}

1. Dans la plateforme Braze, collez l'URL dans le champ **Rich Notification Media**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Pour les mobiles : les images des Content Cards sur iOS et Android sont mises en cache dès leur réception et ne s'actualisent pas.
  - Pour contourner ce problème, planifiez votre Campaign comme un message récurrent quotidien, hebdomadaire ou mensuel avec une date d'expiration correspondante afin que la Content Card soit reformatée. Par exemple, une Content Card qui doit être actualisée une fois par jour doit être définie comme un envoi planifié quotidien avec une expiration d'un jour.
3. Pour garantir que les images en temps réel de Movable Ink fonctionnent et ne seront pas affectées par la mise en cache lorsque la Content Card est reformatée, utilisez Liquid pour ajouter un horodatage à la fin de l'URL de l'image Movable Ink.

Pour ce faire, utilisez la syntaxe suivante, en remplaçant l'URL de l'image si nécessaire :
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Ce modèle prend l'heure actuelle (en secondes), l'ajoute à la fin de l'onglet image de Movable Ink (en tant que paramètre de requête), puis affiche le résultat final. Vous pouvez le prévisualiser à l'aide de l'onglet **Test**, qui évaluera le code et affichera un aperçu.

{% endtab %}
{% endtabs %}

## Résolution des problèmes {#troubleshooting}

### Les images dynamiques ne s'affichent pas correctement ? Quel est le canal qui vous pose problème ? {#dynamic-images-not-showing-correctly-what-channel-are-you-experiencing-difficulties-with}
- **Notification push** : veillez à ce que l'URL de votre image Movable Ink soit précédée d'une logique vide : <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}
- **Messages in-app et Content Cards** : veillez à ce que l'URL de l'image soit unique pour chaque impression. Pour ce faire, ajoutez la balise Liquid appropriée pour différencier toutes les URL. Voir les [instructions relatives aux messages in-app et aux Content Cards]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/#step-4-braze-experience).
- **L'image ne se charge pas** : veillez à remplacer toutes les « balises de fusion » par les champs Liquid correspondants dans le tableau de bord de Braze. Par exemple : {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u=%%email%%`{% endraw %} avec {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}`{% endraw %}.

### Vous avez des difficultés à afficher des GIF sur Android ? {#having-trouble-showing-gifs-on-android}
- Android exige la prise en charge du format GIF dans l'implémentation. Suivez l'article sur la [personnalisation des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) pour Android si vous n'avez pas cette configuration.


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})