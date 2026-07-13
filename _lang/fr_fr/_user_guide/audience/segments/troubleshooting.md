---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes liés aux segments
page_order: 9
page_type: reference
tool:
  - Segments
description: "Cet article de référence couvre la résolution des problèmes liés aux erreurs de segment, à l'éligibilité des utilisateurs, aux problèmes de filtres et aux incohérences d'analyse. Pour les définitions des filtres, consultez Filtres de segmentation. Pour les estimations de taille de segment et les comptages exacts, consultez Mesurer la taille d'un segment."
---

# Résolution des problèmes liés aux segments {#troubleshoot-segments}

> Identifiez votre symptôme dans la liste ci-dessous pour accéder à la section appropriée. Cette page couvre les erreurs de lancement, l'éligibilité des utilisateurs, les problèmes de filtres et les incohérences d'analyse. Pour les définitions des filtres, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Pour les estimations de taille de segment, les comptages exacts et les graphiques d'historique d'appartenance, consultez [Mesurer la taille d'un segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

| Symptôme | Aller à |
|---------|-------|
| L'audience est trop complexe | [L'audience cible est trop complexe pour être lancée](#target-audience-is-too-complex-to-launch) |
| Le filtre ne s'enregistre pas | [Le filtre dépasse 10 000 octets](#filter-exceeds-10000-bytes-or-is-too-long-to-save) |
| Le segment n'a aucun utilisateur | [Le segment affiche zéro utilisateur](#segment-shows-zero-users) |
| L'utilisateur n'est pas dans le segment | [Parcours d'investigation standard](#standard-investigation-path) |
| Le segment est plus grand que prévu | [Le segment est beaucoup plus grand que prévu](#segment-is-much-larger-than-expected) |
| Le nombre du segment ne correspond pas à l'analyse de la campagne | [Incohérence entre *Messages envoyés* ou *Destinataires uniques*](#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count) |
| Les options de filtre ont changé | [Les options de filtre ont changé](#filter-options-changed) |
| L'utilisateur est sur la mauvaise application | [Des informations s'affichent pour des utilisateurs d'autres applications](#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app) |
| Un utilisateur était-il dans ce segment à un moment passé ? | [Appartenance rétroactive à un segment](#retroactive-segment-membership) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Commencez ici : identifiez votre symptôme" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail lorsqu'un utilisateur devrait être dans un segment mais ne l'est pas, ou lorsqu'un comptage de segment semble incorrect.

1. **Lancement bloqué :** si vous voyez une erreur de complexité d'audience ou de filtre de 10 000 octets sur une campagne ou un Canvas, commencez par [Erreurs](#errors) (solution de contournement CSV, simplification des filtres).
2. **Prévisualisation utilisateur ou recherche d'utilisateur :** testez un utilisateur spécifique par rapport aux filtres de votre segment. Lorsqu'un utilisateur ne correspond pas à tout ou partie des critères, les critères manquants sont listés pour la résolution des problèmes. Pour les étapes, consultez [Tester les segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments) dans Créer un segment.
3. **Calculer les statistiques exactes :** si l'estimation du segment affiche 0 utilisateur ou semble incorrecte, sélectionnez **Calculate exact stats** dans le panneau **Utilisateurs pouvant être atteints**. Enregistrez votre segment avant de calculer. Si un calcul est déjà en cours, attendez qu'il se termine ; des chiffres obsolètes peuvent s'afficher jusqu'à ce que le nouveau calcul soit terminé. Pour plus de détails, consultez [Calculer les statistiques exactes]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).
4. **Vérifier les valeurs des filtres :** recherchez les fautes de frappe, les incohérences de type de données, les références obsolètes à des étapes Canvas et la [logique filtre négatif + OU](#segment-is-much-larger-than-expected).
5. **Vérifier la complexité :** si le lancement est bloqué, consultez [L'audience cible est trop complexe pour être lancée](#target-audience-is-too-complex-to-launch).
6. **Contacter l'assistance :** si le problème persiste, contactez l'[assistance Braze]({{site.baseurl}}/braze_support).

## Le segment affiche zéro utilisateur {#segment-shows-zero-users}

La taille du segment dans le tableau de bord est souvent une estimation basée sur un échantillon d'utilisateurs. Les segments très petits peuvent afficher une plage estimée incluant 0, même lorsque des utilisateurs correspondent à vos filtres.

- Sélectionnez **Calculate exact stats** dans le panneau **Utilisateurs pouvant être atteints** pour obtenir un comptage précis. Enregistrez d'abord le segment. Pour plus d'informations, consultez [Considérations relatives aux comptages estimés]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#considerations-for-estimate-counts).
- Si la **Prévisualisation utilisateur** ne renvoie aucun utilisateur pour un petit segment, cela ne signifie pas nécessairement que le segment est vide. Exécutez **Calculate exact stats** pour confirmer. Pour plus d'informations, consultez [Prévisualisation utilisateur]({{site.baseurl}}/user_guide/audience/segments/segment_data#user-preview).

## Appartenance rétroactive à un segment {#retroactive-segment-membership}

Braze ne stocke pas l'historique d'appartenance aux segments par utilisateur. Vous ne pouvez pas vérifier si un utilisateur spécifique faisait partie d'un segment au moment d'un envoi passé.

Pour capturer l'appartenance à un instant donné, exportez les utilisateurs du segment dans le tableau de bord ou appelez l'endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) avant d'envoyer une campagne ou un Canvas. Pour plus d'informations, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) (filtre d'appartenance à un segment) et [Exporter les données de segment en CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

## Erreurs {#errors}

### L'audience cible est trop complexe pour être lancée {#target-audience-is-too-complex-to-launch}

Cette erreur rare se produit lorsque votre audience cible contient trop de valeurs regex, des valeurs regex excessivement longues, des filtres excessivement détaillés (comme « est l'un des 30 000 codes postaux ») ou trop de filtres. Cela inclut tous les filtres d'une audience de campagne ou de Canvas, que les filtres se trouvent dans les segments référencés ou qu'ils soient ajoutés en tant que filtres à l'étape **Target Audience**.

![Erreur pour une audience cible qui atteint le seuil de complexité.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Lorsque vous ajoutez des filtres de segment à une campagne ou un Canvas, ces filtres sont traduits en requêtes dans Braze (le nombre de caractères de ces requêtes n'est pas en correspondance 1:1 avec le nombre de caractères qu'un utilisateur du tableau de bord voit). Lorsque Braze envoie une campagne ou un Canvas, une requête est exécutée pour combiner tous les filtres de l'audience ciblée. Un seuil est appliqué pour limiter le nombre de caractères dans la requête résultante pour une audience cible. Pour une campagne ou un Canvas donné, le nombre de caractères est additionné pour tous les segments référencés, y compris tous les filtres supplémentaires. Pour un segment donné, le nombre de caractères est additionné pour tous les filtres et valeurs de filtre.

Votre tableau de bord affichera une erreur lorsqu'une campagne, un Canvas ou un segment dépasse le seuil et ne peut pas être lancé. Si vous recevez cette erreur, simplifiez votre audience cible avant de relancer, notamment :

- Si votre audience référence plusieurs segments, assurez-vous que les segments ne comportent pas de redondances, comme les mêmes filtres apparaissant dans plusieurs segments.
- Assurez-vous de ne pas référencer des données obsolètes dans les filtres de segment. Par exemple, un filtre obsolète pourrait rechercher des utilisateurs qui n'ont pas reçu une certaine étape du Canvas au cours de la semaine passée, alors que le Canvas est arrêté depuis des mois.
- Les segments qui sont simplement des listes d'ID utilisateur ou d'adresses e-mail (qui utilisent souvent un filtre regex) peuvent être convertis en [import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) et simplifiés en un seul filtre CSV.
- Si vous utilisez CDI, vous pourrez peut-être créer un segment CDI qui extrait le groupe directement depuis votre entrepôt de données.

Vous pouvez également [contacter l'assistance]({{site.baseurl}}/braze_support) pour obtenir de l'aide supplémentaire sur l'optimisation des filtres.

{% alert note %}
La limitation du nombre de caractères a été mise en place en avril 2025. Les campagnes et Canvas lancés avant avril 2025 étaient exemptés, ce qui signifie qu'ils peuvent continuer à dépasser la limite, tandis que les campagnes et Canvas nouvellement créés ne peuvent pas la dépasser. Si vous modifiez ou clonez une campagne ou un Canvas exempté, vous ne pourrez pas le lancer tant que l'audience n'aura pas été mise à jour pour être en dessous de la limite.
{% endalert %}

### X campagnes ou Canvas actifs ou arrêtés dépassent le seuil de complexité de l'audience {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

Ce bandeau s'affiche en haut d'une liste de campagnes ou de Canvas chaque fois que des campagnes ou Canvas actifs ou arrêtés ont des audiences qui dépassent le seuil de complexité de l'audience. Sélectionnez le bandeau pour filtrer la liste et n'afficher que les campagnes ou Canvas dépassant le seuil, puis suivez les étapes de résolution des problèmes dans [L'audience cible est trop complexe pour être lancée](#target-audience-is-too-complex-to-launch).

![Bandeau d'erreur indiquant que 4 Canvas actifs ou arrêtés dépassent le seuil de complexité de l'audience.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### Le filtre dépasse 10 000 octets ou est trop long pour être enregistré {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Braze limite les filtres de segment individuels à un maximum de 10 000 octets, ce qui équivaut à 10 000 caractères anglais ou 3 333 caractères japonais. Un avertissement apparaît chaque fois qu'un filtre individuel dépasse 10 000 octets, que le filtre se trouve dans un segment ou qu'il soit ajouté directement à une campagne ou un Canvas.

![Bandeau d'erreur pour un filtre dont la valeur dépasse 10 000 caractères.]({% image_buster /assets/img/segment/filter_error.png %})

![Erreur pour un filtre d'attribut personnalisé, `menu_item`, dont la valeur d'attribut dépasse 10 000 caractères.]({% image_buster /assets/img/segment/segment_filter_error.png %})


Cette erreur se produit très rarement, mais lorsqu'elle survient, c'est généralement avec des filtres regex qui ciblent une liste d'ID utilisateur ou d'adresses e-mail. Dans ce cas, vous pouvez suivre ces étapes pour convertir les filtres en CSV :

1. Exportez les utilisateurs du segment concerné ou du filtre regex spécifique.
2. Nettoyez le CSV si nécessaire. Vous avez besoin soit de l'ID Braze, soit de l'ID Appboy, mais vous pouvez supprimer toutes les autres colonnes si elles ne sont pas nécessaires. Nous recommandons également de vérifier vos données pour confirmer qu'elles sont récentes (par exemple, supprimez les utilisateurs que vous ne cherchez plus à cibler).
3. [Importez]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) à nouveau le fichier CSV, ce qui regroupe automatiquement les utilisateurs dans un seul filtre basé sur CSV, très efficace.

## Comportement des utilisateurs {#user-behavior}

### Un utilisateur n'est plus dans un segment {#user-is-no-longer-in-a-segment}

Si un utilisateur n'est pas disponible lors de la création d'un segment, ses données utilisateur qui déterminent son éligibilité au segment peuvent avoir changé en raison de sa propre activité ou d'autres campagnes et Canvas avec lesquels il a interagi précédemment. Si la rééligibilité est activée, son profil utilisateur affiche les données les plus récentes de la campagne reçue.

Pour tester si un utilisateur spécifique correspond à votre segment aujourd'hui, utilisez la [Prévisualisation utilisateur ou la recherche d'utilisateur]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

### Des informations s'affichent pour des utilisateurs d'autres applications lorsque je filtre pour une application spécifique {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

Les utilisateurs peuvent avoir plusieurs applications, donc sélectionner une application spécifique dans la section **Applications utilisées** de la page de segmentation donnera des résultats pour les utilisateurs qui ont au moins cette application. Le filtre ne donne pas de résultats uniquement pour les utilisateurs qui ont exclusivement cette application.

## Filtrage {#filtering}

### Les options de filtre ont changé {#filter-options-changed}

Vos options de filtre sont liées au format (type de données) que vous transmettez à Braze pour votre attribut personnalisé. Pour vérifier le type de données que Braze reconnaît pour vos attributs personnalisés, accédez à **Paramètres des données** > **Attributs personnalisés**.

Si vos options de filtre ont changé, cela indique que vos données sont transmises à Braze dans un format (type de données) différent de celui utilisé précédemment. Pour des descriptions détaillées des différents types de données et de leurs options de filtrage, consultez [Types de données des attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#custom-attribute-data-types).

Gardez à l'esprit que modifier le type de données d'un attribut personnalisé dans le tableau de bord rejettera les données envoyées à Braze dans un format différent. Vous ne pouvez pas modifier le type de données d'un attribut personnalisé tant que cet attribut est référencé dans des campagnes, Canvas ou segments actifs ; le tableau de bord affichera une erreur et bloquera la modification.

L'onglet **Valeurs** d'un attribut personnalisé affiche les résultats d'un échantillon d'environ 250 000 utilisateurs. N'utilisez pas l'onglet **Valeurs** pour confirmer l'existence d'une valeur d'attribut spécifique à des fins de résolution des problèmes. Pour plus d'informations, consultez [Onglet Valeurs]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#values-tab).

### Le segment est beaucoup plus grand que prévu {#segment-is-much-larger-than-expected}

Si votre segment semble beaucoup plus grand que prévu malgré des filtres qui paraissent restrictifs, vérifiez si vous utilisez des filtres négatifs (`n'est pas`, `n'est pas égal à`, `ne correspond pas à l'expression régulière` ou `non inclus`) avec l'opérateur **OU** sur le même attribut plus d'une fois. Cette combinaison peut cibler des utilisateurs avec toutes les valeurs de l'attribut.

Pour savoir quand utiliser **ET** au lieu de **OU**, consultez [Quand éviter l'opérateur OU]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#when-to-avoid-the-or-operator) dans Créer un segment.

## Analyse et reporting {#analytics-and-reporting}

### *Messages envoyés* ou *Destinataires uniques* dans l'analyse de la campagne ne correspond pas au nombre du segment {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Si le nombre dans l'analyse de votre campagne pour *Messages envoyés* ou *Destinataires uniques* ne correspond pas au nombre d'utilisateurs dans le filtre de segment `A reçu un message de la campagne X`, il peut y avoir trois raisons possibles.

1. **Des utilisateurs peuvent avoir été archivés, orphelins ou supprimés depuis le lancement de la campagne**<br><br>Par exemple, supposons que 1 000 utilisateurs reçoivent une campagne et que vous effectuez un export CSV le même jour. Vous verrez 1 000 utilisateurs rapportés. Au cours du mois suivant, 50 de ces 1 000 utilisateurs sont supprimés (par exemple, via l'endpoint `users/delete`). Lorsque vous effectuez un autre export CSV, vous verrez 950 utilisateurs rapportés tandis que le nombre de *Destinataires uniques* dans l'**analyse de la campagne** est toujours de 1 000.<br><br>En d'autres termes, l'indicateur *Destinataires uniques* est un compteur incrémenté, tandis que le segmenteur et l'export CSV fournissent un décompte des utilisateurs actuellement existants.<br><br>

2. **La campagne a la rééligibilité activée, ce qui permet aux utilisateurs de réintégrer la campagne plusieurs fois**<br><br>Par exemple, supposons qu'une campagne e-mail a la rééligibilité définie à zéro minute (les utilisateurs peuvent réintégrer la campagne tant qu'ils remplissent les conditions du segment d'audience), et que la campagne est en cours depuis plus d'un mois. Le nombre de *Messages envoyés* dans l'**analyse de la campagne** ne correspondrait pas au nombre dans le segment car ce champ inclurait les messages envoyés à des utilisateurs en double.<br><br>En effet, Braze compte les utilisateurs uniques comme *Destinataires quotidiens uniques*, soit le nombre d'utilisateurs qui ont reçu un message particulier dans une journée. Cela signifie que les utilisateurs rééligibles sont comptés plus d'une fois en tant que destinataire unique car la fenêtre « unique » ne dure qu'une journée. Cela peut entraîner un nombre de *Destinataires quotidiens uniques* supérieur au nombre de profils utilisateur dans l'export CSV. Les profils utilisateur dans le fichier CSV sont véritablement uniques.<br><br>

3. **Des utilisateurs partageant un identifiant de canal correspondent au filtre**<br><br>Le filtre `A reçu un message de la campagne X` (et d'autres filtres « reçu ») peut correspondre à des utilisateurs qui partagent un identifiant de canal, comme le même jeton de notification push ou la même adresse e-mail, avec un autre profil utilisateur qui a reçu, ouvert ou cliqué le message.

### Un utilisateur est affecté à deux applications alors qu'il n'a enregistré une session que dans une seule {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Lors de la création d'un segment, vous pouvez cibler les utilisateurs qui ont [utilisé des applications spécifiques]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-3-choose-your-app-or-platform). Un utilisateur doit avoir eu une session dans une application spécifique pour être affecté à cette application ; cependant, il existe deux scénarios dans lesquels un utilisateur peut tout de même être affecté à une application spécifique sans avoir enregistré de session dans celle-ci.

Le premier scénario est lorsque le champ `app_id` est renseigné lors de l'utilisation de l'endpoint `/users/track` — plus précisément lors de l'utilisation d'un [objet événement]({{site.baseurl}}/api/objects_filters/event_object) ou d'un [objet achat]({{site.baseurl}}/api/objects_filters/purchase_object), comme dans cet exemple :

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

Le second scénario est lorsque le champ `app_id` est renseigné lors de l'utilisation de l'endpoint `/users/track` pour migrer des jetons de notification push, comme dans cet exemple :

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
