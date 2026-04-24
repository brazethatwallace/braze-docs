---
nav_title: Zustellbarkeitsfallen und Spam-Traps
article_title: Zustellbarkeitsfallen und Spam-Traps
page_order: 7
page_type: reference
description: "Dieser Referenzartikel behandelt potenzielle Zustellbarkeitsfallen bei E-Mails, Spam-Traps und wie Sie diese vermeiden können."
channel: email

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}Zustellbarkeitsfallen und Spam-Traps

Ihre E-Mail-Zustellbarkeit kann durch die folgenden Spam-Traps beeinträchtigt werden:

| Trap-Typ | Beschreibung |
|---|---|
| Pristine Traps | E-Mail-Adressen und Domains, die noch nie verwendet wurden. |
| Recycled Traps | E-Mail-Adressen, die ursprünglich echten Nutzer:innen gehörten, aber inzwischen inaktiv sind. |
| Typo Traps | E-Mail-Adressen mit häufigen Tippfehlern. |
| Spam-Beschwerden | Wenn Ihre E-Mail von einer Kundin oder einem Kunden als Spam markiert wird. |
| Hohe Bounce-Rate | Wenn Ihre E-Mail regelmäßig nicht zugestellt werden kann, weil die Adresse der Empfängerin oder des Empfängers ungültig ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## So vermeiden Sie Spam-Traps

Diese Traps lassen sich vermeiden, wenn Sie einen bestätigten Opt-in-Prozess einrichten. Indem Sie eine erste Opt-in-E-Mail senden und Ihre Kund:innen bitten zu bestätigen, dass sie Ihre Nachrichten erhalten möchten, stellen Sie sicher, dass Ihre Empfänger:innen von Ihnen hören möchten und dass Sie an echte, gültige Adressen senden. Hier sind weitere Möglichkeiten, Spam-Traps zu vermeiden:

1. Senden Sie eine Double-Opt-in-E-Mail. Das ist eine E-Mail, bei der Nutzer:innen ihre Abo-Auswahl durch Klicken auf einen Link bestätigen müssen.
2. Implementieren Sie als Best Practice eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **Kaufen Sie niemals E-Mail-Listen.**

{% alert tip %}
Die Braze-Teams für Kundenerfolg und Zustellbarkeit können Ihnen helfen, Best Practices einzuhalten und die Zustellbarkeit weltweit zu maximieren.
{% endalert %}

## Eine E-Mail-Adresse von Ihrer Bounce- oder Spam-Liste entfernen

Sie können Bounce-E-Mails und E-Mails auf Ihrer Braze-Spam-Liste mit den folgenden Endpunkten entfernen:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## E-Mail-Zustellbarkeit verbessern

Best Practices zur Verbesserung Ihrer E-Mail-Zustellbarkeit finden Sie unter [E-Mail-Zustellbarkeit verbessern]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).