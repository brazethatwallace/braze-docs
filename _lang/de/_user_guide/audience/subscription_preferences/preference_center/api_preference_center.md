---
nav_title: API-E-Mail-Präferenzzentrum
article_title: API-E-Mail-Präferenzzentrum
page_order: 1
description: "Dieser Artikel beschreibt das API-E-Mail-Präferenzzentrum und wie Sie es anpassen können."
channel:
  - email
---

# API-E-Mail-Präferenzzentrum {#api-email-preference-center}

> Die Einrichtung eines Präferenzzentrums bietet Ihren Nutzer:innen eine zentrale Anlaufstelle, um ihre Benachrichtigungspräferenzen für Ihr [E-Mail-Messaging]({{site.baseurl}}/user_guide/channels/email) zu bearbeiten und zu verwalten. Dieser Artikel enthält Schritte zum Erstellen eines API-generierten Präferenzzentrums, aber Sie können ein Präferenzzentrum auch mit dem [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center) erstellen.

Gehen Sie im Braze-Dashboard zu **Audience** > **Email Preference Centers**.

Hier können Sie jede Abo-Gruppe verwalten und anzeigen. Jede von Ihnen erstellte Abo-Gruppe wird dieser Präferenzzentrum-Liste hinzugefügt. Sie können mehrere Präferenzzentren erstellen.

{% alert important %}
Das Präferenzzentrum ist für die Verwendung innerhalb des Braze-E-Mail-Kanals vorgesehen. Die Links zum Präferenzzentrum sind dynamisch und basieren auf den einzelnen Nutzer:innen und können nicht extern gehostet werden.
{% endalert %}

## Ein Präferenzzentrum mit API erstellen {#create-a-preference-center-with-api}

Mithilfe der [Braze-Endpunkte für Präferenzzentren]({{site.baseurl}}/api/endpoints/preference_center) können Sie ein Präferenzzentrum erstellen – eine von Braze gehostete Website, die den Abo-Status und die Abo-Gruppenstatusangaben Ihrer Nutzer:innen anzeigen kann. Mit HTML und CSS kann Ihr Entwickler:innen-Team das Präferenzzentrum so gestalten, dass das Styling der Seite Ihren Markenrichtlinien entspricht.

Durch die Verwendung von Liquid können Sie die Namen Ihrer Abo-Gruppen und den Status jeder/jedes Nutzer:in abrufen. Auf diese Weise speichert und ruft Braze diese Daten ab, wenn die Seite geladen wird.

### Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Aktiviertes Präferenzzentrum | Ihr Braze-Dashboard verfügt über die Berechtigungen zur Nutzung des Präferenzzentrum-Features. |
| Gültiger Workspace mit einer E-Mail-, SMS- oder WhatsApp-Abo-Gruppe | Ein funktionierender Workspace mit gültigen Nutzer:innen und einer E-Mail-, SMS- oder WhatsApp-Abo-Gruppe. |
| Gültige:r Nutzer:in | Ein:e Nutzer:in mit einer E-Mail-Adresse und einer externen ID. |
| Generierter API-Schlüssel mit Präferenzzentrum-Berechtigungen | Gehen Sie im Braze-Dashboard zu **Einstellungen** > **API-Schlüssel**, um zu bestätigen, dass Sie Zugriff auf einen API-Schlüssel mit Präferenzzentrum-Berechtigungen haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

### 1. Schritt: Den Endpunkt „Präferenzzentrum erstellen“ verwenden {#step-1-use-the-create-preference-center-endpoint}

Beginnen wir mit dem Erstellen eines Präferenzzentrums mithilfe des [Endpunkts „Präferenzzentrum erstellen“]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center). Um Ihr Präferenzzentrum anzupassen, können Sie HTML, das zu Ihrem Branding passt, in das Feld `preference_center_page_html` und das Feld `confirmation_page_html` einfügen.

Der [Endpunkt „Präferenzzentrum-URL generieren“]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) ermöglicht es Ihnen, die Präferenzzentrum-URL für eine:n bestimmte:n Nutzer:in außerhalb einer über Braze gesendeten E-Mail abzurufen.

