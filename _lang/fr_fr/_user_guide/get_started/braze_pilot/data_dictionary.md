---
nav_title: Dictionnaire de données
article_title: Dictionnaire de données pour Braze Pilot
page_order: 3
page_type: reference
description: "Cet article de référence couvre brièvement les étapes d'intégration requises de la part de vos ingénieurs ou développeurs."
---

# Dictionnaire de données {#data-dictionary}

> Chaque simulation d'application dans Braze Pilot est instrumentée pour collecter divers événements et attributs en fonction de l'activité des utilisateurs dans l'application.

## L'approche des données {#the-approach-to-data}

L'application enregistre des attributs personnalisés et des événements caractéristiques du secteur représenté par la marque fictive. Vous pouvez utiliser ces attributs pour alimenter des démonstrations couvrant divers cas d'utilisation courants.
En règle générale, tous les événements et attributs sont précédés d'un code court correspondant à la simulation d'application responsable des données. Par exemple :

- Toutes les données enregistrées par la simulation de l'application Steppington sont précédées du préfixe `st_`
- Toutes les données enregistrées par la simulation de l'application PantsLabyrinth sont précédées du préfixe `pl_`
- Toutes les données enregistrées par la simulation de l'application MovieCanon sont précédées du préfixe `mc_`

## Liste des événements et attributs enregistrés {#list-of-logged-events-and-attributes}

Le tableau suivant répertorie les événements et les attributs enregistrés par Braze Pilot.

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 32%;
}
th:nth-child(2), td:nth-child(2) {
    width: 15%;
}
th:nth-child(3), td:nth-child(3) {
    width: 10%;
}
th:nth-child(4), td:nth-child(4) {
    width: 20%;
}
th:nth-child(5), td:nth-child(5) {
    width: 28%;
}
</style>

<table aria-label="Liste des événements et attributs enregistrés">
  <caption>Liste des événements et attributs enregistrés</caption>
    <thead>
        <tr>
            <th>Nom</th>
            <th>Application</th>
            <th>Type</th>
            <th>Propriétés</th>
            <th>Quand il est enregistré</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur accède à l'application MovieCanon</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Événement</td>
            <td><code>title: string</code></td>
            <td>Lorsque l'utilisateur termine le visionnage d'une vidéo</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Événement</td>
            <td><code>title: string</code></td>
            <td>Lorsque l'utilisateur consulte une page de film</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>Événement</td>
            <td><code>item_name: string</code></td>
            <td>Lorsque l'utilisateur consulte une page de produit</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur accède à l'application PantsLabyrinth</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>Événement</td>
            <td><code>item_name: string</code></td>
            <td>Lorsque l'utilisateur ajoute un article à sa liste de souhaits</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>Événement</td>
            <td><code>item_name: string</code></td>
            <td>Lorsque l'utilisateur ajoute un article à son panier</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>PantsLabyrinth</td>
            <td>Événement</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>Lorsque l'utilisateur finalise un achat</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur accède à l'application Steppington</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Lorsque l'utilisateur termine une séance d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>benefit_type: string</code></td>
            <td>Lorsque l'utilisateur consulte l'onglet Steppington+ (s'il est activé via l'indicateur de fonctionnalité)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: string</code></td>
            <td>Lorsque l'utilisateur consulte une page d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Lorsque l'utilisateur termine une séance d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Attribut</td>
            <td><code>string</code></td>
            <td>Lorsque l'utilisateur termine une séance d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: string</code></td>
            <td>Lorsque l'utilisateur ajoute un cours à ses favoris</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: string</code></td>
            <td>Lorsque l'utilisateur retire un cours de ses favoris</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur sélectionne le bouton <strong>Start Free Trial</strong></td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>Lorsque l'utilisateur sélectionne le bouton <strong>Start Free Trial</strong>.</td>
        </tr>
    </tbody>
</table>