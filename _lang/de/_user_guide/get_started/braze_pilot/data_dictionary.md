---
nav_title: Datenwörterbuch
article_title: Datenwörterbuch für Braze Pilot
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt kurz die Integrationsschritte, die von Ihren Entwickler:innen durchgeführt werden müssen."
---

# Datenwörterbuch {#data-dictionary}

> Jede App-Simulation in Braze Pilot ist so konfiguriert, dass sie verschiedene Ereignisse und Attribute basierend auf den Aktivitäten der Nutzer:innen in der App erfasst.

## Der Umgang mit Daten {#the-approach-to-data}

Die App protokolliert angepasste Attribute und Ereignisse, die für die Branche typisch sind, die durch die fiktive Marke repräsentiert wird. Sie können diese Attribute verwenden, um Demos für eine Vielzahl gängiger Anwendungsfälle zu erstellen.
Im Allgemeinen werden alle Ereignisse und Attribute mit einem Shortcode als Präfix versehen, der der für die Daten verantwortlichen App-Simulation entspricht. Zum Beispiel:

- Alle von der Steppington-App-Simulation protokollierten Daten haben das Präfix `st_`
- Alle von der PantsLabyrinth-App-Simulation protokollierten Daten haben das Präfix `pl_`
- Alle von der MovieCanon-App-Simulation protokollierten Daten haben das Präfix `mc_`

## Liste der protokollierten Ereignisse und Attribute {#list-of-logged-events-and-attributes}

Die folgende Tabelle listet die von Braze Pilot protokollierten Ereignisse und Attribute auf.

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

<table aria-label="Liste der protokollierten Ereignisse und Attribute">
  <caption>Liste der protokollierten Ereignisse und Attribute</caption>
    <thead>
        <tr>
            <th>Name</th>
            <th>App</th>
            <th>Typ</th>
            <th>Eigenschaften</th>
            <th>Wann es protokolliert wird</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Ereignis</td>
            <td></td>
            <td>Wenn Nutzer:innen die MovieCanon-App öffnen</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Ereignis</td>
            <td><code>title: string</code></td>
            <td>Wenn Nutzer:innen ein Video fertig angesehen haben</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Ereignis</td>
            <td><code>title: string</code></td>
            <td>Wenn Nutzer:innen eine Filmseite aufrufen</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>Ereignis</td>
            <td><code>item_name: string</code></td>
            <td>Wenn Nutzer:innen eine Produktseite aufrufen</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>Ereignis</td>
            <td></td>
            <td>Wenn Nutzer:innen die PantsLabyrinth-App öffnen</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>Ereignis</td>
            <td><code>item_name: string</code></td>
            <td>Wenn Nutzer:innen einen Artikel zu ihrer Wunschliste hinzufügen</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>Ereignis</td>
            <td><code>item_name: string</code></td>
            <td>Wenn Nutzer:innen einen Artikel in ihren Warenkorb legen</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>PantsLabyrinth</td>
            <td>Ereignis</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>Wenn Nutzer:innen einen Kauf abschließen</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td></td>
            <td>Wenn Nutzer:innen die Steppington-App öffnen</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Wenn Nutzer:innen ein Training abschließen</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td><code>benefit_type: string</code></td>
            <td>Wenn Nutzer:innen den Tab „Steppington+“ aufrufen (sofern dieser mit dem Feature-Flag aktiviert ist)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td><code>class_type: string</code></td>
            <td>Wenn Nutzer:innen eine Trainingsseite aufrufen</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Wenn Nutzer:innen ein Training abschließen</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Attribut</td>
            <td><code>string</code></td>
            <td>Wenn Nutzer:innen ein Training abschließen</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td><code>class_type: string</code></td>
            <td>Wenn Nutzer:innen einen Kurs als Favorit speichern</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td><code>class_type: string</code></td>
            <td>Wenn Nutzer:innen einen Kurs aus den Favoriten entfernen</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td></td>
            <td>Wenn Nutzer:innen den Button <strong>Start Free Trial</strong> auswählen</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Ereignis</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>Wenn Nutzer:innen den Button <strong>Start Free Trial</strong> auswählen.</td>
        </tr>
    </tbody>
</table>