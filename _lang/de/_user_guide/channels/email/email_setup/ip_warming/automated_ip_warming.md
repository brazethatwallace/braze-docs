---
nav_title: Automatisiertes IP-Warming
article_title: Automatisiertes IP-Warming
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das automatisierte IP-Warming und wie Sie Ihr IP-Warming überwachen können."
channel: email
---

# Automatisiertes IP-Warming {#automated-ip-warming}

> Nutzen Sie automatisiertes IP-Warming, um das E-Mail-Volumen von einer neuen IP-Adresse schrittweise zu erhöhen und so die Absender-Reputation bei Posteingangsanbietern aufzubauen.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Automated IP warming' %}

## Funktionsweise {#how-it-works}

Sie können automatisiertes IP-Warming einsetzen, um Ihr tägliches Versandvolumen schrittweise zu erhöhen, sodass Posteingangsanbieter Ihre Versandmuster kennenlernen und ihnen vertrauen können. Wenn Sie Ihrem Workspace eine Domain hinzufügen, können Sie die Kachel **Automated IP Warming** im Abschnitt **Pick up where you left off** Ihres Start-Dashboards auswählen. Diese Kachel bleibt dort 60 Tage lang angezeigt.

Braze sendet zuerst an Ihre engagiertesten Abonnent:innen, wodurch das tägliche Volumen in einem Tempo wachsen kann, das den Best Practices entspricht. Anschließend verfolgt Braze Engagement- und Zustellbarkeitssignale. Sollte Braze Probleme feststellen, passt das System Ihren Zeitplan automatisch an.

{% alert note %}
Es ist nur ein IP-Warming durchführbar.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um automatisiertes IP-Warming durchzuführen, benötigen Sie Folgendes:

- Verifizierte Subdomain und aktive IP-Adressen
- Berechtigungen zum Anzeigen und Starten eines IP-Warmups
    - „Nutzungsdaten anzeigen“ zum Anzeigen des IP-Warming-Abschnitts
    - „E-Mail-Templates anzeigen“ zum Anzeigen und Auswählen der E-Mail-Templates für das IP-Warming
    - „E-Mail-Einstellungen verwalten“ zum Starten des IP-Warmups
- „Zugriff auf Campaigns“
- „Campaigns genehmigen und ablehnen“, wenn der Genehmigungs-Workflow für Campaigns aktiviert ist
    - Braze genehmigt die durch automatisiertes IP-Warming erstellten Campaigns automatisch in Ihrem Namen.

{% alert important %}
Dieses Feature wird je nach Ihrer E-Mail-Infrastruktur möglicherweise nicht unterstützt.
{% endalert %}

## Ein automatisiertes IP-Warming einrichten {#set-up-an-automated-ip-warming-plan}

### 1. Schritt: Zeitplan festlegen {#step-1-set-a-schedule}

1. Wählen Sie im Abschnitt **Sending information** die **From address** aus, für die IP-Adressen aufgewärmt werden sollen.
2. Geben Sie das aktuelle tägliche Versandvolumen und das Ziel-Versandvolumen ein.
3. Wählen Sie das Startdatum für das automatisierte IP-Warming. Dieses Datum muss mindestens einen Tag nach dem Start des Plans liegen.
4. Geben Sie die Sendezeit ein. Die Nachrichten werden in der Zeitzone des Unternehmens gesendet.
5. Wählen Sie **Next: Segments**, um die Einrichtung fortzusetzen.

