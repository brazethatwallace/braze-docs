---
nav_title: Zustellbarkeitsfallen und Spam-Traps
article_title: Zustellbarkeitsfallen und Spam-Traps
page_order: 7
page_type: reference
description: "Dieser Referenzartikel befasst sich mit potenziellen Fallstricken bei der E-Mail-Zustellung, mit Spam-Traps und wie Sie diese vermeiden können."
channel: email

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} Zustellbarkeitsfallen und Spam-Traps {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomemail-onboarding-for-pro-and-enterprise-achieving-high-deliverability-stylefloatrightwidth120pxborder0-classnoimgborderdeliverability-pitfalls-and-spam-traps}

> Dieser Artikel behandelt häufige Zustellbarkeitsfallen bei E-Mails, Spam-Traps und wie Sie diese vermeiden können.

Die Zustellbarkeit Ihrer E-Mails kann durch folgende Spam-Traps beeinträchtigt werden:

| Trap-Typ | Beschreibung |
|---|---|
| Unverfälschte Traps | E-Mail-Adressen und Domains, die noch nie benutzt wurden. |
| Recycelte Traps | E-Mail-Adressen, die ursprünglich echten Nutzer:innen gehörten, jetzt aber inaktiv sind. |
| Tippfehler-Traps | E-Mail-Adressen mit häufigen Tippfehlern. |
| Spam-Beschwerden | Wenn Ihre E-Mail von Verbraucher:innen als Spam markiert wird. |
| Hohe Bounce-Rate | Wenn Ihre E-Mail regelmäßig nicht zugestellt werden kann, weil die Adresse der Empfänger:in ungültig ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zustellbarkeitsfallen und Spam-Traps" }

## So vermeiden Sie Spam-Traps {#how-to-avoid-spam-traps}

Diese Traps lassen sich vermeiden, wenn Sie einen bestätigten Opt-in-Prozess einrichten. Indem Sie eine erste Opt-in-E-Mail senden und Abonnent:innen bitten, zu bestätigen, dass sie Ihre Nachrichten erhalten möchten, stellen Sie sicher, dass Ihre Empfänger:innen von Ihnen hören möchten und dass Sie an echte, gültige Adressen senden. Hier sind weitere Möglichkeiten, Spam-Traps zu vermeiden:

1. Senden Sie eine Double-Opt-in-E-Mail. Dies ist eine E-Mail, bei der Nutzer:innen ihre Abo-Auswahl durch Klicken auf einen Link bestätigen müssen.
2. Implementieren Sie als Best Practice eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies).
3. **Kaufen Sie niemals E-Mail-Listen.**

{% alert tip %}
Die Braze-Teams für Kundenerfolg und Zustellbarkeit können Ihnen helfen, Best Practices einzuhalten, um die Zustellbarkeit weltweit zu maximieren.
{% endalert %}

## So lösen Sie eine Blockierung durch eine kostenlose E-Mail-Domain bei Microsoft {#how-to-resolve-a-free-email-domain-block-for-microsoft}

Microsoft hebt Blockierungen für Absender, die Probleme bei der Zustellung an kostenlose E-Mail-Domains (Hotmail, Live, MSN und Outlook) haben, nur selten auf. Reduzieren Sie stattdessen Ihr Sendevolumen an diese Domains konsequent und senden Sie nur an kürzlich aktive Kontakte. Wenn Sie keine Kerngruppe engagierter Empfänger:innen identifizieren können, stellen Sie den Versand an diese Domains vollständig ein.

Ein Beispiel für eine Blockierungsnachricht einer kostenlosen E-Mail-Domain:

`550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your Internet service provider since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

Sie können das Volumen langsam steigern, ähnlich wie beim [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming), und dabei die Metriken genau im Auge behalten. Häufig gibt es eine Grundursache für die Zustellbarkeitsprobleme, die identifiziert und behoben werden muss. In der Regel handelt es sich um fehlende ordnungsgemäße Einwilligungen, mangelnde laufende Listenhygiene oder eine Kombination dieser Faktoren.

## E-Mail-Adresse von Ihrer Bounce- oder Spam-Liste entfernen {#remove-an-email-address-from-your-bounce-or-spam-list}

Sie können E-Mails mit Bounces und E-Mails auf Ihrer Braze-Spam-Liste mit den folgenden Endpunkten entfernen:

- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## E-Mail-Zustellbarkeit verbessern {#improve-email-deliverability}

Weitere Informationen finden Sie unter [E-Mail-Zustellbarkeit verbessern]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability).

## BIMI

Informationen zu BIMI (Brand Indicators for Message Identification) finden Sie unter [E-Mail-Authentifizierung]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).