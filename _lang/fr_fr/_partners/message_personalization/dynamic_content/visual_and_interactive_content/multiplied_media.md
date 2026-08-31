---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Découvrez comment utiliser Multiplied Media avec Braze pour envoyer des images personnalisées, des GIF et des vidéos par e-mail, notifications push, messages in-app, Content Cards et WhatsApp."
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> [Multiplied Media](https://multiplied.media) est un studio de création et d'automatisation qui utilise vos données CRM pour créer des images personnalisées, des GIF et des vidéos — une ressource unique pour chaque client. L'intégration de Multiplied Media et Braze vous permet d'envoyer ces médias par e-mail, notifications push, messages in-app, Content Cards et WhatsApp.
>
> Multiplied Media est un service géré, pas un outil logiciel. L'équipe Multiplied Media prend en charge le concept, le design, l'animation, la connexion des données et le rendu. Pour utiliser cette intégration, insérez une URL de média avec une balise de fusion [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dans votre Campaign ou Canvas.

_Cette intégration est maintenue par Multiplied Media._

## À propos de cette intégration {#about-this-integration}

L'équipe Multiplied Media travaille avec vous du premier concept jusqu'au lancement. Elle conçoit et anime des médias pour votre marque, connecte vos données et automatise le rendu. Vous n'avez pas besoin d'apprendre un nouveau logiciel.

L'intégration connecte vos données Braze — attributs personnalisés et Segments — à Multiplied Media. Multiplied Media génère une ressource média unique pour chaque client et l'héberge à une URL contenant l'identifiant de ce client. Vous référencez cette URL dans votre message Braze à l'aide d'une étiquette Liquid de fusion. Chaque client voit alors sa propre image, son propre GIF ou sa propre vidéo.

L'intégration prend en charge deux flux :

- **Campaigns par lot :** Envoyez les données par CSV, S3 ou API. Multiplied Media génère et héberge tous les médias avant l'envoi.
- **Automatisations Canvas en temps réel :** Une étape [webhook]({{site.baseurl}}/user_guide/channels/webhooks) dans votre Canvas déclenche le rendu lorsqu'un client atteint cette étape.

## Cas d'usage {#use-cases}

- **Campaigns personnalisées :** Lancements de produits, campaigns « wrapped » et récapitulatifs de fin d'année, offres promotionnelles, et visualisations de données personnelles.
- **Automatisations permanentes :** Flux de bienvenue, onboarding, célébrations de jalons, e-mails de reconquête, panier abandonné, notifications d'expédition, alertes de retour en stock et mises à jour de fidélité.
- **Parcours omnicanaux :** Un concept, adapté à chaque canal. Les mêmes données client peuvent devenir une image principale d'e-mail, une image de notification push, un visuel in-app et une vidéo WhatsApp, de sorte qu'un parcours conserve une identité visuelle cohérente à chaque point de contact.

## Prérequis {#prerequisites}

L'architecture Multiplied Media prend en charge les Campaigns par lots via S3 ou API, ainsi que l'automatisation Canvas en temps réel via des webhooks. En pré-générant et en hébergeant des ressources média uniques avant la distribution, Multiplied Media garantit que des expériences visuelles individualisées sont prêtes à être intégrées dans vos modèles à l'aide d'étiquettes Liquid ou d'attributs personnalisés dès que votre message se déclenche.

Avant de commencer, vérifiez que vous disposez des éléments suivants :

| Condition | Description |
| --- | --- |
| Engagement actif avec Multiplied Media | Multiplied Media est un service géré. Avant de démarrer dans Braze, l'équipe Multiplied Media définit le périmètre de votre Campaign, conçoit et développe vos modèles média, et configure le rendu. Pour commencer, rendez-vous sur [multiplied.media](https://multiplied.media) ou écrivez à [hello@multiplied.media](mailto:hello@multiplied.media). |
| Source de données | Connectez vos données client à Multiplied Media par CSV, S3, API ou webhooks Braze. L'équipe Multiplied Media met cela en place avec vous lors de l'onboarding. |
| Identifiant unificateur | Vos données doivent inclure un identifiant partagé entre Braze et Multiplied Media, tel que `external_id`. Cet identifiant fait partie de l'URL média de chaque client, et votre message Braze le référence avec Liquid. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Utiliser Multiplied Media avec Braze {#use-multiplied-media-with-braze}

Multiplied Media conçoit, crée et génère vos médias personnalisés et vous aide à connecter vos données. Les étapes suivantes décrivent ce qu'il reste à faire dans Braze.

### Étape 1 : Confirmer que vos médias sont prêts {#step-1-confirm-your-media-is-ready}

Avant le lancement, l'équipe Multiplied Media confirme que vos médias sont générés (Campaigns par lot) ou que votre endpoint de rendu est en ligne (flux Canvas en temps réel). Elle vous fournit ensuite l'URL média de votre Campaign. Par exemple :

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

L'identifiant dans le chemin de l'URL est l'identifiant commun convenu lors de la configuration.

### Étape 2 : Insérer l'URL dans votre Campaign ou Canvas {#step-2-insert-the-url-into-your-campaign-or-canvas}

Collez l'URL Multiplied Media — avec l'étiquette Liquid de fusion — dans le champ correspondant à votre canal :

- **E-mail :** La source de l'image dans votre modèle d'e-mail.
- **Notifications push :** Le champ image de votre notification push.
- **In-App Messages et Content Cards :** Le champ média.
- **WhatsApp :** Le champ d'en-tête média.

Pour les automatisations Canvas en temps réel, ajoutez l'étape webhook Multiplied Media (configurée avec vous lors de l'onboarding) ainsi qu'un nœud de délai avant votre étape de message. Cela garantit que le média est généré pour chaque client avant la distribution.

### Étape 3 : Prévisualiser, tester et lancer {#step-3-preview-test-and-launch}

Utilisez les prévisualisations et les envois de test de Braze pour confirmer que l'étiquette Liquid se résout correctement et que chaque utilisateur test voit son propre média. L'équipe Multiplied Media examine les envois de test avec vous avant le lancement.

## Considérations {#considerations}

- Chaque ressource média est unique pour chaque client. Si un client ne figure pas dans la source de données connectée, l'URL renvoie une version par défaut (de secours) du média. Multiplied Media conçoit cette version de secours dans le cadre de chaque engagement.
- Multiplied Media génère et héberge les ressources avant la distribution ; elles ne sont pas générées au moment de l'ouverture. Le média se charge immédiatement à l'ouverture et affiche les données du client telles qu'elles étaient au moment du rendu. Si les données doivent être à jour au moment de l'envoi — par exemple, dans des flux Canvas déclenchés —, utilisez l'étape webhook en temps réel.
- Pour les Campaigns planifiées par lot, vos données doivent parvenir à Multiplied Media avant l'heure d'envoi afin que l'équipe puisse générer toutes les ressources. Votre équipe Multiplied Media convient du délai limite avec vous lors de la configuration.

## Résolution des problèmes {#troubleshooting}

Multiplied Media est un service géré, votre équipe Multiplied Media est donc votre premier point de contact pour l'assistance. Contactez-la à l'adresse [hello@multiplied.media](mailto:hello@multiplied.media).

Consultez le tableau suivant si votre image dynamique ne s'affiche pas.

| Problème | Résolution |
| --- | --- |
| L'image dynamique ne s'affiche pas | Confirmez que l'étiquette Liquid dans l'URL correspond à l'identifiant unifiant convenu lors de la configuration (par exemple, `user_id` par rapport à un attribut personnalisé). Confirmez que le client existe dans la source de données connectée. Si l'identifiant est résolu mais qu'aucune ressource personnalisée n'existe, le média de secours est affiché. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }