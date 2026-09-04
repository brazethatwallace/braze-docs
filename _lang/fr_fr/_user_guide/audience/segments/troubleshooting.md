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
| L'audience est trop complexe | [L'audience cible est trop complexe pour le lancement](#target-audience-is-too-complex-to-launch) |
| Le filtre ne s'enregistre pas | [Le filtre dépasse 10 000 octets](#filter-exceeds-10000-bytes-or-is-too-long-to-save) |
| Le Segment n'a aucun utilisateur | [Le Segment affiche zéro utilisateur](#segment-shows-zero-users) |
| L'utilisateur n'est pas dans le Segment | [Parcours d'investigation standard](#standard-investigation-path) |
| Le Segment est plus grand que prévu | [Le Segment est beaucoup plus grand que prévu](#segment-is-much-larger-than-expected) |
| Le nombre du Segment ne correspond pas aux analyses de la Campaign | [Écart entre *Messages envoyés* ou *Destinataires uniques*](#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count) |
| Les options de filtre ont changé | [Les options de filtre ont changé](#filter-options-changed) |
| L'attribut personnalisé imbriqué n'est pas disponible comme filtre | [L'attribut personnalisé imbriqué n'est pas disponible comme option de filtre](#nested-custom-attribute-not-available-as-a-filter-option) |
| L'utilisateur est sur la mauvaise application | [Les informations s'affichent pour les utilisateurs d'autres applications](#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app) |
| Un utilisateur était-il dans ce Segment à un moment passé ? | [Appartenance rétroactive au Segment](#retroactive-segment-membership) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Commencez ici : identifiez votre symptôme" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail lorsqu'un utilisateur devrait se trouver dans un Segment mais n'y est pas, ou lorsque le nombre d'un Segment semble incorrect.

1. **Lancement bloqué :** si vous voyez une erreur de complexité d'audience ou de filtre de 10 000 octets sur une Campaign ou un Canvas, commencez par [Erreurs](#errors) (contournement par CSV, simplification des filtres).
2. **Aperçu utilisateur ou recherche d'utilisateur :** testez un utilisateur spécifique par rapport aux filtres de votre Segment. Lorsqu'un utilisateur ne correspond pas à une partie ou à l'ensemble des critères, les critères manquants sont répertoriés pour la résolution des problèmes. Pour les étapes, consultez [Tester les Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments) dans Créer un Segment.
3. **Calculer les statistiques exactes :** si l'estimation du Segment affiche 0 utilisateur ou semble incorrecte, sélectionnez **Calculer les statistiques exactes** dans le panneau **Utilisateurs joignables**. Enregistrez votre Segment avant de lancer le calcul. Si un calcul est déjà en cours, attendez qu'il se termine ; des chiffres obsolètes peuvent s'afficher jusqu'à la fin du nouveau calcul. Pour plus de détails, consultez [Calcul des statistiques exactes]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).
4. **Vérifier les valeurs des filtres :** recherchez les fautes de frappe, les discordances de types de données, les références obsolètes aux étapes du Canvas et la [logique filtre négatif + OU](#segment-is-much-larger-than-expected).
5. **Vérifier la complexité :** si le lancement est bloqué, consultez [L'audience cible est trop complexe pour être lancée](#target-audience-is-too-complex-to-launch).
6. **Contacter l'assistance :** si vous êtes toujours bloqué, contactez l'[Assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Le Segment affiche zéro utilisateur {#segment-shows-zero-users}

La taille d'un Segment dans le tableau de bord est souvent une estimation basée sur un échantillon d'utilisateurs. Les très petits Segments peuvent afficher une plage estimée incluant 0, même lorsque des utilisateurs correspondent à vos filtres.

- Sélectionnez **Calculer les statistiques exactes** dans le panneau **Utilisateurs joignables** pour obtenir un décompte précis. Enregistrez d'abord le Segment. Pour en savoir plus, consultez [Considérations relatives aux décomptes estimés]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#considerations-for-estimate-counts).
- Si l'**Aperçu utilisateur** renvoie zéro utilisateur pour un petit Segment, cela ne signifie pas nécessairement que le Segment est vide. Lancez **Calculer les statistiques exactes** pour confirmer. Pour en savoir plus, consultez [Aperçu utilisateur]({{site.baseurl}}/user_guide/audience/segments/segment_data#user-preview).

## Appartenance rétroactive à un Segment {#retroactive-segment-membership}

Braze ne conserve pas l'historique d'appartenance aux Segments par utilisateur. Vous ne pouvez pas vérifier si un utilisateur spécifique faisait partie d'un Segment à un moment d'envoi passé.

Pour capturer l'appartenance à un instant donné, exportez les utilisateurs du Segment dans le tableau de bord ou appelez l'endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) avant d'envoyer une Campaign ou un Canvas. Pour en savoir plus, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) (filtre d'appartenance au Segment) et [Exporter les données d'un Segment au format CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

## Erreurs {#errors}

### L'audience cible est trop complexe pour le lancement {#target-audience-is-too-complex-to-launch}

Cette erreur rare se produit lorsque votre audience cible contient un trop grand nombre de valeurs regex, des valeurs regex excessivement longues, des filtres trop détaillés (comme « est l'un des 30 000 codes postaux ») ou trop de filtres. Cela inclut tous les filtres d'une audience de Campaign ou de Canvas, que les filtres se trouvent dans les Segments référencés ou qu'ils aient été ajoutés en tant que filtres à l'étape **Target Audience**.

![Erreur pour une audience cible qui atteint le seuil de complexité.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Lorsque vous ajoutez des filtres de Segment à une Campaign ou un Canvas, ces filtres sont traduits en requêtes dans Braze (le nombre de caractères de ces requêtes n'est pas en correspondance directe avec le nombre de caractères visibles par l'utilisateur du tableau de bord). Lorsque Braze envoie une Campaign ou un Canvas, une requête combinant tous les filtres de l'audience ciblée est exécutée. Nous appliquons un seuil limitant le nombre de caractères dans la requête résultante pour une audience cible. Pour une Campaign ou un Canvas donné, nous additionnons le nombre de caractères de tous les Segments référencés, y compris tous les filtres supplémentaires. Pour un Segment donné, nous additionnons le nombre de caractères de tous les filtres et de leurs valeurs.

Votre tableau de bord affiche une erreur lorsqu'une Campaign, un Canvas ou un Segment dépasse le seuil et ne peut pas être lancé. Si vous recevez cette erreur, simplifiez votre audience cible avant de relancer, notamment :

- Si votre audience fait référence à plusieurs Segments, assurez-vous que les Segments ne contiennent pas de redondances, comme les mêmes filtres apparaissant dans plusieurs Segments.
- Vérifiez que vous ne faites pas référence à des données obsolètes dans les filtres de Segment. Par exemple, un filtre obsolète pourrait rechercher des utilisateurs n'ayant pas reçu une certaine étape de Canvas la semaine précédente, alors que le Canvas est arrêté depuis des mois.
- Les Segments qui sont simplement des listes d'identifiants utilisateur ou d'adresses e-mail (qui utilisent souvent un filtre regex) peuvent être convertis en une [importation CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) et simplifiés en un seul filtre basé sur un CSV.
- Si vous disposez de CDI, vous pouvez éventuellement créer un Segment CDI qui extrait le groupe directement depuis votre entrepôt de données.

Vous pouvez également [contacter l'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) pour obtenir de l'aide supplémentaire concernant l'optimisation des filtres.

{% alert note %}
Nous avons commencé à limiter le nombre de caractères en avril 2025. Les Campaigns et les Canvas lancés avant avril 2025 bénéficient d'une exemption, ce qui signifie qu'ils peuvent continuer à dépasser la limite, contrairement aux Campaigns et Canvas nouvellement créés qui ne peuvent pas la dépasser. Si vous modifiez ou clonez une Campaign ou un Canvas exempté, vous ne pourrez pas le lancer tant que l'audience n'aura pas été mise à jour pour passer sous la limite.
{% endalert %}

### X Campaigns ou Canvas actifs ou arrêtés dépassent le seuil de complexité de l'audience {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

Ce bandeau s'affiche en haut de la liste des Campaigns ou Canvas chaque fois que des Campaigns ou Canvas actifs ou arrêtés ont des audiences dépassant le seuil de complexité de l'audience. Sélectionnez le bandeau pour filtrer la liste et n'afficher que les Campaigns ou Canvas dépassant le seuil, puis suivez les étapes de résolution des problèmes dans [L'audience cible est trop complexe pour le lancement](#target-audience-is-too-complex-to-launch).

![Bandeau d'erreur indiquant que 4 Canvas actifs ou arrêtés dépassent le seuil de complexité de l'audience.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### Le filtre dépasse 10 000 octets ou est trop long pour être enregistré {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Braze limite chaque filtre de Segment à un maximum de 10 000 octets, ce qui équivaut à 10 000 caractères anglais ou 3 333 caractères japonais. Un avertissement apparaît chaque fois qu'un filtre individuel dépasse 10 000 octets, que le filtre se trouve dans un Segment ou qu'il soit ajouté directement à une Campaign ou un Canvas.

![Bandeau d'erreur pour un filtre dont la valeur dépasse 10 000 caractères.]({% image_buster /assets/img/segment/filter_error.png %})

![Erreur pour un filtre d'attribut personnalisé, `menu_item`, dont la valeur d'attribut dépasse 10 000 caractères.]({% image_buster /assets/img/segment/segment_filter_error.png %})

Cette erreur se produit très rarement, mais lorsqu'elle survient, c'est généralement avec des filtres regex ciblant une liste d'identifiants utilisateur ou d'adresses e-mail. Dans ce cas, vous pouvez suivre ces étapes pour convertir les filtres en CSV :

1. Exportez les utilisateurs du Segment concerné ou du filtre regex spécifique.
2. Nettoyez le CSV selon vos besoins. Vous avez besoin soit de l'identifiant Braze, soit de l'identifiant Appboy, mais vous pouvez supprimer toutes les autres colonnes si elles ne sont pas nécessaires. Nous vous recommandons également de vérifier que vos données sont récentes (par exemple, supprimez les utilisateurs que vous ne cherchez plus à cibler).
3. [Importez]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) à nouveau le fichier CSV, ce qui regroupe automatiquement les utilisateurs dans un filtre unique et très efficace basé sur un CSV.

## Comportement des utilisateurs {#user-behavior}

### L'utilisateur ne fait plus partie d'un Segment {#user-is-no-longer-in-a-segment}

Si un utilisateur n'est pas disponible lors de la création d'un Segment, ses données utilisateur qui déterminent son éligibilité au Segment peuvent avoir changé en raison de sa propre activité ou d'autres Campaigns et Canvas avec lesquels il a interagi précédemment. Si la rééligibilité est activée, son profil utilisateur affiche les données les plus récentes de la Campaign reçue.

Pour vérifier si un utilisateur spécifique correspond à votre Segment aujourd'hui, utilisez l'[aperçu utilisateur ou la recherche d'utilisateur]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

### Des informations s'affichent pour des utilisateurs d'autres applications lorsque je filtre par application spécifique {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

Les utilisateurs peuvent avoir plusieurs applications. Sélectionner une application spécifique dans la section **Applications utilisées** de la page de segmentation donnera des résultats pour les utilisateurs qui possèdent au moins cette application. Le filtre ne renvoie pas de résultats uniquement pour les utilisateurs qui possèdent exclusivement cette application.

## Filtrage {#filtering}

### Les options de filtre ont changé {#filter-options-changed}

Vos options de filtre sont liées au format (type de données) que vous transmettez à Braze pour votre attribut personnalisé. Pour vérifier le type de données que Braze reconnaît pour vos attributs personnalisés, accédez à **Paramètres des données** > **Attributs personnalisés**.

Si vos options de filtre ont changé, cela indique que vos données sont transmises à Braze dans un format (type de données) différent de celui utilisé précédemment. Pour des descriptions détaillées des différents types de données et de leurs options de filtrage, consultez [types de données d'attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

Gardez à l'esprit que modifier le type de données d'un attribut personnalisé dans le tableau de bord entraîne le rejet des données envoyées à Braze dans un format différent. Vous ne pouvez pas modifier le type de données d'un attribut personnalisé tant que cet attribut est référencé dans des Campaigns, des Canvas ou des Segments actifs ; le tableau de bord affiche une erreur et bloque la modification.

L'onglet **Valeurs** d'un attribut personnalisé affiche les résultats d'un échantillon d'environ 250 000 utilisateurs. N'utilisez pas l'onglet **Valeurs** pour confirmer l'existence d'une valeur d'attribut spécifique à des fins de résolution des problèmes. Pour plus d'informations, consultez [Onglet Valeurs]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#values-tab).

### Un attribut personnalisé imbriqué n'est pas disponible comme option de filtre {#nested-custom-attribute-not-available-as-a-filter-option}

Si votre attribut personnalisé imbriqué n'apparaît pas comme option de filtre lors de la création d'un Segment, générez d'abord son schéma. Accédez à **Paramètres des données** > **Attributs personnalisés**, trouvez l'attribut et sélectionnez **Générer le schéma**. Une fois le schéma généré, l'attribut devient disponible dans le menu déroulant des filtres de Segment. Pour plus d'informations, consultez [Générer un schéma à l'aide de l'explorateur d'objets imbriqués]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema).

### Le Segment est beaucoup plus grand que prévu {#segment-is-much-larger-than-expected}

Si votre Segment semble beaucoup plus grand que prévu malgré des filtres d'apparence restrictive, vérifiez si vous utilisez des filtres négatifs (`is not`, `does not equal`, `does not match regex` ou `not included`) avec l'opérateur **OR** sur le même attribut plus d'une fois. Cette combinaison peut cibler des utilisateurs avec toutes les valeurs de l'attribut.

Pour savoir quand utiliser **AND** au lieu de **OR**, consultez [Quand éviter l'opérateur OR]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#segmentation-logic-using-and-and-or) dans Créer un Segment.

## Analyse et rapports {#analytics-and-reporting}

### Le nombre de *Messages envoyés* ou de *Destinataires uniques* dans les analyses de Campaign ne correspond pas au nombre du segment {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Si le nombre de *Messages envoyés* ou de *Destinataires uniques* dans les analyses de votre Campaign ne correspond pas au nombre d'utilisateurs dans le filtre de segment `Has received message from campaign X`, il peut y avoir trois raisons possibles.

1. **Des utilisateurs ont pu être archivés, orphelins ou supprimés depuis le lancement de la Campaign**<br><br>Par exemple, imaginons que 1 000 utilisateurs reçoivent une Campaign et que vous effectuez une exportation CSV le même jour. Vous verrez 1 000 utilisateurs rapportés. Au cours du mois suivant, 50 de ces 1 000 utilisateurs sont supprimés (par exemple, via l'endpoint `users/delete`). Lorsque vous effectuez une autre exportation CSV, vous verrez 950 utilisateurs rapportés alors que le nombre de *Destinataires uniques* dans **Campaign Analytics** est toujours de 1 000.<br><br>En d'autres termes, la métrique *Destinataires uniques* est un compteur incrémenté, tandis que le segmenteur et l'exportation CSV fournissent un décompte des utilisateurs existants à l'instant T.<br><br>

2. **La Campaign a la rééligibilité activée, ce qui permet aux utilisateurs de réintégrer la Campaign plusieurs fois**<br><br>Par exemple, imaginons qu'une Campaign d'e-mail a la rééligibilité définie à zéro minute (les utilisateurs peuvent réintégrer la Campaign tant qu'ils remplissent les critères du Segment d'audience), et que la Campaign est active depuis plus d'un mois. Le nombre de *Messages envoyés* dans **Campaign Analytics** ne correspondrait pas au nombre dans le Segment car ce champ inclurait les messages envoyés à des utilisateurs en double.<br><br>Cela s'explique par le fait que Braze comptabilise les utilisateurs uniques en tant que *Destinataires uniques quotidiens*, c'est-à-dire le nombre d'utilisateurs qui ont reçu un message donné au cours d'une journée. Cela signifie que les utilisateurs rééligibles sont comptés plus d'une fois en tant que destinataire unique, car la fenêtre « unique » ne dure qu'une journée. Il peut en résulter un nombre de *Destinataires uniques quotidiens* supérieur au nombre de profils utilisateur dans l'exportation CSV. Les profils utilisateur dans le fichier CSV sont véritablement uniques.<br><br>

3. **Des utilisateurs partageant un identifiant de canal ont correspondu au filtre**<br><br>Le filtre `Has received message from campaign X` (et d'autres filtres « reçu ») peut correspondre à des utilisateurs qui partagent un identifiant de canal, tel que le même jeton de notification push ou la même adresse e-mail, avec un autre profil utilisateur qui a reçu, ouvert ou cliqué sur le message.

### Un utilisateur est assigné à deux applications malgré l'enregistrement d'une session dans une seule application {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Lors de la création d'un Segment, vous pouvez cibler des utilisateurs qui ont [utilisé des applications spécifiques]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-3-choose-your-app-or-platform). Un utilisateur doit avoir eu une session dans une application spécifique pour être assigné à cette application ; cependant, il existe deux scénarios dans lesquels un utilisateur peut tout de même être assigné à une application spécifique sans avoir enregistré de session dans celle-ci.

Le premier scénario survient lorsque le champ `app_id` est renseigné lors de l'utilisation de l'endpoint `/users/track`, plus précisément lors de l'utilisation d'un [objet événement]({{site.baseurl}}/api/objects_filters/event_object) ou d'un [objet achat]({{site.baseurl}}/api/objects_filters/purchase_object), comme dans cet exemple :

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

Le second scénario survient lorsque le champ `app_id` est renseigné lors de l'utilisation de l'endpoint `/users/track` pour migrer des jetons de notification push, comme dans cet exemple :

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