{% alert note %}
Braze rendert `confirmation_page_html` in einem iframe, der eine `data:`-URL verwendet. Browser behandeln `data:`-URLs als opake Ursprünge. Daher können Skripte in diesem iframe keine zusätzlichen externen Ressourcen laden, und das Navigieren des übergeordneten Fensters oder die Kommunikation über Frames von dieser Seite aus schlägt fehl.<br><br>Stattdessen können Sie auf externe Inhalte verlinken, z. B. eine gehostete Umfrage-URL, anstatt Skripte einzubetten. Wenn Sie ein Drittanbieter-Tool einbetten müssen und der Anbieter dies erlaubt, verwenden Sie ein `<iframe title="Beschreibung des eingebetteten Inhalts" src="https://example.com/...">`, das auf die gehostete HTTPS-URL des Tools verweist.
{% endalert %}

### 2. Schritt: In Ihre E-Mail-Kampagne einbinden {#step-2-include-in-your-email-campaign}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Um einen Link zum Präferenzzentrum in Ihren E-Mails zu platzieren, verwenden Sie den folgenden Liquid-Tag an der gewünschten Stelle in Ihrer E-Mail, ähnlich wie Sie Abmelde-URLs einfügen würden.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Sie können auch eine Kombination aus HTML mit Liquid verwenden. Zum Beispiel können Sie Folgendes als URL entweder im HTML-Editor oder im Drag-and-Drop-Editor einfügen. Dies zeigt das grundlegende Präferenzzentrum-Layout, das alle E-Mail-Abo-Gruppen automatisch auflistet. Wenn Sie [Link Aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) verwenden, fügen Sie ein nachgestelltes Fragezeichen (`?`) nach dem Liquid-Tag hinzu, damit Braze Tracking-Parameter anhängen kann.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

Das Präferenzzentrum verfügt über ein Kontrollkästchen, mit dem Ihre Nutzer:innen sich von allen E-Mails abmelden können. Beachten Sie, dass diese Präferenzen nicht gespeichert werden können, wenn sie als Testnachricht gesendet werden.

{% alert important %}
Der obige Liquid-Tag funktioniert nur beim Starten einer Kampagne oder eines Canvas. Das Senden einer Test-E-Mail erzeugt keinen gültigen Link. Um den Präferenzzentrum-Link zu überprüfen, starten Sie die Nachricht in einer Kampagne, die nur auf Ihr Testprofil ausgerichtet ist.
{% endalert %}

#### Ein Präferenzzentrum bearbeiten {#edit-a-preference-center}

Sie können Ihr Präferenzzentrum mithilfe des [Endpunkts „Präferenzzentrum aktualisieren“]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) bearbeiten und aktualisieren.

#### Präferenzzentren und Details identifizieren {#identify-preference-centers-and-details}

Um Ihre Präferenzzentren zu identifizieren, verwenden Sie den [Endpunkt „Details für Präferenzzentrum anzeigen“]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center), um zugehörige Informationen wie den Zeitstempel der letzten Aktualisierung, die Präferenzzentrum-ID und mehr abzurufen.

## Ein Präferenzzentrum anpassen {#customize-a-preference-center}

Braze verwaltet die Abo-Status-Updates aus dem Präferenzzentrum, wodurch das Präferenzzentrum synchron bleibt. Sie können jedoch auch Ihr eigenes Präferenzzentrum erstellen und hosten, indem Sie die [Abo-Gruppen-APIs]({{site.baseurl}}/api/endpoints/subscription_groups) mit den folgenden Optionen verwenden.

### Option 1: Link mit String-Abfrageparametern {#option-1-link-with-string-query-parameters}

Verwenden Sie Abfragestring-Feld-Wert-Paare im Body der URL, um die Nutzer-ID und die E-Mail-Kategorie an die Seite zu übergeben, sodass Nutzer:innen nur ihre Abmeldung bestätigen müssen. Diese Option eignet sich für diejenigen, die einen Nutzer-Bezeichner in einem gehashten Format speichern und noch kein Abo-Zentrum haben.

Für diese Option benötigt jede E-Mail-Kategorie ihren eigenen spezifischen Abmelde-Link:<br>
`http://mycompany.com/query-string-form-fill?field_id=Alex&field_category=offers`

