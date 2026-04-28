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

Nutzen Sie Landing-Pages, um Ihre Zielgruppe zu vergrößern, Nutzerdaten zu erfassen, Sonderangebote zu bewerben und Multichannel-Kampagnen zu unterstützen.

{% alert note %}
Die Verfügbarkeit von Landing-Pages und benutzerdefinierten Domains hängt von Ihrem Braze-Paket ab. Kontaktieren Sie Ihren Account Manager oder Customer-Success-Manager, um loszulegen.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Voraussetzungen {#prerequisites}

Bevor Sie auf Landing-Pages zugreifen, diese erstellen und veröffentlichen können, benötigen Sie entweder Administrator-[Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) oder alle folgenden Berechtigungen:

- Landing-Pages anzeigen
- Landing-Page-Entwürfe bearbeiten
- Landing-Pages veröffentlichen

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Tarifoptionen {#plan-tiers}

Die Anzahl der veröffentlichten Landing-Pages und benutzerdefinierten Domains, die Sie nutzen können, hängt von Ihrem Tariftyp ab: kostenlos oder kostenpflichtig (inkrementell).

| Feature                                                                                                   | Kostenloser Tarif     | Kostenpflichtiger Tarif (inkrementell)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Veröffentlichte Landing-Pages                                                                 | Fünf pro Unternehmen | 20 zusätzlich |
| Benutzerdefinierte Domains          | Eine pro Unternehmen | Fünf zusätzlich |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Google Tag Manager zu einer Landing-Page hinzufügen {#adding-google-tag-manager-to-a-landing-page}

Um Google Tag Manager zu Ihren Landing-Pages hinzuzufügen, fügen Sie einen **Custom Code**-Block zu Ihrer Landing-Page im Drag-and-Drop-Editor hinzu und fügen Sie dann den Tag-Manager-Code in den Block ein. Stellen Sie sicher, dass Sie vor dem Tag-Manager-Code einen Data Layer hinzufügen, wie in diesem Beispiel:

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

Weitere Informationen zur Implementierung von Google Tag Manager finden Sie in der [Dokumentation von Google](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie groß darf eine Landing-Page maximal sein? {#whats-the-maximum-size-for-landing-pages}

Die Größe des Landing-Page-Bodys kann bis zu 500 KB betragen.

### Gibt es technische Anforderungen, um eine Landing-Page zu veröffentlichen? {#are-there-any-technical-requirements-to-publish-a-landing-page}

Nein, es gibt keine technischen Anforderungen.

### Gibt es einen HTML-Editor für Landing-Pages? {#is-there-an-html-editor-for-landing-pages}

Ja. Verwenden Sie den **Custom Code**-Block im Drag-and-Drop-Editor, um HTML hinzuzufügen oder zu bearbeiten.

### Kann ich einen Webhook innerhalb einer Landing-Page erstellen? {#can-i-create-a-webhook-inside-a-landing-page}

Nein, das wird derzeit nicht unterstützt.