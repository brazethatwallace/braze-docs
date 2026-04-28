---
nav_title: FAQ
article_title: FAQ zu E-Mail- und Link-Templates
page_order: 10

page_type: FAQ
description: "Diese Seite behandelt häufig gestellte Fragen zu E-Mail-Templates und Link-Templates."
tool:
  - Templates
channel: email

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Diese Seite enthält Antworten auf einige häufig gestellte Fragen zu E-Mail-Templates und Link-Templates.

## E-Mail-Templates {#email-templates}

### Kann ich einen „Diese E-Mail im Browser anzeigen“-Link zu meinen E-Mails hinzufügen? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Nein, Braze bietet diese Funktionalität nicht an. Der Grund dafür ist, dass eine zunehmende Mehrheit der E-Mails auf Mobilgeräten und in modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte problemlos darstellen.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing-Page (z. B. Ihrer Website) hosten, die dann über das **Link**-Tool beim Bearbeiten des E-Mail-Textes aus der E-Mail-Campaign heraus verlinkt werden kann.

### Wie erstelle ich einen angepassten Abmeldelink für meine E-Mail-Templates? {#how-do-i-create-a-custom-unsubscribe-link-for-my-email-templates}

Es gibt eine Weiterleitungsoption für die Abmeldeseite.

Sie könnten den Abmeldelink in der angepassten Fußzeile von {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} zu einem Link auf Ihre eigene Website mit einem Abfrageparameter ändern, der die Nutzer-ID enthält. Ein Beispiel:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Anschließend könnten Sie den [`/email/status`-Endpunkt]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) aufrufen, um den Abo-Status der/des Nutzer:in zu aktualisieren. Weitere Details finden Sie in unserer Dokumentation zum [Ändern des E-Mail-Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions/#changing-email-subscriptions).

Um diesen neuen Link zu speichern, muss das Standard-Braze-Abmelde-Tag {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} in der Fußzeile vorhanden sein. Das bedeutet, dass Sie den Standardlink einbinden müssen, indem Sie ihn „verstecken“ – entweder indem Sie das Tag in einen Kommentar oder in ein verstecktes `<div>`-Tag setzen.

- **Tag-in-Kommentar-Beispiel:** Tag in Kommentar setzen: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Kommentar in verstecktem `<div>`-Tag-Beispiel:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### Was passiert, wenn ich ein E-Mail-Template bearbeite, das derzeit in einer Campaign verwendet wird? {#what-happens-if-i-edit-an-email-template-that-is-currently-being-used-in-a-campaign}

Änderungen an einem bestehenden Template werden nicht in Campaigns übernommen, die mit früheren Versionen dieses Templates erstellt wurden. Bei API-Campaigns, die ein Template im REST-API-Body verwenden, nutzt Braze zum Sendezeitpunkt die neueste Version des Templates.

## Link-Templates

### Kann ich mehrere Link-Templates in meine E-Mail einfügen? {#can-i-upload-multiple-link-templates-to-my-email}

Ja, Sie können beliebig viele Templates in Ihre E-Mail-Nachrichten einfügen. Als Best Practice sollten Sie Ihre E-Mails testen, um sicherzustellen, dass die Links nicht mehr als 2.000 Zeichen umfassen, da die meisten Browser die Links kürzen oder abschneiden.

### Wie kann ich eine Vorschau meiner Links mit allen angewendeten Tags anzeigen? {#how-do-i-preview-my-links-with-all-of-the-tags-applied}

Es gibt mehrere Möglichkeiten, eine Vorschau Ihrer Links anzuzeigen. Nachdem Sie das [Link-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template/) angewendet haben, können Sie eine [Test-E-Mail]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) an sich selbst senden, um alle Links anzuzeigen.

Im Vorschaufenster in einem neuen Tab können Sie auch die Links öffnen, um sie anzuzeigen. Sie können auch mit der Maus über die Links im Vorschaufenster fahren und sie am unteren Rand Ihres Browsers sehen.

### Wie funktioniert Link-Templating mit Liquid? {#how-does-link-templating-work-with-liquid}

Link-Templates werden erweitert und vor jeder Liquid-Erweiterung zu jeder URL hinzugefügt. Wenn ein Teil Ihrer URL mithilfe eines Liquid-Snippets generiert wird, empfehlen wir, die Basis-URL und das Fragezeichen (?) fest zu codieren, damit Link-Templates korrekt erweitert werden.

Vermeiden Sie es, das Fragezeichen (?) zu Ihrem Liquid hinzuzufügen, da dies dazu führt, dass Link-Templates zuerst ein Fragezeichen (?) hinzufügen und dann der Liquid-Erweiterungsprozess ein zweites Fragezeichen (?) hinzufügt.

## Link Aliasing

### Wie wirkt sich die Aktivierung von Link Aliasing auf meine Content Blocks und Link-Templates aus? {#how-will-enabling-link-aliasing-impact-my-content-blocks-and-link-templates}

Für alle neu erstellten Content Blocks wird Link Aliasing workspace-übergreifend angewendet, da es sich um ein Feature auf Unternehmensebene handelt.

Bestehende Content Blocks werden bei der Aktivierung von Link Aliasing nicht geändert. Bestehende Link-Templates werden zwar nicht geändert, aber der bestehende Link-Template-Abschnitt in einer Nachricht wird entfernt. Weitere Informationen finden Sie unter [Link Aliasing in Content Blocks]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/#link-aliasing-in-content-blocks).

### Kann ich bedingte Liquid-Logik vollständig innerhalb eines HTML-Anchor-Tags verwenden? {#can-i-use-liquid-conditional-logic-entirely-within-an-html-anchor-tag}

Nein, Braze Link Aliasing erkennt das HTML nicht korrekt.

Wenn solche Logik zusammen mit Features verwendet wird, die das HTML parsen müssen (wie ein Preheader oder Link-Templating), kann die zum Scannen des HTML verwendete Bibliothek das Anchor-Tag so verändern, dass das korrekte `href` nicht richtig als Template eingefügt wird. Die Bibliothek stellt dann fest, dass das HTML ungültig ist, da sie den Liquid-Code nicht berücksichtigt.

Verwenden Sie stattdessen Liquid-Logik, die in jeder Phase ein vollständiges Anchor-Tag enthält. Dies beeinträchtigt das HTML-Parsing nicht, da die Logik mehrere Instanzen von gültigem HTML enthält. Sie können Ihre Logik auch vereinfachen, indem Sie eine Variable zuweisen und diese dann als Template in das entsprechende Anchor-Tag einfügen.