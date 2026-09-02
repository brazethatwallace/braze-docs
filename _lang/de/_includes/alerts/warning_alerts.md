{% if include.alert == 'User profile external_id' %}

{% alert warning %}
Weisen Sie einem Nutzerprofil keine `external_id` zu, bevor Sie die Person eindeutig identifizieren können. Nachdem Sie eine:n Nutzer:in identifiziert haben, können Sie sie oder ihn nicht mehr auf anonym zurücksetzen.
<br><br>
Eine `external_id` kann über den [`/users/external_ids/rename`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) aktualisiert werden. Jeder Versuch, während der Sitzung einer Nutzer:in eine andere `external_id` festzulegen, erstellt jedoch ein neues Nutzerprofil, das mit der neuen `external_id` verknüpft ist. Es werden keine Daten zwischen den beiden Profilen übertragen.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Wenn Sie mehr als einen der gleichen Currents-Konnektoren erstellen möchten (z. B. zwei Konnektoren für Nachrichten-Engagement-Events), müssen sich diese in verschiedenen Workspaces befinden. Da die Braze Segment Currents-Integration Events verschiedener Apps in einem einzelnen Workspace nicht isolieren kann, führt ein Verstoß dagegen zu unnötiger Daten-Deduplizierung und Datenverlust.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Vermeiden Sie es, eine aktionsbasierte Campaign oder ein Canvas mit demselben Trigger wie dem Zielgruppenfilter zu konfigurieren (z. B. ein geändertes Attribut oder ein ausgeführtes angepasstes Event). Es kann eine [Race-Condition]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) auftreten, bei der Nutzer:innen zum Zeitpunkt des Trigger-Events nicht zur Zielgruppe gehören, sodass sie die Campaign nicht erhalten oder nicht in das Canvas gelangen.
{% endalert %}

{% endif %}