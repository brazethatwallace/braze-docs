---
nav_title: Nutzerarchivierung
article_title: Nutzerarchivierung
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die Definitionen der Nutzerarchivierung, die Spam-Blockierung und wie Sie Ihre Richtlinie zur Nutzerarchivierung anpassen können."

---
# Nutzerarchivierung {#user-archival}

> Jeden Sonntag um 5:30 Uhr EST führt Braze einen Prozess durch, um inaktive und inaktive:r Nutzer:in aus den Braze-Diensten zu entfernen. Beachten Sie, dass Braze Nutzer:innen erst archiviert, wenn die Anzahl der Nutzer:innen im Workspace den Schwellenwert von 250.000 erreicht.

Dieses Verfahren soll Braze dabei helfen, genaue Statistiken über die für Kampagnen erreichbaren Zielgruppen zu erstellen. Es dient auch der Einhaltung von zwei Schlüsselkonzepten der [DSGVO][1]:

1. Der Grundsatz der Speicherbegrenzung – verarbeitete und gespeicherte personenbezogene Daten sollten nicht länger aufbewahrt werden als notwendig.
2. Es muss ein legitimer Geschäftszweck für die Verarbeitung personenbezogener Daten vorliegen.

Das heißt, personenbezogene Daten, die verarbeitet und gespeichert werden, sollten nicht länger als nötig aufbewahrt werden, und personenbezogene Daten sollten nur für legitime Geschäftszwecke verarbeitet werden. Bei archivierten Nutzer:innen wird auch der Abmeldestatus gemäß DSGVO gelöscht.

{% alert important %}
Archivierte Nutzer:innen werden dauerhaft gelöscht. <br><br>Sie können [Ihre Richtlinie zur Nutzerarchivierung anpassen](#customizing-your-user-archival-policy), indem Sie Canvas verwenden. Kund:innen haben die volle Kontrolle darüber, ob Nutzer:innen als inaktiv oder ruhend eingestuft werden. Canvas bietet die Möglichkeit, dies automatisch zu tun, sodass Sie diese Funktion für einige oder alle Ihrer inaktiven oder ruhenden Nutzer:innen effektiv ausschalten können.
{% endalert %}

## Definitionen der Nutzerarchivierung {#user-archival-definitions}

### Aktive Nutzer:innen {#active-users}

Braze definiert „aktive Nutzer:innen“ für einen bestimmten Zeitraum als alle Nutzer:innen, die eine Sitzung in einer mobilen App oder Website aufgezeichnet, ein Update erhalten, eine Nachricht erhalten oder mit einer Nachricht interagiert haben.

Wenn Sie Nutzer-IDs festlegen, um Nutzer:innen zu identifizieren, wenn sich neue Nutzer:innen anmelden, werden diese als separate aktive Nutzer:innen gezählt. Nutzer:innen, die über die API aktualisiert werden, werden ebenfalls als aktive Nutzer:innen in dem Zeitraum gezählt, in dem sie aktualisiert werden.

{% alert important %}
Sowohl inaktive als auch ruhende Nutzer:innen werden archiviert, es sei denn, sie sind aus den unten aufgeführten Gründen von der Archivierung ausgeschlossen.
{% endalert %}

### Inaktive Nutzer:innen {#inactive-users}

„Inaktive Nutzer:innen“ sind Nutzer:innen, die nicht erreichbar sind und wahrscheinlich abgewandert sind. Inaktive Nutzer:innen sind diejenigen, die alle folgenden Kriterien erfüllen:

- Können keine E-Mails empfangen. Sie haben zum Beispiel keine E-Mail-Adresse oder sind von allen E-Mail-Listen abgemeldet.
- Können keine SMS empfangen. Sie haben zum Beispiel keine gültige Telefonnummer oder sind von allen SMS-Abo-Gruppen abgemeldet.
- Können keinen Push empfangen. Sie haben zum Beispiel die App deinstalliert oder die Push-Berechtigungen deaktiviert.
- Können keine WhatsApp-Nachricht empfangen. Sie haben zum Beispiel keine gültige Telefonnummer oder sind von allen WhatsApp-Abo-Gruppen abgemeldet.
- Können keine LINE-Nachricht empfangen. Sie haben zum Beispiel keine LINE-ID oder sind von allen LINE-Abo-Gruppen abgemeldet.
- Haben seit über sechs Monaten keine mobile App genutzt oder keine Website in einem Workspace besucht.
- Haben seit über sechs Monaten keine Nachrichten aus einem Workspace erhalten.
- Wurden seit mehr als sechs Monaten nicht aktualisiert.

In diesem Fall können diese Nutzer:innen nicht per Messaging erreicht werden und zeigen kein Engagement für Ihre Marke. Diese Nutzer:innen haben sich effektiv abgewandert.

### Ruhende Nutzer:innen {#dormant-users}

„Ruhende Nutzer:innen“ sind Nutzer:innen, die in den letzten zwölf Monaten keine Aktivität gezeigt haben und:

- Seit über zwölf Monaten keine mobile App genutzt oder keine Website in einem Workspace besucht haben.
- Seit über zwölf Monaten keine Nachrichten aus einem Workspace erhalten haben.
- Seit mehr als zwölf Monaten nicht aktualisiert wurden.

## Nutzer:innen der globalen Kontrollgruppe {#global-control-group-users}

Nutzer:innen in der globalen Kontrollgruppe werden niemals archiviert, auch wenn sie die Definition von inaktiven oder ruhenden Nutzer:innen erfüllen.

### Behandlungsstichprobe {#treatment-sample-group}

Nutzer:innen der Behandlungsstichprobe in einem Bericht zur globalen Kontrollgruppe sind von der Archivierung ausgeschlossen.

## Testnutzer:innen {#test-users}

Testnutzer:innen werden niemals archiviert, auch wenn sie die Definition von inaktiven oder ruhenden Nutzer:innen erfüllen.

## Spam-Blockierung {#spam-blocking}

Braze blockiert einzelne Nutzer:innen mit mehr als fünf Millionen Sitzungen („Dummy-Nutzer:innen“) und nimmt deren SDK-Ereignisse nicht mehr auf, da diese in der Regel das Ergebnis einer fehlerhaften Integration sind. Wenn Sie feststellen, dass dies bei einem/einer legitimen Nutzer:in passiert ist, reichen Sie ein Ticket beim Braze-[Support]({{site.baseurl}}/braze_support/) ein.

Um Dummy-Nutzer:innen in Ihrem Dashboard zu finden, führen Sie die folgenden Schritte durch:

1. Erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).
2. Wählen Sie den Filter `Session Count` aus und setzen Sie ihn auf `more than 5,000,000`.
3. Exportieren Sie das Segment über CSV.

