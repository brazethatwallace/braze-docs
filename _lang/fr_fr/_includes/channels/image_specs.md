{% if include.variable_name == "image behavior" %}


| Disposition | Comportement |
| --- | --- |
| Image et texte | Les images hautes ou étroites sont réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
| Image uniquement | Le message sera redimensionné pour s'adapter à la plupart des rapports hauteur/largeur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau" }

{% endif %}

{% if include.variable_name == "payload size" %}

Nous recommandons les tailles de payloads suivantes :

| Système d'envoi de messages | Payload recommandé |
| --- | --- |
| iOS (avant iOS 8) | 0,256 Ko |
| iOS (après iOS 8) | 2 Ko |
| Android (FCM) | 4 Ko |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau" }

{% endif %}

{% if include.variable_name == "in-app messages" %}

Les messages in-app modaux sont conçus pour s'adapter le mieux possible aux proportions de l'appareil, tout en restant fidèles à la taille et aux rapports de l'image ou du texte choisis pour votre message.

Bien qu'il n'y ait pas de limite au nombre de caractères que vous pouvez inclure dans un message in-app (boutons, titre, corps principal, etc.), nous vous recommandons de modérer la quantité de texte utilisée. Un texte trop long obligera les utilisateurs à développer et à faire défiler le message.

Tous les messages in-app ont une taille d'image recommandée de 500 Ko, une taille d'image maximale de 5 Mo, et prennent en charge les types de fichiers PNG, JPEG et GIF. Les images WebP ne sont pas prises en charge par tous les appareils ou navigateurs ; nous vous recommandons de convertir les images WebP au format PNG ou JPEG avant de les ajouter à vos messages in-app.

{% tabs %}
{% tab Portrait %}

| Type | Rapport hauteur/largeur | Qualité de l'image | Remarques |
| --- | --- | --- | --- |
| Portrait plein écran avec texte | 6:5 | Haute résolution 1200 x 1000 px <br>Résolution minimale 600 x 500 px | L'image peut être rognée de tous les côtés, mais elle occupera toujours la moitié supérieure de la fenêtre. |
| Portrait plein écran (image seule, avec ou sans boutons) | 3:5 | Haute résolution 1200 x 2000 px <br> Résolution minimale 600 x 1000 px | Sur les appareils plus grands, l'image peut être rognée sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tableau" }

{% endtab %}
{% tab Paysage %}

| Type | Rapport hauteur/largeur | Qualité de l'image | Remarques |
| --- | --- | --- | --- |
| Paysage plein écran avec texte | 10:3 | Haute résolution 2000 x 600 px <br>Résolution minimale 1000 x 300 px | L'image peut être rognée de tous les côtés, mais elle occupera toujours la moitié supérieure de la fenêtre. |
| Paysage plein écran (image seule, avec ou sans boutons) | 5:3 | Haute résolution 2000 x 600 px <br> Résolution minimale 1000 x 600 px | Sur les appareils plus grands, l'image peut être rognée sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tableau" }

{% endtab %}
{% tab Contextuel %}

| Type | Rapport hauteur/largeur | Qualité de l'image | Remarques |
| --- | --- | --- | --- |
| Contextuel | 1:1 | Haute résolution 150 x 150 px <br> Résolution minimale 50 x 50 px | Les images de différents rapports hauteur/largeur seront insérées dans un conteneur d'images carré, sans rognage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tableau" }

{% endtab %}
{% tab Fenêtre modale %}

| Type | Rapport hauteur/largeur | Qualité de l'image | Remarques |
| --- | --- | --- | --- |
| Fenêtre modale (image seule) | 1:1 | Résolution maximale recommandée : 1200 x 2000 px <br> Résolution minimale : 600 x 600 px | Le message sera redimensionné pour s'adapter à la plupart des rapports hauteur/largeur. La résolution maximale recommandée présente un rapport de 3:5, ce qui peut ne pas fournir des résultats optimaux. Les images de plus grande taille sont utilisables, mais elles peuvent entraîner des temps de chargement plus longs. <br> Le rapport hauteur/largeur idéal pour les images est 1:1. Si ce rapport n'est pas respecté, un avertissement peut apparaître lors du téléchargement. Cet avertissement est une recommandation visant à obtenir les meilleurs résultats possibles et n'empêche pas le téléchargement d'images plus volumineuses. |
| Fenêtre modale avec texte | 29:10 | Haute résolution 1450 x 500 px <br> Résolution minimale 600 x 205 px | Les images hautes seront réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tableau" }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Type de message | Longueur maximale du message | Longueur maximale du titre |
| --- | --- | --- |
| Écran de verrouillage iOS | 175 caractères | 43 caractères |
| Notification iOS | 175 caractères | 43 caractères |
| Alerte en bannière iOS | 85 caractères | 43 caractères |
| Écran de verrouillage Android | 49 caractères | 43 caractères |
| Tiroir de notification Android | 597 caractères | 43 caractères |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tableau" }

