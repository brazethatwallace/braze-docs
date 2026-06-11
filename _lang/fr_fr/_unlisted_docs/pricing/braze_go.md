---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go offre un accès simplifié à la plateforme d'engagement client Braze pour aider vos équipes marketing à démarrer n'importe où et à aller partout. Conçu pour la simplicité et l'efficacité, Braze Go est adapté à certains marchés émergents.

{% alert important %}
Braze Go n'est pas disponible sur tous les marchés. Si vous souhaitez en savoir plus sur Braze Go, contactez votre gestionnaire de compte.
{% endalert %}

Braze Go offre les mêmes fonctionnalités que Braze, avec des modifications ciblées sur les fonctionnalités suivantes :

- Vous pouvez avoir jusqu'à 30 campagnes actives.
- Vous pouvez avoir jusqu'à 20 Canvas actifs.
- La limite de débit par défaut totale de la REST API est de 50 000 par heure et par espace de travail.
    - Pour une utilisation hors Braze Go, consultez les [limites de la REST API]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type).
- La rétention des données d'interaction des campagnes et des Canvas est de 2 mois sans restauration.
    - Pour une utilisation hors Braze Go, consultez la [disponibilité des données d'interaction des messages]({{site.baseurl}}/messaging_interaction_data/).

{% alert note %}
Les données d'interaction pour les campagnes et les Canvas sont différentes des données Snowflake et n'ont aucun effet sur celles-ci.
{% endalert %}

- Les webhooks Braze-vers-Braze ne sont pas pris en charge.
- Les filtres liés aux étiquettes ne sont pas pris en charge, en particulier les filtres suivants :
    - Clicked or Opened Campaign or Canvas with Tag
    - Last Received Message from Campaign or Canvas with Tag
    - Received Campaign or Canvas with Tag
- Braze peut également mettre en œuvre une politique de rétention des données pour les événements du profil utilisateur et les données d'achat, supprimant les événements, les achats, ou les deux datant de plus d'un an et n'ayant pas été effectués à nouveau depuis un an. Cependant, ces données resteraient disponibles dans les extensions de segments SQL pendant 2 ans.

Si l'une des fonctionnalités ci-dessus est mise à jour, cela sera reflété dans cet article et mentionné dans nos [notes de version]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes).