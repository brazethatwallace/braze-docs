{% if include.alert == 'User profile external_id' %}

{% alert warning %}
N'attribuez pas d'`external_id` à un profil utilisateur avant de pouvoir l'identifier de manière unique. Une fois que vous avez identifié un utilisateur, vous ne pouvez plus le rendre anonyme.
<br><br>
Un `external_id` peut être mis à jour à l'aide de l'[endpoint `/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename). Cependant, toute tentative de définir un `external_id` différent pendant la session d'un utilisateur créera un nouveau profil utilisateur associé au nouvel `external_id`. Aucune donnée ne sera transmise entre les deux profils.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Si vous avez l'intention de créer plusieurs connecteurs Currents identiques (par exemple, deux connecteurs d'événement d'engagement lié aux messages), ils doivent se trouver dans des espaces de travail différents. Étant donné que l'intégration Braze Segment Currents ne peut pas isoler les événements de différentes applications au sein d'un seul espace de travail, ne pas respecter cette règle entraînera une déduplication inutile des données et des pertes de données.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Évitez de configurer une campagne ou un Canvas basé sur une action avec le même déclencheur que le filtre d'audience (comme un attribut modifié ou un événement personnalisé effectué). Une [condition de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) peut survenir lorsque l'utilisateur ne fait pas partie de l'audience au moment où il déclenche l'événement, ce qui signifie qu'il ne recevra pas la campagne ou n'entrera pas dans le Canvas.
{% endalert %}

{% endif %}