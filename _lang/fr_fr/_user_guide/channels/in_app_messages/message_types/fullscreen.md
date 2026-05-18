---
nav_title: "Plein écran"
article_title: Messages in-app plein écran
description: "Cet article de référence couvre les exigences de message et de conception des messages in-app plein écran."
page_type: reference
page_order: 1
channel:
  - in-app messages
tool:
  - Media

---

# Messages in-app plein écran {#fullscreen-in-app-messages}

> Les messages plein écran occupent la totalité de l'écran de l'appareil ! Ce type de message est idéal lorsque vous avez vraiment besoin de l'attention de vos utilisateurs, par exemple pour des mises à jour obligatoires de l'application.

Ce type de message est disponible dans l'[éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) et dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

{% tabs %}
{% tab Portrait %}

![Deux messages in-app plein écran côte à côte en orientation portrait, détaillant les recommandations d'image et de texte. Consultez les sections suivantes pour plus de détails.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Paysage %}

![Deux messages in-app plein écran côte à côte en orientation paysage, détaillant les recommandations d'image et de texte. Consultez les sections suivantes pour plus de détails.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Images {#images}

Les messages in-app plein écran remplissent toute la hauteur de l'appareil et sont recadrés horizontalement (côtés gauche et droit) si nécessaire. Les messages plein écran avec image et texte remplissent 50 % de la hauteur de l'appareil. Tous les messages in-app plein écran remplissent la barre d'état sur les appareils à encoche.

- Toutes les images doivent peser moins de 5&nbsp;Mo.
- Nous acceptons uniquement les formats PNG, JPEG et [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/#gifs).
- Nous recommandons que vos images pèsent 500&nbsp;Ko.

{% alert tip %} Créez vos ressources en toute confiance ! Nos modèles d'images pour messages in-app et nos superpositions de zones sûres sont conçus pour s'adapter parfaitement aux appareils de toutes tailles. [Télécharger le ZIP des modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Portrait {#portrait}

| Disposition | Taille de la ressource | Notes |
|--- | --- | --- |
| Image et texte | Rapport hauteur/largeur 6:5<br> Haute résolution 1200 x 1000&nbsp;px<br> Minimum 600 x 500&nbsp;px | Un recadrage peut se produire sur tous les côtés, mais l'image remplira toujours les 50 % supérieurs de la zone d'affichage |
| Image uniquement | Rapport hauteur/largeur 3:5<br> Haute résolution 1200 x 2000&nbsp;px<br> Minimum 600 x 1000&nbsp;px | Un recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Portrait" }

### Paysage {#landscape}

| Disposition | Taille de la ressource | Notes |
|--- | --- | --- |
| Image et texte | Rapport hauteur/largeur 10:3<br> Haute résolution 2000 x 600px<br> Minimum 1000 x 300&nbsp;px | Un recadrage peut se produire sur tous les côtés, mais l'image remplira toujours les 50 % supérieurs de la zone d'affichage |
| Image uniquement | Rapport hauteur/largeur 5:3<br> Haute résolution 2000 x 1200px<br> Minimum 1000 x 600&nbsp;px | Un recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paysage" }

### Zone sûre de l'image {#image-safe-zone}

Lors de la prévisualisation d'un message in-app plein écran dans la plateforme Braze, vous pouvez activer la zone sûre de l'image pour visualiser la partie du message qui ne sera pas recadrée lors de l'affichage sur différents appareils. En plus de tester la zone sûre de l'image dans le volet de prévisualisation, nous vous recommandons de toujours [tester votre message]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message).

![Prévisualisation d'un message in-app dans Braze avec l'option « Afficher la zone sûre de l'image » activée. La zone sûre de l'image est une superposition sur l'image qui indique quelles parties de l'image ne seront pas recadrées.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Écrans plus grands {#larger-screens}

Sur une tablette ou un navigateur de bureau, un message in-app plein écran s'affiche au centre de l'écran de l'application, comme illustré dans la capture d'écran suivante.

{% tabs %}
{% tab Portrait %}

![Message in-app plein écran tel qu'il apparaîtrait sur un grand écran en orientation portrait. Le message s'affiche sous forme de grande fenêtre modale centrée à l'écran.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Paysage %}

![Message in-app plein écran tel qu'il apparaîtrait sur un grand écran en orientation paysage. Le message s'affiche sous forme de grande fenêtre modale centrée à l'écran.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}