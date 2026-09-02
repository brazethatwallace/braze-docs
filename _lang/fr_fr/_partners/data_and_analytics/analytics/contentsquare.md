---
nav_title: Contentsquare
article_title: Contentsquare
description: "Cet article de référence décrit le partenariat entre Braze et Contentsquare, une plateforme d'analyse de l'expérience numérique qui vous permet d'améliorer la pertinence et les taux de conversion de vos campagnes en ciblant les messages en fonction de l'expérience numérique de vos clients."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) est une plateforme d'analyse de l'expérience numérique qui permet une compréhension sans précédent de l'expérience client.

_Cette intégration est assurée par Contentsquare._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Contentsquare vous permet d'envoyer des en direct Signals (fraude, signaux de frustration, etc.) en tant qu'événements personnalisés dans Braze. Exploitez les informations d'expérience de Contentsquare pour améliorer la pertinence de vos campagnes et les taux de conversion en ciblant les messages en fonction de l'expérience numérique et du langage corporel de vos clients.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Contentsquare | Un compte Contentsquare est requis pour profiter de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. Pour créer une nouvelle clé dans le tableau de bord de Braze, accédez à **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({% image_buster /assets/img/contentsquare_custom_events.png %}). Votre endpoint dépendra de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Voici quelques cas d'utilisation courants de Braze et Contentsquare :
- Hyper-personnalisez les messages en fonction de l'intention du client en faisant apparaître les données d'expérience client dans Braze.
- Reciblez les clients en fonction de leur comportement numérique, de leurs hésitations, de leur frustration et de leur intention.
- Identifiez les mauvaises expériences au sein de Contentsquare et récupérez les clients avec des messages ciblés et des offres de rétention.
- Récupérez les clients à risque en envoyant des messages plus pertinents et empathiques au bon moment et au bon endroit.

## Intégration {#integration}

Pour intégrer Contentsquare dans Braze, vous devez demander l'installation d'une intégration « en direct Signals » à partir du catalogue d'intégration de Contentsquare :

1. Dans Contentsquare, cliquez sur **Console** dans le menu **Settings**. Vous serez redirigé vers le projet sur lequel vous travaillez actuellement.
2. Sur la page **Projects**, accédez à l'onglet **Integrations** et cliquez sur le bouton **+ Add integration**.
3. Dans le catalogue des intégrations, recherchez l'intégration **en direct Signals** et cliquez sur **Add**. L'équipe de Contentsquare vous contactera ensuite pour configurer l'extrait de code afin d'envoyer des en direct Signals à Braze.
4. Contentsquare va maintenant traiter votre intégration. Le texte de l'indicateur sera mis à jour une fois l'intégration terminée.

Pour plus d'informations, consultez la section [Demander une intégration Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Utilisation de cette intégration {#using-this-integration}

Une fois l'intégration terminée, les événements personnalisés Contentsquare seront disponibles pour être utilisés dans vos Campaigns et Canvas. Vous pouvez vérifier quels événements sont envoyés à Braze depuis **Paramètres des données** > **Événements personnalisés**.

![Données Live Signals de Contentsquare dans l'onglet Événements personnalisés de Braze]({% image_buster /assets/img/contentsquare_custom_events.png %})