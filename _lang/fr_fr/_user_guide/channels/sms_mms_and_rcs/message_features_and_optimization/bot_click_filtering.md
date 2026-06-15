---
nav_title: "Filtrage des clics de bots"
article_title: "Filtrage des clics de bots SMS et RCS"
description: "Cet article de référence couvre le filtrage des clics de bots pour les SMS et les RCS."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 5
channel:
  - SMS
  - RCS
---

# Filtrage des clics de bots SMS et RCS {#sms-and-rcs-bot-click-filtering}

> Le filtrage des clics de bots SMS et RCS améliore l'analytique des campagnes et les workflows en excluant les clics suspectés d'être générés par des bots. Un « clic de bot » désigne les clics automatisés sur les liens raccourcis dans les messages SMS et RCS, tels que ceux provenant de robots d'indexation web, des aperçus de liens Android et iOS, ou de logiciels de sécurité CPaaS. Cette fonctionnalité facilite un reporting précis, une segmentation fiable et une orchestration efficace pour engager les vrais utilisateurs. <br><br> Pour le filtrage des clics de bots dans les campagnes e-mail, consultez [Filtrage des bots pour les e-mails]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering/).

## Comment ça fonctionne {#how-it-works}

Braze dispose d'un système de détection propriétaire qui utilise plusieurs entrées pour identifier les clics suspectés d'être générés par des bots, également appelés interactions non humaines (NHI). Les clics de bots peuvent gonfler les taux de clics, faussant les indicateurs d'engagement. En les filtrant, Braze facilite la capture de données fiables pour la prise de décision.

Notre système analyse les agents utilisateurs associés aux robots d'indexation web, aux aperçus de liens Android et iOS, ou aux logiciels de sécurité CPaaS. Quelques exemples d'agents utilisateurs filtrés incluent `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` et `Barracuda Sentinel (EE)`.

## Indicateurs et workflows impactés {#affected-metrics-and-workflows}

Les indicateurs et workflows Braze suivants sont impactés par les clics de bots :

- **_Total des clics_ :** L'analytique des Campaigns et l'analytique des Canvas exclura les clics de bots, reflétant uniquement les interactions humaines.
- **Filtres de segmentation :** Les filtres de segment référençant les interactions de liens SMS excluront les clics de bots pour un reciblage plus précis dans les Campaigns et les Canvas.
- **Orchestration :** Les clics de bots sont filtrés des déclencheurs basés sur les actions et des parcours d'actions Canvas qui référencent les interactions de liens SMS, permettant aux déclencheurs de refléter le comportement humain.
- **Braze Intelligence :**
    - **Sélection intelligente :** Exclut les clics de bots lors de l'optimisation de la sélection des variantes.
    - **Canal intelligent :** Exclut les clics de bots lorsque le SMS ou le RCS est sélectionné pour une sélection de canal précise.
    - **Étapes d'expérience :** Exclut les clics de bots pour des résultats d'expérience fiables.
    - **Exportations de données Currents :** Inclut les champs `is_suspected_bot_click` et `suspected_bot_click_reason` pour aider à analyser les clics humains par rapport aux clics de bots. Ces champs sont disponibles dans [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), le [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) et le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/).

Les désabonnements provenant de clics de bots suspectés ne sont pas affectés. Braze traite toutes les demandes de désabonnement normalement. Pour bloquer ces désabonnements, [soumettez un retour produit]({{site.baseurl}}/user_guide/administer/personal/braze_support/).

## Champs Currents dans les événements de clic SMS {#currents-fields-in-sms-click-events}

Braze inclut les champs Currents suivants pour les événements de clic SMS :

| Champ | Type de données | Description |
| --- | --- | --- |
| `is_suspected_bot_click` | Valeur booléenne | Indique si le clic est un clic de bot suspecté. Renvoie `null` pour tous les utilisateurs jusqu'à ce que le filtrage des clics de bots soit activé pour votre société. Une fois activé, il sera renseigné avec `true` ou `false` pour tous les nouveaux clics à venir. |
| `suspected_bot_click_reason` | Chaîne de caractères, tableau | Indique la raison d'un clic de bot suspecté (comme `user_agent`). Ce champ est renseigné même si le filtrage est désactivé, fournissant un aperçu de l'activité potentielle des bots. Ce champ est disponible globalement et renseigné avec une raison pour tous les utilisateurs, même si le filtrage des clics de bots n'est pas encore activé. Cela fournit un aperçu de l'activité potentielle des bots avant que vous n'activiez le filtrage des clics de bots. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Currents fields in SMS click events" }

## Modèle du Générateur de requêtes {#query-builder-template}

Pour vous aider à analyser vos données, vous pouvez utiliser le modèle mobile prédéfini **SMS click events by bots** dans le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates/).

## Questions fréquentes {#frequently-asked-questions}

### Comment le filtrage des clics de bots impacte-t-il les performances des campagnes ? {#how-does-bot-click-filtering-impact-campaign-performance}

Le filtrage n'affecte pas les campagnes précédemment envoyées. Une fois activé, il réduit les taux de clics à partir de ce moment en excluant les clics de bots.

### Le filtrage des clics de bots empêche-t-il les bots de cliquer sur les liens de désabonnement ? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

Non. Toutes les demandes de désabonnement sont traitées normalement.

### Les aperçus de liens sont-ils inclus dans le filtrage des clics de bots ? {#are-link-previews-included-in-bot-click-filtering}

Oui. Les aperçus de liens (tels que les aperçus de liens Android et iOS) sont signalés comme des clics de bots et filtrés.

### Comment activer le filtrage des clics de bots ? {#how-do-i-enable-bot-click-filtering}

Vous devez contacter votre équipe de compte Braze pour activer le filtrage des clics de bots pendant l'accès anticipé. Lorsque le filtrage des clics de bots sera disponible de manière générale, la fonctionnalité sera activée par défaut pour tous les utilisateurs SMS et RCS.

Assurez-vous également d'avoir activé le suivi avancé des clics pour le [raccourcissement de liens]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/). Cela vous permet de recevoir l'analytique des clics de bots, car nous suivons ces données au niveau de l'utilisateur individuel.

{% alert note %}
Pour une assistance supplémentaire, [contactez l'assistance]({{site.baseurl}}/braze_support/).
{% endalert %}