{% alert tip %}
Es ist auch möglich, die externe ID der/des Nutzer:in zum Zeitpunkt des Versands mithilfe eines Liquid-Filters zu hashen. Dies konvertiert die `user_id` in einen MD5-Hash-Wert, zum Beispiel:
{% raw %}
```liquid
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Option 2: Mit JSON Web Token authentifizieren {#option-2-authenticate-with-json-web-token}

Verwenden Sie ein [JSON Web Token](https://auth0.com/learn/json-web-tokens/), um Nutzer:innen bei einem Teil Ihres Webservers zu authentifizieren (z. B. Kontopräferenzen), der normalerweise hinter einer Authentifizierungsschicht wie Benutzername und Passwort liegt.

Dieser Ansatz erfordert keine in die URL eingebetteten Abfragestring-Wert-Paare, da diese im Payload des JSON Web Tokens übergeben werden können, zum Beispiel:

```json
{
    "user_id": "1234567890",
    "name": "Alex Smith",
    "category": "offers"
}
```

## Häufig gestellte Fragen {#frequently-asked-questions}

### Ich habe kein Präferenzzentrum erstellt. Warum sehe ich „PreferenceCenterBrazeDefault“ in meinem Dashboard? {#i-havent-created-a-preference-center-why-am-i-seeing-preferencecenterbrazedefault-on-my-dashboard}

Dies wird verwendet, um das Präferenzzentrum zu rendern, wenn das Legacy-Liquid {%raw%}`${preference_center_url}`{%endraw%} verwendet wird. Das bedeutet, dass Canvas-Schritte oder Templates, die entweder {%raw%}`${preference_center_url}` oder `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} referenzieren, nicht funktionieren. Dies gilt auch für zuvor gesendete Nachrichten, die das Legacy-Liquid oder „PreferenceCenterBrazeDefault“ als Teil der Nachricht enthielten.

Wenn Sie {%raw%}`${preference_center_url}`{%endraw%} in einer neuen Nachricht erneut referenzieren, wird ein Präferenzzentrum mit dem Namen „PreferenceCenterBrazeDefault“ erneut erstellt.

### Unterstützen Präferenzzentren mehrere Sprachen? {#do-preference-centers-support-multiple-languages}

Nein. Sie können jedoch Liquid nutzen, wenn Sie das HTML für benutzerdefinierte Opt-in- und Opt-out-Seiten schreiben. Wenn Sie dynamische Links zur Verwaltung von Abmeldungen verwenden, handelt es sich um einen einzelnen Link.

Wenn Sie beispielsweise die Abmeldungsrate für spanischsprachige Nutzer:innen verfolgen, müssten Sie entweder separate Kampagnen verwenden oder Analytics rund um Currents nutzen (z. B. prüfen, wann sich ein:e Nutzer:in abmeldet, und die bevorzugte Sprache dieser/dieses Nutzer:in überprüfen).

Als weiteres Beispiel könnten Sie für das Tracking der Abmeldungsraten für spanischsprachige Nutzer:innen einen Abfrageparameter-String wie `?Spanish=true` zur Abmelde-URL hinzufügen, wenn die Sprache der/des Nutzer:in Spanisch ist, und andernfalls einen regulären Abmelde-Link verwenden:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Dann könnten Sie über Currents identifizieren, welche Nutzer:innen Spanisch sprechen und wie viele Klick-Ereignisse es für diesen Abmelde-Link gab.

### Sind sowohl Abmelde-Links als auch E-Mail-Präferenzzentren für den Versand erforderlich? {#are-both-unsubscribe-links-and-email-preference-centers-required-for-sending}

Nein. Wenn Sie beim Erstellen einer E-Mail-Kampagne die Meldung „Your Email Body does not include an unsubscribe link“ sehen, ist diese Warnung zu erwarten, wenn sich Ihr Abmelde-Link in einem Content-Block befindet.

### Wie aktualisiere ich das Standard-Browser-Symbol? {#how-do-i-update-the-default-browser-icon}

Standardmäßig verwendet das Symbol neben dem Browser-Tab-Namen (Favicon) das Braze-Logo. Um ein benutzerdefiniertes Favicon hinzuzufügen, legen Sie es über das Attribut `links-tags` in Ihrem API-Aufruf zum Erstellen oder Aktualisieren des [Präferenzzentrums]({{site.baseurl}}/api/endpoints/preference_center) fest. Braze fügt dann den {% raw %}`<link rel="icon" ...>`{% endraw %}-Tag in die gehostete Seite für Sie ein.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}