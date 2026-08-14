---
nav_title: FAQ
article_title: FAQ zum automatisierten IP-Warming
channel: email
page_order: 3
description: "Antworten auf häufig gestellte Fragen zum automatisierten IP-Warming in Braze."
---

# FAQ zum automatisierten IP-Warming {#automated-ip-warming-faq}

> Antworten auf häufige Fragen zum [automatisierten IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming). Informationen zu IP-Warming-Konzepten und manuellen Zeitplänen finden Sie unter [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).

## Wann sollte ich automatisiertes IP-Warming verwenden? {#when-should-i-use-automated-ip-warming}

Verwenden Sie automatisiertes IP-Warming, wenn Sie Folgendes benötigen:

- Erstmaliges Aufwärmen neuer IP-Adressen
- Aufwärmen neuer Geschäftsbereiche oder Marken mit neuen Subdomains
- Erneutes Aufwärmen bestehender IPs zur Verbesserung der Zustellbarkeit
- Erneutes Aufwärmen für bestimmte Postfachanbieter zur Verbesserung der Zustellbarkeit

Informationen zu Einrichtungsschritten und Voraussetzungen finden Sie unter [Automatisiertes IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming).

## Wie weit im Voraus muss das Startdatum liegen? {#how-far-in-advance-must-the-start-date-be}

Das Startdatum muss morgen oder später in der Zeitzone Ihres Workspace (oder der Unternehmenszeitzone, wenn der Workspace keine eigene Einstellung hat) liegen.

Braze erstellt Campaigns um Mitternacht in dieser Zeitzone für den aktuellen Tag und den nächsten Tag (0 bis 1 Tage vor dem Versand). Beim Starten eines Plans werden anstehende Campaigns ebenfalls sofort erstellt.

## Wie viele Templates werden benötigt? {#how-many-templates-are-required}

Braze berechnet das Minimum aus Ihren geplanten Versandvolumen und den per E-Mail erreichbaren Nutzer:innen in den ausgewählten Segmenten (nicht der gesamten Segmentgröße). Stellen Sie mehr Templates als das Minimum bereit, damit das System bei Zustellbarkeitsproblemen Anpassungen vornehmen kann, ohne anzuhalten. Weitere Informationen finden Sie unter [Schritt 3: Nachrichten zum Versand auswählen]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Kann ich dasselbe Segment für mehrere Aufwärmversuche verwenden? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

Innerhalb eines einzelnen aktiven Plans schließt Braze automatisch Nutzer:innen aus, die bereits vorherige IP-Warming-Sendungen für dasselbe Template erhalten haben. Wenn Sie einen Plan stoppen und einen neuen starten, der dieselben Segmente wiederverwendet, fügen Sie einen Filter hinzu, um Nutzer:innen auszuschließen, die Campaigns aus dem vorherigen Plan erhalten haben.

## Kann ich das IP-Warming mitten im Zeitplan starten? {#can-i-start-ip-warming-mid-schedule}

Automatisiertes IP-Warming erstellt den Zeitplan immer vom Beginn der Aufwärmphase an. Um einen Start mitten im Zeitplan zu simulieren, setzen Sie **Aktuelles tägliches Versandvolumen** auf einen Wert größer als 0, der Ihrem aktuellen Volumen entspricht. Wenn das aktuelle Volumen größer als 0 ist, wendet Braze keine IP-Anzahl-Skalierung auf Tag 1 an.

## Welche Zeitzone wird für den Versand verwendet? {#what-time-zone-is-used-for-sending}

Sendungen verwenden die Workspace-Zeitzone, wenn eine festgelegt ist; andernfalls die Unternehmenszeitzone. Campaigns werden nicht in der Ortszeit der einzelnen Nutzer:innen erstellt. Um in Ortszeit zu versenden, aktualisieren Sie die vom Plan erstellten Campaigns manuell.

## Wie viele IP-Warming-Pläne können gleichzeitig laufen? {#how-many-ip-warming-plans-can-run-at-the-same-time}

Wenn Ihr Workspace mehrere Pläne unterstützt, können mehrere Pläne gleichzeitig laufen. Weitere Informationen finden Sie unter [Mehrfaches IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming).

