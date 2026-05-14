---
nav_title: Liens profonds de navigation
article_title: Liens profonds de navigation dans Braze Pilot
page_order: 4
page_type: reference
description: "Cet article de référence présente brièvement les étapes d'intégration requises de la part de vos ingénieurs ou développeurs."
---

# Liens profonds de navigation dans Braze Pilot {#navigation-deep-links-in-braze-pilot}

> Braze Pilot prend en charge la création de liens profonds depuis l'envoi de messages Braze vers des sections spécifiques de l'application Pilot. Cela vous permet de créer des cas d'utilisation engageants, incitant les utilisateurs à explorer différentes parties de l'application Pilot. Vous pouvez également utiliser des paramètres de lien profond facultatifs pour personnaliser le contenu de certaines pages de l'application pour l'utilisateur. Pour en savoir plus sur la création de liens profonds, consultez [Création de liens profonds vers du contenu in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#what-is-deep-linking).

## Général {#general}

Voici les liens profonds vers les principales pages de navigation de l'application Pilot.

| Écran | Lien profond |
| --- | --- |
| Projets | `braze-pilot://navigation/projects` |
| Données de journal | `braze-pilot://navigation/logdata` |
| Configuration | `braze-pilot://navigation/setup` |
| Changer de langue | `braze-pilot://navigation/selectlanguage` |
| Appareil photo | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Général" }

## Steppington
Voici les liens profonds pour l'application de la marque fictive Steppington dans Pilot.

### Exemple de lien profond {#steppington-example-deep-link}

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Liens profonds sans paramètres {#steppington-deep-links-without-parameters}

| Écran | Lien profond |
| --- | --- |
| Écran de démarrage | `braze-pilot://navigation/steppington/splash` |
| Accueil | `braze-pilot://navigation/steppington/home` |
| Page Steppington+ | `braze-pilot://navigation/steppington/plus` |
| Écran des objectifs | `braze-pilot://navigation/steppington/goals` |
| Écran de modification des objectifs | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liens profonds sans paramètres" }

### Liens profonds avec paramètres {#steppington-deep-links-with-parameters}

| Écran | Lien profond |
| --- | --- |
| Entraînement | `braze-pilot://navigation/steppington/workout` |
| Entraînement actif | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liens profonds avec paramètres" }

#### Paramètres acceptés {#steppington-accepted-parameters}

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

<table aria-label="Paramètres acceptés">
  <caption>Paramètres acceptés</caption>
    <thead>
        <tr>
            <th>Paramètre</th>
            <th>Description</th>
            <th>Requis</th>
            <th>Par défaut (si non spécifié)</th>
            <th>Type</th>
            <th>Exemple</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>Le titre à afficher en haut de l'écran.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>Running</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>Une chaîne de caractères représentant l'icône à utiliser.</td>
            <td>Non</td>
            <td><code>RUNNING_HOME</code></td>
            <td>Chaîne de caractères</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>L'URL de l'image de l'élément.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>Informations sur l'entraînement, affichées au-dessus du bouton de démarrage de l'entraînement.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>Le nom de l'entraînement. Envoyé dans l'événement <code>st_completed_class</code>.</td>
            <td>Oui</td>
            <td></td>
            <td>Nombre</td>
            <td>5k%20Run</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>Le nombre de calories à afficher sur l'écran d'entraînement actif. Envoyé dans l'événement <code>st_completed_class</code>.</td>
            <td>Non</td>
            <td>Nombre aléatoire entre 500 et 1 250</td>
            <td>Nombre</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>La durée de l'entraînement. Envoyée dans l'événement <code>st_completed_class</code>.</td>
            <td>Non</td>
            <td></td>
            <td>Nombre</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>Le texte à utiliser dans la carte de gauche sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>Road%20Run</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>L'icône à utiliser dans la carte de gauche sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>Le texte à utiliser dans la carte centrale sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>L'icône à utiliser dans la carte centrale sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>Le texte à utiliser dans la carte de droite sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>L'icône à utiliser dans la carte de droite sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### Options d'icônes {#icon-options}

| Icône | Image |
| --- | --- |
| `RUNNING_HOME` | ![Icône de chaussure de course.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![Icône de cœur.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![Icône de chronomètre.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![Icône d'une personne en posture de yoga.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![Icône de vélo.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![Icône d'haltère.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Options d'icônes" }

## PantsLabyrinth
Voici les liens profonds pour l'application de la marque fictive PantsLabyrinth dans Pilot.

### Exemple de lien profond {#pantslabyrinth-example-deep-link}

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Liens profonds sans paramètres {#pantslabyrinth-deep-links-without-parameters}

| Écran | Lien profond |
| --- | --- |
| Écran de démarrage | `braze-pilot://navigation/pantslabyrinth/splash` |
| Écran d'accueil | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Écran de liste | `braze-pilot://navigation/pantslabyrinth/listing` |
| Page du panier | `braze-pilot://navigation/pantslabyrinth/cart` |
| Page de la liste de souhaits | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liens profonds sans paramètres" }

### Liens profonds avec paramètres {#pantslabyrinth-deep-links-with-parameters}

| Écran | Lien profond |
| --- | --- |
| Page de détails de l'article | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liens profonds avec paramètres" }

#### Paramètres acceptés {#pantslabyrinth-accepted-parameters}

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

<table aria-label="Paramètres acceptés">
  <caption>Paramètres acceptés</caption>
    <thead>
        <tr>
            <th>Paramètre</th>
            <th>Description</th>
            <th>Requis</th>
            <th>Par défaut (si non spécifié)</th>
            <th>Type</th>
            <th>Exemple</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>Le nom de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>Le prix de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>L'URL de l'image de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>La description de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>La quantité de l'article.</td>
            <td>Non</td>
            <td>1</td>
            <td>Nombre</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>Une chaîne de caractères représentant la taille de l'article.</td>
            <td>Non</td>
            <td>M</td>
            <td>Chaîne de caractères</td>
            <td>Large</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>Une liste de couleurs hexadécimales séparées par des virgules. Il s'agit des couleurs disponibles pour l'article.</td>
            <td>Non</td>
            <td>%23000000</td>
            <td>Chaîne de caractères</td>
            <td>%230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>Une liste de noms de couleurs séparés par des virgules. Représente les couleurs sous forme de texte.</td>
            <td>Non</td>
            <td>Black</td>
            <td>Chaîne de caractères</td>
            <td>Blue, Red</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>L'index de la couleur à sélectionner dans le sélecteur de couleurs lorsque l'utilisateur arrive sur l'écran. Si aucune valeur n'est spécifiée, la première couleur est sélectionnée.</td>
            <td>Non</td>
            <td>0</td>
            <td>Nombre</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon
Voici les liens profonds pour l'application de la marque fictive MovieCanon dans Pilot.

### Exemple de lien profond {#moviecanon-example-deep-link}

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Liens profonds sans paramètres {#moviecanon-deep-links-without-parameters}

| Écran | Lien profond |
| --- | --- |
| Écran de démarrage | `braze-pilot://navigation/moviecannon/splash` |
| Écran d'accueil | `braze-pilot://navigation/moviecannon/welcome` |
| Page de liste des films | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liens profonds sans paramètres" }

### Liens profonds avec paramètres {#moviecanon-deep-links-with-parameters}

| Écran | Lien profond |
| --- | --- |
| Page de détails du film | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liens profonds avec paramètres" }

#### Paramètres acceptés {#moviecanon-accepted-parameters}

| Paramètre | Description | Requis | Type | Exemple |
| --- | --- | --- | --- | --- |
| `id` | L'ID du film. | Oui | Nombre | 1 |
| `title` | Le titre du film. | Oui | Chaîne de caractères | Jaws |
| `thumbnail` | L'URL web de la vignette à afficher avant le film. | Oui | Chaîne de caractères | `https://picsum.photos/400` |
| `video` | L'index dans la liste des vidéos à afficher. | Non | Nombre | 0 |
| `description` | La description de la vidéo. | Oui | Chaîne de caractères | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Paramètres acceptés" }