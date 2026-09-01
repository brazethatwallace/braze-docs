---
nav_title: Filtrage des bots pour les e-mails
article_title: Filtrage des bots pour les e-mails
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Cet article donne un aperçu du filtrage des bots pour les e-mails."
---

# Filtrage des bots pour les e-mails {#bot-filtering-for-emails}

> Configurez le filtrage des robots dans vos [Préférences des e-mails]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) pour exclure tous les clics suspectés d'être des machines ou des robots. Un « clic de robot » dans un e-mail fait référence à un clic sur des hyperliens dans un e-mail généré par un programme automatisé. En filtrant ces clics de robots, vous pouvez déclencher et envoyer intentionnellement des messages à des destinataires réellement engagés.

{% alert important %}
À partir du 9 juillet 2025, tous les nouveaux espaces de travail créés auront le paramètre de filtrage des robots activé pour des rapports de clics plus précis dans Braze.
{% endalert %}

## À propos des clics de bots {#about-bot-clicks}

Braze dispose d'un système de détection qui utilise plusieurs sources de données pour identifier les clics suspectés d'être générés par des bots, également appelés interactions non humaines (NHI). Les clics de bots peuvent fausser vos indicateurs d'engagement e-mail en gonflant artificiellement les taux de clics. Cette approche nous permet de distinguer les interactions humaines authentiques de l'activité suspectée des bots, afin de préserver l'intégrité des indicateurs et des informations relatifs à l'engagement par clic.

## Indicateurs affectés par les clics de robots {#metrics-affected-by-bot-clicks}

{% alert note %}
Le filtrage des robots bloque activement les clics automatisés suspects afin d'améliorer la précision de vos indicateurs d'engagement. Cependant, les scanners et les robots évoluent constamment au fil du temps, et Braze ne peut donc pas garantir la suppression de toutes les interactions non humaines.
{% endalert %}

Les indicateurs Braze suivants peuvent être affectés par les clics de robots :

- Taux de clics total
- Taux de clics unique
- Taux de clics par ouverture
- Taux de conversion (si « Clics sur la Campaign » est sélectionné comme événement de conversion)
- Carte de chaleur
- Certains filtres de Segment

Lorsque le filtrage des robots est activé, les clics suspects de robots sont exclus des données de clics. Les [fonctionnalités BrazeAI Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence_suite) suivantes peuvent afficher des volumes liés aux clics plus faibles en conséquence :

- Canal intelligent
- Timing intelligent
- Étape d'expérimentation
    - Chemin gagnant
- Taux d'ouverture réel estimé

[Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) peut également afficher des volumes liés aux clics plus faibles lorsque vous optimisez pour un objectif basé sur les clics.

Les désabonnements provenant de clics suspects de robots ne seront pas affectés. Braze continuera à traiter toutes les demandes de désabonnement comme d'habitude. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Filtres de segmentation affectés par le filtrage des bots {#segmentation-filters-affected-by-bot-filtering}

Les [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) suivants peuvent être affectés par le filtrage des bots pour les e-mails :

- [Clicked/Opened Campaign or Canvas With Tag]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Clicked/Opened Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Clicked Alias in Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [Clicked Alias in Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Clicked Alias in Any Campaign or Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Last Engaged with Message]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [Intelligent Channel]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## Activer le filtrage des bots {#turning-on-bot-filtering}

Accédez à **Paramètres** > **Préférences d'e-mail**. Ensuite, sélectionnez **Supprimer les clics des bots**. Ce paramètre est appliqué au niveau de l'espace de travail.

Les clics suspectés d'être générés par des bots ne seront supprimés qu'après l'activation du paramètre, et cela ne s'applique pas rétroactivement aux indicateurs de votre espace de travail.

![Paramètre de filtrage des bots pour les e-mails activé dans les préférences d'e-mail.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Si vous activez ce paramètre puis le désactivez par la suite, Braze ne pourra pas restaurer les activités de bots précédemment supprimées dans vos analyses.
{% endalert %}

## Champs dans les événements de clic e-mail pour Currents et Snowflake {#fields-in-email-click-events-for-currents-and-snowflake}

Braze enverra les champs `is_suspected_bot_click` et `suspected_bot_click_reason` dans Currents et Snowflake pour un événement de clic e-mail.

| Champ | Type de donnée | Description |
| `is_suspected_bot_click` | Booléen | Indique qu'il s'agit d'un clic suspecté de provenir d'un bot. Ce champ enverra des valeurs nulles jusqu'à ce que vous activiez le paramètre d'espace de travail **Supprimer les clics de bots**. Cette approche vous permet de comprendre de manière programmatique quand le filtrage des clics suspects de bots a commencé dans votre espace de travail, afin de comparer avec précision ces données avec celles de Currents et Snowflake. |
| `suspected_bot_click_reason` | Tableau | Indique la raison pour laquelle ce clic est suspecté de provenir d'un bot. Ce champ sera rempli avec des valeurs, telles que `user_agent` et `ip_address`, même si le paramètre d'espace de travail de filtrage des bots est désactivé. Ce champ peut fournir des informations sur l'impact potentiel de l'activation de ce paramètre en comparant le nombre de clics provenant de clics suspects de bots avec les interactions humaines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Champs dans les événements de clic e-mail pour Currents et Snowflake" }

## Questions fréquemment posées {#frequently-asked-questions}

### Comment le filtrage des bots va-t-il affecter les performances de ma campagne ? {#how-will-bot-filtering-impact-my-campaigns-performance}

Cela n'aura pas d'impact sur les indicateurs des Campaigns précédentes déjà envoyées. Lorsque le filtrage des bots est activé dans votre espace de travail, Braze commence à filtrer les clics suspects provenant de bots parmi tous les clics. Vous pourriez constater une baisse des taux de clics, mais le taux de clics représente alors de manière plus précise l'engagement réel de vos utilisateurs avec leurs e-mails.

### Le filtrage des bots empêchera-t-il les bots qui cliquent sur le lien de désabonnement Braze de se désabonner ? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

Non. Toutes les demandes de désabonnement continueront d'être traitées.

### Les ouvertures automatisées sont-elles prises en compte dans le filtrage des clics de bots ? {#are-machine-opens-considered-in-the-bot-click-filtering}

Non.