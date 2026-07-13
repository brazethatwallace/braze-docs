---
nav_title: Nutzer:innen tracken
article_title: Nutzer:innen über ein Formular tracken
description: "Erfahren Sie, wie Sie Nutzer:innen identifizieren, die ein Formular über Ihre Landing-Page absenden, indem Sie Ihren Nachrichten einen Liquid-Tag hinzufügen."
page_order: 2
---

# Nutzer:innen über ein Formular tracken {#track-users-through-a-form}

> Erfahren Sie, wie Sie Nutzer:innen tracken, die ein Formular über Ihre Landing-Page absenden, indem Sie Ihren Nachrichten einen Landing-Page-Liquid-Tag hinzufügen. Dieser Liquid-Tag wird über alle Braze-Messaging-Kanäle hinweg unterstützt, einschließlich E-Mail, SMS, In-App Messages und mehr. Weitere Informationen zum Tracking von Daten finden Sie unter [Über Landing-Page-Tracking-Daten]({{site.baseurl}}/user_guide/messaging/landing_pages/about_tracking_data).

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, müssen Sie eine [Landing-Page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) und eine [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) erstellen.

## So funktioniert es {#how-it-works}

Sie können einen {% raw %}`{% landing_page_url %}`{% endraw %}-Liquid-Tag zu jeder Ihrer Einzel- oder Multi-Channel-Nachrichten in Braze hinzufügen. Wenn Nutzer:innen diese Landing-Page besuchen und das Formular absenden, verknüpft Braze diese Daten automatisch mit dem bestehenden Profil, anstatt ein neues Profil zu erstellen. Im folgenden Beispiel wird der Landing-Page-Liquid-Tag verwendet, um Kund:innen mit einer Umfrage zu verknüpfen:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Sie können Landing-Pages auch zur Lead-Generierung nutzen, indem Sie die Seiten-URL in Ihre externen Kanäle einbetten. Nachdem Sie eine Landing-Page erstellt haben, gehen Sie zu **Landing Page Details**, um die eindeutige URL für Ihre Landing-Page zu erhalten.
{% endalert %}

## Landing-Page-Liquid-Tags verwenden {#using-landing-page-liquid-tags}

### 1. Schritt: Seiten-URL überprüfen {#page-url}

Braze verwendet die URL Ihrer Landing-Page, um den eindeutigen Liquid-Tag zu generieren. Wenn Sie die aktuelle Seiten-URL ändern möchten, gehen Sie zu **Messaging** > **Landing Pages** und öffnen Sie Ihre Landing-Page. Unter **Page URL** können Sie eine neue Seiten-URL eingeben.

{% alert warning %}
Wenn Sie die Seiten-URL nach dem Senden Ihrer Nachricht ändern, werden Nutzer:innen, die versuchen, Ihre Landing-Page über die alte URL zu besuchen, auf eine `404`-Seite weitergeleitet.
{% endalert %}

![Eine beispielhafte Seiten-URL für eine Landing-Page in Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### 2. Schritt: Liquid-Tag generieren {#step-2-generate-the-liquid-tag}

Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie eine Campaign aus. Wählen Sie in Ihrem Nachrichten-Editor **Personalization** aus.

![Der Button „Add personalization“ im Drag-and-Drop-Editor.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze generiert automatisch einen Liquid-Tag unter Verwendung Ihrer [Landing-Page-URL](#page-url). Verwenden Sie die folgende Tabelle, um Ihren Tag zu generieren:

| **Personalisierungstyp** | Wählen Sie **Landing Page** aus. |
| **Landing-Page** | Wählen Sie die Landing-Page aus, die Sie [zuvor erstellt haben](#prerequisites). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2. Schritt: Liquid-Tag generieren" }

Um den Liquid-Tag zu Ihrer Nachricht hinzuzufügen, können Sie entweder **Einfügen** auswählen oder das Snippet in Ihre Zwischenablage kopieren und manuell hinzufügen.

![Ein automatisch generierter Liquid-Tag für die ausgewählte Landing-Page.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Ihr Snippet sieht in etwa so aus:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### 3. Schritt: Nachricht fertigstellen und senden {#step-3-finalize-and-send-your-message}

Betten Sie das Liquid-Snippet in Ihre Nachricht ein und stellen Sie den Rest Ihrer Nachricht fertig. Zum Beispiel:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Wenn Sie bereit sind, können Sie die Nachricht senden, um Nutzer:innen über Ihre Landing-Page zu tracken.