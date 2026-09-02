---
nav_title: Landing-Pages
article_title: Landing-Pages
page_order: 8
guide_top_header: "Landing-Pages"
description: "Dieser Artikel enthält Ressourcen zum Erstellen und Anpassen von Braze Landing-Pages."
alias: /landing_pages/
---

# Über Landing-Pages {#about-landing-pages}

> Braze Landing-Pages sind eigenständige Webseiten, die Ihre Strategie zur Nutzer:innen-Gewinnung und zum Engagement unterstützen können.

Nutzen Sie Landing-Pages, um Ihre Zielgruppe zu vergrößern, Nutzerdaten zu erfassen, Sonderangebote zu bewerben und Multichannel-Kampagnen zu unterstützen. Eine Referenz der Drag-and-Drop-Blöcke für Landing-Pages finden Sie unter [Editor-Blöcke (Landing-Pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

{% alert note %}
Die Verfügbarkeit von Landing-Pages und angepassten Domains hängt von Ihrem Braze-Paket ab. Kontaktieren Sie Ihren Account Manager:in oder CSM or Customer-Success-Manager or Customer-Success-Manager:in, um loszulegen.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Voraussetzungen {#prerequisites}

Bevor Sie auf Landing-Pages zugreifen, diese erstellen und veröffentlichen können, benötigen Sie entweder [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) als Administrator:in oder alle folgenden Berechtigungen:

- Landing-Pages anzeigen
- Landing-Page-Entwürfe bearbeiten
- Landing-Pages veröffentlichen

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Planstufen {#plan-tiers}

Die Anzahl der veröffentlichten Landing-Pages, angepassten Domains und Features, die Sie nutzen können, hängt von Ihrem Plantyp ab: Free oder Pro (inkrementell).

| Feature                                                                                                   | Free-Stufe     | Pro-Stufe (inkrementell)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Veröffentlichte Landing-Pages                                                                 | Fünf pro Unternehmen | 20 zusätzlich |
| Angepasste Domains          | Eine pro Unternehmen | Fünf zusätzlich |
| [Liquid-Personalisierung]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | Nicht verfügbar | Verfügbar |
| Vorausgefüllte Formularfelder | Nicht verfügbar | Verfügbar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Planstufen" }

## Rate-Limits {#rate-limits}

Braze wendet ein Rate-Limit von 500 Anfragen pro drei Sekunden (ca. 167 Anfragen pro Sekunde) pro Workspace für nicht zwischengespeicherte Landing-Pages an. Dieses Limit trägt dazu bei, die Systemleistung und Zuverlässigkeit während Zeiten mit hohem Datenverkehr aufrechtzuerhalten.

Zwischengespeicherte Landing-Page-Aufrufe werden nicht auf dieses Limit angerechnet. Informationen dazu, wie Caching den Datenverkehr beeinflusst, finden Sie unter [Können Landing-Pages Szenarien mit hohem Datenverkehr bewältigen?](#can-landing-pages-handle-high-traffic-scenarios).

## Google Tag Manager:in zu einer Landing-Page hinzufügen {#adding-google-tag-manager-to-a-landing-page}

Um Google Tag Manager:in zu Ihren Landing-Pages hinzuzufügen, fügen Sie im Drag-and-Drop-Editor einen **Custom Code**-Block zu Ihrer Landing-Page hinzu und setzen Sie dann den Tag Manager:in-Code in den Block ein. Stellen Sie sicher, dass Sie vor dem Tag Manager:in-Code einen Data Layer hinzufügen, wie in diesem Beispiel:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Weitere Informationen zur Implementierung von Google Tag Manager:in finden Sie in der [Dokumentation von Google](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie groß darf eine Landing-Page maximal sein? {#whats-the-maximum-size-for-landing-pages}

Die maximale Größe des Landing-Page-Bodys beträgt 500 KB.

### Können Landing-Pages hohe Traffic-Szenarien bewältigen? {#can-landing-pages-handle-high-traffic-scenarios}

Ja. Nicht personalisierte Landing-Pages bewältigen hohe Traffic-Szenarien effektiv. Wenn eine Landing-Page zum ersten Mal angefordert wird, wird sie von Braze über Cloudflare zwischengespeichert. Nachfolgende Anfragen für denselben Link werden aus dem Cache bedient, was in Zeiten mit hohem Traffic hilfreich ist. Dieser Cache gilt 24 Stunden, und zwischengespeicherte Seitenaufrufe werden nicht auf die [Rate-Limits](#rate-limits) angerechnet.

Personalisierte Landing-Pages verwenden einen kürzeren Cloudflare-Cache und erzeugen mehr nicht zwischengespeicherte Anfragen an Braze. Diese nicht zwischengespeicherten Anfragen unterliegen dem pro Workspace geltenden Rate-Limit, das unter [Rate-Limits](#rate-limits) beschrieben ist.

Informationen zu Größenlimits und weiteren Performance-Empfehlungen für personalisierte Seiten finden Sie unter [Überlegungen zur Personalisierung]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations).

### Gibt es technische Voraussetzungen, um eine Landing-Page zu veröffentlichen? {#are-there-any-technical-requirements-to-publish-a-landing-page}

Nein, es gibt keine technischen Voraussetzungen.

### Gibt es einen HTML-Editor für Landing-Pages? {#is-there-an-html-editor-for-landing-pages}

Ja. Verwenden Sie den **Custom Code**-Block im Drag-and-Drop-Editor, um HTML hinzuzufügen oder zu bearbeiten. Informationen zur Anbindung an das Braze SDK or Software-Development-Kit aus Ihrem angepassten Code finden Sie unter [JavaScript-Bridge für Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge). Um eine vollständig angepasste UI mit einem Landing-Page-Formular zu verbinden, lesen Sie [Angepasste Formularblöcke erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks).

### Kann ich iframes auf Landing-Pages verwenden? {#can-i-use-iframes-on-landing-pages}

Ja. Fügen Sie einen **Custom Code**-Block im Drag-and-Drop-Editor hinzu und ergänzen Sie ein iframe-Element mit der URL des Inhalts, den Sie einbetten möchten.

Wenn die eingebettete Website das Framing über `frame-ancestors` in ihrer Content Security Policy (CSP) oder `X-Frame-Options` einschränkt, wird die Seite möglicherweise nicht im iframe geladen. Braze kann diese Einstellungen nicht überschreiben – die eingebettete Website muss so konfiguriert sein, dass Ihre Landing-Page-Domain zugelassen wird.

### Kann ich einen Webhook innerhalb einer Landing-Page erstellen? {#can-i-create-a-webhook-inside-a-landing-page}

Nein, aber das Ereignis **Submitted a Landing Page form** kann als Trigger or triggern für Canvase oder Webhook-Campaigns dienen:

- **Canvas:** Verwenden Sie das Ereignis **Submitted a Landing Page form** als Canvas-Entry-Trigger or triggern und fügen Sie einen Webhook-Schritt hinzu.
- **Campaign:** Verwenden Sie das Ereignis **Submitted a Landing Page form**, um basierend auf der Formularübermittlung zu Trigger or triggern or triggern.

Wenn die Seite nicht über einen Braze-Kanal gesendet wird (z. B. über eine Website oder Anzeige), kann bei der Übermittlung ein neues Kundenprofil or Nutzerprofil erstellt werden – auch wenn diese Person bereits in Braze existiert. Um dies zu handhaben, richten Sie ein Canvas ein, das durch **Submitted a Landing Page form** getriggert wird, und fügen Sie einen Braze-to-Braze-Webhook-Schritt hinzu, der den Endpunkt [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) aufruft, um das neue Profil mit dem bestehenden zusammenzuführen.

Wenn Sie den Liquid-Tag `landing_page_url` verwenden, um die Seite zu teilen, werden Formularübermittlungen automatisch dem bestehenden Kundenprofil or Nutzerprofil zugeordnet. Sie können dann die auf der Landing-Page übermittelten Nutzerattribute über Liquid für nachfolgendes Templating referenzieren.