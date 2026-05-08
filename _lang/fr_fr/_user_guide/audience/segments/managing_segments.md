---
nav_title: Gérer les segments
article_title: Gérer les segments
page_order: 2
page_type: tutorial
tool: Segments
description: "Cet article présente les actions que vous pouvez effectuer pour gérer vos segments, comme filtrer une liste de segments, créer des segments et modifier des segments."

---

# Gérer les segments {#manage-segments}

> La section Segments vous permet de consulter une liste complète de vos segments existants, de créer de nouveaux segments et de modifier les segments existants. Vous pouvez affiner la liste des segments en sélectionnant divers filtres et colonnes afin que seules les informations les plus pertinentes pour vous soient affichées.

![La section Segments affichant une liste de segments actifs.]({% image_buster /assets/img/segment/segments_page.png %})

## Personnaliser votre vue {#customizing-your-view}

Adaptez votre vue de la liste des segments en utilisant des filtres et en modifiant les colonnes que vous souhaitez afficher. Lorsque vous quittez la section **Segments** et y revenez, la liste revient à la vue par défaut, effaçant tous les filtres que vous aviez précédemment sélectionnés.

### Filtre par état {#status-filter}

Vous pouvez restreindre la liste pour n'afficher que les segments actifs ou archivés. Tout segment non archivé est considéré comme actif.

### Filtres {#filters}

Triez les segments de la liste en ajustant les filtres suivants :
- **Last Edited By :** L'utilisateur qui a modifié les segments en dernier
- **Last Edited :** Plage de temps pendant laquelle les segments ont été modifiés pour la dernière fois
- **Estimated Size :** Plage approximative du nombre d'utilisateurs dans les segments
- **Tags :** Étiquettes associées aux segments
- **Teams :** Équipes associées aux segments
- **Advanced Tracking Segments Only :** Afficher uniquement les segments pour lesquels le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#segment-analytics-tracking) est activé.

### Colonnes {#columns}

Voici les colonnes d'informations que vous pouvez sélectionner pour les afficher dans la liste des segments :
- **Filters :** Nombre de filtres dans le segment
- **Last edited :** Date de la dernière modification du segment
- **Last edited by :** L'utilisateur qui a modifié le segment en dernier
- **Tags :** Étiquettes associées au segment
- **Teams :** Équipes associées au segment
- **Estimated size :** Nombre estimé d'utilisateurs dans le segment
- **Canvases :** Nombre de Canvas qui utilisent le segment
- **Campaigns :** Nombre de Campaigns qui utilisent le segment

### Afficher uniquement les favoris {#show-starred-only}

Sélectionner **Show Starred Only** restreint votre vue aux segments que vous avez marqués comme favoris.

## Consulter l'utilisation d'un segment dans l'envoi de messages {#messaging-use}

Accédez à la section **Messaging Use** d'un segment pour obtenir un aperçu des endroits où le segment est utilisé, par exemple dans d'autres segments, Campaigns et Canvas.

{% alert note %}
Pour éviter les boucles de segments se référençant mutuellement, les segments qui utilisent le filtre **Segment Membership** ne peuvent pas être référencés par d'autres segments. Pour plus de détails, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).
{% endalert %}

## Gérer des segments spécifiques {#managing-specific-segments}

![Le menu de modification d'un segment affichant les options « Edit », « Duplicate », « Archive » et « Add to starred ».]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Pour gérer un segment spécifique, survolez-le et sélectionnez l'icône de menu à la fin de la ligne pour afficher les options suivantes :
- **Edit :** Modifier les filtres de votre segment.
- **Duplicate :** Créer une copie de votre segment.
- **Archive :** Archiver le segment. Notez que cela archivera également toutes les Campaigns ou Canvas qui utilisent ce segment.
- **Add to starred :** Marquer le segment comme favori, ce qui vous permet d'y accéder rapidement en cochant la case « Show starred only » dans la section des segments.

Vous pouvez également effectuer des actions groupées, notamment l'archivage groupé et l'étiquetage groupé, en cochant les cases à côté de plusieurs noms de segments.

{% alert tip %}
Si vous avez besoin d'un export lisible par une machine des segments existants dans l'espace de travail (et pas seulement la vue actuelle du tableau), utilisez l'[endpoint Exporter la liste des segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) et paginez les résultats. Pour auditer les segments archivés, consultez-les séparément dans le tableau de bord **Segments** en utilisant le filtre par état.
{% endalert %}

![Plusieurs segments sélectionnés avec « CRM » sélectionné dans le champ déroulant « Tag As ».]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Modifications depuis la dernière consultation {#changes-since-last-viewed}

Le nombre de mises à jour des segments effectuées par d'autres membres de votre équipe est suivi par l'indicateur *Changes Since Last Viewed* sur la page d'aperçu du segment. Sélectionnez **Changes Since Last Viewed** pour consulter un journal des modifications apportées au nom, à la description et à l'audience cible du segment. Pour chaque mise à jour, vous pouvez voir qui a effectué la modification et quand. Vous pouvez utiliser ce journal des modifications pour auditer les changements apportés à votre segment.

## Rechercher des segments {#searching-for-segments}

Recherchez des noms de segments en saisissant des termes dans le champ de recherche.

Tous les termes et chaînes de caractères saisis dans ce champ seront recherchés. Par exemple, la recherche de « test segment 1 » renverra les segments contenant « test », « segment » ou « 1 » n'importe où dans leur nom. Pour rechercher une chaîne exacte, mettez votre terme de recherche entre guillemets. La recherche de [« test segment 1 »] renverra tous les segments contenant la phrase exacte « test segment 1 » dans leur nom.

![Les résultats de recherche pour la saisie de « all users » dans le champ de recherche incluent « All Users (Test) », « All Users », « All Users 15 ».]({% image_buster /assets/img/segment/segments_search.png %})

### Segments dans les Canvas {#segments-in-canvases}

Pour rechercher toutes les références de segments, y compris celles dans d'autres segments, Campaigns ou Canvas, accédez à la section [Utilisation dans l'envoi de messages](#messaging-use) d'un segment. Le filtre **Target segment** sur la page **Canvas** recherche uniquement les segments d'audience Canvas.

![Filtre Target segment sur la page Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}