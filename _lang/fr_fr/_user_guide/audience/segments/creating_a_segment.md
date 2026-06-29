---
nav_title: Créer un segment
article_title: Créer un segment
page_order: 1
page_type: tutorial
description: "Cet article pratique vous guidera dans la configuration et la création d'un segment avec Braze."
tool: Segments
search_rank: 3
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Créer un segment {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordercreate-a-segment}

> La segmentation vous permet de cibler les utilisateurs en fonction de leurs caractéristiques et actions démographiques, comportementales ou techniques. Une utilisation créative et intelligente de la segmentation et de l'automatisation des messages vous permet de faire passer vos utilisateurs du premier contact à une relation client durable, de façon fluide. Les segments se mettent à jour en temps réel à mesure que les données changent, et vous pouvez créer autant de segments que nécessaire pour vos besoins de ciblage et d'envoi de messages.

## Étape 1 : Accéder à la section des segments {#step-1-navigate-to-the-segments-section}

Allez dans **Audience** > **Segments**.

## Étape 2 : Nommer votre segment {#step-2-name-your-segment}

Sélectionnez **Créer un segment** pour commencer à construire votre segment. Nommez votre segment en décrivant le type d'utilisateur que vous souhaitez filtrer. Cela vous aidera à identifier le segment lorsque vous voudrez le cibler pour vos Campaigns ou Canvas. Des titres de segment vagues peuvent prêter à confusion.

Vous pouvez également effectuer les actions suivantes :
- Ajouter une description au segment pour fournir plus de détails sur l'intention de cette audience et laisser des notes auxquelles les autres membres de l'équipe pourront se référer.
- Ajouter une [équipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams) à votre segment.
- Ajouter des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) à votre segment pour une meilleure organisation.

