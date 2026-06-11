---
nav_title: Mention Me
article_title: Intégrer Mention Me à Braze
description: "Guide de configuration de l'intégration de Mention Me"
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> Ensemble, [Mention Me](https://www.mention-me.com/) et Braze peuvent être votre porte d'entrée pour attirer des clients haut de gamme et favoriser une fidélité inébranlable à votre marque. En intégrant de façon fluide les données first-party de recommandation dans Braze, vous pouvez proposer des expériences omnicanales hautement personnalisées, ciblées sur les fans de votre marque.

_Cette intégration est maintenue par Mention Me._

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Prérequis | Description |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Mention Me | Un compte [Mention Me](https://mention-me.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Une clé REST API Braze | Une clé REST API Braze avec les autorisations `users.track` et `templates.email.create`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

* Envoyez les données de contact et les abonnements des clients recommandés par Mention Me vers Braze en temps réel.
* Utilisez les données de recommandation pour créer des e-mails de rappel de coupons.
* Améliorez les performances des autres canaux marketing en utilisant les données de recommandation pour segmenter et cibler les clients à forte valeur ajoutée.

## Quelles données sont envoyées de Mention Me à Braze ? {#what-data-is-sent-from-mention-me-to-braze}

Lorsque vous configurez cette intégration, Mention Me crée automatiquement vos attributs clients et vos événements&#8212;il n'est donc pas nécessaire de le faire au préalable.

Les adresses e-mail de vos clients dans Braze seront utilisées pour associer les événements et les attributs personnalisés pertinents. Mention Me enverra des événements et des attributs de profil de contact pour tout prospect ou client existant qui déclenche cet événement via Mention Me, quel que soit son statut d'abonnement.

Pour plus de détails, reportez-vous à la section [Attributs et événements du profil de contact](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Intégrer Mention Me {#integrating-mention-me}

{% alert tip %}
Pour une description complète étape par étape, reportez-vous à la [documentation de configuration de Braze de Mention Me](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

Pour intégrer Mention Me à Braze :

1. Dans Mention Me, accédez à la page d'[intégration de Braze](https://mention-me.com/merchant/~/integrations/braze), puis sélectionnez **Connect**.
2. Sélectionnez **Create New Authorization**, puis ajoutez la [clé API que vous avez précédemment créée](#prerequisites) et sélectionnez votre instance Braze.
3. Choisissez un ou plusieurs pays avec lesquels vous souhaitez synchroniser vos données.
4. Lorsque vous avez terminé, sélectionnez **Connect**.