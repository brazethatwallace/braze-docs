Après avoir [intégré le SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration), les utilisateurs qui lancent votre application pour la première fois sont considérés comme « anonymes » jusqu'à ce que vous appeliez la méthode `changeUser` et que vous leur attribuiez un `external_id`. Une fois celui-ci attribué, vous ne pouvez plus les rendre anonymes. Cependant, s'ils désinstallent et réinstallent votre application, ils redeviennent anonymes jusqu'à ce que `changeUser` soit appelé.

Si un utilisateur précédemment identifié démarre une session sur un nouvel appareil, Braze fusionne les champs spécifiques du profil anonyme qui n'existent pas déjà sur le profil identifié après que vous avez appelé `changeUser` sur cet appareil à l'aide de son `external_id`. Toutes les données ne sont pas transférées : seuls les champs qui ne sont pas déjà renseignés sur le profil identifié sont fusionnés. Pour la liste complète des champs transférés, consultez le [comportement de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

{% if include.section == "user_guide" %}
{% alert tip %}
Pour une description complète, consultez la section [Définition des ID utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).
{% endalert %}
{% endif %}