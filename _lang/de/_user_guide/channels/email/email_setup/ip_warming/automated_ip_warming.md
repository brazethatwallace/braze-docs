---
nav_title: Automatisiertes IP-Warming
article_title: Automatisiertes IP-Warming
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das automatisierte IP-Warming und wie Sie Ihr IP-Warming überwachen können."
channel: email
---

# Automatisiertes IP-Warming {#automated-ip-warming}

> Nutzen Sie automatisiertes IP-Warming, um das E-Mail-Volumen von neuen dedizierten IPs schrittweise zu erhöhen und so die Absender-Reputation bei Posteingangsanbietern aufzubauen.

## So funktioniert es {#how-it-works}

Sie können automatisiertes IP-Warming nutzen, um Ihr tägliches Sendevolumen schrittweise zu erhöhen, sodass Posteingangs-Anbieter Ihre Sendemuster kennenlernen und ihnen vertrauen können. Wenn Sie eine Domain zu Ihrem Workspace hinzufügen, können Sie die Kachel **Automated IP Warming** im Abschnitt **Pick up where you left off** Ihres Home-Dashboards auswählen. Diese Kachel bleibt 60 Tage lang sichtbar, während sich Ihr Workspace im Onboarding-Fenster für neue Sender befindet.

Jeder automatisierte IP-Warming-Plan ist an eine Absenderadresse gebunden. Diese Absenderadresse wird einer Sende-Subdomain und einem IP-Pool zugeordnet. Wenn der Pool mehrere dedizierte IPs enthält, führt Braze das Warming in einem einzigen Plan gemeinsam durch.

Braze sendet zuerst an Ihre am stärksten engagierten Abonnent:innen, sodass das tägliche Volumen in einem Tempo wachsen kann, das den Best Practices entspricht. Anschließend verfolgt Braze Engagement- und Zustellbarkeits-Signale. Wenn Braze Probleme erkennt, passt das System Ihren Zeitplan automatisch an.

Nachdem Sie mindestens einen Plan abgeschlossen haben, können Sie abgeschlossene Pläne unter **Settings** > **Email Preferences** > **Automated IP warming** einsehen.

{% alert note %}
Wenn Sie in Ihrem Dashboard nur eine Einzelplan-Ansicht sehen, hat Ihr Workspace möglicherweise noch keinen Zugriff auf mehrere IP-Warming-Pläne. Wenden Sie sich an Ihr Braze-Kontoteam, um die Verfügbarkeit zu erfahren.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um automatisiertes IP-Warming durchzuführen, benötigen Sie Folgendes:

- Verifizierte Subdomain und aktive IP-Adressen
- Berechtigungen zum Anzeigen und Starten eines IP-Warmups
    - „View Usage Data“ zum Anzeigen des IP-Warming-Bereichs
    - „View Email Templates“ zum Anzeigen und Auswählen der E-Mail-Templates für IP-Warming
    - „Manage Email Settings“ zum Starten des IP-Warmups
- „Access Campaigns“
- „Approve and Deny Campaigns“, wenn der Genehmigungsworkflow für Campaigns aktiviert ist
    - Braze genehmigt die durch automatisiertes IP-Warming erstellten Campaigns automatisch in Ihrem Namen.

{% alert important %}
Dieses Feature wird je nach Ihrer E-Mail-Infrastruktur möglicherweise nicht unterstützt.
{% endalert %}

## Einen automatisierten IP-Warming-Plan einrichten {#set-up-an-automated-ip-warming-plan}

### Schritt 1: Zeitplan festlegen {#step-1-set-a-schedule}

1. Wenn Ihr Workspace mehrere IP-Warming-Pläne unterstützt, geben Sie einen eindeutigen **Plannamen** ein. Plannamen dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten und müssen in Ihrem Workspace eindeutig sein. Ein Planname ist erforderlich, bevor Sie den Plan starten können.
2. Wählen Sie im Abschnitt **Sending information** die **From address** aus, für die IP-Adressen aufgewärmt werden sollen. Braze zeigt den zugehörigen **IP pool** und die Anzahl der **IP addresses in pool** für diese Absenderadresse an.
3. Geben Sie das **Current daily send volume** und das **Target send volume** ein. Braze empfiehlt ein Zielversandvolumen von bis zu 2 Millionen Sendungen pro IP im ausgewählten Pool. Wenn Ihr aktuelles tägliches Versandvolumen 0 beträgt, beginnt der erste Tag Ihres Zeitplans mit bis zu 50 Sendungen pro IP, begrenzt auf insgesamt 500.
4. Wählen Sie das Startdatum für das automatisierte IP-Warming aus. Dieses Datum muss mindestens einen Tag nach dem Start des Plans liegen.
5. Geben Sie die Sendezeit ein. Die Nachrichten werden in der Zeitzone des Unternehmens gesendet.
6. Wählen Sie **Next: Segments**, um mit der Einrichtung fortzufahren.

