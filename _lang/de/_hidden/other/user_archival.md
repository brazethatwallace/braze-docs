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

## Definitionen zur Nutzerarchivierung {#user-archival-definitions}

### Aktive Nutzer:innen {#active-users}

Braze definiert „aktive:r Nutzer:in“ für einen bestimmten Zeitraum als jede:n Nutzer:in, die oder der eine Sitzung in einer mobilen App oder auf einer Website aufgezeichnet hat, aktualisiert wurde, eine Nachricht erhalten hat oder mit einer Nachricht interagiert hat.

Wenn Sie Nutzer-IDs festlegen, um Nutzer:innen zu identifizieren, wenn sich ein:e neue:r Nutzer:in anmeldet, werden diese als separate aktive Nutzer:innen gezählt. Nutzer:innen, die über die API aktualisiert werden, werden ebenfalls als aktive Nutzer:innen in dem Zeitraum gezählt, in dem sie aktualisiert werden.

{% alert important %}
Sowohl inaktive als auch ruhende Nutzer:innen werden archiviert, es sei denn, die oder der Nutzer:in ist aus den unten aufgeführten Gründen von der Archivierung ausgeschlossen.
{% endalert %}

### Inaktive Nutzer:innen {#inactive-users}

„Inaktive Nutzer:innen“ sind Nutzer:innen, die nicht erreichbar sind und wahrscheinlich abgewandert sind. Inaktive Nutzer:innen sind diejenigen, die alle folgenden Kriterien erfüllen:

- Können keine E-Mail empfangen. Zum Beispiel haben sie keine E-Mail-Adresse oder haben sich von allen E-Mail-Listen abgemeldet.
- Können keine SMS empfangen. Zum Beispiel haben sie keine gültige Telefonnummer oder haben sich von allen SMS-Abo-Gruppen abgemeldet.
- Können keinen Push empfangen. Zum Beispiel haben sie die App deinstalliert oder Push-Berechtigungen deaktiviert.
- Können keine WhatsApp-Nachricht empfangen. Zum Beispiel haben sie keine gültige Telefonnummer oder haben sich von allen WhatsApp-Abo-Gruppen abgemeldet.
- Können keine LINE-Nachricht empfangen. Zum Beispiel haben sie keine LINE-ID oder haben sich von allen LINE-Abo-Gruppen abgemeldet.
- Haben seit mehr als sechs Monaten keine mobile App in einem Workspace genutzt und keine Website besucht.
- Haben seit mehr als sechs Monaten keine Nachrichten von einem Workspace erhalten.
- Wurden seit mehr als sechs Monaten nicht aktualisiert.

In diesem Fall können diese Nutzer:innen nicht kontaktiert werden und interagieren nicht mit Ihrer Marke. Diese Nutzer:innen sind praktisch abgewandert.

### Ruhende Nutzer:innen {#dormant-users}

„Ruhende Nutzer:innen“ sind Nutzer:innen, die in den letzten zwölf Monaten keine Aktivität hatten und:

- Seit mehr als 12 Monaten keine mobile App in einem Workspace genutzt und keine Website besucht haben.
- Seit mehr als 12 Monaten keine Nachrichten von einem Workspace erhalten haben.
- Seit mehr als 12 Monaten nicht aktualisiert wurden.

## Nutzer:innen der globalen Kontrollgruppe {#global-control-group-users}

Nutzer:innen in der globalen Kontrollgruppe werden niemals archiviert, auch wenn sie die Definition inaktiver Nutzer:innen erfüllen.

### Treatment-Stichprobengruppe {#treatment-sample-group}

Nutzer:innen der Treatment-Stichprobengruppe in einem Bericht zur globalen Kontrollgruppe sind von der Archivierung ausgeschlossen.

## Testnutzer:innen {#test-users}

Testnutzer:innen werden niemals archiviert, auch wenn sie die Definition von inaktiven Nutzer:innen erfüllen.

## Spam-Blockierung {#spam-blocking}

Braze blockiert einzelne Nutzerprofile, die ungewöhnlich groß werden („Dummy-Nutzer:innen“), da diese in der Regel auf eine fehlerhafte Integration zurückzuführen sind. Ein Profil wird blockiert, wenn es einen der folgenden Schwellenwerte überschreitet:

| Schwellenwert | Beschreibung |
| --- | --- |
| Mehr als 5.000.000 Sitzungen | Wird typischerweise dadurch verursacht, dass eine einzelne `external_id` für viele Nutzer:innen wiederverwendet wird. |
| Mehr als 20.000 verschiedene Namen für angepasste Events | Wird typischerweise dadurch verursacht, dass für jedes Event ein neuer Event-Name generiert wird, anstatt einen festen Satz von Namen wiederzuverwenden. |
| Mehr als 20.000 verschiedene Produktnamen in Käufen | Wird typischerweise dadurch verursacht, dass für jeden Kauf eine neue `product_id` generiert wird, anstatt einen festen Satz von Produkt-IDs wiederzuverwenden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schwellenwerte für die Blockierung von Dummy-Nutzer:innen" }

Nachdem ein Profil blockiert wurde, stoppt Braze die Aufnahme aller eingehenden Daten für dieses Profil – sowohl von den SDKs als auch von der REST API. Anfragen an [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), die einen blockierten Bezeichner referenzieren, geben den Fehler `"provided external_id is blacklisted and disallowed"` zurück. Dieser Wortlaut stammt wörtlich aus der API-Antwort. Braze benachrichtigt außerdem Ihren Braze Account Manager:in, damit dieser das Integrationsproblem mit Ihnen besprechen kann.

Falls dies bei einem legitimen Nutzer bzw. einer legitimen Nutzerin passiert ist, erstellen Sie ein Ticket beim Braze-[Support]({{site.baseurl}}/braze_support).

Um die Dummy-Nutzer:innen Ihres Dashboards zu finden, führen Sie die folgenden Schritte aus:

1. Erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Wählen Sie den Filter `Session Count` aus und setzen Sie ihn auf `more than 5,000,000`.
3. Exportieren Sie das Segment als CSV.

Der Filter **Session Count** findet nur sitzungsbasierte Dummy-Nutzer:innen. Es gibt keinen Segmentierungsfilter für die Anzahl verschiedener Namen angepasster Events oder Produktnamen in einem Profil. Wenden Sie sich daher an Ihren Braze Account Manager:in, um Profile zu identifizieren, die aus diesen Gründen blockiert wurden.

Bei Bedarf können Sie die Nutzer:innen über den [`/users/delete`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) löschen.

## Anpassen Ihrer Nutzerarchivierungsrichtlinie {#customizing-your-user-archival-policy}

Braze bietet Features zur Datenorchestrierung, mit denen Sie Ihre Nutzerarchivierungsrichtlinie anpassen können. Erstellen Sie eine Nutzerarchivierungsrichtlinie, die Ihnen das Beste aus beiden Welten bietet – mit der Canvas-Komponente [User Update]({{site.baseurl}}/user_update).

Damit können Sie:

- Die DSGVO und bewährte Datenschutzpraktiken einhalten, indem Sie Nutzerprofile löschen, die nicht mehr wertvoll sind.
- Jedes Kundenprofil beibehalten, für das ein berechtigtes geschäftliches Interesse besteht.

### Schritte {#steps}

1. Sprechen Sie Nutzer:innen an, die den Archivierungskriterien Ihrer Marke entsprechen und die Sie beibehalten möchten. Beispielsweise könnten Sie Nutzer:innen beibehalten, die:
    - Zuletzt vor mehr als 23 Wochen eine Nachricht erhalten haben oder noch nie eine Nachricht erhalten haben<br>UND<br>
    - Zuletzt vor mehr als 23 Wochen Ihre App genutzt haben oder null Sitzungen in Ihrer App hatten<br><br>
      ![Zielgruppe: Nutzer:innen, die zuletzt vor mehr als 23 Wochen eine Nachricht erhalten haben, nie eine Nachricht aus einer Campaign oder einem Canvas-Schritt erhalten haben, diese Apps zuletzt vor mehr als 23 Wochen genutzt haben und diese Apps genau null Mal verwendet haben.][2]<br><br>
2. Stellen Sie die erneute Berechtigung auf etwas weniger als 6 Monate ein.<br><br>
      ![Entry-Kontrollen mit aktivierter erneuter Berechtigung und einem Fenster für die erneute Berechtigung von 23 Wochen.][3]<br><br>
3. Konfigurieren Sie den User-Update-Schritt, um jedem Profil ein Event hinzuzufügen.<br><br>
      ![User-Update-Schritt, der das Event „do_not_archive“ zum Kundenprofil hinzufügt.][4]
{% details Beispiel für ein User-Update-Objekt %}

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