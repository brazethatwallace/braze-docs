---
nav_title: Automatisiertes IP-Warming
article_title: Automatisiertes IP-Warming
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das automatisierte IP-Warming und wie Sie Ihr IP-Warming überwachen können."
channel: email
---

# Automatisiertes IP-Warming {#automated-ip-warming}

> Nutzen Sie automatisiertes IP-Warming, um das E-Mail-Volumen von neuen dedizierten IPs schrittweise zu erhöhen und so die Absender-Reputation bei Posteingangsanbietern aufzubauen. Häufig gestellte Fragen finden Sie in den [FAQ zum automatisierten IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

## So funktioniert es {#how-it-works}

Sie können automatisiertes IP-Warming nutzen, um Ihr tägliches Sendevolumen schrittweise zu erhöhen, sodass Posteingangs-Provider Ihre Sendemuster kennenlernen und ihnen vertrauen können. Wenn Sie eine Domain zu Ihrem Workspace hinzufügen, können Sie die Kachel **Automated IP Warming** im Abschnitt **Pick up where you left off** Ihres Home-Dashboards auswählen. Diese Kachel bleibt 60 Tage lang sichtbar, während sich Ihr Workspace im Onboarding-Zeitraum für neue Sender befindet, und wird ausgeblendet, nachdem Sie mindestens einen Plan abgeschlossen haben.

Jeder automatisierte IP-Warming-Plan ist mit einer Absenderadresse verknüpft. Diese Absenderadresse ist einer Sende-Subdomain und einem IP-Pool zugeordnet. Wenn der Pool mehrere dedizierte IPs enthält, erwärmt Braze diese gemeinsam in einem einzigen Plan.

Braze sendet zuerst an Ihre am stärksten engagierten Abonnent:innen, wodurch das tägliche Volumen in einem Tempo wachsen kann, das den Best Practices entspricht. Anschließend verfolgt Braze Engagement- und Zustellbarkeits-Signale. Wenn Braze Probleme erkennt, passt das System Ihren Zeitplan automatisch an.

Nachdem Sie mindestens einen Plan abgeschlossen haben, können Sie abgeschlossene Pläne unter **Settings** > **Email Preferences** > **Automated IP warming** einsehen.

## Voraussetzungen {#prerequisites}

Für das automatisierte IP-Warming müssen die folgenden Voraussetzungen erfüllt sein:

- Verifizierte Subdomain und aktive IP-Adressen
- Berechtigungen zum Anzeigen und Einrichten eines Plans:
    - „View Email Settings“ zum Anzeigen von IP-Warming-Plänen und des Home-Dashboard-Widgets
    - „View Email Templates“ zum Auswählen von E-Mail-Templates
    - „View Segments“ zum Auswählen von Segmenten
- Berechtigungen zum Starten eines Plans:
    - „Edit Email Settings“
    - „Edit Campaigns“
    - „Launch Campaigns“
    - „Approve Campaigns“

{% alert note %}
Wenn der Workflow zur Campaign-Genehmigung aktiviert ist, genehmigt Braze automatisch Campaigns, die durch das automatisierte IP-Warming in Ihrem Namen erstellt werden.
{% endalert %}

## Einen automatisierten IP-Warming-Plan einrichten {#set-up-an-automated-ip-warming-plan}

### Schritt 1: Zeitplan festlegen {#step-1-set-a-schedule}

1. Geben Sie einen eindeutigen **Plan-Namen** ein. Plan-Namen dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten und müssen in Ihrem Workspace eindeutig sein. Ein Plan-Name ist erforderlich, bevor Sie starten können.
2. Wählen Sie im Abschnitt **Sending information** die **From address** aus, für die Sie IP-Adressen aufwärmen möchten. Braze zeigt den zugehörigen **IP pool** und die Anzahl der **IP addresses in pool** für diese Absenderadresse an.
3. Geben Sie das **Current daily send volume** und das **Target send volume** ein. Braze empfiehlt ein Zielvolumen von bis zu 2 Millionen Sendungen pro IP im ausgewählten Pool. Wenn Ihr aktuelles tägliches Sendevolumen 0 beträgt, beginnt der erste Tag Ihres Zeitplans mit bis zu 50 Sendungen pro IP, begrenzt auf insgesamt 500.
4. Wählen Sie das Startdatum für das automatisierte IP-Warming. Dieses Datum muss mindestens einen Tag nach dem Start des Plans liegen.
5. Geben Sie die Sendezeit ein. Die Nachrichten werden in der Workspace-Zeitzone (oder der Unternehmens-Zeitzone, falls der Workspace keine Überschreibung hat) versendet.
6. Wählen Sie **Next: Segments**, um mit der Einrichtung fortzufahren.

![Beispielhafte Details zum Zeitplan.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Schritt 2: Segmente auswählen und priorisieren {#step-2-select-and-rank-segments}

1. Wählen Sie als Nächstes die Segmente aus, die angesprochen werden sollen. Beim IP-Warming beginnt Braze mit dem Versand an Ihre am stärksten engagierten Nutzer:innen und erhöht das Sendevolumen schrittweise über die Zeit, wobei nach und nach Segmente mit geringerem Engagement hinzugefügt werden.
2. Ordnen Sie die Segmente dann per Drag-and-Drop von hohem zu niedrigem Engagement. Hohes Engagement umfasst Empfänger:innen, die Ihre E-Mails regelmäßig öffnen und auf Links klicken. Niedriges Engagement umfasst Empfänger:innen, die unregelmäßig mit Ihren E-Mails interagieren oder seit sehr langer Zeit nicht mehr mit Ihren E-Mails interagiert haben.
3. Wählen Sie **Next: Messages**, um mit der Einrichtung fortzufahren.

{% alert important %}
Stellen Sie sicher, dass die Gesamtzahl der per E-Mail erreichbaren Nutzer:innen über alle ausgewählten Segmente hinweg größer oder gleich Ihrem **Target send volume** ist. Wenn Ihre Zielgruppe kleiner als Ihr Zielvolumen ist, erhalten einige Nutzer:innen mehr als ein E-Mail-Template am selben Tag. Weitere Informationen finden Sie unter [Zielgruppengröße und mehrere Sendungen pro Nutzer:in](#audience-size-and-multiple-sends-per-user).
{% endalert %}

![Zwei ausgewählte Segmente als Zielgruppe für automatisiertes IP-Warming.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Schritt 3: Zu sendende Nachrichten auswählen {#step-3-select-the-messages-to-send}

1. Wählen Sie **Select email templates**.
2. Wählen Sie die E-Mail-Templates für die zu versendenden Nachrichten aus. Die Inhalte, die Sie während des IP-Warmings versenden, sollten Öffnungen und Klicks fördern. Wir empfehlen, Inhalte auszuwählen, die in der Vergangenheit gut angekommen sind. Sie können beispielsweise Aktionsangebote nutzen, um sofortiges Engagement und Käufe zu fördern.
3. Wählen Sie **Select templates**. Braze berechnet die Anzahl der erforderlichen Templates, bevor Sie starten können. Wir empfehlen, mehr Templates als die mindestens erforderliche Anzahl bereitzustellen, damit das System bei Zustellbarkeitsproblemen Anpassungen vornehmen kann, ohne den Prozess zu stoppen.
4. Nachdem Sie die erforderliche Anzahl an Templates hinzugefügt haben, wählen Sie **Next: Summary**.

{% alert important %}
Änderungen an den Campaigns, die über das IP-Warming-Tool erstellt wurden (z. B. Änderungen am geplanten Datum, Segment oder Volumen), werden auf der **Summary**-Seite des IP-Warmings nicht widergespiegelt.
{% endalert %}

### Schritt 4: Konversions-Events auswählen {#step-4-select-conversion-events}

Sie können bis zu vier der folgenden Konversions-Events zum Tracking definieren. Diese Konversions-Events können nach dem Start des automatisierten IP-Warming-Plans nicht mehr geändert werden.

- Sitzung starten
- Bestellung aufgeben
- Angepasstes Event ausführen
- App upgraden
- E-Mail öffnen
- E-Mail klicken

Wählen Sie anschließend die Konversionsfrist aus. Dies ist die maximale Zeitspanne, die zwischen dem Eintritt einer Nutzer:in in eine Campaign und dem Konversions-Event vergehen darf.

![Konversionseinstellungen mit Auswahl des Konversions-Events und der Konversionsfrist.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Schritt 5: Überprüfen und starten {#step-5-review-and-launch}

Überprüfen Sie die Details Ihres IP-Warming-Plans. Wählen Sie dann **Launch**.

## Mehrere IPs gleichzeitig aufwärmen {#multiple-ip-warming}

Verwenden Sie mehrere automatisierte IP-Warming-Pläne, wenn Sie mehr als eine Absenderadresse oder einen IP-Pool aufwärmen müssen.

| Szenario | Empfehlung |
| --- | --- |
| Mehrere dedizierte IPs in einem IP-Pool | Erstellen Sie einen Plan und wählen Sie die Absenderadresse für diesen Pool aus |
| Mehrere IP-Pools oder Absenderadressen | Erstellen Sie einen separaten Plan für jede Absenderadresse |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Szenarien für mehrere IP-Warming-Pläne" }

### Mehrere IPs in einem Pool aufwärmen {#warm-multiple-ips-in-one-pool}

Wenn Sie in [Schritt 1: Zeitplan festlegen](#step-1-set-a-schedule) eine Absenderadresse auswählen, zeigt Braze den zugehörigen IP-Pool und die IP-Adressen im Pool an. Braze verwendet die Anzahl der IPs, um Ihren Ramp-Zeitplan zu erstellen und Ihr Ziel-Sendevolumen vorzuschlagen.

Wenn Ihr **Aktuelles tägliches Sendevolumen** 0 beträgt, beginnt der erste geplante Tag mit bis zu 50 Sends pro IP im Pool, begrenzt auf insgesamt 500. Braze schlägt ein **Ziel-Sendevolumen** von bis zu 2 Millionen Sends pro IP im Pool vor.

### Mehrere IP-Pools aufwärmen {#warm-multiple-ip-pools}

So wärmen Sie mehr als eine Absenderadresse oder einen IP-Pool auf:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Einstellungen** > **Automatisiertes IP-Warming**.
2. Wählen Sie **Neuer IP-Warming-Plan** aus.
3. Geben Sie einen eindeutigen **Plannamen** ein.
4. Schließen Sie die Einrichtung für diese Absenderadresse ab.
5. Wiederholen Sie den Vorgang für jede weitere Absenderadresse oder jeden weiteren IP-Pool, den Sie aufwärmen möchten.

Verfolgen Sie jeden Plan in der Tabelle **Automatisiertes IP-Warming**. Jeder Plan hat seinen eigenen Zeitplan, eigene Segmente, Templates, Campaigns und einen eigenen Tracker. Pläne können den Status **Entwurf**, **In Bearbeitung**, **Abgeschlossen** oder **Gestoppt** haben.

{% alert important %}
Vermeiden Sie es, große Nicht-Warming-Campaigns von derselben Absenderadresse oder demselben IP-Pool zu senden, während ein automatisierter IP-Warming-Plan aktiv ist. Zusätzliche Sends während des Warmings können die Zustellbarkeits-Signale beeinflussen und es erschweren, Probleme zu isolieren.
{% endalert %}

## Während des aktiven IP-Warmings {#during-active-ip-warming}

IP-Warming-Campaigns werden um Mitternacht in der geltenden Zeitzone für den aktuellen Tag und den nächsten Tag erstellt (0 bis 1 Tage vor dem Versand). Beim Starten eines Plans werden auch bevorstehende Campaigns sofort erstellt. Diese Campaigns werden automatisch im folgenden Format benannt: `IP Warming Day [X] - [Date] - [Template Name]`.

Wenn das angestrebte tägliche Versandziel erreicht ist, stoppt das System den Versand für diesen Tag, um Ihre Reputation zu schützen.

Braze bewertet die Zustellbarkeit für Campaigns, die vor 12 bis 20 Stunden gesendet wurden. Wenn einer der folgenden Schwellenwerte überschritten wird, hält Braze das Volumen für den nächsten Versandtag, anstatt es zu erhöhen:

- Zustellrate unter 90 %
- Öffnungsrate unter 10 %
- Absprungrate über 5 %
- Spam-Beschwerderate über 0,04 %

Informationen dazu, was passiert, wenn das Volumen gehalten wird, finden Sie unter [Was passiert, wenn das Volumen gehalten wird?]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq#what-happens-when-volume-is-held).

## Zielgruppengröße und mehrfache Zustellungen pro Nutzer:in {#audience-size-and-multiple-sends-per-user}

Um das Versandziel für jeden Tag zu erreichen, durchläuft Braze die von Ihnen ausgewählten E-Mail-Templates. Innerhalb eines Plans schließt Braze Nutzer:innen aus, die ein bestimmtes Template bereits erhalten haben, aber Nutzer:innen, die ein anderes Template erhalten haben, bleiben berechtigt. Wenn die für den Zeitplan des jeweiligen Tages verfügbare Zielgruppe erschöpft ist, beginnt der Plan erneut mit dem Durchlauf Ihrer Templates, sodass einige Nutzer:innen am selben Tag ein zweites Template erhalten.

Wenn die Gesamtzahl der per E-Mail erreichbaren Nutzer:innen in Ihren ausgewählten Segments kleiner als Ihr **Ziel-Versandvolumen** ist, lässt sich dieses Ergebnis am letzten Tag oder an den letzten Tagen des Plans nicht vermeiden, wenn das tägliche Volumen am höchsten ist. Wenn Ihre Segments beispielsweise 400.000 per E-Mail erreichbare Nutzer:innen enthalten und Ihr Ziel-Versandvolumen 600.000 beträgt, erhalten am letzten Tag etwa 200.000 Nutzer:innen zwei Templates und die verbleibenden 200.000 Nutzer:innen eines.

Nutzer:innen können auch an verschiedenen Tagen unterschiedliche Templates erhalten, selbst wenn Ihre Zielgruppe größer als Ihr Ziel-Versandvolumen ist. Da Braze die Zielgruppe jedes Tages auf Ihre Templates aufteilt, ohne zu berücksichtigen, welches Template eine Nutzer:in zuvor erhalten hat, kann eine Nutzer:in, die ein Template erhalten hat, später im Plan für ein anderes Template ausgewählt werden.

Braze hindert Sie nicht daran, einen Plan zu starten, wenn Ihr Ziel-Versandvolumen größer als Ihre verfügbare Zielgruppe ist. Um jede Nutzer:in auf ein Template pro Versandtag zu beschränken, führen Sie vor dem Start eine der folgenden Maßnahmen durch:

- Fügen Sie Segments hinzu, sodass die Gesamtzahl der per E-Mail erreichbaren Nutzer:innen größer oder gleich Ihrem Ziel-Versandvolumen ist.
- Senken Sie Ihr **Ziel-Versandvolumen**, sodass es nicht größer als Ihre Gesamtzahl an per E-Mail erreichbaren Nutzer:innen ist.

## Einen IP-Warming-Plan stoppen {#stop-an-ip-warmup-plan}

Sie können einen IP-Warming-Plan stoppen, um die Erstellung zukünftiger Campaigns zu verhindern. Das Stoppen eines Plans deaktiviert auch alle zugehörigen Campaigns. Nachdem Sie einen Plan gestoppt haben, können Sie ihn nicht wieder aufnehmen. Richten Sie einen neuen Plan ein, um dort weiterzumachen, wo Sie aufgehört haben, indem Sie:

- Die vorhandenen Daten Ihres gestoppten Plans herunterladen, um sie für Ihre Unterlagen aufzubewahren
- Das **Aktuelle tägliche Sendevolumen** auf das zuletzt verwendete Volumen aktualisieren
- Einen Filter zu einem Segment hinzufügen, falls Sie dasselbe Segment aus dem letzten IP-Warming verwenden möchten, indem Sie Nutzer:innen ausschließen, die bereits vorherige Campaigns erhalten haben

## Wenn ein IP-Warming abgeschlossen wird {#when-an-ip-warming-completes}

IP-Warming wird als abgeschlossen markiert, wenn der letzte Tag des IP-Warmings um Mitternacht in Ihrer Workspace-Zeitzone (oder Unternehmens-Zeitzone, falls der Workspace keine eigene Einstellung hat) endet. Wenn zum Beispiel die letzte Campaign im Plan um 20 Uhr gesendet wird, wird der Plan vier Stunden später um Mitternacht als abgeschlossen markiert.

Abgeschlossene Pläne bleiben unter **Einstellungen** > **E-Mail-Einstellungen** > **Automatisches IP-Warming** verfügbar. Der Tracker bleibt außerdem noch 90 Tage nach Ende des Plans auf dem Dashboard der Startseite sichtbar. Nach 90 Tagen wird der Tracker von der Startseite entfernt.

Der Datendownload enthält diese Standard-E-Mail-Metriken:

- _Gesendet_
- _Zugestellt_
- _Bounces_
- _Spam-Berichte_
- _Gesamte Öffnungen_
- _Eindeutige Öffnungen_
- _Geklickt_
- _Abgemeldet_

Wenn an einem Tag mehrere Campaigns verwendet werden, um die Volumenanforderungen zu erfüllen, werden diese in der Tagesansicht zusammengefasst.

![IP-Warming-Tracker mit Sendevolumen für die Woche vom 16. Januar.]({% image_buster /assets/img/automated_ip_warming_example.png %})