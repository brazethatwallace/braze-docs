---
nav_title: Optimierungen
article_title: Optimieren Sie A/B-Tests mit Gewinnervarianten oder personalisierten Varianten
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Sie die Varianten „Gewinnervariante“ oder „Personalisierte Variante“ bei der Erstellung von multivariaten und A/B-Tests verwenden können."
---

# Optimieren Sie A/B-Tests mit Gewinnervarianten oder personalisierten Varianten {#optimize-ab-tests-with-winning-variant-or-personalized-variants}

> Erfahren Sie, wie Sie die Varianten „Gewinnervariante“ oder „Personalisierte Variante“ bei der Erstellung von multivariaten und A/B-Tests verwenden können.

Bei der [Erstellung eines A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) für E-Mail-, Push-, Webhook-, SMS- und WhatsApp-Kampagnen, die für einen einmaligen Versand geplant sind, können Sie eine Optimierung auswählen. Es gibt zwei Optimierungsmöglichkeiten: **Gewinnervariante** und **Personalisierte Variante**.

![Optimierungsoptionen, die im Abschnitt „A/B-Tests“ aufgeführt sind, wenn Sie Ihre Zielgruppe auswählen. Es werden drei Optionen aufgeführt: Keine Optimierung, Gewinnervariante und Personalisierte Variante. Personalisierte Variante ist ausgewählt.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Beide Optionen funktionieren, indem Sie einen ersten Test an einen Prozentsatz Ihres Zielsegments senden. Nach Beendigung des Tests wird den verbleibenden Nutzern Ihrer Zielgruppe entweder die Variante mit der besten Leistung (Gewinnervariante) oder die Variante, mit der sie sich am ehesten beschäftigen werden (personalisierte Variante), zugesandt.

{% alert tip %}
Optimierungen finden Sie im Schritt **Zielgruppen** bei der Kampagnenerstellung unter **A/B-Tests**.
{% endalert %}

## Gewinnervariante {#winning-variant}

Das Versenden der Gewinnervariante ist ähnlich wie ein normaler A/B-Test. Nutzer:innen in dieser Gruppe erhalten die Gewinnervariante, sobald der erste Test abgeschlossen ist.

1. Wählen Sie **Gewinnervariante** aus und legen Sie fest, welcher Prozentsatz Ihrer Kampagnenzielgruppe der Gewinnervarianten-Gruppe zugewiesen werden soll.
2. Konfigurieren Sie die folgenden zusätzlichen Einstellungen.

| Feld | Beschreibung |
| --- | --- |
| Gewinnervariante bestimmen | Die Metrik, für die optimiert werden soll. Wählen Sie zwischen *Eindeutige Öffnungen* oder *Klicks* für E-Mail, *Öffnungen* für Push oder *Primäre Konversionsrate* für alle Kanäle. Die Auswahl von *Öffnungen* oder *Klicks* zur Bestimmung der Gewinnervariante hat keinen Einfluss auf die [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) Ihrer Campaign. <br><br>Beachten Sie: Wenn Sie eine Kontrollgruppe verwenden, können Nutzer:innen in der Kontrollgruppe keine *Öffnungen* oder *Klicks* ausführen, sodass die Performance der Kontrollgruppe garantiert `0` beträgt. Daher kann die Kontrollgruppe den A/B-Test nicht gewinnen. Dennoch kann es sinnvoll sein, eine Kontrollgruppe zu verwenden, um andere Metriken für Nutzer:innen zu verfolgen, die keine Nachricht erhalten. |
| Sendezeitpunkt der Gewinnervariante | Datum und Uhrzeit, zu der die Gewinnervariante gesendet wird. |
| Wenn keine Gewinnervariante bestimmt werden kann | Was passiert, wenn keine Variante mit statistisch signifikantem Vorsprung gewinnt. Wählen Sie zwischen dem Senden der leistungsstärksten Variante oder dem Beenden des Tests ohne weitere Nachrichten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Personalisierte Variante {#personalized-variant}

Verwenden Sie personalisierte Varianten, um jeder Person in Ihrem Zielsegment die Variante zu senden, mit der sie am wahrscheinlichsten interagieren wird.

Um die beste Variante für jede Person zu bestimmen, sendet Braze zunächst einen Test an einen Teil Ihrer Zielgruppe, um Zusammenhänge zwischen Nutzermerkmalen und Nachrichtenpräferenzen zu ermitteln. Basierend darauf, wie Nutzer:innen auf die einzelnen Varianten im ersten Test reagieren, werden diese Merkmale verwendet, um zu bestimmen, welche verbleibenden Nutzer:innen welche Variante erhalten. Wenn keine Zusammenhänge gefunden werden und keine Personalisierung möglich ist, wird die Gewinnervariante automatisch an die verbleibenden Nutzer:innen gesendet. Weitere Informationen darüber, wie personalisierte Varianten bestimmt werden, finden Sie unter [Analytics für multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#personalized-variant).

1. Wählen Sie **Personalisierte Variante** aus und legen Sie fest, welcher Prozentsatz Ihrer Kampagnenzielgruppe der Gruppe für personalisierte Varianten zugewiesen werden soll.
2. Konfigurieren Sie die folgenden zusätzlichen Einstellungen.

| Feld | Beschreibung |
| --- | --- |
| Personalisierte Variante bestimmen | Die Metrik, für die optimiert werden soll. Wählen Sie zwischen *Eindeutige Öffnungen* oder *Klicks* für E-Mail, *Öffnungen* für Push oder *Primäre Konversionsrate* für alle Kanäle. Die Auswahl von *Öffnungen* oder *Klicks* zur Bestimmung der personalisierten Variante hat keinen Einfluss auf die [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) Ihrer Campaign. <br><br>Beachten Sie: Wenn Sie eine Kontrollgruppe verwenden, können Nutzer:innen in der Kontrollgruppe keine *Öffnungen* oder *Klicks* ausführen, sodass die Performance der Kontrollgruppe garantiert `0` beträgt. Daher kann die Kontrollgruppe den A/B-Test nicht gewinnen. Dennoch kann es sinnvoll sein, eine Kontrollgruppe zu verwenden, um andere Metriken für Nutzer:innen zu verfolgen, die keine Nachricht erhalten. |
| Sendezeitpunkt der personalisierten Variante | Datum und Uhrzeit, zu der die personalisierte Variante gesendet wird. |
| Wenn keine personalisierte Variante bestimmt werden kann | Was passiert, wenn keine personalisierten Varianten gefunden werden. Wählen Sie zwischen dem Senden der Gewinnervariante oder dem Beenden des Tests ohne weitere Nachrichten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Analytics

Informationen zu den Ergebnissen Ihres A/B-Tests mit einer Optimierung finden Sie unter [Analytics für multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).