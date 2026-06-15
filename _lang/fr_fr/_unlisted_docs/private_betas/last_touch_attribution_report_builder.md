---
nav_title: "Attribution au dernier contact"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# Indicateurs d'attribution au dernier contact {#last-touch-attribution-metrics}

> Ajoutez des indicateurs d'attribution au dernier contact à vos rapports dans le Générateur de rapports.

{% alert note %}
Les indicateurs d'attribution au dernier contact sont en accès anticipé. Si vous souhaitez participer à l'accès anticipé, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

L'attribution au dernier contact (LTA) est un modèle d'attribution de conversion qui attribue l'intégralité du crédit d'une conversion au dernier message avec lequel un utilisateur a interagi avant de convertir. Contrairement aux fenêtres de conversion au niveau des campagnes, la LTA utilise des fenêtres d'attribution standard du secteur pour chaque canal :

| Canal | Fenêtre d'attribution |
| --- | --- |
| E-mail | 30 jours |
| SMS | 7 jours |
| WhatsApp | 7 jours |
| Push | 7 jours |
| Message in-app | 3 jours |
| Content Cards | 3 jours |
| Webhook | exclu de ce modèle |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si une conversion se produit en dehors de la fenêtre d'attribution d'un canal, elle n'est pas comptabilisée dans ce modèle.
{% endalert %}

## Avantages {#benefits}

L'attribution au dernier contact offre des avantages clés par rapport au suivi de conversion standard :

* Elle vous permet d'attribuer des conversions à des points de contact spécifiques, ce qui vous donne la possibilité de comprendre quels canaux (et pas seulement quelles campagnes ou quels Canvas) génèrent des résultats.
* Le crédit est attribué exclusivement au dernier message touché, de sorte que chaque conversion n'est comptée qu'une seule fois, éliminant ainsi les conversions en double entre les campagnes ou Canvas partageant des événements de conversion et des audiences communs.

## Ajouter des indicateurs d'attribution au dernier contact à votre rapport {#add-last-touch-attribution-metrics-to-your-report}

1. Accédez au **Générateur de rapports**, sous **Analytics**.
2. Sélectionnez **Créer le rapport** > **Créer un rapport personnalisé**.
3. Dans le menu déroulant **Lignes**, sélectionnez l'objet sur lequel vous souhaitez créer un rapport.
4. (Facultatif) Sélectionnez **Ajouter un sous-niveau**, puis choisissez un domaine pour approfondir votre analyse.
5. Sous **Colonnes**, sélectionnez **Personnaliser les indicateurs**.
6. Sous **Conversions**, sélectionnez **Last Touch Attribution**, puis sélectionnez **Tout sélectionner**.

{% alert note %}
Les indicateurs de chiffre d'affaires et d'achat ne sont pas disponibles.
{% endalert %}

![Le panneau Personnaliser les indicateurs avec les indicateurs d'attribution au dernier contact.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. Suivez les étapes 7 à 9 sur la page du [Générateur de rapports](https://www.braze.com/docs/user_guide/analytics/reporting/report_builder).

{% alert note %}
Envoyez des commentaires à votre gestionnaire de la satisfaction client ou fournissez-les après avoir sélectionné le bouton **Envoyer des commentaires**.
{% endalert %}