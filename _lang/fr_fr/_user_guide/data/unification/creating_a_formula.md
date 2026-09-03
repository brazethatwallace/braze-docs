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

## Cas d'usage {#use-cases}

Les formules, en particulier lorsqu'elles sont combinées avec des événements personnalisés, peuvent vous aider à comprendre les comportements des utilisateurs au sein de votre application. Les formules peuvent également fournir des informations plus approfondies sur les habitudes d'achat des Segments, même si votre entreprise utilise des médias payants en complément de Braze, comme Google Ads ou la télévision.

Voici quelques exemples de types de comportements pouvant être détectés à l'aide des formules :

- **Applications de covoiturage :** si vous disposez d'un événement personnalisé pour les annulations de course par l'utilisateur, vous pouvez configurer une fonction Courses annulées / utilisateurs actifs quotidiens pour déterminer si certains Segments d'utilisateurs ont tendance à annuler plus de courses que d'autres.
- **Applications e-commerce :** en configurant une fonction pour les achats d'un ID de produit donné / utilisateurs actifs mensuels, vous pouvez comparer la popularité d'un produit récemment promu entre différents Segments, même si toutes les promotions n'ont pas pu être suivies via Braze.
- **Applications multimédias utilisant des publicités :** si l'expérience des utilisateurs est interrompue par des publicités entre des clips vidéo ou audio, enregistrer les sorties en cours de publicité comme événement personnalisé et calculer le ratio sorties en cours de publicité / utilisateurs actifs quotidiens peut aider à identifier les meilleurs Segments à cibler avec une Campaign d'abonnements premium sans publicité.

## Création de formules {#creating-formulas}

Les formules sont accessibles depuis les pages [Accueil]({{site.baseurl}}/user_guide/analytics/dashboards/home), [Rapport de revenus]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) et [Rapport d'événements personnalisés]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) du tableau de bord. Sur les pages **Accueil** et **Rapport de revenus**, ouvrez le graphique **Performance Over Time**, définissez **Statistics For** sur **KPI Formulas**, puis sélectionnez au moins une formule. Sur la page **Custom Events Report**, ouvrez **Filters**, sélectionnez une ou plusieurs options **KPI formula**, puis sélectionnez **Apply**.

![Afficher les statistiques pour les formules KPI dans le tableau de bord de Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Pour créer une nouvelle formule :

1. Accédez au tableau de bord approprié (**Accueil**, **Rapport de revenus** ou **Custom Events Report**).
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
| Utilisateurs actifs quotidiens | Utilisateurs actifs mensuels |
| Sessions | Utilisateurs actifs quotidiens |
| | Taille du Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau de bord d'aperçu" }

### Tableau de bord des revenus {#revenue-dashboard}

| Numérateurs | Dénominateurs |
| --- | --- |
| Achats (tous) | Utilisateurs actifs quotidiens |
| Achats sélectionnés (tels qu'une carte cadeau ou un ID de produit) | Utilisateurs actifs mensuels |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau de bord des revenus" }

### Tableau de bord des événements personnalisés {#custom-event-dashboard}

| Numérateurs | Dénominateurs |
| --- | --- |
| Nombre d'événements personnalisés | Utilisateurs actifs mensuels |
|  | Utilisateurs actifs quotidiens |
|  | Taille du Segment (seuls les Segments pour lesquels le [suivi analytique]({{site.baseurl}}/viewing_and_understanding_segment_data) est activé peuvent être utilisés) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau de bord des événements personnalisés" }