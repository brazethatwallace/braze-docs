---
nav_title: Indicateurs par segments
article_title: Indicateurs par segments
page_order: 3
page_type: reference
description: "Cette page décrit comment utiliser les modèles de rapports du Générateur de requêtes pour ventiler les indicateurs de performance des campagnes, Canvas, variantes et étapes par segments."
tool:
  - Segments
  - Reports

---

# Indicateurs par segments {#metrics-by-segments}

> Utilisez les modèles de rapports du [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) pour ventiler les indicateurs de performance des campagnes, Canvas, variantes et étapes par segments.

Le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) doit être activé pour les segments dont vous souhaitez consulter les indicateurs.

Pour exécuter ces rapports, procédez comme suit :
1. Dans le **Générateur de requêtes**, choisissez de créer un nouveau rapport SQL à partir d'un modèle.
2. Sélectionnez **Segment breakdowns** pour l'indicateur, ce qui filtre les modèles pour ceux dont les indicateurs incluent des ventilations par segment, à savoir :
- Indicateurs de performance des e-mails par segment
- Indicateurs d'engagement des e-mails pour les variantes ou étapes, par segment
- Achats et chiffre d'affaires par segment
- Achats et chiffre d'affaires pour les variantes ou étapes, par segment
- Performance des notifications push par segment

![La page Segment breakdown contient un éditeur SQL, un panneau latéral avec des onglets pour les Variables, les Tables de données disponibles, l'Historique des requêtes et le Générateur de requêtes IA, ainsi qu'une section de résultats.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Modèles de rapports {#report-templates}

{% tabs %}
{% tab Indicateurs d'engagement des e-mails par segment %}

### Consulter les indicateurs pour les campagnes ou Canvas {#campaign-canvas-email}

Pour consulter les indicateurs de performance des e-mails ventilés par segment au niveau de la campagne ou du Canvas, utilisez l'onglet [Variables](#variables) pour spécifier les campagnes ou Canvas et une période pour l'extraction des données. Si aucune campagne ou aucun Canvas n'est spécifié, le rapport inclura les e-mails de toutes les campagnes et de tous les Canvas de la période spécifiée. Vous pouvez également choisir d'afficher toutes les campagnes et tous les Canvas associés à certaines étiquettes.

Les indicateurs d'e-mail suivants sont disponibles dans ce rapport :
- Envois
- Livraisons
- Plaintes
- Ouvertures uniques
- Ouvertures automatiques uniques
- Ouvertures non automatiques uniques
- Clics uniques
- Désabonnements
- Rebonds
- Échecs provisoires d'envoi
- Différés

#### Résultats {#results}

Vos résultats afficheront les indicateurs d'engagement des e-mails par segment pour les campagnes ou Canvas que vous avez sélectionnés. Si vous n'avez pas sélectionné de campagnes ou Canvas spécifiques, votre rapport affichera les indicateurs d'e-mail pour chaque segment sur l'ensemble des campagnes et Canvas d'e-mails dans la période de votre rapport.

- **Lignes :** Segments
- **Colonnes :** Indicateurs d'engagement des e-mails

### Consulter les indicateurs pour les variantes ou étapes {#viewing-metrics-for-variants-or-steps}

Pour consulter les performances des e-mails ventilées par segment au niveau de la variante de campagne, de la variante du Canvas ou de l'étape du Canvas, choisissez d'abord un rapport au niveau des variantes ou des étapes (ce sont les rapports dont le titre contient « pour les variantes ou étapes »), puis utilisez l'onglet **Variables** pour spécifier les éléments suivants :

- Campagne ou Canvas spécifique (requis pour un rapport au niveau des variantes ou des étapes)
- Variantes (requis pour un rapport au niveau des variantes ou des étapes)
- Étape du Canvas (facultatif)

Les indicateurs sont les mêmes que ceux proposés pour le modèle au [niveau de la campagne ou du Canvas](#campaign-canvas-email). Si vous choisissez plusieurs variantes, vos résultats seront regroupés par variante.

#### Résultats

Vos résultats afficheront les indicateurs d'engagement des e-mails par segment pour les variantes ou étapes sélectionnées.

- **Lignes :** Segments
- **Colonnes :** Indicateurs d'engagement des e-mails

{% endtab %}

{% tab Achats et chiffre d'affaires par segment %}
### Consulter les indicateurs pour les campagnes ou Canvas {#viewing-metrics-for-campaigns-or-canvases}

Pour consulter les indicateurs d'achats et de chiffre d'affaires ventilés par segment pour une campagne ou un Canvas spécifique, utilisez l'onglet [Variables](#variables) pour spécifier les éléments suivants :

- Fenêtre de conversion (le nombre de jours après la réception ou le clic sur l'e-mail pendant lesquels Braze attribuera les achats ou le chiffre d'affaires)
- Produit spécifique (facultatif)

De plus, utilisez l'onglet **Variables** pour indiquer si le rapport doit être exécuté pour une ou plusieurs campagnes ou Canvas, ou une ou plusieurs étiquettes. Si aucune campagne, aucun Canvas ou aucune étiquette n'est sélectionné, le rapport sera exécuté pour tous les e-mails des campagnes ou Canvas pendant la période choisie.

Actuellement, ce rapport extrait les indicateurs uniquement du canal e-mail. Les données de chiffre d'affaires ou d'achats provenant d'autres canaux que l'e-mail ne seront pas reflétées dans le rapport.

Les indicateurs suivants sont disponibles pour les e-mails :

- Achats uniques à la réception
- Chiffre d'affaires à la réception
- Achats uniques au clic
- Chiffre d'affaires au clic
- Destinataires uniques
- Clics uniques sur les e-mails

Tous les indicateurs de taux utilisent les destinataires uniques d'e-mails comme dénominateur.

#### Définitions {#definitions}

- « À la réception » fait référence aux événements d'achat ou au chiffre d'affaires survenus dans la fenêtre de conversion spécifiée, après que les utilisateurs ont reçu les campagnes ou Canvas spécifiés.
- « Au clic » fait référence aux événements d'achat ou au chiffre d'affaires survenus après les événements d'achat, dans la fenêtre de conversion spécifiée, après que les utilisateurs ont cliqué sur les campagnes ou Canvas spécifiés.

Par exemple, supposons qu'un segment contienne 10 utilisateurs et que cinq d'entre eux aient effectué un achat après avoir reçu votre e-mail. Si l'un de ces cinq a effectué un achat après avoir cliqué sur votre e-mail, votre « taux d'achats uniques à la réception » serait de 50 % et votre « taux d'achats uniques au clic » serait de 10 %.

![Le rapport affiche les indicateurs d'e-mail, notamment les achats uniques à la réception, le chiffre d'affaires à la réception, les achats uniques au clic, le chiffre d'affaires au clic, les destinataires uniques et les clics uniques sur les e-mails.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Résultats

Vos résultats afficheront les indicateurs d'achats par segment pour les campagnes ou Canvas sélectionnés. Si vous n'avez pas sélectionné de campagnes ou Canvas spécifiques, votre rapport affichera les indicateurs d'achats pour chaque segment sur l'ensemble des campagnes ou Canvas d'e-mails dans la période de votre rapport.

- **Lignes :** Segments
- **Colonnes :** Indicateurs d'achats


### Consulter les indicateurs pour les variantes ou étapes

Pour consulter les indicateurs d'achats et de chiffre d'affaires ventilés par segment pour une variante de campagne, une variante du Canvas ou une étape du Canvas spécifique, utilisez l'onglet [Variables](#variables) pour spécifier les éléments suivants :

- Campagne ou Canvas spécifique
- Variantes
- Étape du Canvas (facultatif)
- Période
- Produit spécifique (facultatif)

#### Résultats

Vos résultats afficheront les indicateurs d'achats par segment pour les variantes ou étapes sélectionnées.

- **Lignes :** Segments
- **Colonnes :** Indicateurs d'achats

{% endtab %}
{% tab Meilleurs ou moins bons résultats pour l'engagement des e-mails %}

### Consulter les indicateurs des meilleurs ou moins bons résultats {#viewing-metrics-for-the-top-or-bottom-performers}

Ce rapport dans l'onglet [Variables](#variables) affiche les campagnes, Canvas ou étapes du Canvas ayant obtenu les meilleurs ou les moins bons résultats pour un indicateur d'engagement des e-mails spécifié.

Les cas d'utilisation incluent :
- 10 campagnes avec les taux d'ouverture unique d'e-mails les plus élevés
- 25 Canvas avec le plus de désabonnements par e-mail
- 50 étapes du Canvas avec le plus de clics uniques

Les indicateurs d'e-mail suivants sont disponibles dans ce rapport :
- Envois
- Livraisons
- Plaintes
- Ouvertures uniques
- Ouvertures automatiques uniques
- Ouvertures non automatiques uniques
- Clics uniques
- Désabonnements
- Rebonds
- Échecs provisoires d'envoi
- Plaintes

Pour consulter ce rapport, vous devez spécifier les variables suivantes dans l'onglet **Variables** :
- **Indicateurs :** Sélectionnez l'un des indicateurs selon lequel classer vos résultats
- **Nombre de rapports :** Sélectionnez les meilleurs ou les moins bons résultats et le nombre de résultats, par exemple les 10 meilleurs ou les 15 moins bons
- **Type de message :** Indiquez si vos résultats concernent des campagnes, des Canvas ou des étapes du Canvas

#### Résultats

Vos résultats afficheront les meilleures (ou moins bonnes) campagnes, Canvas ou étapes du Canvas que vous avez sélectionnés. Par exemple, si vous avez sélectionné les 10 meilleures campagnes pour le taux de clics, vos résultats afficheront les 10 meilleures campagnes classées du taux de clics le plus élevé au plus bas. Vos colonnes afficheront tous les indicateurs d'engagement des e-mails pour chaque ligne (campagnes, Canvas ou étapes de message).

{% endtab %}
{% tab Meilleurs ou moins bons résultats pour les achats %}

### Consulter les indicateurs des meilleurs ou moins bons résultats

Ce rapport dans l'onglet [Variables](#variables) affiche les campagnes, Canvas ou étapes du Canvas ayant obtenu les meilleurs ou les moins bons résultats pour un indicateur d'achats ou de chiffre d'affaires spécifié.

Les cas d'utilisation incluent :
- 20 campagnes avec les taux d'achat les plus élevés pour un produit spécifique
- 25 Canvas ayant généré le plus de chiffre d'affaires
- 10 étapes du Canvas avec le taux d'achat de produit le plus bas

Les indicateurs d'e-mail suivants sont disponibles dans ce rapport :
- Achats uniques à la réception
- Chiffre d'affaires à la réception
- Achats uniques au clic
- Chiffre d'affaires au clic
- Destinataires uniques
- Clics uniques sur les e-mails

Pour consulter ce rapport, vous devez spécifier les variables suivantes dans l'onglet **Variables** :
- **Indicateurs :** Sélectionnez l'un des indicateurs selon lequel classer vos résultats
- **Nombre de rapports :** Sélectionnez les meilleurs ou les moins bons résultats et le nombre de résultats, par exemple les 10 meilleurs ou les 15 moins bons
- **Type de message :** Indiquez si vos résultats concernent des campagnes, des Canvas ou des étapes du Canvas
- **Fenêtre de conversion :** Le nombre de jours après la réception ou le clic sur l'e-mail pendant lesquels Braze attribuera les achats ou le chiffre d'affaires

#### Définitions

- « À la réception » fait référence aux événements d'achat ou au chiffre d'affaires survenus dans la fenêtre de conversion spécifiée, après que les utilisateurs ont reçu les campagnes ou Canvas spécifiés.
- « Au clic » fait référence aux événements d'achat ou au chiffre d'affaires survenus après les événements d'achat, dans la fenêtre de conversion spécifiée, après que les utilisateurs ont cliqué sur les campagnes ou Canvas spécifiés.

Par exemple, supposons qu'un segment contienne 10 utilisateurs et que cinq d'entre eux aient effectué un achat après avoir reçu votre e-mail. Si l'un de ces cinq a effectué un achat après avoir cliqué sur votre e-mail, votre taux « d'achats uniques à la réception » serait de 50 % et votre taux « d'achats uniques au clic » serait de 10 %.

#### Résultats

Vos résultats afficheront les meilleures (ou moins bonnes) campagnes, Canvas ou étapes du Canvas que vous avez sélectionnés. Par exemple, si vous avez sélectionné les 10 meilleures campagnes pour le « chiffre d'affaires au clic », vos résultats afficheront les 10 meilleures campagnes classées du « chiffre d'affaires au clic » le plus élevé au plus bas. Vos colonnes afficheront tous les indicateurs d'achats pour chaque ligne (campagnes, Canvas ou étapes de message).

{% endtab %}
{% tab Performance des notifications push par segment %}

### Consulter les indicateurs push pour les segments {#viewing-push-metrics-for-segments}

Ce rapport dans l'onglet [Variables](#variables) affiche les indicateurs push ventilés par segments.

Dans l'onglet **Variables**, spécifiez les campagnes ou Canvas pour lesquels consulter les indicateurs ainsi qu'une période pour l'extraction des données. Si vous ne sélectionnez aucune campagne ou aucun Canvas, le rapport affichera les notifications push de toutes les campagnes et de tous les Canvas dans la période spécifiée. Vous pouvez également afficher toutes les campagnes et tous les Canvas associés à certaines étiquettes.

Les indicateurs push suivants sont disponibles dans ce rapport :

- Envois
- Rebonds
- Livraisons
- Ouvertures directes

#### Résultats

Votre rapport affichera les résultats suivants :

- **Lignes :** Segments
- **Colonnes :** Indicateurs push
{% endtab %}
{% endtabs %}