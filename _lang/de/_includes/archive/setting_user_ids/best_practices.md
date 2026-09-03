### Automatische Speicherung des anonymen Nutzerverlaufs {#automatic-preservation-of-anonymous-user-history}

| Identifizierungskontext | Speicherverhalten |
| ---------------------- | -------------------------- |
| Nutzer:in wurde zuvor **nicht** identifiziert | Der anonyme Verlauf wird bei der Identifizierung mit dem Kundenprofil **zusammengeführt**. |
| Nutzer:in **wurde** zuvor in der App oder über die API identifiziert | Der anonyme Verlauf wird bei der Identifizierung **nicht** mit dem Kundenprofil zusammengeführt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Automatische Speicherung des anonymen Nutzerverlaufs" }

Unter [Identifizierte Nutzerprofile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) finden Sie weitere Informationen darüber, was passiert, wenn Sie anonyme Nutzer:innen identifizieren.

### Zusätzliche Hinweise und Best Practices {#additional-notes-and-best-practices}

Beachten Sie Folgendes:

- Wenn Ihre App von mehreren Personen genutzt wird, können Sie jeder/jedem Nutzer:in einen eindeutigen Bezeichner zuweisen, um sie/ihn zu verfolgen.
- Nachdem eine Nutzer-ID festgelegt wurde, können Sie diese:n Nutzer:in nicht mehr in ein anonymes Profil zurückversetzen.
- Ändern Sie die Nutzer-ID nicht, wenn sich ein:e Nutzer:in abmeldet, da dies das Gerät vom Kundenprofil trennen kann.
  - Infolgedessen können Sie die zuvor abgemeldeten Nutzer:innen nicht mit Nachrichten zur erneuten Interaktion ansprechen. Wenn Sie mit mehreren Nutzer:innen auf demselben Gerät rechnen, aber nur eine:n von ihnen ansprechen möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die Nutzer-ID, die Sie ansprechen möchten, während der Abmeldung separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser Nutzer-ID zu wechseln. Standardmäßig erhält nur der/die zuletzt angemeldete Nutzer:in Push-Benachrichtigungen von Ihrer App.
- Der Wechsel von einem/einer identifizierten Nutzer:in zu einem/einer anderen ist ein relativ kostspieliger Vorgang.
  - Wenn Sie den Nutzerwechsel anfordern, wird die aktuelle Sitzung für den/die vorherige:n Nutzer:in automatisch geschlossen und eine neue Sitzung gestartet. Braze stellt automatisch eine Datenaktualisierungsanfrage für In-App-Nachrichten und andere Braze-Ressourcen für den/die neue:n Nutzer:in.

{% alert tip %}
Wenn Sie sich dafür entscheiden, einen Hash eines eindeutigen Bezeichners als Ihre Nutzer-ID zu verwenden, stellen Sie sicher, dass Sie die Eingabe für Ihre Hash-Funktion normalisieren. Wenn Sie z. B. einen Hash einer E-Mail-Adresse verwenden, sollten Sie sicherstellen, dass Sie führende und abschließende Leerzeichen aus der Eingabe entfernen und die Lokalisierung berücksichtigen.
{% endalert %}