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

## À propos des clics de robots {#about-bot-clicks}

Braze dispose d'un système de détection qui emploie plusieurs entrées pour identifier les clics suspectés de robots, également appelés interactions non humaines (INH). Les clics de robots peuvent fausser les indicateurs d'engagement de vos e-mails en gonflant artificiellement les taux de clics. Cette approche nous permet de faire la différence entre les interactions humaines authentiques et les activités présumées des robots afin de préserver l'intégrité des indicateurs et des informations sur l'engagement des clics.

## Indicateurs affectés par les clics de robots {#metrics-affected-by-bot-clicks}

{% alert note %}
Le filtrage des robots bloque activement les clics automatisés suspectés afin d'améliorer la précision de vos indicateurs d'engagement. Cependant, les scanners et les robots évoluent constamment, de sorte que Braze ne peut pas garantir la suppression de toutes les interactions non humaines.
{% endalert %}

Les indicateurs Braze suivants peuvent être affectés par les clics de robots :

- Taux de clics total
- Taux de clics unique
- Taux de clics par ouverture
- Taux de conversion (si « Clics sur la campagne » est sélectionné comme événement de conversion)
- Carte de chaleur
- Certains filtres de segmentation

Les [fonctionnalités Braze Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence_suite) qui exploitent les données de clics en plus de nos systèmes de détection peuvent être impactées. L'activation du paramètre peut perturber temporairement nos systèmes de détection, ce qui peut entraîner une diminution de l'indicateur ou de l'entrée en raison de cette exclusion des clics de robots suspectés :

- Sélection intelligente
- Canal intelligent
- Timing intelligent
- Étape d'expérience
    - Chemin gagnant
    - Chemin personnalisé
- Campaign
    - Variante gagnante
    - Variante personnalisée
- Taux d'ouverture réel estimé

Les désabonnements résultant de clics de robots suspectés ne seront pas affectés. Braze continuera à traiter toutes les demandes de désabonnement comme d'habitude. Si vous souhaitez que Braze bloque ces désabonnements, soumettez un [retour produit]({{site.baseurl}}/user_guide/administer/personal/product_portal).

## Filtres de segmentation affectés par le filtrage des robots {#segmentation-filters-affected-by-bot-filtering}

Les [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) suivants peuvent être affectés par le filtrage des robots pour les e-mails :

- [Clicked/Opened Campaign or Canvas With Tag]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Clicked/Opened Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Clicked Alias in Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [Clicked Alias in Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Clicked Alias in Any Campaign or Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Last Engaged with Message]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [Intelligent Channel]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## Activer le filtrage des robots {#turning-on-bot-filtering}

Accédez à **Paramètres** > **Préférences des e-mails**, puis sélectionnez **Remove bot clicks**. Ce paramètre s'applique au niveau de l'espace de travail.

Les clics de robots suspectés ne seront supprimés qu'après l'activation du paramètre ; cette suppression ne s'applique pas rétroactivement aux indicateurs de votre espace de travail.

![Paramètre de filtrage des robots pour les e-mails activé dans les préférences des e-mails.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Si vous activez ce paramètre puis le désactivez ultérieurement, Braze ne pourra pas restaurer les activités de robots précédemment supprimées dans vos analyses.
{% endalert %}

## Champs dans les événements de clic d'e-mail pour Currents et Snowflake {#fields-in-email-click-events-for-currents-and-snowflake}

Braze enverra les champs `is_suspected_bot_click` et `suspected_bot_click_reason` dans Currents et Snowflake pour un événement de clic d'e-mail.

| Champ | Type de données | Description |
| `is_suspected_bot_click` | Valeur booléenne | Indique qu'il s'agit d'un clic de robot suspecté. Ce champ enverra des valeurs nulles tant que vous n'aurez pas activé le paramètre d'espace de travail **Remove bots clicks**. Cette approche vous permet de comprendre de manière programmatique quand le filtrage des clics de robots suspectés a commencé dans votre espace de travail, afin de comparer précisément ces données avec celles de Currents et Snowflake. |
| `suspected_bot_click_reason` | Array | Indique la raison pour laquelle il s'agit d'un clic de robot suspecté. Ce champ sera rempli avec des valeurs, telles que `user_agent` et `ip_address`, même si le paramètre de filtrage des robots de l'espace de travail est désactivé. Ce champ peut fournir des informations sur l'impact potentiel de l'activation de ce paramètre en comparant le nombre de clics provenant de clics de robots suspectés aux interactions humaines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Champs dans les événements de clic d'e-mail pour Currents et Snowflake" }

## Questions fréquentes {#frequently-asked-questions}

### Quel sera l'impact du filtrage des robots sur les performances de ma campagne ? {#how-will-bot-filtering-impact-my-campaigns-performance}

Cela n'aura pas d'impact sur les indicateurs des campagnes précédemment envoyées. Lorsque le filtrage des robots est activé dans votre espace de travail, Braze commence à filtrer les clics de robots suspectés parmi l'ensemble des clics. Vous pouvez constater une baisse des taux de clics, mais ce taux sera une représentation plus fidèle de l'engagement réel de vos utilisateurs avec leurs e-mails.

### Le filtrage des robots empêchera-t-il les robots qui cliquent sur le lien de désabonnement Braze de se désabonner ? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

Non. Toutes les demandes de désabonnement continueront d'être traitées.

### Les ouvertures automatiques sont-elles prises en compte dans le filtrage des clics de robots ? {#are-machine-opens-considered-in-the-bot-click-filtering}

Non.