## Wie skaliert das Volumen bei IP-Pools mit mehreren IPs? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

Wenn **Aktuelles tägliches Versandvolumen** auf 0 steht, beginnt Tag 1 mit dem niedrigeren Wert aus 50 Sendungen pro IP oder 500 insgesamt. Das Volumen wächst dann um etwa das 1,75-Fache pro Sendetag, vorbehaltlich der Aufwärm-Leitplanken. Beispiel mit 10 IPs: 500 → 875 → 1.532 → 2.681.

Wenn Sie ein angepasstes aktuelles Volumen größer als 0 festlegen, wird die IP-Anzahl-Skalierung nicht auf Tag 1 angewendet. Weitere Informationen zu Multi-IP-Plänen finden Sie unter [Mehrere IPs in einem Pool aufwärmen]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool).

## Unterstützt automatisiertes IP-Warming Rate-Limiting pro Campaign? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

Nein. Jede Campaign wird zur konfigurierten Zeit ohne ein Campaign-spezifisches Rate-Limit versendet.

## Wann hält Braze das Volumen während des IP-Warmings? {#when-does-braze-hold-volume-during-ip-warming}

Braze bewertet die Zustellbarkeit für Campaigns, die vor 12 bis 20 Stunden versendet wurden. Wenn die Raten für Zustellung, Öffnungen, Bounces oder Spam-Beschwerden die Benchmarks in [Während des aktiven IP-Warmings]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming) überschreiten, hält Braze das Volumen für den nächsten Sendetag, anstatt es zu erhöhen.

## Was passiert, wenn das Volumen gehalten wird? {#what-happens-when-volume-is-held}

Das Halten des Volumens ist die automatische Anpassung, die Braze vornimmt, wenn diese Schwellenwerte überschritten werden. Der nächste geplante Versand behält dasselbe Volumen bei, anstatt zu steigen. Braze plant zukünftige Zeitplaneinträge neu, archiviert bestehende zukünftige Campaigns des Plans und erstellt sofort neue Campaigns für den aktualisierten Zeitplan. Der Plan kann länger brauchen, um das Zielvolumen zu erreichen.

## Warum werden Campaign-Änderungen nicht im IP-Warming-Tracker angezeigt? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

Änderungen, die Sie an Campaigns vornehmen, die durch automatisiertes IP-Warming erstellt wurden (wie Zeitplan, Segment oder Volumen), werden nicht mit dem IP-Warming-Tracker synchronisiert. Zugehörige Einrichtungshinweise finden Sie unter [Schritt 3: Nachrichten zum Versand auswählen]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Kann ich einen IP-Warming-Plan stoppen? {#can-i-stop-an-ip-warming-plan}

Ja. Das Stoppen beendet den Plan dauerhaft: Braze deaktiviert verknüpfte Campaigns und erstellt keine zukünftigen mehr. Sie können einen gestoppten Plan nicht fortsetzen – erstellen Sie einen neuen Plan, um fortzufahren. Informationen zum Fortfahren nach einem Stopp finden Sie unter [Einen IP-Warming-Plan stoppen]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan).

## Wann wird ein IP-Warming-Plan als abgeschlossen markiert? {#when-is-an-ip-warming-plan-marked-as-complete}

Der Plan wird als abgeschlossen markiert, nachdem der letzte geplante Sendetag endet, um Mitternacht in der geltenden Zeitzone (Workspace oder Unternehmen). Wenn beispielsweise die letzte Campaign um 20 Uhr versendet wird, wird der Plan vier Stunden später um Mitternacht als abgeschlossen markiert.

## Welche Daten kann ich herunterladen? {#what-data-can-i-download}

Der CSV-Export enthält Zeilen pro Campaign mit Metriken auf Tagesebene: *Gesendet*, *Zugestellt*, *Bounces*, *Spam-Berichte*, *Öffnungen gesamt*, *Eindeutige Öffnungen*, *Geklickt* und *Abgemeldet*. Die Tracker-Tabelle fasst mehrere Campaigns desselben Tages in einer Tagesansicht zusammen. Weitere Informationen finden Sie unter [Wenn ein IP-Warming abgeschlossen ist]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes).