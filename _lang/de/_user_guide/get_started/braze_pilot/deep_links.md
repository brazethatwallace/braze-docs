---
nav_title: Navigations-Deeplinks
article_title: Navigations-Deeplinks in Braze Pilot
page_order: 4
page_type: reference
description: "Dieser Referenzartikel beschreibt kurz die erforderlichen Integrationsschritte für Ihre Entwickler:innen."
---

# Navigations-Deeplinks in Braze Pilot {#navigation-deep-links-in-braze-pilot}

> Braze Pilot unterstützt Deeplinking von Braze-Messaging zu bestimmten Bereichen der Pilot-App. So können Sie Engagement-Anwendungsfälle erstellen und Nutzer:innen in verschiedene Bereiche der Pilot-Anwendung leiten. Sie können auch optionale Deeplink-Parameter verwenden, um den Inhalt bestimmter Seiten in der App für die Nutzer:innen anzupassen. Weitere Informationen zum Deeplinking finden Sie unter [Deeplinking zu In-App-Inhalten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#what-is-deep-linking).

## Allgemein {#general}

Dies sind die Deeplinks für die Hauptnavigationsseiten in der Pilot-App.

| Bildschirm | Deeplink |
| --- | --- |
| Projekte | `braze-pilot://navigation/projects` |
| Protokolldaten | `braze-pilot://navigation/logdata` |
| Einrichtung | `braze-pilot://navigation/setup` |
| Sprache ändern | `braze-pilot://navigation/selectlanguage` |
| Kamera | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Allgemein" }

## Steppington
Dies sind die Deeplinks für die App der fiktiven Marke Steppington in Pilot.

### Beispiel-Deeplink {#steppington-example-deep-link}

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Deeplinks ohne Parameter {#steppington-deep-links-without-parameters}

| Bildschirm | Deeplink |
| --- | --- |
| Startbildschirm | `braze-pilot://navigation/steppington/splash` |
| Home | `braze-pilot://navigation/steppington/home` |
| Steppington+-Seite | `braze-pilot://navigation/steppington/plus` |
| Zielbildschirm | `braze-pilot://navigation/steppington/goals` |
| Ziele-ändern-Bildschirm | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinks ohne Parameter" }

### Deeplinks mit Parametern {#steppington-deep-links-with-parameters}

| Bildschirm | Deeplink |
| --- | --- |
| Training | `braze-pilot://navigation/steppington/workout` |
| Aktives Training | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinks mit Parametern" }

#### Akzeptierte Parameter {#steppington-accepted-parameters}

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 22%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table aria-label="Akzeptierte Parameter">
  <caption>Akzeptierte Parameter</caption>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Beschreibung</th>
            <th>Erforderlich</th>
            <th>Standard (wenn nicht angegeben)</th>
            <th>Typ</th>
            <th>Beispiel</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>Der Titel, der oben auf dem Bildschirm angezeigt wird.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Running</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>Ein String, der angibt, welches Symbol verwendet werden soll.</td>
            <td>Nein</td>
            <td><code>RUNNING_HOME</code></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>Die URL des Bildes des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>Informationen zum Training, die über dem Start-Button des Trainings angezeigt werden.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>Der Name des Trainings. Wird im <code>st_completed_class</code>-Ereignis gesendet.</td>
            <td>Ja</td>
            <td></td>
            <td>Zahl</td>
            <td>5k%20Run</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>Die Anzahl der Kalorien, die auf dem aktiven Trainingsbildschirm angezeigt werden. Wird im <code>st_completed_class</code>-Ereignis gesendet.</td>
            <td>Nein</td>
            <td>Zufallszahl zwischen 500 und 1.250</td>
            <td>Zahl</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>Die Dauer des Trainings. Wird im <code>st_completed_class</code>-Ereignis gesendet.</td>
            <td>Nein</td>
            <td></td>
            <td>Zahl</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>Der Text, der auf der linken Karte auf dem aktiven Trainingsbildschirm angezeigt wird.</td>
            <td>Nein</td>
            <td></td>
            <td>String</td>
            <td>Road%20Run</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>Das Symbol, das auf der linken Karte auf dem aktiven Trainingsbildschirm angezeigt wird.</td>
            <td>Nein</td>
            <td></td>
            <td>String</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>Der Text, der auf der mittleren Karte auf dem aktiven Trainingsbildschirm angezeigt wird.</td>
            <td>Nein</td>
            <td></td>
            <td>String</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>Das Symbol, das auf der mittleren Karte auf dem aktiven Trainingsbildschirm angezeigt wird.</td>
            <td>Nein</td>
            <td></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>Der Text, der auf der rechten Karte auf dem aktiven Trainingsbildschirm angezeigt wird.</td>
            <td>Nein</td>
            <td></td>
            <td>String</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>Das Symbol, das auf der rechten Karte auf dem aktiven Trainingsbildschirm angezeigt wird.</td>
            <td>Nein</td>
            <td></td>
            <td>String</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### Symboloptionen {#icon-options}

| Symbol | Bild |
| --- | --- |
| `RUNNING_HOME` | ![Ein Laufschuh-Symbol.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![Ein Herz-Symbol.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![Ein Stoppuhr-Symbol.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![Ein Symbol einer Person in einer Yoga-Pose.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![Ein Fahrrad-Symbol.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![Ein Hantel-Symbol.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symboloptionen" }

## PantsLabyrinth
Dies sind die Deeplinks für die App der fiktiven Marke PantsLabyrinth in Pilot.

### Beispiel-Deeplink {#pantslabyrinth-example-deep-link}

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Deeplinks ohne Parameter {#pantslabyrinth-deep-links-without-parameters}

| Bildschirm | Deeplink |
| --- | --- |
| Startbildschirm | `braze-pilot://navigation/pantslabyrinth/splash` |
| Willkommensbildschirm | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Auflistungsbildschirm | `braze-pilot://navigation/pantslabyrinth/listing` |
| Warenkorbseite | `braze-pilot://navigation/pantslabyrinth/cart` |
| Wunschliste | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinks ohne Parameter" }

### Deeplinks mit Parametern {#pantslabyrinth-deep-links-with-parameters}

| Bildschirm | Deeplink |
| --- | --- |
| Artikeldetailseite | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinks mit Parametern" }

#### Akzeptierte Parameter {#pantslabyrinth-accepted-parameters}

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 20%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table aria-label="Akzeptierte Parameter">
  <caption>Akzeptierte Parameter</caption>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Beschreibung</th>
            <th>Erforderlich</th>
            <th>Standard (wenn nicht angegeben)</th>
            <th>Typ</th>
            <th>Beispiel</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>Der Name des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>Der Preis des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>Die URL des Bildes des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>Die Beschreibung des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>Die Menge des Artikels.</td>
            <td>Nein</td>
            <td>1</td>
            <td>Zahl</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>Ein String, der die Größe des Artikels angibt.</td>
            <td>Nein</td>
            <td>M</td>
            <td>String</td>
            <td>Large</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>Eine durch Kommas getrennte Liste von Hex-Farben. Dies sind die für den Artikel verfügbaren Farben.</td>
            <td>Nein</td>
            <td>%23000000</td>
            <td>String</td>
            <td>%230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>Eine durch Kommas getrennte Liste von Farb-Strings. Stellt die Farben als Text dar.</td>
            <td>Nein</td>
            <td>Black</td>
            <td>String</td>
            <td>Blue, Red</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>Der ausgewählte Index der Farbe, die im Farbselektor vorausgewählt sein soll, wenn die Nutzer:innen den Bildschirm aufrufen. Wenn kein Wert angegeben wird, ist die erste Farbe ausgewählt.</td>
            <td>Nein</td>
            <td>0</td>
            <td>Zahl</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon
Dies sind die Deeplinks für die App der fiktiven Marke MovieCanon in Pilot.

### Beispiel-Deeplink {#moviecanon-example-deep-link}

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Deeplinks ohne Parameter {#moviecanon-deep-links-without-parameters}

| Bildschirm | Deeplink |
| --- | --- |
| Startbildschirm | `braze-pilot://navigation/moviecannon/splash` |
| Willkommensbildschirm | `braze-pilot://navigation/moviecannon/welcome` |
| Filmübersichtsseite | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinks ohne Parameter" }

### Deeplinks mit Parametern {#moviecanon-deep-links-with-parameters}

| Bildschirm | Deeplink |
| --- | --- |
| Filmdetailseite | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinks mit Parametern" }

#### Akzeptierte Parameter {#moviecanon-accepted-parameters}

| Parameter | Beschreibung | Erforderlich | Typ | Beispiel |
| --- | --- | --- | --- | --- |
| `id` | Die ID des Films. | Ja | Zahl | 1 |
| `title` | Der Titel des Films. | Ja | String | Jaws |
| `thumbnail` | Die Web-URL des Vorschaubilds, das vor dem Film angezeigt wird. | Ja | String | `https://picsum.photos/400` |
| `video` | Der Index in der Liste der anzuzeigenden Videos. | Nein | Zahl | 0 |
| `description` | Die Beschreibung des Videos. | Ja | String | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Akzeptierte Parameter" }