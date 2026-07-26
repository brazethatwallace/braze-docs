---
nav_title: Angepasste E-Mail-Fußzeile
article_title: Angepasste E-Mail-Fußzeile
page_order: 6.5
description: "Dieser Artikel beschreibt, wie Sie eine arbeitsbereichsweite angepasste E-Mail-Fußzeile einrichten können."
channel:
  - email

---

# Angepasste E-Mail-Fußzeile {#custom-email-footer}

> Sie können eine arbeitsbereichsweite angepasste E-Mail-Fußzeile festlegen, die Sie mit dem Liquid-Attribut {% raw %}`{{${email_footer}}}`{% endraw %} als Template in jede E-Mail einfügen können.

Durch die Verwendung angepasster E-Mail-Fußzeilen müssen Sie nicht mehr für jedes E-Mail-Template oder jede E-Mail-Campaign eine neue Fußzeile erstellen. Alle neuen und bestehenden E-Mail-Campaigns übernehmen die Änderungen, die Sie an Ihrer angepassten Fußzeile vornehmen. Beachten Sie, dass die Einhaltung des [CAN-SPAM Act von 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) erfordert, dass Sie eine physische Adresse Ihres Unternehmens und einen Abmeldelink in Ihren E-Mails angeben.

{% alert warning %}
Es liegt in Ihrer Verantwortung, sicherzustellen, dass Ihre angepasste Fußzeile die oben genannten Anforderungen erfüllt.
{% endalert %}

## Erstellen Ihrer angepassten Fußzeile {#create-your-custom-footer}

Um Ihre angepasste Fußzeile zu erstellen oder zu bearbeiten, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Präferenzen** > **Abo-Seiten und -Fußzeilen**.
2. Gehen Sie zum Abschnitt **Angepasste Fußzeile** und aktivieren Sie angepasste Fußzeilen.
3. Wählen Sie **Bearbeiten** und bearbeiten Sie dann Ihre Fußzeile im Abschnitt **Verfassen**.
4. Wählen Sie **Vorschau**, um eine Vorschau Ihrer E-Mail-Fußzeile im Posteingang einer geschäftskunden anzuzeigen. Optional können Sie **Vorschaulink kopieren** auswählen, um einen teilbaren Vorschaulink zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Der Link ist sieben Tage gültig, bevor er neu generiert werden muss.
5. Senden Sie eine Testnachricht.

![Ein Beispiel für eine angepasste Fußzeile.]({% image_buster /assets/img_archive/custom_footer.png %})

Die Standard-Fußzeile verwendet das Attribut {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} und unsere physische Postadresse. Wenn Sie diese Standard-Fußzeile verwenden, stellen Sie sicher, dass Sie **&#60;other&#62;** für das **Protokoll** auswählen.

{% alert important %}
Um die CAN-SPAM-Vorschriften einzuhalten, muss Ihre angepasste Fußzeile einen Abmeldelink enthalten. Sie können dafür das Liquid-Attribut {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} oder Ihre eigene angepasste Abmelde-URL verwenden. Sie können eine angepasste Fußzeile nicht ohne Abmeldelink speichern.
{% endalert %}

![Protokoll- und URL-Werte, die für die angepasste Fußzeile benötigt werden.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Fußzeilen ohne Abmeldelinks {#footers-without-unsubscribe-links}

Seien Sie sehr vorsichtig, wenn Sie ein Template mit der angepassten Fußzeile {% raw %}`{{${email_footer}}}` aber ohne den Abmeldelink-Tag `{{${set_user_to_unsubscribed_url}}}`{% endraw %} verwenden. Es wird eine Warnung angezeigt, aber es liegt an Ihnen, ob Sie eine E-Mail mit oder ohne Abmeldelink senden.

Hier ist eine Warnung im E-Mail-Composer:

![Beispiel einer E-Mail, die ohne Fußzeile verfasst wurde.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Hier ist eine Warnung im Campaign-Composer:

![Campaign-Erstellung ohne Fußzeile.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Einen angepassten Abmeldelink hinzufügen {#adding-a-custom-unsubscribe-link}

Um einen angepassten Abmeldelink hinzuzufügen, können Sie den Abmeldelink in der angepassten Fußzeile von {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} zu einem Link auf Ihre eigene Website mit einem Abfrageparameter ändern, der die Nutzer-ID enthält. Ein Beispiel:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Rufen Sie anschließend den [`/email/status`-Endpunkt]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) auf, um den Abo-Status der Nutzer:in zu aktualisieren. Weitere Details finden Sie in unserer Dokumentation zum [Ändern von E-Mail-Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

Speichern Sie dann diesen neuen Link. Der Standard-Braze-Abmelde-Tag {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} muss in der Fußzeile enthalten sein. Das bedeutet, dass Sie den Standardlink einbinden müssen, indem Sie ihn „verstecken“ – entweder durch Platzierung des Tags in einem Kommentar oder in einem versteckten `<div>`-Tag.

## Best Practices {#best-practices}

Wir empfehlen die folgenden Best Practices beim Erstellen und Verwenden angepasster Fußzeilen.

### Personalisierung mit Attributen {#personalizing-with-attributes}

Beim Erstellen einer angepassten Fußzeile empfiehlt Braze die Verwendung von [Attributen zur Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags). Der vollständige Satz an Standard- und angepassten Attributen ist verfügbar, aber hier sind einige, die Sie nützlich finden könnten:

| Attribut | Tag |
| --------- | --- |
| E-Mail-Adresse der Nutzer:in | {% raw %}`{{${email_address}}}`{% endraw %} |
| Angepasste Abmelde-URL der Nutzer:in | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Dieser Tag ersetzt den früheren {% raw %}`{{${unsubscribe_url}}}`{% endraw %}-Tag. Wir empfehlen, stattdessen den neueren {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}-Tag zu verwenden. |
| Angepasste Opt-in-URL der Nutzer:in | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| Angepasste Abo-URL der Nutzer:in | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| Angepasste Braze-Präferenzzentrum-URL der Nutzer:in | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalisierung mit Attributen" }

### Abmeldelink und Opt-in-Link einbinden {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
Als Best Practice empfiehlt Braze, sowohl einen Abmeldelink (wie ``{{${set_user_to_unsubscribed_url}}}``) als auch einen Opt-in-Link (wie ``{{${set_user_to_opted_in_url}}}``) in Ihre angepasste Fußzeile aufzunehmen. Auf diese Weise können sich Nutzer:innen sowohl abmelden als auch anmelden, und Sie können passiv Opt-in-Daten für einen Teil Ihrer Nutzer:innen sammeln.
{% endraw %}

### Angepasste Fußzeilen für Nur-Text-E-Mails einrichten {#setting-custom-footers-for-plaintext-emails}

Sie können auch eine angepasste Fußzeile für Nur-Text-E-Mails im Tab **Abo-Seiten und -Fußzeilen** auf der Seite **E-Mail-Präferenzen** einrichten, die denselben Regeln wie die angepasste Fußzeile für HTML-E-Mails folgt.

Wenn Sie keine Nur-Text-Fußzeile angeben, erstellt Braze automatisch eine aus der HTML-Fußzeile. Wenn Ihre angepassten Fußzeilen Ihren Vorstellungen entsprechen, wählen Sie **Speichern**.

![E-Mail mit ausgewählter Option „Angepasste Nur-Text-Fußzeile festlegen“.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## Hinweise {#considerations}


### BrazeAI Decisioning Studio™

Wenn Sie [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) verwenden, beachten Sie, dass {% raw %}`{{${email_footer}}}`{% endraw %} kein Standard-Liquid-Tag ist. Es wird vorverarbeitet, bevor Liquid ausgeführt wird. Die Verwendung von {% raw %}`{{${email_footer}}}`{% endraw %} als Wert einer Kontextvariablen und der Aufruf des `:rerender`-Flags schlägt daher stillschweigend fehl. Verwenden Sie stattdessen einen [Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers) für eine E-Mail-Fußzeile.

### Link-Templates und UTM-Parameter {#link-templates-and-utm-parameters}

Link-Templates werden bei Verwendung von {% raw %}`{{${email_footer}}}`{% endraw %} nicht automatisch an Links in angepassten E-Mail-Fußzeilen angehängt. Wenn Sie Link-Templates wie UTM-Parameter in Ihren Fußzeilen-Links benötigen, verwenden Sie stattdessen einen [Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers) oder hängen Sie die UTM-Parameter manuell an die jeweiligen Links in Ihrer angepassten Fußzeile an.