![Beispiel für Zeitplandetails.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Schritt 2: Segmente auswählen und priorisieren {#step-2-select-and-rank-segments}

1. Wählen Sie als Nächstes die Segmente aus, die angesprochen werden sollen. Während des IP-Warmings beginnt Braze mit dem Versand an Ihre am stärksten engagierten Nutzer:innen und erhöht das Versandvolumen schrittweise über die Zeit, wobei nach und nach Segmente mit geringerem Engagement hinzugefügt werden.
2. Ziehen Sie die Segmente per Drag-and-Drop, um sie von hohem zu niedrigem Engagement zu ordnen. Hohes Engagement umfasst Empfänger:innen, die Ihre E-Mails regelmäßig öffnen und anklicken. Niedriges Engagement umfasst Empfänger:innen, die unregelmäßig mit Ihren E-Mails interagieren oder seit sehr langer Zeit nicht mehr mit Ihren E-Mails interagiert haben.
3. Wählen Sie **Next: Messages**, um mit der Einrichtung fortzufahren.

![Zwei ausgewählte Segmente für das automatisierte IP-Warming.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Schritt 3: Zu sendende Nachrichten auswählen {#step-3-select-the-messages-to-send}

1. Wählen Sie **Select email templates**.
2. Wählen Sie die E-Mail-Templates für die zu sendenden Nachrichten aus. Die Inhalte, die Sie während des IP-Warmings versenden, sollten Öffnungen und Klicks fördern. Wir empfehlen, Inhalte zu wählen, die in der Vergangenheit gut angekommen sind. Sie können beispielsweise Aktionsangebote nutzen, um sofortiges Engagement und Käufe zu fördern.
3. Wählen Sie **Select templates**. Braze berechnet die Anzahl der erforderlichen Templates, bevor Sie starten können. Wir empfehlen, mehr Templates als die Mindestanzahl bereitzustellen, damit das System bei Zustellbarkeitsproblemen Anpassungen vornehmen kann, ohne den Prozess zu stoppen.
4. Nachdem Sie die erforderliche Anzahl an Templates hinzugefügt haben, wählen Sie **Next: Summary**.

{% alert important %}
Änderungen an den Campaigns, die über das IP-Warming-Tool erstellt wurden (z. B. Änderungen am geplanten Datum, Segment oder Volumen), werden nicht auf der IP-Warming-Seite **Summary** widergespiegelt.
{% endalert %}

### Schritt 4: Konversions-Events auswählen {#step-4-select-conversion-events}

Sie können bis zu vier der folgenden Konversions-Events zur Nachverfolgung definieren. Diese Konversions-Events können nach dem Start des automatisierten IP-Warming-Plans nicht mehr aktualisiert werden.

- Sitzung starten
- Bestellung aufgeben
- Angepasstes Event ausführen
- App-Upgrade durchführen
- E-Mail öffnen
- E-Mail anklicken

Wählen Sie anschließend die Konversionsfrist aus. Dies ist die maximale Zeitspanne, die zwischen dem Eintritt einer Nutzerin oder eines Nutzers in eine Campaign und dem Konversions-Event vergehen darf.

![Konversionseinstellungen mit Auswahl des Konversions-Events und der Konversionsfrist.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Schritt 5: Überprüfen und starten {#step-5-review-and-launch}

Überprüfen Sie die Details Ihres IP-Warming-Plans. Wählen Sie dann **Launch**.

## Mehrere IPs gleichzeitig aufwärmen {#multiple-ip-warming}

Verwenden Sie mehrere automatisierte IP-Warming-Pläne, wenn Sie mehr als eine Absenderadresse oder einen IP-Pool aufwärmen müssen.

| Szenario | Empfehlung |
| --- | --- |
| Mehrere dedizierte IPs in einem IP-Pool | Erstellen Sie einen Plan und wählen Sie die Absenderadresse für diesen Pool aus |
| Mehrere IP-Pools oder Absenderadressen | Erstellen Sie einen separaten Plan für jede Absenderadresse |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Szenarien für das Aufwärmen mehrerer IPs" }

### Mehrere IPs in einem Pool aufwärmen {#warm-multiple-ips-in-one-pool}

Wenn Sie in [Schritt 1: Zeitplan festlegen](#step-1-set-a-schedule) eine Absenderadresse auswählen, zeigt Braze den zugehörigen IP-Pool und die IP-Adressen im Pool an. Braze verwendet die Anzahl der IPs, um Ihren Ramp-Zeitplan zu erstellen und Ihr Ziel-Sendevolumen vorzuschlagen.

Wenn Ihr **Aktuelles tägliches Sendevolumen** 0 beträgt, beginnt der erste geplante Tag mit bis zu 50 Sendungen pro IP im Pool, begrenzt auf insgesamt 500. Braze schlägt ein **Ziel-Sendevolumen** von bis zu 2 Millionen Sendungen pro IP im Pool vor.

### Mehrere IP-Pools aufwärmen {#warm-multiple-ip-pools}

So wärmen Sie mehr als eine Absenderadresse oder einen IP-Pool auf:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Einstellungen** > **Automatisiertes IP-Warming**.
2. Wählen Sie **Neuer IP-Warming-Plan** aus.
3. Geben Sie einen eindeutigen **Plannamen** ein.
4. Schließen Sie die Einrichtung für diese Absenderadresse ab.
5. Wiederholen Sie den Vorgang für jede weitere Absenderadresse oder jeden weiteren IP-Pool, den Sie aufwärmen müssen.

Verfolgen Sie jeden Plan über die Tabelle **Automatisiertes IP-Warming**. Jeder Plan hat seinen eigenen Zeitplan, eigene Segmente, Templates, Campaigns und einen eigenen Tracker. Pläne können den Status **Entwurf**, **In Bearbeitung**, **Abgeschlossen** oder **Gestoppt** haben.

{% alert important %}
Vermeiden Sie es, große Nicht-Warming-Campaigns von derselben Absenderadresse oder demselben IP-Pool zu senden, während ein automatisierter IP-Warming-Plan aktiv ist. Zusätzliche Sendungen während des Warmings können die Zustellbarkeitssignale beeinflussen und es erschweren, Probleme zu isolieren.
{% endalert %}

## Während des aktiven IP-Warmings {#during-active-ip-warming}

IP-Warming-Campaigns werden 1 bis 2 Tage im Voraus erstellt, es sei denn, Sie starten ein IP-Warming am nächsten Tag. Diese Campaigns werden automatisch im folgenden Format benannt: `IP Warming Day [X] - [Date] - [Template Name]`.

Wenn das angestrebte tägliche Versandziel erreicht ist, stoppt das System den Versand für diesen Tag, um Ihre Reputation zu schützen.

Das System überwacht Ihren Zustand anhand der folgenden Branchen-Benchmarks:

- Zustellrate fällt auf 90 % oder darunter
- Öffnungsrate unter 10 %
- Bounces über 5 %
- Spam-Beschwerderate über 0,04 %

Wenn die Statistiken unter unseren Benchmarks liegen, hält das System das Volumen am nächsten Tag, anstatt es zu erhöhen, um das Risiko für Ihre Absender-Reputation zu minimieren.

## IP-Warming-Plan stoppen {#stop-an-ip-warmup-plan}

Braze ermöglicht es Ihnen, das IP-Warming und die Erstellung zukünftiger Campaigns zu stoppen. Wenn jedoch eine Campaign bereits aktiv oder für die nächsten 24 bis 48 Stunden geplant ist, müssen Sie die betreffende Campaign möglicherweise manuell stoppen. Das Stoppen eines IP-Warming-Plans stoppt auch alle zugehörigen Campaigns.

Wenn ein IP-Warming-Plan gestoppt wurde, kann er allerdings nicht wieder aufgenommen werden. Stattdessen müssen Sie einen neuen Plan einrichten, um dort weiterzumachen, wo Sie aufgehört haben, indem Sie:

- Die vorhandenen Daten Ihres gestoppten Plans herunterladen, um sie für Ihre Unterlagen aufzubewahren
- Das **Aktuelle tägliche Sendevolumen** auf das zuletzt verwendete Volumen aktualisieren
- Einen Filter zu einem Segment hinzufügen, falls Sie dasselbe Segment aus dem letzten IP-Warming verwenden möchten, indem Sie Nutzer:innen ausschließen, die bereits vorherige Campaigns erhalten haben

## Wenn ein IP-Warming abgeschlossen ist {#when-an-ip-warmup-completes}

IP-Warming wird als abgeschlossen markiert, wenn der letzte Tag des IP-Warmings um Mitternacht in der Zeitzone Ihres Unternehmens endet. Wenn beispielsweise die letzte Campaign im IP-Warming-Plan um 20 Uhr gesendet wird, wird der Plan nach vier Stunden als abgeschlossen markiert.

Abgeschlossene Pläne bleiben unter **Einstellungen** > **E-Mail-Einstellungen** > **Automatisiertes IP-Warming** verfügbar. Wenn Ihr Workspace die Einzelplan-Ansicht verwendet, bleibt der Tracker auch 90 Tage nach Ende des Plans auf dem Start-Dashboard sichtbar. Nach 90 Tagen wird der Tracker vom Start-Dashboard entfernt.

Der Datendownload enthält diese Standard-E-Mail-Metriken:

- _Gesendet_
- _Zugestellt_
- _Bounces_
- _Spam-Berichte_
- _Öffnungen gesamt_
- _Eindeutige Öffnungen_
- _Geklickt_
- _Abgemeldet_

Wenn an einem Tag mehrere Campaigns verwendet werden, um die Volumenanforderungen zu erfüllen, werden diese in der Tagesansicht aggregiert.

![IP-Warming-Tracker mit Sendevolumen für die Woche vom 16. Januar.]({% image_buster /assets/img/automated_ip_warming_example.png %})