Falls erforderlich, können Sie die Nutzer:innen über den [`/users/delete`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) löschen.

## Richtlinie zur Nutzerarchivierung anpassen {#customizing-your-user-archival-policy}

Braze bietet Features zur Daten-Orchestrierung, mit denen Sie Ihre Richtlinie zur Nutzerarchivierung anpassen können. Erstellen Sie eine Richtlinie zur Nutzerarchivierung, die Ihnen das Beste aus beiden Welten bietet – mit der Canvas-Komponente [Nutzeraktualisierung]({{site.baseurl}}/user_update/).

So können Sie:

- Die DSGVO und bewährte Datenschutzpraktiken einhalten, indem Sie Nutzerprofile löschen, die nicht mehr von Nutzen sind.
- Alle Nutzerprofile aufbewahren, für die Sie einen legitimen geschäftlichen Grund haben.

### Schritte {#steps}

1. Erstellen Sie eine Zielgruppe aus Nutzer:innen, die den Archivierungskriterien Ihrer Marke entsprechen und die Sie behalten möchten. Sie könnten zum Beispiel Nutzer:innen behalten, die:
    - Zuletzt vor mehr als 23 Wochen eine Nachricht erhalten haben oder noch nie eine Nachricht erhalten haben<br>UND<br>
    - Ihre App zuletzt vor mehr als 23 Wochen genutzt haben oder keine Sitzungen in Ihrer App hatten<br><br>
      ![Zielgruppe aus Nutzer:innen, die zuletzt vor mehr als 23 Wochen eine Nachricht erhalten haben, noch nie eine Nachricht aus einer Kampagne oder einem Canvas-Schritt erhalten haben, diese Apps zuletzt vor mehr als 23 Wochen verwendet haben und diese Apps genau null Mal verwendet haben.][2]<br><br>
2. Setzen Sie die Neuqualifizierung auf etwas weniger als sechs Monate.<br><br>
      ![Eingangskontrollen mit aktivierter Neuqualifizierung und einem Neuqualifizierungsfenster von 23 Wochen.][3]<br><br>
3. Konfigurieren Sie den Schritt „Nutzeraktualisierung“, um jedem Profil ein Ereignis hinzuzufügen.<br><br>
      ![Schritt „Nutzeraktualisierung“, der das Ereignis „do_not_archive“ zum Profil der Nutzer:innen hinzufügt.][4]
{% details Beispiel für ein Nutzeraktualisierungsobjekt %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}