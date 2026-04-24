---
nav_title: Einwilligung und Adresserfassung
article_title: Einwilligung und Adresserfassung
page_order: 6
page_type: reference
description: "Dieser Referenzartikel behandelt Best Practices für die Einholung von Einwilligungen und die Erfassung von E-Mail-Adressen und definiert die verschiedenen möglichen Abo-Status von Nutzer:innen."
channel: email

---

# Einwilligung und Adresserfassung

> Bevor Sie Ihre ersten E-Mails versenden, ist es wichtig, zunächst die Erlaubnis Ihrer Kund:innen einzuholen. Das ist eine Frage der Höflichkeit und wirkt Wunder für Ihre Öffnungsraten!

## Abo-Status

Es gibt drei E-Mail-Abo-Status für Nutzer:innen: **Opted In**, **Subscribed** und **Unsubscribed**. Um den Abo-Status von Nutzer:innen zu ändern, lesen Sie unseren Artikel zum [Ändern von Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions/#changing-subscriptions) oder nutzen Sie unsere [Subscription-APIs]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Abo-Status | Beschreibung |
|---|---|
| Opted In | Diese Kund:innen haben auf den Link in einer Bestätigungs-E-Mail geklickt und sich aktiv für den Empfang Ihrer Nachrichten entschieden. |
| Subscribed | Standardmäßig sind Nutzer:innen für E-Mails abonniert, solange eine gültige E-Mail-Adresse in ihrem Profil hinterlegt ist. Nutzer:innen bleiben abonniert, bis sie sich abmelden oder ein Opt-in durchführen. |
| Unsubscribed | Um als abgemeldet markiert zu werden, hat sich ein:e Kund:in entweder ausdrücklich von Ihren E-Mails abgemeldet oder eine E-Mail als Spam markiert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Methoden zur Adresserfassung

Neben der Einholung der Erlaubnis Ihrer Nutzer:innen vor dem Versand gibt es verschiedene Methoden zur Erfassung von E-Mail-Adressen, die sich auf Ihre Zustellbarkeit auswirken können.

### Gekaufte Adresslisten

Das Versenden von E-Mails an gekaufte oder gemietete Listen verstößt gegen Ihren Braze-Vertrag! Wenn Sie E-Mail-Adressen kaufen, versenden Sie völlig unaufgeforderte Nachrichten und setzen sich dem Risiko von Zustellbarkeitsproblemen aus.

### Co-Registrierung

Co-Registrierung bezeichnet eine Vereinbarung zwischen Unternehmen zur Erfassung von Nutzerinformationen. Dies ist eine riskante Erfassungsmethode. Sie meldet Nutzer:innen für den Empfang von E-Mails von Drittanbietern an, manchmal ohne Wissen oder Erlaubnis der Kund:innen. Wenn Sie diesen Weg wählen, stellen Sie sicher, dass klare Hinweise und die Möglichkeit zur Abmeldung am Erfassungspunkt vorhanden sind.

### Vorab aktiviertes oder erzwungenes Opt-in

Vorab aktiviertes Opt-in ist eine E-Mail-Registrierungsmethode, bei der das Kontrollkästchen für die E-Mail-Registrierung bereits aktiviert ist, damit Abonnent:innen Ihre E-Mails erhalten. Indem das Kontrollkästchen aktiviert bleibt, stimmen Abonnent:innen zu und geben ihre Einwilligung zum Empfang Ihrer E-Mails. Diese Methode neigt dazu, Menschen zu verärgern (und ist zudem für E-Mails, die nach oder innerhalb von Kanada gesendet werden, illegal). Sie erhalten möglicherweise eine ansehnliche E-Mail-Liste, können aber nicht sicher sein, dass diese Nutzer:innen Ihre Marketing-E-Mails tatsächlich erhalten möchten.

### Single Opt-in

Ein Single Opt-in erfolgt, wenn sich Abonnent:innen über ein Registrierungsformular anmelden und sofort zu Ihrer E-Mail-Liste hinzugefügt werden. Bei dieser Methode führen Nutzer:innen einen einzigen Schritt zur Registrierung durch, z. B. die Eingabe ihrer E-Mail-Adresse in ein Erfassungsfeld oder das Aktivieren eines Kontrollkästchens im Rahmen einer Transaktion.

### Bestätigtes Opt-in

Ein bestätigtes Opt-in liegt vor, wenn Nutzer:innen ein Kontrollkästchen für E-Mail-Kommunikation aktivieren und im Gegenzug eine Bestätigungsnachricht erhalten. Diese Methode ermöglicht es Nutzer:innen, Art und Häufigkeit der Inhalte zu wählen, und verbessert das Engagement.

Um sicherzustellen, dass Sie nur die engagiertesten Nutzer:innen ansprechen, können Sie auch die Methode des doppelt bestätigten Opt-ins verwenden. Bei diesem Ansatz wird ein zusätzlicher Schritt hinzugefügt, bei dem Nutzer:innen auf einen Button oder Link in der Bestätigungs-E-Mail klicken müssen, um in die E-Mail-Liste aufgenommen zu werden.