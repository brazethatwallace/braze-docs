---
nav_title: "Attribution au dernier contact"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# Indicateurs d'attribution au dernier contact {#last-touch-attribution-metrics}

> Ajoutez des indicateurs d'attribution au dernier contact à vos rapports dans le générateur de rapports.

{% alert note %}
Les indicateurs d'attribution au dernier contact sont en accès anticipé. Si vous souhaitez participer à l'accès anticipé, contactez votre gestionnaire du succès des clients.
{% endalert %}

L'attribution au dernier contact (LTA) est un modèle d'attribution de conversion qui attribue l'intégralité du crédit d'une conversion au dernier message avec lequel un utilisateur a interagi avant de convertir. Contrairement aux fenêtres de conversion au niveau des campagnes, la LTA utilise des fenêtres d'attribution standard du secteur pour chaque canal :

| Canal | Fenêtre d'attribution |
| --- | --- |
| E-mail | 30 jours |
| SMS | 7 jours |
| WhatsApp | 7 jours |
| Notification push | 7 jours |
| Message in-app | 3 jours |
| Content Cards | 3 jours |
| Webhook | exclu de ce modèle |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si une conversion se produit en dehors de la fenêtre d'attribution d'un canal, elle n'est pas comptabilisée dans ce modèle.
{% endalert %}

## Avantages {#benefits}

L'attribution au dernier point de contact offre des avantages clés par rapport au suivi de conversion standard :

* Elle vous permet d'attribuer les conversions à des points de contact spécifiques, ce qui vous donne la possibilité de comprendre quels canaux (et pas seulement quels Campaigns ou Canvas) génèrent des résultats.
* Le crédit est attribué exclusivement au dernier message consulté, de sorte que chaque conversion n'est comptabilisée qu'une seule fois, éliminant ainsi les conversions qui se chevauchent entre les Campaigns ou Canvas partageant des événements de conversion et des audiences communs.

## Ajouter des indicateurs d'attribution au dernier contact à votre rapport {#add-last-touch-attribution-metrics-to-your-report}

1. Accédez au **générateur de rapports**, sous **Analytics**.
2. Sélectionnez **Create report** > **Create custom report**.
3. Dans le menu déroulant **Rows**, sélectionnez l'élément sur lequel vous souhaitez créer un rapport.
4. (Facultatif) Sélectionnez **Add drilldown**, puis choisissez un domaine pour approfondir votre analyse.
5. Sous **Columns**, sélectionnez **Customize metrics**
6. Sous **Conversions**, sélectionnez **Last Touch Attribution**, puis sélectionnez **Select All**.

{% alert note %}
Les indicateurs de chiffre d'affaires et d'achats ne sont pas disponibles.
{% endalert %}

![Le panneau de personnalisation des indicateurs avec les indicateurs d'attribution au dernier contact.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. Suivez les étapes 7 à 9 sur la page du [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="last-touch attribution metrics in Report Builder" %}
{% endalert %}