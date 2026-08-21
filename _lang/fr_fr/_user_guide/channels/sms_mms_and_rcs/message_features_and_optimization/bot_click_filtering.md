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

> Le filtrage des clics de bots SMS et RCS améliore l'analytique des Campaigns et les workflows en excluant les clics suspectés d'être générés par des bots. Un « clic de bot » désigne les clics automatisés sur les liens raccourcis dans les messages SMS et RCS, tels que ceux provenant de robots d'indexation web, des aperçus de liens Android et iOS, ou de logiciels de sécurité CPaaS. Cette fonctionnalité facilite un reporting précis, une segmentation fiable et une orchestration efficace pour engager les vrais utilisateurs. <br><br> Pour le filtrage des clics de bots dans les campagnes e-mail, consultez [Filtrage des bots pour les e-mails]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering).

## Fonctionnement {#how-it-works}

Braze dispose d'un système de détection propriétaire qui utilise plusieurs entrées pour identifier les clics suspects provenant de bots, également appelés interactions non humaines (NHI). Les clics de bots peuvent gonfler les taux de clics, faussant ainsi les indicateurs d'engagement. En les filtrant, Braze facilite la capture de données fiables pour la prise de décision.

Notre système analyse les agents utilisateurs associés aux robots d'indexation web, aux aperçus de liens Android et iOS, ou aux logiciels de sécurité CPaaS. Voici quelques exemples d'agents utilisateurs filtrés : `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` et `Barracuda Sentinel (EE)`.

## Indicateurs et workflows concernés {#affected-metrics-and-workflows}

Les indicateurs et workflows Braze suivants sont impactés par les clics de bots :

- **_Total des clics_ :** Les analyses de Campaign et de Canvas excluent les clics de bots, reflétant uniquement les interactions humaines.
- **Filtres de segmentation :** Les filtres de Segment faisant référence aux interactions de liens SMS excluent les clics de bots pour un reciblage plus précis dans les Campaigns et les Canvas.
- **Orchestration :** Les clics de bots sont filtrés des déclencheurs basés sur les actions et des parcours d'action Canvas qui font référence aux interactions de liens SMS, permettant aux déclencheurs de refléter le comportement humain.
- **Braze Intelligence :**
    - **Sélection intelligente :** Exclut les clics de bots lors de l'optimisation de la sélection de variante.
    - **Canal intelligent :** Exclut les clics de bots lorsque le SMS ou le RCS est sélectionné pour une sélection de canal précise.
    - **Étapes d'expérimentation :** Exclut les clics de bots pour des résultats d'expérimentation fiables.
    - **Exports de données Currents :** Inclut les champs `is_suspected_bot_click` et `suspected_bot_click_reason` pour aider à analyser les clics humains par rapport aux clics de bots. Ces champs sont disponibles dans [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) et [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder).

Les désabonnements provenant de clics de bots suspectés ne sont pas affectés. Braze traite toutes les demandes de désabonnement comme d'habitude. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Champs Currents dans les événements de clic SMS {#currents-fields-in-sms-click-events}

Braze inclut les champs Currents suivants pour les événements de clic SMS :

| Champ | Type de donnée | Description |
| --- | --- | --- |
| `is_suspected_bot_click` | Booléen | Indique si le clic est un clic de bot suspecté. Pour les clics sur les liens courts SMS et RCS, Braze évalue la détection de bots à chaque clic et renseigne ce champ avec `true` ou `false`. |
| `suspected_bot_click_reason` | Chaîne de caractères, Tableau | Indique la raison d'un clic de bot suspecté (par exemple `user_agent`). Renseigné lorsque la détection de bots s'exécute pour les clics sur les liens courts SMS et RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Champs Currents dans les événements de clic SMS" }

## Modèle du Query Builder {#query-builder-template}

Pour vous aider à analyser vos données, vous pouvez utiliser le modèle mobile prédéfini **SMS click events by bots** dans le [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates).

## Questions fréquentes {#frequently-asked-questions}

### Comment le filtrage des clics de bots affecte-t-il les performances des campagnes ? {#how-does-bot-click-filtering-impact-campaign-performance}

Le filtrage des clics de bots s'exécute automatiquement pour les clics sur les liens raccourcis SMS et RCS. Les taux de clics du tableau de bord excluent les clics suspectés d'être générés par des bots, de sorte que les taux rapportés reflètent les interactions humaines plutôt que les aperçus de liens automatisés ou le trafic des robots d'indexation.

### Le filtrage des clics de bots empêche-t-il les bots de cliquer sur les liens de désabonnement ? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

Non. Toutes les demandes de désabonnement sont traitées normalement.

### Les aperçus de liens sont-ils inclus dans le filtrage des clics de bots ? {#are-link-previews-included-in-bot-click-filtering}

Oui. Les aperçus de liens (tels que les aperçus de liens Android et iOS) sont signalés comme des clics de bots et filtrés.