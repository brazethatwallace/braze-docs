{% if include.content == "Differences" %}

Sie können [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [Berechtigungssätze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) und [Nutzer:innen-Rollen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) verwenden, um den Zugriff und die Verantwortlichkeiten der Unternehmensnutzer:innen innerhalb von Braze zu verwalten. Jedes Feature umfasst eine andere Sammlung von Berechtigungen und Zugriffskontrollen.

### Wesentliche Unterschiede {#key-differences}

Auf übergeordneter Ebene hat jedes Feature einen anderen Geltungsbereich:
- Berechtigungssätze legen fest, welche Aktionen Unternehmensnutzer:innen in allen Workspaces ausführen dürfen.
- Rollen steuern, welche Aktionen Unternehmensnutzer:innen in bestimmten Workspaces ausführen können.
- Teams steuern die Zielgruppen, die Unternehmensnutzer:innen mit ihren Nachrichten erreichen können.

| Feature | Was Sie tun können | Umfang&nbsp;des&nbsp;Zugriffs |
| - | - | - |
| [Berechtigungssätze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Bündeln Sie Berechtigungen für bestimmte Themenbereiche oder Aktionen (z. B. für „Entwickler:innen“ und „Marketer“) und wenden Sie diese dann auf Unternehmensnutzer:innen an, die dieselben Berechtigungen in verschiedenen Workspaces benötigen. | Unternehmensweit |
| [Rollen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Bündeln Sie individuelle angepasste Berechtigungen und Zugriffskontrollen für Workspaces (z. B. „Marketer – Modemarken“, wobei die Nutzer:in bestimmte Berechtigungen in Verbindung mit ihrer Rolle als Marketer hat und auf die Workspaces „Modemarken“ beschränkt ist). Weisen Sie anschließend den Unternehmensnutzer:innen eine Rolle zu, um ihnen direkt die entsprechenden Berechtigungen und den Zugriff auf den Workspace zu gewähren. <br><br>Nutzer:innen mit dieser Zugriffsebene sind in der Regel Manager:innen in streng kontrollierten Umgebungen mit vielen Marken oder regionalen Workspaces in einem Dashboard. | Spezifische Workspaces |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | Beschränken Sie den Zugriff von Unternehmensnutzer:innen auf Ressourcen basierend auf der Zielgruppe (z. B. Standort des Kundenstamms, Sprache und angepasste Attribute). <br><br>Nutzer:innen mit dieser Zugriffsebene sind in der Regel für einen bestimmten Bereich innerhalb der Marke verantwortlich, an der sie arbeiten, beispielsweise für die Erstellung sprachspezifischer Inhalte für eine mehrsprachige Marke. | Spezifisches Dashboard |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Key differences" }

{% endif %}