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
Die Verfügbarkeit von Landing-Pages und angepassten Domains hängt von Ihrem Braze-Paket ab. Kontaktieren Sie Ihren Account Manager oder Customer-Success-Manager, um loszulegen.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Voraussetzungen {#prerequisites}

Bevor Sie auf Landing-Pages zugreifen, diese erstellen und veröffentlichen können, benötigen Sie entweder Administrator-[Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) oder alle folgenden Berechtigungen:

- Landing-Pages anzeigen
- Landing-Page-Entwürfe bearbeiten
- Landing-Pages veröffentlichen

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Tarifoptionen {#plan-tiers}

Die Anzahl der veröffentlichten Landing-Pages, angepassten Domains und Features, die Sie nutzen können, hängt von Ihrem Tariftyp ab: kostenlos oder kostenpflichtig (inkrementell).

| Feature | Kostenloser Tarif | Kostenpflichtiger Tarif (inkrementell) |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Veröffentlichte Landing-Pages | Fünf pro Unternehmen | 20 zusätzlich |
| Angepasste Domains | Eine pro Unternehmen | Fünf zusätzlich |
| [Liquid-Personalisierung]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | Nicht verfügbar | Verfügbar |
| Vorausgefüllte Formularfelder | Nicht verfügbar | Verfügbar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tarifoptionen" }

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

### Können Landing-Pages hohe Traffic-Szenarien bewältigen? {#can-landing-pages-handle-high-traffic-scenarios}

Ja, nicht personalisierte Landing-Pages können hohe Traffic-Szenarien effektiv bewältigen. Wenn eine nicht personalisierte Landing-Page zum ersten Mal angefordert wird, wird sie von Braze über Cloudflare gecacht. Das bedeutet, dass alle nachfolgenden Anfragen für denselben Link aus dem Cache bedient werden, sodass die Performance bei hohem Anfragevolumen nicht beeinträchtigt wird. Dieser Cache ist 24 Stunden gültig, und gecachte Seitenaufrufe zählen nicht für Rate-Limits.

Für personalisierte Landing-Pages (mit Liquid-Personalisierung) gelten Rate-Limits für nicht gecachte Anfragen. Um eine optimale Performance aufrechtzuerhalten, lesen Sie [Hinweise zur Personalisierung]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations).

### Gibt es technische Anforderungen, um eine Landing-Page zu veröffentlichen? {#are-there-any-technical-requirements-to-publish-a-landing-page}

Nein, es gibt keine technischen Anforderungen.

### Gibt es einen HTML-Editor für Landing-Pages? {#is-there-an-html-editor-for-landing-pages}

Ja. Verwenden Sie den **Custom Code**-Block im Drag-and-Drop-Editor, um HTML hinzuzufügen oder zu bearbeiten.

### Kann ich einen Webhook innerhalb einer Landing-Page erstellen? {#can-i-create-a-webhook-inside-a-landing-page}

Nein, aber das Ereignis **Submitted a Landing Page form** kann als Trigger für Canvases oder Webhook-Kampagnen dienen:

- **Canvas:** Verwenden Sie das Ereignis **Submitted a Landing Page form** als Canvas-Eingangs-Trigger und fügen Sie einen Webhook-Schritt hinzu.
- **Campaign:** Verwenden Sie das Ereignis **Submitted a Landing Page form**, um basierend auf der Formularübermittlung zu triggern.

Wenn die Seite nicht über einen Braze-Kanal gesendet wird (z. B. über eine Website oder Anzeige), kann bei der Übermittlung ein neues Nutzerprofil erstellt werden – selbst wenn diese Person bereits in Braze existiert. Um dies zu handhaben, richten Sie einen Canvas ein, der durch **Submitted a Landing Page form** getriggert wird, und fügen Sie einen Braze-zu-Braze-Webhook-Schritt hinzu, der den Endpunkt [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) aufruft, um das neue Profil mit dem bestehenden zusammenzuführen.

Wenn Sie den Liquid-Tag `landing_page_url` verwenden, um die Seite zu teilen, werden Formularübermittlungen automatisch dem bestehenden Nutzerprofil zugeordnet. Sie können dann die auf der Landing-Page übermittelten Nutzerattribute über Liquid für nachfolgendes Templating referenzieren.