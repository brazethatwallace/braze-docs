---
nav_title: Aktions- und Medien-URLs
article_title: Aktions- und Medien-URLs mit Liquid personalisieren
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie Aktions- und Medien-URLs mit Liquid personalisieren können."
---

# Aktions- und Medien-URLs mit Liquid personalisieren {#personalize-action-and-media-urls-with-liquid}

> Personalisieren Sie Linkziele und Inhalte für alle Nutzer:innen, die Ihre Nachricht erhalten, indem Sie Liquid-Variablen zu den URLs für Buttons, Links, Bilder und Videos hinzufügen.

## Deeplink zu In-App-Inhalten {#deep-link-to-in-app-content}

{% alert tip %}
**Für Entwickler:innen:** Integrationsanweisungen finden Sie unter [Android-Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=android) oder [Swift-Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Hilfe bei der Auswahl eines iOS-Linktyps finden Sie im [iOS-Deeplinking-Leitfaden]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Zur Diagnose von Problemen siehe [Fehlerbehebung bei Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

### Was ist Deeplinking? {#what-is-deep-linking}

Deeplinking ist eine Methode, eine native App zu starten und ihr zusätzliche Informationen zu übergeben, damit sie eine bestimmte Aktion ausführt oder bestimmte Inhalte anzeigt.

Dies besteht aus drei Teilen:

1. Identifizieren, welche App gestartet werden soll.
2. Die App anweisen, welche Aktion ausgeführt werden soll.
3. Der Aktion alle zusätzlichen Daten bereitstellen, die sie benötigt.

Deeplinks sind benutzerdefinierte URIs, die auf einen bestimmten Teil der App verweisen und alle drei dieser Teile enthalten. Der Schlüssel liegt in der Definition eines benutzerdefinierten Schemas. `http:` ist das Schema, mit dem fast alle vertraut sind, aber Schemata können mit jedem Wort beginnen. Ein Schema muss mit einem Buchstaben beginnen, kann dann aber Buchstaben, Zahlen, Pluszeichen, Minuszeichen oder Punkte enthalten. Da es praktisch kein zentrales Register gibt, um Konflikte zu vermeiden, ist es eine Best Practice, Ihren Domainnamen in das Schema aufzunehmen. Zum Beispiel ist `twitter://` der iOS-URI zum Starten der mobilen App für X, ehemals Twitter.

Alles nach dem Doppelpunkt innerhalb eines Deeplinks ist Freitext. Es liegt an Ihnen, dessen Struktur und Interpretation zu definieren; eine gängige Konvention ist jedoch, ihn nach dem Vorbild von `http:`-URLs zu modellieren, einschließlich eines führenden `//` und Abfrageparametern (zum Beispiel `?foo=1&bar=2`). Für das vorherige Beispiel würde `twitter://user?screen_name=[id]` verwendet, um ein bestimmtes Profil in der App zu starten.

{% alert important %}
Für Apps, die mit Wrapper-Frameworks erstellt wurden (zum Beispiel Flutter oder Cordova), bietet Braze keine Wrapper-spezifische Deeplinking-Unterstützung. Sie müssen Deeplinks auf den nativen iOS- und Android-Ebenen konfigurieren. Für Cordova siehe [Deeplinking in Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
{% endalert %}

### System-URI-Schemata {#system-uri-schemes}

Standard-URI-Schemata, die nativ von iOS und Android verarbeitet werden (wie `tel:`, `mailto:` und `sms:`), können direkt in das Deeplink-URL-Feld eingegeben werden, ohne dass eine benutzerdefinierte Deeplink-Integration in Ihrer App erforderlich ist.

| Schema | Beispiel | Aktion |
| ------ | ------- | ------ |
| `tel:` | `tel:+18005555555` | Öffnet die Telefon-Wähltastatur |
| `mailto:` | `mailto:support@example.com` | Öffnet die E-Mail-Erstellung |
| `sms:` | `sms:+18005555555` | Öffnet die SMS-Erstellung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="System-URI-Schemata"}

Diese funktionieren für das Klickverhalten von Push-Benachrichtigungen und Button-Aktionen in In-App-Nachrichten. Es sind keine zusätzlichen SDK-Konfigurationen oder App-Code-Änderungen erforderlich.

### Deeplink in die Anwendung {#deep-link-into-application}

Beim Erstellen von Push-Benachrichtigungen, In-App-Nachrichten, Bannern oder Content Cards wählen Sie **Deeplink into application**, um einen bestimmten Bildschirm oder eine bestimmte Aktion in Ihrer App zu öffnen. In einigen Composern erscheint diese Option als **Deep Link Into App**.

Bevor Sie diese Option verwenden, arbeiten Sie mit Ihren Entwickler:innen zusammen, um das URI-Format zu definieren und Ihre App so zu konfigurieren, dass sie es öffnet. Benutzerdefinierte Schemata wie `myapp://` öffnen die installierte App direkt. Universal Links (iOS) und App Links (Android) verwenden `https://`-URLs, die die App öffnen können, wenn sie installiert ist, und auf eine Webseite zurückfallen, wenn die App nicht installiert ist.

So legen Sie dieses Klickverhalten fest:

1. Suchen Sie in Ihrem Campaign- oder Canvas-Composer nach **On-Klick, der behavior**:
   - Für Push-Benachrichtigungen und Content Cards gehen Sie zum Tab **Compose**.
   - Für In-App-Nachrichten gehen Sie zum Tab **Compose**. Wählen Sie im Drag-and-Drop-Editor einen Button- oder Bildblock aus und öffnen Sie dessen Eigenschaftenpanel.
2. Wählen Sie **Deeplink into application** oder **Deep Link Into App**.
3. Geben Sie den Link in das URL-Feld ein – zum Beispiel `myapp://products/12345` für ein benutzerdefiniertes Schema oder `https://example.com/products/12345` für einen Universal Link oder App Link.
4. Senden Sie eine Testnachricht an ein physisches Gerät. Ein erfolgreicher Test öffnet die App und leitet zum beabsichtigten Bildschirm oder zur beabsichtigten Aktion weiter. Testen Sie bei einem Universal Link oder App Link auch ein Gerät ohne installierte App, um den erwarteten Web-Fallback zu bestätigen.

### UTM Tags und Campaign-Attribution {#utm-tags-and-campaign-attribution}

#### Was ist ein UTM Tag? {#what-is-a-utm-tag}

[UTM (Urchin Traffic Manager:in) Tags](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) ermöglichen es Ihnen, Campaign-Attribution-Details direkt in Links einzubetten. UTM Tags werden von Google Analytics verwendet, um Campaign-Attribution-Daten zu erfassen, und können zur Nachverfolgung der folgenden Eigenschaften verwendet werden:

- `utm_source`: Der Bezeichner für die Quelle des Traffics (zum Beispiel `my_app`)
- `utm_medium`: Das Campaign-Medium (zum Beispiel `newsfeed`)
- `utm_campaign`: Der Bezeichner für die Campaign (zum Beispiel `spring_2016_campaign`)
- `utm_term`: Bezeichner für einen bezahlten Suchbegriff, der Nutzer:innen zu Ihrer App oder Website geführt hat (zum Beispiel `pizza`)
- `utm_content`: Ein Bezeichner für den spezifischen Link oder Inhalt, auf den Nutzer:innen geklickt haben (zum Beispiel `toplink` oder `android_iam_button2`)

UTM Tags können sowohl in reguläre HTTP-(Web-)Links als auch in Deeplinks eingebettet und über Google Analytics nachverfolgt werden.

##### Berechnung von UTM Tags {#utm-tag-calculations}

Braze meldet _Gesamtklicks_ für alle Links in einer Campaign oder einem Canvas-Schritt, was auch Links ohne UTM Tags umfassen kann. Das bedeutet, dass Sie in Ihren Google Analytics Campaign-Tracking-Links möglicherweise ein anderes (oft niedrigeres) Ergebnis sehen als die in Ihrer Campaign-Performance oder im Berichts-Builder angezeigten _Gesamtklicks_.

#### Verwendung von UTM Tags mit Braze {#using-utm-tags-with-braze}

Wenn Sie UTM Tags mit regulären HTTP-(Web-)Links verwenden möchten (zum Beispiel für die Campaign-Attribution Ihrer E-Mail-Campaigns) und Ihre Organisation bereits Google Analytics nutzt, können Sie [Googles URL-Builder](https://ga-dev-tools.google/ga4/campaign-url-builder/) verwenden, um UTM-Links zu generieren. Diese Links können wie jeder andere Link problemlos in den Braze-Campaign-Text eingebettet werden.

Um UTM Tags in Deeplinks zu Ihrer App zu verwenden, muss Ihre App das entsprechende [Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/) integriert und korrekt für die Verarbeitung von Deeplinks konfiguriert haben. Wenden Sie sich an Ihre Entwickler:innen, wenn Sie sich diesbezüglich unsicher sind.

Nachdem das Analytics SDK integriert und konfiguriert ist, können UTM Tags mit Deeplinks in Braze-Campaigns verwendet werden. Um UTM Tags für Ihre Campaign einzurichten, fügen Sie die erforderlichen UTM Tags in die Ziel-URL oder die Deeplinks ein. Die folgenden Beispiele zeigen, wie UTM Tags in Push-Benachrichtigungen und In-App-Nachrichten verwendet werden.

##### Push-Öffnungen und In-App-Nachricht-Klicks mit UTM Tags zuordnen {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab Push-Öffnungen %}

Um UTM Tags in Ihre Deeplinks für Push-Benachrichtigungen einzufügen, legen Sie das Klickverhalten der Push-Nachricht als Deeplink fest und geben Sie die Deeplink-Adresse ein. Fügen Sie die gewünschten UTM Tags wie folgt ein:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![Screenshot zur Zuordnung von Push-Öffnungen und In-App-Nachricht-Klicks mit UTM Tags.]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab In-App-Nachricht-Klicks %}

Um UTM Tags in die Deeplinks Ihrer In-App-Nachrichten einzufügen, verwenden Sie Folgendes:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![Screenshot zur Zuordnung von Push-Öffnungen und In-App-Nachricht-Klicks mit UTM Tags.]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## Liquid-Personalisierung in URLs verwenden {#use-liquid-personalization-in-urls}

Sie können Ihre URL direkt im Braze-Composer dynamisch erstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. um Nutzer:innen zu ihrem abgebrochenen Warenkorb oder zu einem bestimmten Produkt weiterzuleiten, das wieder auf Lager ist).

### Eine URL mit unterstützten Liquid-Personalisierungs-Tags erstellen {#create-a-url-with-supported-liquid-personalization-tags}

URLs können durch die Verwendung beliebiger [unterstützter Liquid-Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) dynamisch generiert werden.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Wir unterstützen auch die Kürzung benutzerdefinierter Liquid-Variablen, wie in den folgenden Beispielen:

### Eine URL mit Liquid-Variablen erstellen {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Von Liquid-Variablen gerenderte URLs kürzen {#shorten-urls-rendered-by-liquid-variables}

**Unterstützte Kanäle:** KakaoTalk, LINE, SMS, RCS, WhatsApp

Wir kürzen URLs, die von Liquid gerendert werden, auch solche, die in API-Trigger-Eigenschaften enthalten sind. Wenn beispielsweise {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, kürzen und tracken wir diese URL, bevor die Nachricht gesendet wird.

### URLs im `/messages/send`-Endpunkt kürzen {#shorten-urls-in-messagessend-endpoint}

Link-Kürzung ist auch für reine API-Nachrichten über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) aktiviert. Eine vollständige Liste der Anfrageparameter finden Sie unter [Anfrageparameter]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Ja | Boolean | Setzen Sie `link_shortening_enabled` auf `true`, um die Link-Kürzung zu aktivieren. Um Tracking zu verwenden, müssen eine `campaign_id` und eine `message_variation_id` vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="URLs im /messages/send-Endpunkt kürzen" }