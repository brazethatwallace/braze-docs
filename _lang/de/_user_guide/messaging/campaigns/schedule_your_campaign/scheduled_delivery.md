---
nav_title: Geplante Zustellung
article_title: Geplante Zustellung
page_order: 0
page_type: reference
description: "Dieser Referenzartikel beschreibt die Unterschiede zwischen den zeitabhängigen Planungsoptionen für die Campaign-Zustellung."
tool: Campaigns

---

# Geplante Zustellung {#scheduled-delivery}

> Campaigns, die mit zeitbasierter geplanter Zustellung gesendet werden, werden an festgelegten Tagen zugestellt.

## Option 1: Sofort nach dem Start der Campaign senden {#option-1-send-as-soon-as-the-campaign-is-launched}

Wenn Sie eine Nachricht sofort nach dem Start senden möchten, beginnt der Versand, sobald Sie die Erstellung Ihrer Campaign abgeschlossen haben.

![Der Abschnitt „Zustellung“ mit ausgewählter Option „Geplant“ und der zeitabhängigen Planungsoption, die Campaign sofort nach dem Start zu senden.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Diese Art von Zeitplan ist für einmalige Campaigns gedacht, die Sie sofort senden möchten, z. B. Nachrichten zu einem aktuellen Ereignis. Eine Sport-App könnte beispielsweise Push-Benachrichtigungen zu Spielstandaktualisierungen mit dieser Option planen. Darüber hinaus können Sie beim Senden von Testnachrichten, die nur an Sie selbst oder Ihr Team gerichtet sind, diese Option nutzen, um sie sofort zuzustellen.

Wenn Sie die Campaign nach dem Anzeigen des Tests bearbeiten und erneut senden möchten, aktivieren Sie das Kontrollkästchen, das Nutzer:innen [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility), die Campaign zu erhalten. Standardmäßig sendet Braze eine Campaign nur einmal an eine:n Nutzer:in, es sei denn, dieses Kontrollkästchen ist aktiviert.

## Option 2: Zu einem festgelegten Zeitpunkt senden {#option-2-send-at-a-designated-time}

Wenn Sie eine Campaign für einen festgelegten Zeitpunkt planen, können Sie die Tage und Uhrzeiten angeben, an denen Ihre Campaign gesendet wird. Sie können eine Nachricht einmalig, täglich, wöchentlich oder monatlich zu einer bestimmten Uhrzeit senden und festlegen, wann Ihre Campaign beginnen und enden soll. Dieses Enddatum ist inklusiv, d. h. der letzte Versand erfolgt am Enddatum.

Wenn Sie einen monatlich wiederkehrenden Zeitplan auswählen, beachten Sie, dass einige Monate den ausgewählten Tag möglicherweise nicht haben. Angenommen, Sie legen fest, dass eine Campaign monatlich am 31. Tag gesendet wird. In diesem Szenario sendet Braze am letzten Tag des jeweiligen Monats, z. B. am 30. April, da der 31. April nicht existiert.

Wenn Sie **Geplante Zustellung** auswählen und nicht den Versand zur Ortszeit der Nutzer:innen wählen, wird Ihre Campaign gemäß der Zeitzone gesendet, die auf Ihrer Seite **Unternehmenseinstellungen** angegeben ist.

![Die zeitabhängigen Planungsoptionen zum Senden einer Campaign zu einem festgelegten Zeitpunkt.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campaigns in lokaler Zeitzone {#local-time-zone-campaigns}

Sie können die Nachricht in der Ortszeit der Nutzer:innen zustellen, damit Mitglieder Ihrer internationalen Zielgruppe keine Benachrichtigung zu ungünstigen Zeiten erhalten. Campaigns in lokaler Zeitzone müssen 24 Stunden im Voraus geplant werden, um sicherzustellen, dass berechtigte Nutzer:innen aus allen Zeitzonen sie erhalten können. Lesen Sie die [Campaign-FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign), um zu verstehen, wie Campaigns in lokaler Zeitzone funktionieren und welche Zustellungsregeln gelten.

Segmente, die mit Campaigns in lokaler Zeitzone angesprochen werden, sollten mindestens ein 2-Tage-Fenster umfassen, um Nutzer:innen aus allen Zeitzonen einzubeziehen. Wenn Ihre Campaign beispielsweise für den Abend geplant ist, aber nur ein 1-Tage-Fenster hat, könnten einige Nutzer:innen bereits aus dem Segment gefallen sein, wenn ihre Zeitzone erreicht wird. Beispiele für Filter, die ein 2-Tage-Fenster erzeugen, sind „zuletzt vor mehr als 1 Tag verwendet“ und „zuletzt vor weniger als 3 Tagen verwendet“ oder „erster Kauf vor mehr als 7 Tagen“ und „erster Kauf vor weniger als 9 Tagen“.

### Anwendungsfälle {#use-cases}

Festgelegte Zeitpläne eignen sich am besten für im Voraus geplante Nachrichten und wiederkehrende Campaigns, wie Onboarding- und Bindungs-Campaigns, die regelmäßig an alle qualifizierten Nutzer:innen gesendet werden.

## Option 3: Intelligentes Timing {#option-3-intelligent-timing}

[Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) ermöglicht es Ihnen, eine Campaign zu einem individuellen Zeitpunkt an jede:n Nutzer:in zuzustellen. Braze berechnet den optimalen Zeitpunkt für jede Person basierend darauf, wann diese:r Nutzer:in typischerweise mit Ihrer App und deren Benachrichtigungen interagiert. Optional können Sie festlegen, dass Campaigns mit intelligentem Timing nur während eines bestimmten Teils des Tages gesendet werden. Wenn Sie beispielsweise Nutzer:innen über eine Aktion informieren, die um Mitternacht endet, möchten Sie möglicherweise, dass Ihre Nachrichten spätestens um 22 Uhr gesendet werden.

![Die zeitabhängigen Planungsoptionen für die Verwendung von intelligentem Timing, um eine Campaign zur beliebtesten Nutzungszeit der App unter allen Nutzer:innen zu senden.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Zustellungsregeln {#delivery-rules}

Da der optimale Zeitpunkt einer:eines Nutzer:in zu jeder beliebigen Zeit innerhalb von 24 Stunden liegen kann, müssen alle Campaigns mit intelligentem Timing 24 Stunden im Voraus geplant werden. Ähnlich wie bei Campaigns mit festgelegtem Zeitpunkt werden bei Nachrichten mit einem 1-Tage-Fenster Nutzer:innen verpasst, die vor ihrem optimalen Zeitpunkt in ihrer Zeitzone aus dem Segment fallen. Segmente für Campaigns mit intelligentem Timing sollten mindestens ein 3-Tage-Fenster umfassen, um dies zu berücksichtigen.

Wenn das Profil einer:eines Nutzer:in nicht genügend Daten enthält, um einen optimalen Zeitpunkt zu berechnen, können Sie eine Fallback-Methode wählen: entweder den Versand zur beliebtesten Nutzungszeit der App unter allen Nutzer:innen oder eine angepasste Fallback-Zeit.

### Anwendungsfälle

Campaigns mit intelligentem Timing eignen sich am besten für einmalige und wiederkehrende Nachrichten, bei denen eine gewisse Flexibilität hinsichtlich der Zustellzeit besteht – sie sind beispielsweise weniger geeignet für Eilmeldungen oder zeitgebundene Ankündigungen.

## Auswertung der Zielgruppenkriterien bei Verzögerungen {#audience-criteria-evaluation-with-delays}

Bei Campaigns mit geplanter Zustellung werden die Zielgruppenkriterien immer zum Zeitpunkt des geplanten Versands ausgewertet, nicht beim Start der Campaign. Dies gilt für jede Verzögerung zwischen Planung und Versand – beispielsweise durch Rate-Limiting, lokale Zeitzone, intelligentes Timing oder einen Trigger-Zeitplan.

## Fehlerbehebung {#troubleshooting}

### Warum hat meine geplante E-Mail-Campaign nicht die gesamte geschätzte Zielgruppe erreicht? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

Der Versand kann geringer ausfallen als die geschätzte Zielgruppe, wenn Nutzer:innen keine E-Mail-Adresse haben, E-Mails nicht abonniert haben oder zum Sendezeitpunkt durch Zustellbarkeitsfilter ausgeschlossen werden. Eine kürzliche Änderung der E-Mail-Adresse einer:eines Nutzer:in kann ebenfalls die Berechtigung beeinflussen, wenn die Zielgruppenkriterien beim Versand erneut ausgewertet werden. Weitere Faktoren finden Sie unter [Warum ist der Versand geringer als die geschätzte Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size).

### Warum wurde meine Campaign einen Tag vor dem geplanten Zeitpunkt gesendet? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

Wenn eine Campaign früher als der in den **Unternehmenseinstellungen** festgelegte Zeitplan gesendet wird, aktivieren Sie **In lokaler Zeitzone senden** oder fügen Sie ein Zustellzeitfenster für Campaigns mit intelligentem Timing hinzu. Ohne diese Einstellungen kann die Zeitzonenauswertung den Versand für Nutzer:innen in früheren Zeitzonen vor Ihrem beabsichtigten Zeitplan in die Warteschlange stellen. Weitere Informationen finden Sie unter [Campaigns in lokaler Zeitzone](#local-time-zone-campaigns) und [Wann wertet Braze Nutzer:innen für die Zustellung in lokaler Zeitzone aus?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery).