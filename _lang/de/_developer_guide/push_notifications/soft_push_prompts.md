---
page_order: 6
nav_title: Sanfte Push-Aufforderungen
article_title: Sanfte Push-Aufforderungen für das Internet
description: "Erfahren Sie, wie Sie sanfte Push-Aufforderungen für das Braze Web SDK einrichten, bevor die native Browser-Benachrichtigungsberechtigungsaufforderung angezeigt wird."
channel:
  - push notifications
---

# Sanfte Push-Aufforderungen für das Internet {#soft-push-prompts-for-web}

> Sanfte Push-Aufforderungen sind angepasste Nachrichten, die Sie vor der nativen Benachrichtigungsberechtigungsaufforderung des Browsers anzeigen. Sie erklären, warum Nutzer:innen Push-Benachrichtigungen aktivieren sollten, und können die Opt-in-Rate im Vergleich zur Anzeige der Systemaufforderung beim ersten Besuch verbessern. Dieser Leitfaden behandelt die Implementierung sanfter Push-Aufforderungen mit dem Braze Web SDK, einschließlich des Zeitpunkts zum Triggern der Aufforderung, der Anpassung des Nachrichteninhalts und bewährter Verfahren für das Timing der Anfrage, nachdem Nutzer:innen den Mehrwert von Push verstanden haben.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/soft_push_prompts.md %}
{% endsdktab %}
{% endsdktabs %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was ist eine sanfte Push-Aufforderung? {#what-is-a-soft-push-prompt}

Eine sanfte Push-Aufforderung ist eine angepasste In-App- oder On-Site-Nachricht, die Sie vor dem nativen Benachrichtigungsberechtigungsdialog des Browsers anzeigen. Sie erklärt den Mehrwert von Push, sodass Nutzer:innen eher zustimmen, wenn die Systemaufforderung erscheint.

### Wann sollte ich eine sanfte Push-Aufforderung anzeigen? {#when-should-i-show-a-soft-push-prompt}

Zeigen Sie eine sanfte Push-Aufforderung an, nachdem Nutzer:innen den Mehrwert Ihres Produkts verstanden haben – zum Beispiel nach dem Onboarding oder einer bedeutsamen In-App-Aktion – und nicht beim ersten Seitenaufruf. Weitere Informationen zur Implementierung finden Sie in den Web-SDK-Schritten in diesem Leitfaden.