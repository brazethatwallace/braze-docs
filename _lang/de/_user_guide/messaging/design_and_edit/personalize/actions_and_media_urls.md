---
nav_title: Aktions- und Medien-URLs
article_title: Aktions- und Medien-URLs mit Liquid personalisieren
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie Aktions- und Medien-URLs mit Liquid personalisieren können."
---

# Aktions- und Medien-URLs mit Liquid personalisieren {#personalize-action-and-media-urls-with-liquid}

> Personalisieren Sie Linkziele und Inhalte für alle Nutzer:innen, die Ihre Nachricht erhalten, indem Sie Liquid-Variablen zu den URLs für Buttons, Links, Bilder und Videos hinzufügen.

## Deeplinking zu In-App-Inhalten {#deep-link-to-in-app-content}

{% alert tip %}
**Für Entwickler:innen:** Einen Leitfaden zur Auswahl zwischen benutzerdefinierten Schemata, Universal Links und anderen Optionen – einschließlich der Frage, wann Sie eine AASA-Datei benötigen, welche App-Delegate-Methoden zu implementieren sind und wie Sie Probleme debuggen – finden Sie unter [iOS-Deeplinking-Leitfaden]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide) und [Fehlerbehebung bei Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

### Was ist Deeplinking? {#what-is-deep-linking}

Deeplinking ist eine Methode, um eine native App zu starten und ihr zusätzliche Informationen zu übergeben, damit sie eine bestimmte Aktion ausführt oder bestimmte Inhalte anzeigt.

Dies besteht aus drei Teilen:

1. Identifizieren, welche App gestartet werden soll.
2. Die App anweisen, welche Aktion ausgeführt werden soll.
3. Der Aktion alle zusätzlichen Daten bereitstellen, die sie benötigt.

Deeplinks sind benutzerdefinierte URIs, die auf einen bestimmten Teil der App verweisen und alle drei dieser Teile enthalten. Der Schlüssel liegt in der Definition eines benutzerdefinierten Schemas. `http:` ist das Schema, mit dem fast jeder vertraut ist, aber Schemata können mit jedem Wort beginnen. Ein Schema muss mit einem Buchstaben beginnen, kann dann aber Buchstaben, Zahlen, Pluszeichen, Minuszeichen oder Punkte enthalten. Praktisch gesehen gibt es kein zentrales Register zur Vermeidung von Konflikten, daher ist es eine Best Practice, Ihren Domainnamen in das Schema aufzunehmen. Zum Beispiel ist `twitter://` der iOS-URI zum Starten der mobilen App für X, ehemals Twitter.

Alles nach dem Doppelpunkt innerhalb eines Deeplinks ist Freitext. Es liegt an Ihnen, dessen Struktur und Interpretation zu definieren; eine gängige Konvention ist jedoch, ihn nach dem Vorbild von `http:`-URLs zu modellieren, einschließlich eines führenden `//` und Abfrageparametern (zum Beispiel `?foo=1&bar=2`). Für das vorherige Beispiel würde `twitter://user?screen_name=[id]` verwendet, um ein bestimmtes Profil in der App zu starten.

{% alert important %}
Für Apps, die mit Wrapper-Frameworks erstellt wurden (zum Beispiel Flutter oder Cordova), bietet Braze keine Wrapper-spezifische Deeplinking-Unterstützung. Sie müssen Deeplinks auf den nativen iOS- und Android-Ebenen konfigurieren. Für Cordova siehe [Deeplinking in Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
{% endalert %}

### UTM Tags und Kampagnen-Attribution {#utm-tags-and-campaign-attribution}

#### Was ist ein UTM Tag? {#what-is-a-utm-tag}

[UTM (Urchin Traffic Manager) Tags](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) ermöglichen es Ihnen, Kampagnen-Attributionsdetails direkt in Links einzubetten. UTM Tags werden von Google Analytics verwendet, um Kampagnen-Attributionsdaten zu erfassen, und können zum Tracking der folgenden Eigenschaften verwendet werden:

- `utm_source`: Der Bezeichner für die Traffic-Quelle (zum Beispiel `my_app`)
- `utm_medium`: Das Kampagnenmedium (zum Beispiel `newsfeed`)
- `utm_campaign`: Der Bezeichner für die Kampagne (zum Beispiel `spring_2016_campaign`)
- `utm_term`: Bezeichner für einen bezahlten Suchbegriff, der die Nutzer:innen zu Ihrer App oder Website geführt hat (zum Beispiel `pizza`)
- `utm_content`: Ein Bezeichner für den spezifischen Link oder Inhalt, auf den die Nutzer:innen geklickt haben (zum Beispiel `toplink` oder `android_iam_button2`)

UTM Tags können sowohl in reguläre HTTP-(Web-)Links als auch in Deeplinks eingebettet und über Google Analytics getrackt werden.

##### Berechnung von UTM Tags {#utm-tag-calculations}

Braze meldet _Gesamtklicks_ für alle Links in einer Campaign oder einem Canvas-Schritt, was auch Links ohne UTM Tags einschließen kann. Das bedeutet, dass Sie in Ihren Google-Analytics-Kampagnen-Tracking-Links möglicherweise ein anderes (oft niedrigeres) Ergebnis sehen als die _Gesamtklicks_, die in Ihrer Kampagnen-Performance oder im Berichts-Builder angezeigt werden.

#### UTM Tags mit Braze verwenden {#using-utm-tags-with-braze}

Wenn Sie UTM Tags mit regulären HTTP-(Web-)Links verwenden möchten (zum Beispiel für die Kampagnen-Attribution Ihrer E-Mail-Kampagnen) und Ihre Organisation bereits Google Analytics nutzt, können Sie [Googles URL-Builder](https://ga-dev-tools.google/ga4/campaign-url-builder/) verwenden, um UTM-Links zu generieren. Diese Links können wie jeder andere Link einfach in den Braze-Kampagnentext eingebettet werden.

Um UTM Tags in Deeplinks zu Ihrer App zu verwenden, muss Ihre App das entsprechende [Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/) integriert und korrekt konfiguriert haben, um Deeplinks zu verarbeiten. Wenden Sie sich an Ihre Entwickler:innen, wenn Sie sich diesbezüglich unsicher sind.

Nachdem das Analytics SDK integriert und konfiguriert ist, können UTM Tags mit Deeplinks in Braze-Kampagnen verwendet werden. Um UTM Tags für Ihre Kampagne einzurichten, fügen Sie die erforderlichen UTM Tags in die Ziel-URL oder die Deeplinks ein. Die folgenden Beispiele zeigen, wie UTM Tags in Push-Benachrichtigungen und In-App-Nachrichten verwendet werden.

##### Push-Öffnungen und In-App-Nachrichten-Klicks mit UTM Tags zuordnen {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab Push-Öffnungen %}

Um UTM Tags in Ihre Deeplinks für Push-Benachrichtigungen einzufügen, setzen Sie das Klickverhalten der Push-Nachricht auf einen Deeplink und geben Sie die Deeplink-Adresse mit den gewünschten UTM Tags wie folgt ein:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![Screenshot zur Zuordnung von Push-Öffnungen und In-App-Nachrichten-Klicks mit UTM Tags.]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab In-App-Nachrichten-Klicks %}

Um UTM Tags in die Deeplinks Ihrer In-App-Nachrichten einzufügen, verwenden Sie Folgendes:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![Screenshot zur Zuordnung von Push-Öffnungen und In-App-Nachrichten-Klicks mit UTM Tags.]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## Liquid-Personalisierung in URLs verwenden {#use-liquid-personalization-in-urls}

Sie können Ihre URL direkt im Braze-Composer dynamisch erstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. um Nutzer:innen zu ihrem Warenkorb-Abbruch oder zu einem bestimmten Produkt weiterzuleiten, das wieder auf Lager ist).

### Eine URL mit unterstützten Liquid-Personalisierungs-Tags erstellen {#create-a-url-with-supported-liquid-personalization-tags}

URLs können durch die Verwendung beliebiger [unterstützter Liquid-Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) dynamisch generiert werden.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Wir unterstützen auch die Verkürzung von benutzerdefinierten Liquid-Variablen. Nachfolgend finden Sie einige Beispiele:

### Eine URL mit Liquid-Variablen erstellen {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Von Liquid-Variablen gerenderte URLs verkürzen {#shorten-urls-rendered-by-liquid-variables}

**Unterstützte Kanäle:** KakaoTalk, LINE, SMS, RCS, WhatsApp

Wir verkürzen URLs, die von Liquid gerendert werden, auch solche, die in API-Trigger-Eigenschaften enthalten sind. Wenn zum Beispiel {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, verkürzen und tracken wir diese URL, bevor die Nachricht gesendet wird.

### URLs im `/messages/send`-Endpunkt verkürzen {#shorten-urls-in-messagessend-endpoint}

Die Linkverkürzung ist auch für reine API-Nachrichten über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) aktiviert. Eine vollständige Liste der Anfrageparameter finden Sie unter [Anfrageparameter]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Ja | Boolescher Wert | Setzen Sie `link_shortening_enabled` auf `true`, um die Linkverkürzung zu aktivieren. Um Tracking zu verwenden, müssen eine `campaign_id` und eine `message_variation_id` vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="URLs im /messages/send-Endpunkt verkürzen" }