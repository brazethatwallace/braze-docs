In Braze dienen Geofences und Standort-Tracking unterschiedlichen Zwecken:

| | Standort-Tracking | Geofences |
|---|---|---|
| Zweck | Nutzer:innen basierend auf ihrem Aufenthaltsort segmentieren | Messaging Trigger or triggern or triggern, wenn Nutzer:innen einen Bereich betreten oder verlassen |
| Typische Verwendung | `Most Recent Location` und verwandte Filter | Realtime-Campaigns bei Geofence-Eintritt oder -Austritt |
| Wann der Standort ausgewertet wird | Wird aktualisiert, wenn die App geöffnet ist (Sitzungsstart); spiegelt den zuletzt bekannten Standort der Nutzer:innen wider | Wird vom Betriebssystem überwacht, wenn Standortberechtigungen dies erlauben – auch wenn die App im Hintergrund läuft oder geschlossen ist |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Location tracking compared to geofences" }

- **Standort-Tracking:** Erfasst und speichert den letzten bekannten Standort jeder Nutzer:in in ihrem Profil. Sie verwenden diese Daten für rückblickende Segmentierung – beispielsweise zielt der Filter `Most Recent Location` auf Nutzer:innen basierend darauf ab, wo sie Ihre App zuletzt geöffnet haben, nicht unbedingt darauf, wo sie sich in Realtime befinden.
- **Geofences:** Definieren virtuelle Grenzen um einen Breiten- und Längengrad mit einem Radius. Wenn eine Nutzer:in eine Grenze betritt oder verlässt, kann Braze Aktionen Trigger or triggern or triggern, wie z. B. das Senden einer Campaign. Geofences erfordern eine zusätzliche SDK or Software-Development-Kit-Einrichtung über das grundlegende Standort-Tracking hinaus.

Beide Features erfordern, dass Nutzer:innen Standortberechtigungen erteilen. Wenn eine Nutzer:in das Standort-Tracking deaktiviert, werden zuvor gespeicherte Standortdaten nicht automatisch aus ihrem Profil entfernt, aber es werden keine neuen Standortdaten mehr erfasst.