![Fenêtre modale de création de segment où le segment est nommé « Lapsed Users » avec la description du segment « This is our main Lapsed User segment to target non-actives within the past fourteen days. » et deux boutons : Cancel et Create Segment.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Étape 3 : Choisir votre application ou plateforme {#step-3-choose-your-app-or-platform}

Choisissez les applications ou plateformes que vous souhaitez cibler en sélectionnant **Users from all apps** (par défaut) ou **Users from specific apps**. **Users from specific apps** cible les utilisateurs ayant au moins une session dans les applications spécifiées.

Par exemple, si vous souhaitez envoyer un message in-app uniquement aux appareils iOS, sélectionnez votre application iOS. Cela garantira que les utilisateurs qui utilisent à la fois un appareil iOS et un appareil Android ne recevront le message que sur leur appareil iOS. Dans la liste des applications spécifiques, l'option **Users from no apps** vous permet d'inclure des utilisateurs sans sessions et sans données d'application (généralement créés via une importation d'utilisateurs ou la REST API).

![Panneau des détails du segment avec l'option « Users from all apps » sélectionnée dans la section Apps Used.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Étape 4 : Ajouter des filtres à votre segment {#step-4-add-filters-to-your-segment}

Ajoutez au moins un filtre à votre segment. Vous pouvez combiner autant de filtres que vous le souhaitez pour rendre votre segmentation plus précise.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### Groupes de filtres {#filter-groups}

Les filtres sont organisés en groupes de filtres. Chaque filtre doit faire partie d'un groupe de filtres contenant au minimum un filtre. Un segment peut avoir plusieurs groupes de filtres. Pour en ajouter un, sélectionnez **Add filter group**. Modifiez le nom du groupe de filtres en sélectionnant l'icône qui apparaît lorsque vous passez la souris à côté.

![Groupe de filtres avec une icône de modification à côté de son nom.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Sélectionnez les icônes à côté de chaque filtre pour réduire l'éditeur de filtre ou dupliquer des filtres individuels. Après avoir dupliqué un filtre, vous pouvez ajuster ses valeurs dans chaque menu déroulant.

### Logique de segmentation avec AND et OR {#segmentation-logic-using-and-and-or}

Au sein d'un groupe de filtres, les filtres peuvent être reliés par « AND » ou « OR ». Entre les groupes de filtres, les groupes peuvent être reliés par « AND » ou « OR ». En utilisant les groupes de filtres, vous pouvez créer une logique de segmentation telle que :
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

Sélectionner « OR » pour vos filtres signifie que votre segment contiendra les utilisateurs satisfaisant n'importe quelle combinaison d'un, de plusieurs ou de tous ces filtres. Sélectionner « AND » signifie que les utilisateurs qui ne correspondent pas à ce filtre ne seront pas inclus dans votre segment.

{% alert tip %}
Lorsque vous sélectionnez « OR » pour des filtres incluant un filtre négatif (tel que « is not » dans un groupe d'abonnement), n'oubliez pas que les utilisateurs n'ont besoin de satisfaire qu'un seul des filtres « OR » pour être inclus dans le segment. Pour appliquer le filtre négatif indépendamment des autres filtres, utilisez un [groupe d'exclusion](#exclusion).
{% endalert %}

{% details Quand éviter l'opérateur OR %}

Il peut y avoir des situations de ciblage d'utilisateurs où l'utilisation de l'opérateur `OR` devrait être évitée. L'opérateur `OR` crée une instruction qui est évaluée comme vraie si un utilisateur remplit les critères d'un ou plusieurs des filtres dans une instruction. Par exemple, si vous souhaitez créer un segment d'utilisateurs qui appartiennent à « Foodies » mais n'appartiennent ni à « Non-foodies » ni à « Candy-lovers », alors l'utilisation de l'opérateur `OR` fonctionnerait ici.

![Groupe de filtres pour les utilisateurs dans le segment « foodies » et pas dans les segments « non-foodies » ou « candy-lovers ».]({% image_buster /assets/img_archive/or_operator_segment.png %})

Cependant, si votre objectif est de segmenter les utilisateurs qui appartiennent au segment « Foodies » et qui ne sont dans aucun des segments « Non-foodies » et « Candy-lovers », alors utilisez l'opérateur `AND`. De cette façon, les utilisateurs qui reçoivent la Campaign ou le Canvas sont dans le segment prévu (« foodies ») et ne sont pas dans les autres segments (« Non-foodies » et « Candy-lovers ») en même temps.

Les critères de ciblage négatif suivants ne doivent pas être utilisés avec l'opérateur `OR` lorsque deux filtres ou plus font référence au même attribut :

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Si `not included`, `is not`, `does not equal` ou `does not match regex` sont utilisés avec l'opérateur `OR` deux fois ou plus dans une instruction, les utilisateurs avec toutes les valeurs pour l'attribut concerné seront ciblés.

{% enddetails %}

### Opérateurs de filtre {#filter-operators}

Selon le filtre spécifique que vous sélectionnez, vous disposerez de différents opérateurs pour identifier les valeurs de filtre. Pour approfondir les opérateurs disponibles pour les différents types d'attributs personnalisés, consultez [Stockage des attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#setting-custom-attributes). Notez que lorsque vous utilisez l'opérateur « is any of », le nombre maximum d'éléments que vous pouvez inclure dans ce champ est de 256.

{% alert note %}
Braze ne génère pas de profils pour les utilisateurs tant qu'ils n'ont pas utilisé l'application pour la première fois, vous ne pouvez donc pas cibler les utilisateurs qui n'ont pas encore ouvert votre application.
{% endalert %}

![Groupes de filtres du segmenteur avec l'opérateur AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Les segments utilisant déjà le filtre **Segment Membership** ne peuvent pas être davantage inclus ou imbriqués dans d'autres segments. Cela empêche un cycle où le segment A inclut le segment B, qui tente ensuite d'inclure le segment A à nouveau. Si cela se produisait, le segment continuerait à se référencer lui-même, rendant impossible le calcul de qui appartient réellement au segment.

De plus, l'imbrication de segments de cette manière ajoute de la complexité et peut ralentir les choses. À la place, recréez le segment que vous essayez d'inclure en utilisant les mêmes filtres.
{% endalert %}

### Groupes d'exclusion (facultatif) {#exclusion}

Lors de la construction d'un segment, vous pouvez appliquer un ou plusieurs groupes d'exclusion. Les groupes d'exclusion contiennent des critères qui identifient les utilisateurs à exclure de votre segment, et seront toujours connectés à vos groupes de filtres avec un opérateur « AND NOT ».

Les groupes d'exclusion remplacent les critères du segment. Si un utilisateur correspond aux critères de votre groupe d'exclusion, il ne fera pas partie de votre segment, même s'il remplit les critères de vos groupes de filtres.

Créez un groupe d'exclusion en ajoutant des filtres comme vous le feriez pour les groupes de filtres. La statistique *Estimated Reachable Users* dans un groupe d'exclusion indique le nombre estimé d'utilisateurs restant dans votre segment après l'application des critères d'exclusion.

Les utilisateurs exclus ne seront pas comptabilisés dans la statistique *Total reachable users* de votre segment.

![Un groupe d'exclusion avec deux filtres.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### Afficher les statistiques de l'entonnoir {#viewing-funnel-statistics}

Sélectionnez **View funnel statistics** pour afficher les statistiques de ce groupe de filtres et voir comment chaque filtre ajouté impacte les statistiques de votre segment. Vous verrez un nombre estimé et un pourcentage d'utilisateurs ciblés par tous les filtres jusqu'à ce point. Une fois les statistiques affichées pour un groupe de filtres, elles se mettront à jour automatiquement chaque fois que vous modifierez les filtres. Ces statistiques sont estimées et peuvent prendre un moment à se générer.

Gardez à l'esprit que si vous utilisez AND entre vos filtres, les statistiques de l'entonnoir diminueront ; si vous utilisez OR entre vos filtres, les statistiques de l'entonnoir augmenteront.

![Deux filtres avec les statistiques de l'entonnoir du segment.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

En ajoutant des filtres qui documentent votre flux d'utilisateurs, vous pouvez voir les points où les utilisateurs décrochent. Par exemple, si vous êtes une application de réseau social et que vous souhaitez voir où vous pourriez perdre des utilisateurs pendant votre processus d'onboarding, vous pouvez ajouter des filtres de données personnalisées pour l'inscription, l'ajout d'amis et l'envoi du premier message. Si vous constatez que 85 % des utilisateurs s'inscrivent et ajoutent des amis, mais que seulement 45 % ont envoyé le premier message, alors vous saurez qu'il faut vous concentrer sur l'encouragement à envoyer plus de messages pendant vos Campaigns d'onboarding et de marketing.

### Tester les segments {#testing-segments}

Après avoir ajouté des applications et des filtres à votre segment, vous pouvez vérifier si votre segment est configuré comme prévu en recherchant un utilisateur pour confirmer s'il correspond aux critères du segment. Pour ce faire, recherchez l'`external_id` ou le `braze_id` d'un utilisateur dans la section **User Lookup**.

{% alert note %}
**User Lookup** n'accepte que les valeurs `external_id` et `braze_id`. Il n'accepte pas les adresses e-mail, les numéros de téléphone ou d'autres identifiants. Pour trouver un profil par e-mail, téléphone ou d'autres champs, utilisez plutôt [**Rechercher des utilisateurs**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles).
{% endalert %}

![Section User Lookup avec un champ de recherche.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

La recherche d'utilisateur est disponible lorsque vous :
- Créez un segment
- Configurez une audience de Campaign ou de Canvas
- Configurez une étape de parcours d'audience

Lorsqu'un utilisateur correspond aux critères du segment, du filtre et de l'application, une alerte l'indiquera.

![Une recherche d'utilisateur pour « testuser » déclenche une alerte indiquant « testuser matches all of the segments, filters, and apps. »]({% image_buster /assets/img_archive/user_lookup_match.png %})

Lorsqu'un utilisateur ne correspond pas à une partie ou à la totalité des critères du segment, du filtre ou de l'application, les critères manquants sont listés à des fins de résolution des problèmes.

![Une recherche d'utilisateur avec une alerte indiquant « test1 does not match the following targeting criteria: » et affichant les critères manquants.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### Segments à utilisateur unique {#single-user-segments}

Vous pouvez créer des segments à utilisateur unique (ou des segments d'une poignée d'utilisateurs) en utilisant des attributs uniques qui identifient les utilisateurs, comme un nom d'utilisateur ou un ID utilisateur.

Cependant, les statistiques de segmentation ou l'aperçu peuvent ne pas afficher cet utilisateur individuel car les statistiques de segment sont calculées sur la base d'un échantillon aléatoire avec un intervalle de confiance de 95 % indiquant que le résultat se situe dans une marge de +/- 1 %. Plus votre base d'utilisateurs est importante, plus il est probable que la taille de votre segment soit une estimation approximative. Pour vous assurer que votre segment contient l'utilisateur unique que vous ciblez, sélectionnez **Calculate exact statistics**. Cela calculera le nombre exact d'utilisateurs dans votre segment avec une précision supérieure à 99,999 %.

Braze dispose de filtres de test pour cibler des utilisateurs spécifiques par ID utilisateur ou adresse e-mail.

## Étape 5 : Enregistrer votre segment {#step-5-save-your-segment}

Sélectionnez **Save**. Vous êtes maintenant prêt à commencer à envoyer des messages à vos utilisateurs !

## Mesurer la taille d'un segment {#measuring-segment-size}

Pour en savoir plus sur le suivi de l'appartenance et de la taille de votre segment, consultez [Mesurer la taille d'un segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Archiver des segments {#archiving-segments}

Si vous n'avez plus besoin d'un segment spécifique ou souhaitez le retirer, vous pouvez l'archiver en accédant à la page **Segments** et en sélectionnant **Archiver** dans le menu de la ligne de ce segment.

{% alert warning %}
Lorsque vous archivez un segment, toutes les Campaigns ou Canvas qui l'utilisent (même si le segment n'est utilisé que dans un seul composant Canvas) seront également archivés. Cela inclut également les segments imbriqués où les deux segments et toutes les Campaigns ou Canvas qui les utilisent seront également archivés.
<br><br>
Vous recevrez un avertissement listant les Campaigns et Canvas qui sont sur le point d'être archivés en archivant le segment associé.
{% endalert %}

Vous pouvez désarchiver le segment en y accédant dans la page **Segments**, puis en sélectionnant **Unarchive**.

## Comportement du ciblage lorsque les utilisateurs ont plusieurs appareils {#targeting-behavior-when-users-have-multiple-devices}

Les utilisateurs ont plus d'un appareil s'ils se connectent au même compte sur plusieurs appareils. Vous pouvez vérifier la présence de plusieurs appareils dans la section **Recent Devices** d'un [profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

Lors de la segmentation avec des filtres dépendants de l'appareil (modèle d'appareil, système d'exploitation de l'appareil et version de l'application), votre segment contiendra tous les utilisateurs qui correspondent à vos critères de filtre. Ces utilisateurs recevront un message sur tous leurs appareils, y compris ceux qui ne correspondent pas nécessairement à vos critères de filtre. Par exemple, supposons que l'utilisateur A possède deux appareils : l'appareil 1 est sous OS 13.0 et l'appareil 2 est sous OS 10.0. Si un segment cible les utilisateurs avec OS 10.0, cet utilisateur fera partie de ce segment et recevra des messages sur ses deux appareils.

### Notifications push {#push-notifications}

Vous pouvez spécifier qu'une seule notification push est envoyée à chaque utilisateur. Lors de la [rédaction de votre message]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#step-4-compose-your-push-message), sélectionnez **Only send to the user's last used device** sous **Additional Settings**.

![« Additional Settings » avec une case à cocher pour envoyer uniquement au dernier appareil utilisé par l'utilisateur.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considérations {#considerations}

- **Le nombre de messages envoyés peut dépasser la taille de l'audience.** Lorsque certains utilisateurs ont plus d'un appareil, chaque appareil peut recevoir un message. Cela entraîne un nombre d'envois de messages supérieur au nombre d'utilisateurs dans votre segment.
- **L'appartenance d'un utilisateur à un segment peut ne pas correspondre à ce que vous attendez.**
    - Un utilisateur peut être ciblé sur son appareil actuel en fonction d'attributs associés à un autre appareil. Si vous ne vous attendiez pas à ce qu'un utilisateur reçoive un message, vérifiez son profil utilisateur pour la présence de plusieurs appareils.
    - Un utilisateur peut avoir fait partie de votre segment cible au moment de l'envoi, mais en raison de comportements associés à l'un de ses appareils, il peut ne plus faire partie de ce segment par la suite. Cela peut entraîner la réception d'une Campaign ou d'un Canvas par un utilisateur même s'il ne correspond plus actuellement aux critères de filtre. <br><br>Par exemple, un utilisateur pourrait recevoir un message ciblant les utilisateurs avec la version d'application la plus récente sous OS 10.0 même s'il est actuellement sous OS 13.0. Dans ce cas, l'utilisateur était sous OS 10.0 lorsque le message a été envoyé, puis a effectué la mise à jour vers OS 13.0 par la suite.<br><br> De même, si un utilisateur utilise ultérieurement un appareil avec une version d'application différente, son profil utilisateur sera mis à jour avec une nouvelle version d'application la plus récente. Cela peut donner l'impression que l'utilisateur n'aurait pas dû être éligible au message, alors qu'il l'était au moment de l'envoi.