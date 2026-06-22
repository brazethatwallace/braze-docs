---
nav_title: Optimierungen
article_title: A/B-Tests mit Gewinnervariante oder personalisierten Varianten optimieren
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Sie die Gewinnervariante oder personalisierte Variante bei der Erstellung von multivariaten und A/B-Tests verwenden können."
---

# A/B-Tests optimieren {#optimize-ab-tests}

> Erfahren Sie, wie Sie die Variantenoptimierung bei der Erstellung von multivariaten und A/B-Tests verwenden können.


## Push {#push}
Bei der [Erstellung eines A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) für Push gibt es eine Optimierungsoption: [BrazeAI<sup>TM</sup> Variantenauswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection/). Dieses Feature ermöglicht es, dass Ihre einmaligen oder wiederkehrenden A/B-Tests automatisch ein Experiment durchführen und für die besten Engagement-Ergebnisse optimieren.

## E-Mail, Webhook, SMS und WhatsApp {#email-webhook-sms-and-whatsapp}

Bei der [Erstellung eines A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) für E-Mail-, Webhook-, SMS- und WhatsApp-Campaigns, die für einen einmaligen Versand geplant sind, können Sie zwischen zwei Optimierungsoptionen wählen: **Gewinnervariante** und **Personalisierte Variante**.

![Optimierungsoptionen im Abschnitt „A/B-Tests“ bei der Auswahl Ihrer Zielgruppe. Es werden drei Optionen aufgeführt: Keine Optimierung, Gewinnervariante und Personalisierte Variante. Personalisierte Variante ist ausgewählt.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Beide Optionen funktionieren, indem zunächst ein Test an einen Prozentsatz Ihres Zielsegments gesendet wird. Nach Beendigung des Tests wird den verbleibenden Nutzer:innen Ihrer Zielgruppe entweder die Variante mit der besten Performance (Gewinnervariante) oder die Variante, mit der sie am ehesten interagieren werden (Personalisierte Variante), zugesandt.

{% alert tip %}
Optimierungen finden Sie im Schritt **Zielgruppen** bei der Campaign-Erstellung unter **A/B Testing**.
{% endalert %}

## Gewinnervariante {#winning-variant}

Das Versenden der Gewinnervariante ist ähnlich wie ein normaler A/B-Test. Nutzer:innen in dieser Gruppe erhalten die Gewinnervariante, sobald der erste Test abgeschlossen ist.

1. Wählen Sie **Gewinnervariante** aus und legen Sie fest, welcher Prozentsatz Ihrer Campaign-Zielgruppe der Gewinnervarianten-Gruppe zugewiesen werden soll.
2. Konfigurieren Sie die folgenden zusätzlichen Einstellungen.

| Feld | Beschreibung |
| --- | --- |
| Gewinnervariante bestimmen | Die Metrik, für die optimiert werden soll. Wählen Sie zwischen *eindeutigen Öffnungen* oder *Klicks* für E-Mail, *Öffnungen* für Push oder *primärer Konversionsrate* für alle Kanäle. Die Auswahl von *Öffnungen* oder *Klicks* zur Bestimmung der Gewinnervariante hat keinen Einfluss auf die [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) Ihrer Campaign. <br><br>Beachten Sie: Wenn Sie eine Kontrollgruppe verwenden, können Nutzer:innen in der Kontrollgruppe keine *Öffnungen* oder *Klicks* ausführen, sodass die Performance der Kontrollgruppe garantiert `0` beträgt. Daher kann die Kontrollgruppe den A/B-Test nicht gewinnen. Dennoch kann es sinnvoll sein, eine Kontrollgruppe zu verwenden, um andere Metriken für Nutzer:innen zu verfolgen, die keine Nachricht erhalten. |
| Sendezeitpunkt der Gewinnervariante | Datum und Uhrzeit, zu der die Gewinnervariante gesendet wird. |
| Wenn keine Gewinnervariante bestimmt werden kann | Was passiert, wenn keine Variante mit statistisch signifikantem Vorsprung gewinnt. Wählen Sie zwischen dem Senden der leistungsstärksten Variante oder dem Beenden des Tests ohne weitere Nachrichten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gewinnervariante" }

## Personalisierte Variante {#personalized-variant}

Verwenden Sie personalisierte Varianten, um jeder Person in Ihrem Zielsegment die Variante zu senden, mit der sie am wahrscheinlichsten interagieren wird.

Um die beste Variante für jede Person zu bestimmen, sendet Braze zunächst einen Test an einen Teil Ihrer Zielgruppe, um Zusammenhänge zwischen Nutzerattributen und Nachrichtenpräferenzen zu ermitteln. Basierend darauf, wie Nutzer:innen auf die einzelnen Varianten im ersten Test reagieren, werden diese Merkmale verwendet, um zu bestimmen, welche verbleibenden Nutzer:innen welche Variante erhalten. Wenn keine Zusammenhänge gefunden werden und keine Personalisierung möglich ist, wird die Gewinnervariante automatisch an die verbleibenden Nutzer:innen gesendet. Weitere Informationen darüber, wie personalisierte Varianten bestimmt werden, finden Sie unter [Analytics für multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#personalized-variant).

1. Wählen Sie **Personalisierte Variante** aus und legen Sie fest, welcher Prozentsatz Ihrer Campaign-Zielgruppe der Gruppe für personalisierte Varianten zugewiesen werden soll.
2. Konfigurieren Sie die folgenden zusätzlichen Einstellungen.

| Feld | Beschreibung |
| --- | --- |
| Personalisierte Variante bestimmen | Die Metrik, für die optimiert werden soll. Wählen Sie zwischen *eindeutigen Öffnungen* oder *Klicks* für E-Mail, *Öffnungen* für Push oder *primärer Konversionsrate* für alle Kanäle. Die Auswahl von *Öffnungen* oder *Klicks* zur Bestimmung der personalisierten Variante hat keinen Einfluss auf die [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) Ihrer Campaign. <br><br>Beachten Sie: Wenn Sie eine Kontrollgruppe verwenden, können Nutzer:innen in der Kontrollgruppe keine *Öffnungen* oder *Klicks* ausführen, sodass die Performance der Kontrollgruppe garantiert `0` beträgt. Daher kann die Kontrollgruppe den A/B-Test nicht gewinnen. Dennoch kann es sinnvoll sein, eine Kontrollgruppe zu verwenden, um andere Metriken für Nutzer:innen zu verfolgen, die keine Nachricht erhalten. |
| Sendezeitpunkt der personalisierten Variante | Datum und Uhrzeit, zu der die personalisierte Variante gesendet wird. |
| Wenn keine personalisierte Variante bestimmt werden kann | Was passiert, wenn keine personalisierten Varianten gefunden werden. Wählen Sie zwischen dem Senden der Gewinnervariante oder dem Beenden des Tests ohne weitere Nachrichten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalisierte Variante" }

## Analytics {#analytics}

Informationen zu den Ergebnissen Ihres A/B-Tests mit einer Optimierung finden Sie unter [Analytics für multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).