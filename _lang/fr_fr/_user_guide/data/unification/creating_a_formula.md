---
nav_title: Créer une formule
article_title: Créer une formule
page_order: 3
page_type: reference
description: "Cet article de référence couvre la création et la gestion des formules pour vous aider à comprendre facilement les relations complexes entre vos données."
tool: Reports

---
# Créer une formule {#create-a-formula}

> Lors de la consultation des analyses dans Braze, vous pouvez combiner plusieurs points de données pour obtenir des informations précieuses sur vos données utilisateur. On les appelle des formules. Utilisez des formules pour normaliser vos données de séries chronologiques en fonction de votre nombre total d'utilisateurs actifs par mois (MAU) et d'utilisateurs actifs quotidiens (DAU).

Les formules vous aident à comprendre les relations complexes qui existent dans vos données. Par exemple, vous pouvez comparer combien d'événements personnalisés ont été effectués par des utilisateurs actifs quotidiens qualifiés pour un segment spécifique, par rapport à l'ensemble des utilisateurs (ou par rapport à un autre segment).

## Cas d'utilisation {#use-cases}

Les formules, en particulier lorsqu'elles sont associées à des événements personnalisés, peuvent vous aider à comprendre les comportements des utilisateurs au sein de votre application. Les formules peuvent également donner des informations plus approfondies sur les tendances d'achat de vos segments, même si votre entreprise utilise des médias payants en même temps que Braze, comme Google Ads ou des publicités télévisées.

Voici quelques exemples de types de comportements qui peuvent être détectés grâce aux formules :

- **Applications de covoiturage :** Si vous disposez d'un événement personnalisé pour l'annulation d'un trajet par l'utilisateur, vous pouvez configurer une fonction pour les trajets annulés / DAU afin de déterminer si certains segments d'utilisateurs ont tendance à annuler plus de trajets que d'autres.
- **Applications de commerce électronique :** En configurant une fonction pour les achats d'un certain ID de produit / MAU, vous pouvez comparer la popularité d'un produit récemment promu entre les segments, même si toutes les promotions n'ont pas pu être suivies à l'aide de Braze.
- **Applications média utilisant des publicités :** Si l'expérience des utilisateurs est interrompue par des publicités entre des clips vidéo ou audio, enregistrer en tant qu'événement personnalisé les sorties pendant la publicité et calculer le ratio sorties mi-publicité / DAU peut aider à identifier les meilleurs segments à cibler avec une campagne pour des abonnements premium sans publicité.

## Création de formules {#creating-formulas}

Les formules sont accessibles dans les panneaux de statistiques des pages [Accueil]({{site.baseurl}}/user_guide/analytics/dashboards/home), [Rapport sur les revenus]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) et [Rapport d'événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) du tableau de bord. Pour afficher ce panneau, allez dans le graphique **Performance Over Time**, changez le menu déroulant **Statistics For** en **KPI Formulas**, puis sélectionnez au moins une formule d'indicateur clé de performance pour remplir le graphique.

![Afficher les statistiques des formules d'indicateurs clés de performance sur le tableau de bord de Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Pour créer une nouvelle formule :

1. Accédez au tableau de bord approprié (**Home**, **Revenue Report** ou **Custom Events Report**).
2. Sélectionnez **Manage KPI Formulas**.
3. Saisissez un nom pour votre formule.
4. Sélectionnez les numérateurs et dénominateurs pertinents.
5. Sélectionnez **Save**.

## Numérateurs et dénominateurs disponibles {#available-numerators-and-denominators}

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Tableau de bord d'aperçu {#overview-dashboard}

| Numérateurs | Dénominateurs |
| --- | --- |
| DAU | MAU |
| Sessions | DAU |
| | Taille du segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau de bord d'aperçu" }

### Tableau de bord des revenus {#revenue-dashboard}

| Numérateurs | Dénominateurs |
| --- | --- |
| Achats (tous) | DAU |
| Achats sélectionnés (comme une carte-cadeau ou un ID de produit) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau de bord des revenus" }

### Tableau de bord des événements personnalisés {#custom-event-dashboard}

| Numérateurs | Dénominateurs |
| --- | --- |
| Nombre d'événements personnalisés | MAU |
|  | DAU |
|  | Taille du segment (seuls les segments pour lesquels le [suivi analytique]({{site.baseurl}}/viewing_and_understanding_segment_data) est activé peuvent être utilisés) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau de bord des événements personnalisés" }