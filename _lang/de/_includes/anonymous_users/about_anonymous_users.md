Nachdem Sie [das Braze SDK integriert haben]({{site.baseurl}}/developer_guide/sdk_integration), werden Nutzer:innen, die Ihre App zum ersten Mal starten, als „anonym“ betrachtet, bis Sie die Methode `changeUser` aufrufen und ihnen eine `external_id` zuweisen. Einmal zugewiesen, können Sie sie nicht wieder anonymisieren. Wenn sie jedoch Ihre App deinstallieren und neu installieren, werden sie wieder anonym, bis `changeUser` aufgerufen wird.

Wenn ein zuvor identifizierter Nutzer eine Sitzung auf einem neuen Gerät startet, führt Braze bestimmte Felder aus dem anonymen Profil, die auf dem identifizierten Profil noch nicht vorhanden sind, zusammen, nachdem Sie `changeUser` auf diesem Gerät mit der entsprechenden `external_id` aufgerufen haben. Es werden nicht alle Daten übertragen – nur Felder, die auf dem identifizierten Profil noch nicht ausgefüllt sind, werden zusammengeführt. Die vollständige Liste der übertragenen Felder finden Sie unter [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

{% if include.section == "user_guide" %}
{% alert tip %}
Eine vollständige Anleitung finden Sie unter [Nutzer:innen-IDs einrichten]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).
{% endalert %}
{% endif %}