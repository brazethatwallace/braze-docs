---
nav_title: "Transaktions-E-Mail erstellen"
article_title: "Transaktions-E-Mail erstellen"
page_order: 1

description: "Dieser Referenzartikel beschreibt, wie Sie eine neue Braze-Transaktions-E-Mail-Campaign erstellen und konfigurieren."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Transaktions-E-Mail erstellen {#create-a-transactional-email}

> Braze-Transaktions-E-Mails werden versendet, um eine vereinbarte Transaktion zwischen einem Sender und dem/der Empfänger:in zu ermöglichen. Dieser Referenzartikel beschreibt, wie Sie eine Transaktions-E-Mail-Campaign im Braze-Dashboard erstellen und eine `campaign_id` generieren, die Sie in Ihre API-Aufrufe für unseren [`/transactional/v1/campaigns/{campaign_id}/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) einbinden können.

{% alert important %}
Braze-Transaktions-E-Mails sind nur als Teil ausgewählter Braze-Pakete verfügbar. Kontaktieren Sie Ihren Braze-Customer-Success-Manager oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support) für weitere Details.
{% endalert %}

Der Campaign-Typ für Transaktions-E-Mails ist speziell dafür konzipiert, automatisierte, nicht-werbliche E-Mail-Nachrichten zu versenden, um eine vereinbarte Transaktion zwischen Ihnen und Ihren Kund:innen zu ermöglichen. Dazu gehören Informationen wie:

- Bestellbestätigungen
- Passwortzurücksetzungen
- Rechnungsbenachrichtigungen
- Versandbenachrichtigungen

Kurz gesagt können Sie Transaktions-E-Mails verwenden, um geschäftskritische Benachrichtigungen zu versenden, die von Ihrem Dienst für einzelne Nutzer:innen stammen und bei denen Geschwindigkeit von höchster Bedeutung ist.

{% alert important %}
Transaktions-E-Mails unterscheiden sich von transaktionalen Campaigns, die verwendet werden können, um Ihre Nutzer:innen ohne zusätzliche Kosten anzusprechen. Transaktionale Campaigns können beispielsweise Nachrichten umfassen, die gesendet werden, nachdem ein:e Nutzer:in einen Artikel in den Warenkorb gelegt hat. Weitere Informationen finden Sie unter [Zielgruppen-Targeting-Optionen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users).
{% endalert %}

{% alert note %}
API-Sendungen für Transaktions-E-Mails unterstützen die Nachrichtenarchivierung. Wenn die Nachrichtenarchivierung für E-Mail in Ihrem Workspace aktiviert ist, speichert Braze eine gerenderte Kopie jeder Transaktions-E-Mail-Sendung. Weitere Informationen finden Sie unter [Nachrichtenarchivierung]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving).
{% endalert %}

## 1. Schritt: Neue Campaign erstellen {#step-1-create-a-new-campaign}

Um eine neue Transaktions-E-Mail-Campaign zu erstellen, erstellen Sie eine Campaign und wählen Sie **Transactional Email** als Ihren Messaging-Kanal aus.

![Dropdown „Kampagne erstellen“ mit der hervorgehobenen Option für Transaktions-E-Mail.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Nun können Sie mit der Konfiguration Ihrer Transaktions-E-Mail-Campaign fortfahren.

## 2. Schritt: Campaign konfigurieren {#step-2-configure-your-campaign}

Der Campaign-Erstellungsablauf für Transaktions-E-Mail-Campaigns ist im Vergleich zu einer [Standard-E-Mail-Campaign]({{site.baseurl}}/user_guide/channels/email/html_editor) vereinfacht, um sicherzustellen, dass Ihre geschäftskritischen Transaktions-E-Mails alle Nutzer:innen erreichen können.

Daher werden Sie feststellen, dass einige Einstellungen, die Sie möglicherweise von anderen Braze-Campaign-Typen kennen, beim Einrichten dieses Campaign-Typs nicht erforderlich sind:

- Der Schritt **Zustellung** wurde vereinfacht, um Planungsoptionen zu entfernen. Transaktions-E-Mails werden immer über die Braze REST API unter Verwendung der auf der Seite **Zustellung** angezeigten Campaign-ID getriggert. Zusätzliche Einstellungen wie Kontrollen zur erneuten Berechtigung und Frequency-Capping-Einstellungen wurden ebenfalls entfernt, um sicherzustellen, dass alle Nutzer:innen für diese kritischen Transaktionsbenachrichtigungen erreichbar sind, wenn Ihr Dienst eine Sendeanfrage auslöst.
- Der Schritt **Zielgruppen** wurde entfernt. Da Transaktions-E-Mails Ihre gesamte Nutzerbasis als berechtigt einschreiben (einschließlich abgemeldeter Nutzer:innen), müssen keine Filter oder Segmente angegeben werden. Wenn Sie daher eine Logik anwenden möchten, wer diese Nachricht erhalten soll, empfehlen wir, diese Logik anzuwenden, bevor Sie entscheiden, ob die API-Anfrage an Braze gesendet werden soll, um die Nachricht an eine:n bestimmte:n Nutzer:in zu triggern.
- Der Schritt **Conversions** wurde entfernt. Transaktions-E-Mails unterstützen derzeit kein Konversions-Event-Tracking.

![Workflow „Verfassen“, „Zustellung“ und „Bestätigen“ zum Erstellen einer Transaktions-E-Mail-Campaign.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Um Ihre Transaktions-E-Mail-Campaign zu konfigurieren, folgen Sie diesen Schritten:

1. Fügen Sie einen aussagekräftigen Namen hinzu, damit Sie die Ergebnisse auf Ihrer **Campaigns**-Seite finden können, nachdem Sie Ihre Nachrichten gesendet haben.
2. Verfassen Sie Ihre E-Mail oder wählen Sie ein Template aus.
3. Notieren Sie sich Ihre `campaign_id`. Nachdem Sie Ihre API-Campaign gespeichert haben, müssen Sie die generierte `campaign_id` in Ihre API-Anfrage einfügen, wie im Artikel zum [Transaktions-E-Mail-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) beschrieben.
4. Klicken Sie auf **Save Campaign**, und Sie können mit Ihrer API-Campaign beginnen!

{% alert note %}
Die Einstellung für die Ein-Klick-Listenabmeldung bei Transaktions-E-Mail-Campaigns ist standardmäßig auf **Use workspace default** gesetzt, ähnlich wie bei anderen E-Mail-Campaigns. Da dies für transaktionales Messaging vorgesehen ist, fügt Braze keine Ein-Klick-Abmeldung hinzu. Um eine Ein-Klick-Abmeldung zu diesem Campaign-Typ hinzuzufügen, [bearbeiten Sie diese Einstellung]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#message-level-one-click-list-unsubscribe) unter **Sending Info**.
{% endalert %}

### Nicht zulässige Tags in Transaktions-E-Mails {#disallowed-tags-in-transactional-emails}

Die Liquid-Tags `Connected Content` und `Promotion Code` sind in Transaktions-E-Mail-Campaigns nicht verfügbar.

Die Verwendung des `Connected Content`-Tags erfordert, dass Braze während des Sendeprozesses eine ausgehende API-Anfrage stellt, was den Nachrichtenversand verlangsamen kann, wenn der externe Dienst, den wir anfragen, Latenz aufweist. Ebenso erfordert der `Promotion Code`-Tag, dass Braze eine zusätzliche Verarbeitung durchführt, um die Verfügbarkeit einer Aktion vor dem Senden zu prüfen, was den Sendeprozess verlangsamen kann, falls keine verfügbar ist.

Daher unterstützen wir die Einbindung von `Connected Content`- oder `Promotion Code`-Tags in keinem Feld Ihrer Transaktions-E-Mail-Campaign.