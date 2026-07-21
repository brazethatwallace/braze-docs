---
nav_title: Données du Canvas
article_title: Exporter les données du Canvas
page_order: 3
page_type: reference
description: "Cet article de référence explique comment exporter les analyses de Canvas."
tool:
  - Canvas
  - Reports

---

# Exporter les données du Canvas {#export-canvas-data}

> Les données utilisateur peuvent être exportées vers un fichier CSV. Cette page explique comment exporter des données pour l'ensemble de votre Canvas ou pour un composant spécifique du Canvas.

## Exporter les données d'un Canvas {#exporting-data-for-a-canvas}

Pour exporter les données d'un Canvas, procédez comme suit :

1. Accédez à **Envoi de messages** > **Canvas** et sélectionnez votre Canvas.
2. Sélectionnez la liste déroulante **Données utilisateur** dans la section **Détails du Canvas**.
3. Sélectionnez l'une des options d'exportation suivantes :
  - **Exporter les données utilisateur en CSV** ou
  - **Exporter les adresses e-mail en CSV**.

Vous pouvez également exporter les données utilisateur de tous les participants d'un Canvas sous forme de fichier CSV.

## Exporter les utilisateurs ayant accédé ou réaccédé à un Canvas {#export-users-who-entered-or-re-entered-a-canvas}

Lorsque la [rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) est activée, les utilisateurs peuvent accéder au même Canvas plusieurs fois. L'option **Exporter les données utilisateur en CSV** sur la page de détails du Canvas exporte les utilisateurs ayant accédé au Canvas, mais n'inclut pas le nombre d'accès de chaque utilisateur ni l'horodatage de chaque accès.

Pour analyser quand les utilisateurs ont accédé ou réaccédé à un Canvas, utilisez l'une des options suivantes :

- **Accès le plus récent par utilisateur :** Exportez un segment avec le champ [`canvases_received`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) en utilisant l'endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment). Pour chaque Canvas, l'exportation inclut les horodatages `last_entered` et `last_exited` pour cet utilisateur. Le champ `canvases_received` contient les données des 90 derniers jours.
- **Chaque accès, y compris les réentrées :** Utilisez les [événements d'entrée dans le Canvas]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-entry-events) dans Braze Currents ou le partage de données Snowflake. Chaque événement `users.canvas.Entry` représente un accès au Canvas et inclut un horodatage `time`. Comptez les événements par utilisateur pour déterminer combien de fois ils y ont accédé.
- **Créer une liste d'utilisateurs dans le tableau de bord :** Créez un segment avec un filtre **Entered Canvas Variation**, puis exportez le segment en CSV. Consultez la [résolution des problèmes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#user-didnt-enter-the-canvas).

{% alert note %}
Si vous n'avez pas intégré Currents et que vous avez besoin de chaque horodatage d'accès historique, contactez votre gestionnaire du succès des clients Braze.
{% endalert %}

Pour une étape spécifique du Canvas dans le flux de travail d'origine, utilisez **Exporter les données utilisateur en CSV** sur la page de détails de l'étape.

## Exporter les données d'un composant (flux de travail d'origine uniquement) {#exporting-data-for-a-component-original-workflow-only}

Les résultats de Canvas peuvent être exportés composant par composant pour le flux de travail Canvas d'origine. Pour ce faire, sélectionnez le composant souhaité, puis sélectionnez la liste déroulante **Données utilisateur** sur la page **Détails de l'étape du Canvas**.

![Liste déroulante « Données utilisateur » sur la page « Détails du Canvas ».]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez notre article de [résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}