La taille recommandée pour toutes les images push est de 500 Ko.

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Tableau">
  <thead>
    <tr>
      <th>Type d'image</th>
      <th>Rapport hauteur/largeur</th>
      <th>Pixels maximums</th>
      <th>Taille maximale de l'image</th>
      <th>Types de fichier</th>
      <th>Remarques</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (recommandé)</td>
      <td>1038 x 1038</td>
      <td>5 Mo</td>
      <td>PNG, JPEG, GIF</td>
      <td>Depuis janvier 2020, les notifications push riches iOS peuvent gérer des images de 1038 x 1038 px tant que leur taille est inférieure à 10 Mo, mais nous recommandons d'utiliser des fichiers aussi petits que possible. En pratique, l'envoi de fichiers volumineux peut entraîner une surcharge inutile du réseau et rendre les délais d'expiration de téléchargement plus fréquents.<br><br>Pour plus d'informations, consultez la rubrique <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">Notifications push riches iOS</a>.</td>
    </tr>
    <tr>
      <td>Icône push Android</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 Ko</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Image de notification étendue Android</td>
      <td>2:1</td>
      <td><b>Petite :</b><br>512 x 256<br><br><b>Moyenne :</b><br>1024 x 512<br><br><b>Grande :</b><br>2048 x 1024</td>
      <td>500 Ko</td>
      <td>PNG, JPEG</td>
      <td>Utilisée dans les <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">notifications push riches Android</a>.</td>
    </tr>
    <tr>
      <td>Image intégrée Android</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>PNG, JPEG</td>
      <td>Pour plus de détails, consultez la section <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Notification push avec image intégrée Android</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 aria-label="Tableau" }

{% endif %}

{% if include.variable_name == "email" %}

| Type d'e-mail | Propriétés maximales recommandées |
| --- | --- |
| Texte uniquement | 25 Ko |
| Texte avec images | 60 Ko |
| Largeur de l'e-mail | 600 px |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau" }

| Spécifications des images | Propriétés maximales recommandées |
| --- | --- |
| Taille | 5 Mo |
| Largeur | En-tête : 600 px<br>Corps : 480 px |
| Types de fichier | PNG, JPEG, GIF<br><br> La prise en charge des images WebP varie selon les clients de messagerie. Pour garantir un rendu fiable, convertissez les images WebP au format PNG ou JPEG avant de les ajouter à vos e-mails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau" }

| Spécifications du texte | Propriétés maximales recommandées |
| --- | --- |
| Longueur de la ligne d'objet | 35 caractères<br>6 à 10 mots |
| Longueur du `"From: Name"` | 25 caractères |
| Longueur du pré-en-tête | 85 caractères |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau" }

{% endif %}

{% if include.variable_name == "content cards" %}

| Type de carte | Rapport hauteur/largeur | Qualité de l'image |
| --------- | ---------------- | ------------------- |
| Classique   | Format 1:1 | 60 x 60&nbsp;px        |
| Avec légende | Format 4:3 | Largeur minimale de 600&nbsp;px |
| Bannière    | N'importe quel rapport hauteur/largeur | Largeur minimale de 600&nbsp;px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tableau" }

Pour plus d'informations, reportez-vous aux [détails créatifs des Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details).

{% endif %}

{% if include.variable_name == "WhatsApp images" %}

Ces spécifications s'appliquent aux en-têtes de modèles, aux messages média de réponse et aux messages image.

| Propriété | Spécifications | Remarques |
|---|---|---|
| Formats pris en charge | JPEG, PNG | Meta ne prend officiellement en charge que les formats JPEG et PNG pour les messages image. Le format WebP est uniquement pris en charge pour les stickers (pas pour les messages image standard). |
| Taille maximale du fichier | 5 Mo | |
| Mode couleur | 8 bits, RVB ou RVBA | |
| Légende (messages image uniquement) | Facultatif ; 1 024 caractères maximum | |
| Dimensions recommandées | 1 125 × 600 px | Nous recommandons d'utiliser des images JPEG ou PNG de 1 125 × 600 px (1.91:1) pour un rendu homogène sur tous les appareils et en conformité avec les exigences de Meta. |
| Rapport hauteur/largeur recommandé | 1.91:1 (large) | Les formats carré (1:1) et large (16:9) sont acceptés, mais les images peuvent être rognées ou agrandies selon l'appareil de l'utilisateur.<br><br> Pour les cartes de carrousel, les images d'en-tête sont automatiquement rognées au format large par WhatsApp, sauf en l'absence de corps de texte, auquel cas elles s'affichent au format carré.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tableau" }

{% endif %}

{% if include.variable_name == "WhatsApp videos" %}

Les spécifications suivantes s'appliquent aux en-têtes de modèles, aux messages média de réponse, aux messages vidéo et aux en-têtes de cartes de carrousel.

| Propriété | Spécifications |
|---|---|
| Formats pris en charge | MP4, 3GPP |
| Taille du fichier | 16 Mo maximum |
| Codec vidéo | H.264 uniquement |
| Codec audio | AAC uniquement |
| Flux audio | Un seul flux audio ou aucun flux audio |
| Légende (messages vidéo uniquement) | Facultatif ; 1 024 caractères maximum |
| Rapport hauteur/largeur recommandé | 1.91:1 (large) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tableau" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

{% endif %}