![Beispiel für Zeitplandetails.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### 2. Schritt: Segmente auswählen und priorisieren {#step-2-select-and-rank-segments}

1. Wählen Sie als Nächstes die Segmente aus, die Sie ansprechen möchten. Während des IP-Warmings beginnt Braze mit dem Versand an Ihre am stärksten engagierten Nutzer:innen und erhöht das Versandvolumen schrittweise über die Zeit, wobei nach und nach Segmente mit geringerem Engagement hinzugefügt werden.
2. Ziehen Sie die Segmente per Drag-and-Drop, um sie von hohem zu niedrigem Engagement zu ordnen. Hohes Engagement umfasst Empfänger:innen, die Ihre E-Mails regelmäßig öffnen und anklicken. Niedriges Engagement umfasst Empfänger:innen, die unregelmäßig mit Ihren E-Mails interagieren oder seit sehr langer Zeit nicht mehr mit Ihren E-Mails interagiert haben.
3. Wählen Sie **Next: Messages**, um die Einrichtung fortzusetzen.

![Zwei ausgewählte Segmente als Zielgruppe für automatisiertes IP-Warming.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### 3. Schritt: Nachrichten zum Senden auswählen {#step-3-select-the-messages-to-send}

1. Wählen Sie **Select email templates**.
2. Wählen Sie die E-Mail-Templates für die zu sendenden Nachrichten aus. Der Inhalt, den Sie während des IP-Warmings senden, sollte Öffnungen und Klicks fördern. Wir empfehlen, Inhalte zu wählen, die in der Vergangenheit gut angekommen sind. Sie können beispielsweise Aktionsangebote verwenden, um sofortiges Engagement und Käufe zu fördern.
3. Wählen Sie **Select templates**. Braze berechnet die Anzahl der erforderlichen Templates, bevor Sie starten können. Wir empfehlen, mehr Templates als das erforderliche Minimum bereitzustellen, damit das System bei Zustellbarkeitsproblemen Anpassungen vornehmen kann, ohne den Prozess zu stoppen.
4. Nachdem Sie die erforderliche Anzahl an Templates hinzugefügt haben, wählen Sie **Next: Summary**.

{% alert important %}
Änderungen an den durch das IP-Warming-Tool erstellten Campaigns (wie z. B. Änderungen am geplanten Datum, Segment oder Volumen) werden nicht auf der IP-Warming-Seite **Summary** widergespiegelt.
{% endalert %}

### 4. Schritt: Konversions-Events auswählen {#step-4-select-conversion-events}

Sie können bis zu vier der folgenden Konversions-Events zum Tracking definieren. Diese Konversions-Events können nach dem Start des automatisierten IP-Warming-Plans nicht mehr aktualisiert werden.

- Sitzung starten
- Bestellung aufgeben
- Angepasstes Event ausführen
- App upgraden
- E-Mail öffnen
- E-Mail anklicken

Wählen Sie als Nächstes die Konversionsfrist aus – die maximale Zeit, die zwischen dem Eintritt von Nutzer:innen in eine Campaign und dem Konversions-Event vergehen darf.

![Konversionseinstellungen mit Auswahl des Konversions-Events und der Konversionsfrist.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### 5. Schritt: Überprüfen und starten {#step-5-review-and-launch}

Überprüfen Sie die Details Ihres IP-Warming-Plans. Wählen Sie dann **Launch**.

## Während des aktiven IP-Warmings {#during-active-ip-warming}

IP-Warming-Campaigns werden 1 bis 2 Tage im Voraus erstellt, es sei denn, Sie starten ein IP-Warmup am nächsten Tag. Diese Campaigns werden automatisch im folgenden Format benannt: `IP Warming Day [X] - [Date] - [Template Name]`.

Wenn das angestrebte tägliche Versandziel erreicht ist, stoppt das System den Versand für diesen Tag, um Ihre Reputation zu schützen.

Das System überwacht Ihren Zustand anhand der folgenden Branchen-Benchmarks:

- Zustellrate fällt auf 90 % oder darunter
- Öffnungsrate unter 10 %
- Bounces über 5 %
- Spam-Beschwerderate über 0,04 %

Wenn die Statistiken unter unseren Benchmarks liegen, hält das System das Volumen am nächsten Tag, anstatt es zu erhöhen, um das Risiko für Ihre Absender-Reputation zu minimieren.

## Einen IP-Warming-Plan stoppen {#stop-an-ip-warmup-plan}

Braze ermöglicht es Ihnen, das IP-Warming und die Erstellung zukünftiger Campaigns zu stoppen. Wenn jedoch eine Campaign bereits aktiv oder für die nächsten 24 bis 48 Stunden geplant ist, müssen Sie die betreffende Campaign möglicherweise manuell stoppen. Das Stoppen eines IP-Warming-Plans stoppt auch alle zugehörigen Campaigns.

Wenn ein IP-Warming gestoppt wurde, kann es nicht fortgesetzt werden. Stattdessen müssen Sie einen neuen Plan einrichten, um dort weiterzumachen, wo Sie aufgehört haben:

- Laden Sie die vorhandenen Daten Ihres gestoppten Plans herunter, um sie für Ihre Unterlagen aufzubewahren, da der vorherige Tracker entfernt wird, sobald Sie ein neues IP-Warmup starten.
- Aktualisieren Sie das **Current daily send volume** auf das zuletzt verwendete Volumen.
- Fügen Sie einem Segment einen Filter hinzu, wenn Sie dasselbe Segment aus dem letzten IP-Warmup verwenden möchten, indem Sie Nutzer:innen ausschließen, die bereits vorherige Campaigns erhalten haben.

## Wenn ein IP-Warmup abgeschlossen ist {#when-an-ip-warmup-completes}

Das IP-Warming wird als abgeschlossen markiert, wenn der letzte Tag des IP-Warmings um Mitternacht in der Zeitzone Ihres Unternehmens endet. Wenn beispielsweise die letzte Campaign im IP-Warming-Plan um 20 Uhr gesendet wird, wird der Plan nach vier Stunden als abgeschlossen markiert.

Der Tracker bleibt 90 Tage nach Ende des Plans auf der Startseite sichtbar. Nach 90 Tagen wird der Tracker entfernt. Der Datendownload enthält diese Standard-E-Mail-Metriken:

- _Gesendet_
- _Zugestellt_
- _Bounces_
- _Spam-Berichte_
- _Öffnungen gesamt_
- _Eindeutige Öffnungen_
- _Angeklickt_
- _Abgemeldet_

Wenn ein Tag mehrere Campaigns umfasst, die zur Erfüllung der Volumenanforderungen verwendet wurden, werden diese in der Tagesansicht aggregiert.

![IP-Warming-Tracker mit Versandvolumen für die Woche vom 16. Januar.]({% image_buster /assets/img/automated_ip_warming_example.png %})