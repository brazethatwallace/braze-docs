---
nav_title: Unterstützte Personalisierungs-Tags
article_title: Unterstützte Liquid-Personalisierungs-Tags
page_order: 1
description: "Dieser Referenzartikel enthält eine vollständige Liste der unterstützten Liquid-Personalisierungs-Tags."
search_rank: 1
---

# Unterstützte Personalisierungs-Tags {#supported-personalization-tags}

> Dieser Referenzartikel enthält eine vollständige Liste der unterstützten Liquid-Personalisierungs-Tags.

## Zusammenfassung der unterstützten Tags {#summary-of-supported-tags}

Zur besseren Übersicht finden Sie hier eine Zusammenfassung der unterstützten Personalisierungs-Tags. Für weitere Details zu den einzelnen Tag-Typen und Best Practices lesen Sie bitte weiter.

{% raw %}

| Personalisierungs-Tag-Typ | Tags |
| -------------  | ---- |
| Standard-Attribute | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Geräte-Attribute | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/channels/email/subscriptions#changing-email-subscriptions'>E-Mail-Listen-Attribute</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Dieses Tag ersetzt das frühere `{{${unsubscribe_url}}}`-Tag. Obwohl das ältere Tag in zuvor erstellten E-Mails weiterhin funktioniert, empfehlen wir, stattdessen das neuere Tag zu verwenden. <br><br> `{{${set_user_to_one_click_list_unsubscribe}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}` |
| <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#Trigger or triggern-messages'>Kurzmitteilungsdienst or SMS-Attribute</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/channels/whatsapp/message_processing/messaging_users'>WhatsApp-Attribute</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` <br> `{{whats_app.${inbound_profile_name}}}` |
| Campaign-Attribute und Canvas-Schritt-Attribute | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Canvas-Attribute | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Card-Attribute | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Geofencing-Ereignisse | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Event-Eigenschaften <br> (Diese sind spezifisch für Ihren Workspace.)| `{{event_properties.${your_custom_event_property}}}` |
| Canvas-Kontextvariablen | `{{context.${your_context_variable}}}` |
| Angepasste Attribute <br> (Diese sind spezifisch für Ihren Workspace.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object'>API-Trigger or triggern-Eigenschaften</a> | `{{api_trigger_properties.${your_api_trigger_property}}}` |
| Canvas-Entry-Eigenschaften | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zusammenfassung der unterstützten Tags" }

{% endraw %}

{% alert note %}
API-Trigger or triggern-Eigenschaften müssen zwei geschweifte Klammern pro Tag verwenden: {% raw %}`{{api_trigger_properties.${your_api_trigger_property}}}`. Dreifache Klammern (zum Beispiel `{{{...}}}`){% endraw %} sind keine gültige Braze-Personalisierungssyntax. Siehe [Warum schlägt mein API-getriggertes Liquid in Braze fehl?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).
{% endalert %}

### Unterstützte Attribute {#supported-attributes}

Campaign-, Card- und Canvas-Attribute werden nur in ihren entsprechenden Messaging-Templates unterstützt. Zum Beispiel wird `dispatch_id` in Liquid für Messaging-Kanäle wie E-Mail, Push, Kurzmitteilungsdienst or SMS und WhatsApp unterstützt, jedoch nicht für In-App-Nachrichten oder Banner.

Weitere Details finden Sie unter [Campaign- und Canvas-Attribute über verschiedene Quellen hinweg]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources).

### Unterschiede zwischen Canvas- und Campaign-Tags {#canvas-and-campaign-tag-differences}

Das Verhalten der folgenden Tags unterscheidet sich zwischen Canvas und Campaigns:
{% raw %}
- Das Verhalten von `dispatch_id` unterscheidet sich, da Braze Canvas-Schritte als getriggerte Ereignisse behandelt, auch wenn sie „geplant“ sind (mit Ausnahme von Entry-Schritten, die geplant werden können). Weitere Informationen finden Sie unter [Dispatch-ID-Verhalten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).
- Die Verwendung des `{{campaign.${name}}}`-Tags mit Canvas zeigt den Namen der Canvas-Komponente an. Bei der Verwendung dieses Tags mit Campaigns wird der Campaign-Name angezeigt.
{% endraw %}

#### Campaign-Namen in URLs {#campaign-names-in-urls}

{% raw %}
Campaign- und Nachrichtenvarianten-Namen können Zeichen enthalten, die nicht URL-sicher sind, wie `%`, Leerzeichen oder `&`. Wenn Sie `{{campaign.${name}}}` oder `{{campaign.${message_name}}}` in einen Link oder Query-String einfügen, z. B. als `utm_campaign`-Parameter, wenden Sie den [`url_encode`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#url-filters)-Filter an, damit die URL korrekt geparst wird. Zum Beispiel:

```liquid
https://example.com/?utm_campaign={{ campaign.${name} | url_encode }}
```
{% endraw %}

## Informationen zum zuletzt verwendeten Gerät {#most-recently-used-device-information}

Sie können die folgenden Attribute für das zuletzt verwendete Gerät der Nutzer:innen über alle Plattformen hinweg als Template verwenden. Wenn Nutzer:innen Ihre Anwendung nicht verwendet haben (z. B. wenn Sie die Nutzer:innen über die Representational State Transfer API importiert haben), sind alle diese Werte `null`.

{% raw %}

| Tag | Beschreibung |
|---|---|
|`{{most_recently_used_device.${browser}}}` | Der zuletzt verwendete Browser auf dem Gerät der Nutzer:innen. Beispiele sind „Chrome“ und „Safari“. |
|`{{most_recently_used_device.${id}}}` | Der Braze-Gerätebezeichner. Unter iOS kann dies der Identifier for Vendors (IDFV) oder eine UUID sein. Für Android und andere Plattformen ist es eine zufällig generierte UUID. |
| `{{most_recently_used_device.${carrier}}}` | Der Mobilfunkanbieter des zuletzt verwendeten Geräts, falls verfügbar. Beispiele sind „Verizon“ und „Orange“. |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Ob das Gerät Ad-Tracking aktiviert hat oder nicht. Dies ist ein boolescher Wert (`true` oder `false`). |
| `{{most_recently_used_device.${idfa}}}` | Für iOS-Geräte ist dieser Wert der Identifier for Advertising (IDFA), wenn Ihre Anwendung mit unserer [optionalen IDFA-Erfassung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection) konfiguriert ist. Für Nicht-iOS-Geräte ist dieser Wert null. |
| `{{most_recently_used_device.${google_ad_id}}}` | Für Android-Geräte ist dieser Wert die Google Play Advertising Identifier, wenn Ihre Anwendung mit unserer optionalen Google Play Advertising ID-Erfassung konfiguriert ist. Für Nicht-Android-Geräte ist dieser Wert null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Für Roku-Geräte ist dieser Wert die Roku Advertising Identifier, die erfasst wird, wenn Ihre Anwendung mit Braze konfiguriert ist. Für Nicht-Roku-Geräte ist dieser Wert null. |
| `{{most_recently_used_device.${model}}}` | Der Modellname des Geräts, falls verfügbar. Beispiele sind „iPhone 6S“, „Nexus 6P“ und „Firefox“. |
| `{{most_recently_used_device.${os}}}` | Das Betriebssystem des Geräts, falls verfügbar. Beispiele sind „iOS 9.2.1“, „Android (Lollipop)“ und „Windows“. |
| `{{most_recently_used_device.${platform}}}` | Die Plattform des Geräts, falls verfügbar. Wenn gesetzt, ist der Wert einer von `ios`, `android`, `kindle`, `android_china`, `web` oder `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informationen zum zuletzt verwendeten Gerät" }

Da es eine große Bandbreite an Mobilfunkanbietern, Modellnamen und Betriebssystemen gibt, empfehlen wir Ihnen, jedes Liquid gründlich zu testen, das bedingt von einem dieser Werte abhängt. Diese Werte sind `null`, wenn sie auf einem bestimmten Gerät nicht verfügbar sind.

## Informationen zur Ziel-App {#targeted-app-information}

Für In-App-Nachrichten können Sie die folgenden App-Attribute in Liquid verwenden. Die Werte basieren darauf, welchen SDK or Software-Development-Kit-API-Schlüssel Ihre Apps verwenden, um Messaging anzufordern.

|Tag | Beschreibung |
|------------------|---|
| `{{app.${api_id}}}` | Der API-Schlüssel der App, die die Nachricht anfordert. Sie verwenden diesen Schlüssel beispielsweise in Verbindung mit `abort_message()` Liquid, um das Senden von In-App-Nachrichten an bestimmte Apps zu vermeiden, z. B. TV-Plattformen oder Entwicklungs-Builds, die einen separaten SDK or Software-Development-Kit-API-Schlüssel verwenden.|
| `{{app.${name}}}` | Der Name der App (wie im Braze-Dashboard definiert), die die Nachricht anfordert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informationen zur Ziel-App" }

Dieser Liquid-Code bricht beispielsweise eine Nachricht ab, wenn die anfragenden Apps nicht einem der beiden API-Schlüssel in der Liste entsprechen:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informationen zum Zielgerät {#targeted-device-information}

Für Push-Benachrichtigungen, In-App-Nachrichten und Banner können Sie die folgenden Attribute für das Gerät, das die Nachricht empfängt, als Template verwenden. Eine Push-Benachrichtigung, In-App-Nachricht oder ein Banner kann Attribute des Geräts enthalten, auf dem die Nutzer:innen die Nachricht lesen. Diese Attribute funktionieren nicht für Content Cards oder E-Mails. Bei E-Mails werden Nachrichten vor dem Versand gerendert, sodass das Gerät, auf dem die Nutzer:innen die E-Mail öffnen, zu diesem Zeitpunkt unbekannt ist.

|Tag | Beschreibung |
|------------------|---|
| `{{targeted_device.${id}}}` | Dies ist der Braze-Gerätebezeichner. Unter iOS kann dies der Identifier for Vendors (IDFV) oder eine UUID sein. Für Android und andere Plattformen ist es eine zufällig generierte UUID. Wenn beispielsweise eine Nutzer:in fünf Geräte hat, wird ein Sendeversuch für alle fünf Geräte durchgeführt, wobei jeweils der entsprechende Gerätebezeichner verwendet wird. Wenn eine Nachricht so konfiguriert ist, dass sie an das zuletzt verwendete Gerät einer Nutzer:in gesendet wird, erfolgt nur ein Sendeversuch an das zuletzt verwendete Gerät, das über Braze identifiziert wurde. |
| `{{targeted_device.${carrier}}}` | Der Mobilfunkanbieter des zuletzt verwendeten Geräts, falls verfügbar. Beispiele sind „Verizon“ und „Orange“. |
| `{{targeted_device.${idfa}}}` | Für iOS-Geräte ist dieser Wert der Identifier for Advertisers (IDFA), wenn Ihre Anwendung mit unserer [optionalen IDFA-Erfassung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection) konfiguriert ist. Für Nicht-iOS-Geräte ist dieser Wert null. |
| `{{targeted_device.${google_ad_id}}}` | Für Android-Geräte ist dieser Wert die Google Play Advertising Identifier, wenn Ihre Anwendung mit unserer [optionalen Google Play Advertising ID-Erfassung] konfiguriert ist. Für Nicht-Android-Geräte ist dieser Wert null. |
| `{{targeted_device.${roku_ad_id}}}` | Für Roku-Geräte ist dieser Wert der Roku Advertising Identifier, der erfasst wird, wenn Ihre Anwendung mit Braze konfiguriert ist. Für Nicht-Roku-Geräte ist dieser Wert null. |
| `{{targeted_device.${model}}}` | Der Modellname des Geräts, falls verfügbar. Beispiele sind „iPhone 6S“, „Nexus 6P“ und „Firefox“. |
| `{{targeted_device.${os}}}` | Das Betriebssystem des Geräts, falls verfügbar. Beispiele sind „iOS 9.2.1“, „Android (Lollipop)“ und „Windows“. |
| `{{targeted_device.${platform}}}` | Die Plattform des Geräts, falls verfügbar. Wenn gesetzt, ist der Wert einer von `ios`, `android`, `kindle`, `android_china`, `web` oder `tvos`. Sie können auch den Personalisierungs-Tag `most_recently_used_device` verwenden. |
| `{{targeted_device.${foreground_push_enabled}}}` | Dieser Wert ist `true`, wenn das Zielgerät für Vordergrund-Push aktiviert ist, andernfalls `false`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informationen zum Zielgerät" }

{% endraw %}

Da es eine große Bandbreite an Mobilfunkanbietern, Modellnamen und Betriebssystemen gibt, empfehlen wir Ihnen, jede Logik, die bedingt von einem dieser Werte abhängt, gründlich zu testen. Diese Werte sind `null`, wenn sie auf einem bestimmten Gerät nicht verfügbar sind.

Darüber hinaus ist es bei Push-Benachrichtigungen möglich, dass Braze unter bestimmten Umständen das mit der Push-Benachrichtigung verknüpfte Gerät nicht ermitteln kann, z. B. wenn das Push-Token / Textbaustein über die API importiert wurde, was dazu führt, dass die Werte für diese Nachrichten `null` sind.

![Beispiel für die Verwendung eines Standardwerts „there“ bei Nutzung einer Vornamens-Variable in einer Push-Nachricht.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Bedingte Logik anstelle eines Standardwerts verwenden {#using-conditional-logic-instead-of-a-default-value}

Unter bestimmten Umständen können Sie sich dafür entscheiden, [bedingte Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic) anstelle eines Standardwerts zu verwenden. Bedingte Logik ermöglicht es Ihnen, Nachrichten zu senden, die sich je nach Wert eines angepassten Attributs unterscheiden. Zusätzlich können Sie bedingte Logik verwenden, um Nachrichten an Kund:innen mit null- oder leeren Attributwerten [abzubrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

#### Anwendungsfall {#use-case}

Nehmen wir beispielsweise an, Sie senden eine Benachrichtigung über den Rewards-Kontostand an Kund:innen. Es gibt keine gute Möglichkeit, Kund:innen mit niedrigen und null-Kontoständen mithilfe von Standardwerten zu berücksichtigen.

In diesem Fall gibt es zwei Optionen, die besser funktionieren können als das Setzen eines Standardwerts:

1. Brechen Sie die Nachricht für Kund:innen mit niedrigen, null- und leeren Kontoständen ab.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Senden Sie eine völlig andere Nachricht an diese Kund:innen, wie zum Beispiel:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

In diesem Anwendungsfall erhält eine Nutzer:in mit einem leeren oder null-Vornamen die Nachricht „Thanks for downloading“. Sie sollten einen [Standardwert]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) für den Vornamen einfügen, um sicherzustellen, dass Ihre Kund:innen im Falle eines Fehlers kein Liquid sehen.

{% endraw %}

## Variablen-Tags {#variable-tags}

Sie können den `assign`-Tag verwenden, um eine Variable im Nachrichten-Editor zu erstellen. Wir empfehlen, einen eindeutigen Namen für Ihre Variable zu verwenden. Wenn Sie eine Variable mit einem ähnlichen Namen wie die unterstützten Personalisierungs-Tags erstellen (z. B. `language`), kann dies Ihre Messaging-Logik beeinträchtigen.

Nachdem Sie eine Variable erstellt haben, können Sie diese Variable in Ihrer Messaging-Logik oder Nachricht referenzieren. Dieser Tag ist besonders nützlich, wenn Sie Inhalte umformatieren möchten, die von unserem [Connected-Content]({% image_buster /assets/img_archive/personalized_firstname_.png %})-Feature zurückgegeben werden. Weitere Informationen finden Sie in der Shopify-Dokumentation zu [Variablen-Tags](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert important %}
Strings, die innerhalb eines `assign`-Tags in einfache Anführungszeichen eingeschlossen sind, werden als literale Strings behandelt. Liquid-Personalisierungs-Tags innerhalb einfacher Anführungszeichen werden nicht interpoliert. Zum Beispiel:

{% raw %}
```liquid
{% assign name_intro = 'My name is {{${first_name}}}' %}
{{ name_intro }}
```
{% endraw %}

Dies gibt den literalen Text {% raw %}`My name is {{${first_name}}}`{% endraw %} aus, anstatt den Vornamen der Nutzer:innen.

Um Personalisierung einzubeziehen, verwenden Sie Variablen oder verketten Sie Strings mit dem [`append`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#string-filters)-Filter. Für URL-Templating mit Personalisierung lesen Sie den Abschnitt [Link-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).
{% endalert %}

{% alert tip %}
Weisen Sie in jeder Nachricht dieselben Variablen zu? Anstatt den `assign`-Tag immer wieder auszuschreiben, können Sie diesen Tag als Content-Block speichern und ihn stattdessen an den Anfang Ihrer Nachricht setzen.

1. [Erstellen Sie einen Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Geben Sie Ihrem Content-Block einen Namen (ohne Leerzeichen oder Sonderzeichen).
3. Wählen Sie **Bearbeiten** am unteren Rand der Seite.
4. Geben Sie Ihre `assign`-Tags ein.

Solange sich der Content-Block am Anfang Ihrer Nachricht befindet, verweist die Variable jedes Mal, wenn sie als Objekt in Ihre Nachricht eingefügt wird, auf Ihr gewähltes angepasstes Attribut.
{% endalert %}

### Anwendungsfall

Nehmen wir an, Sie erlauben Ihren Kund:innen, ihre Rewards-Punkte gegen Preise einzulösen, nachdem sie 100 Rewards-Punkte gesammelt haben. Sie möchten also nur Kund:innen ansprechen, deren Punktestand größer oder gleich 100 wäre, wenn sie diesen zusätzlichen Kauf tätigen würden:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Iterations-Tags {#iteration-tags}

{% raw %}
Iterations-Tags können verwendet werden, um einen Codeblock wiederholt auszuführen. Der folgende Anwendungsfall zeigt den `for`-Tag.

### Anwendungsfall

Nehmen wir an, Sie haben einen Sale auf Nike-Sneaker und möchten Kund:innen ansprechen, die Interesse an Nike gezeigt haben. Sie haben ein Array von Produktmarken, die im Profil jeder Kund:in angesehen wurden. Dieses Array könnte bis zu 25 Produktmarken enthalten, aber Sie möchten nur Kund:innen ansprechen, die ein Nike-Produkt als eines ihrer 5 zuletzt angesehenen Produkte betrachtet haben.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

In diesem Anwendungsfall prüfen wir die ersten fünf Einträge im Array der angesehenen Sneaker-Marken. Wenn einer dieser Einträge „Converse“ ist, erstellen wir die Variable `converse_viewer` und setzen sie auf „true“.

Anschließend senden wir die Sale-Nachricht, wenn `converse_viewer` den Wert „true“ hat. Andernfalls brechen wir die Nachricht ab.

Dies ist ein einfaches Beispiel dafür, wie Iterations-Tags im Braze-Nachrichten-Editor verwendet werden können. Weitere Informationen finden Sie in der Shopify-Dokumentation zu [Iterations-Tags](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Syntax-Tags {#syntax-tags}

Syntax-Tags können verwendet werden, um zu steuern, wie Liquid gerendert wird. Sie können den `echo`-Tag verwenden, um einen Ausdruck zurückzugeben. Dies entspricht dem Umschließen eines Ausdrucks mit geschweiften Klammern, außer dass Sie diesen Tag innerhalb von Liquid-Tags verwenden können. Sie können auch den `liquid`-Tag verwenden, um einen Liquid-Block ohne Trennzeichen für jeden Tag zu erstellen. Jeder Tag muss in einer eigenen Zeile stehen, wenn Sie den `liquid`-Tag verwenden. Weitere Informationen und Beispiele finden Sie in der Shopify-Dokumentation zu [Syntax-Tags](https://shopify.dev/api/liquid/tags#syntax-tags).

Mit [Whitespace-Kontrolle](https://shopify.github.io/liquid/basics/whitespace/) können Sie Leerzeichen um Ihre Tags entfernen und so die Liquid-Ausgabe noch besser kontrollieren.

## HTTP-Statuscodes {#http-personalization}

Sie können den HTTP-Status eines [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)-Aufrufs nutzen, indem Sie ihn zunächst als lokale Variable speichern und dann den Schlüssel `__http_status_code__` verwenden. Zum Beispiel:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Dieser Schlüssel wird dem Connected-Content-Objekt nur automatisch hinzugefügt, wenn der Endpunkt ein JSON-Objekt zurückgibt. Wenn der Endpunkt ein Array oder einen anderen Typ zurückgibt, kann dieser Schlüssel nicht automatisch in der Antwort gesetzt werden.
{% endalert %}

## Nachrichten basierend auf Sprache, letztem Gebietsschema und Zeitzone senden {#send-messages-based-on-language-most-recent-locale-and-time-zone}

In manchen Situationen möchten Sie möglicherweise Nachrichten senden, die auf bestimmte Gebietsschemas zugeschnitten sind. Beispielsweise unterscheidet sich brasilianisches Portugiesisch in der Regel von europäischem Portugiesisch.

### Anwendungsfall: Lokalisierung basierend auf dem letzten Gebietsschema {#use-case-localize-based-on-recent-locale}

Hier ist ein Anwendungsfall, wie Sie das letzte Gebietsschema verwenden können, um eine internationalisierte Nachricht weiter zu lokalisieren.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

In diesem Anwendungsfall erhalten Kund:innen mit dem letzten Gebietsschema `pt_BR` eine Nachricht in brasilianischem Portugiesisch, und Kund:innen mit dem letzten Gebietsschema `pt_PT` erhalten eine Nachricht in europäischem Portugiesisch. Kund:innen, die die ersten beiden Bedingungen nicht erfüllen, aber deren Sprache auf Portugiesisch eingestellt ist, erhalten eine Nachricht in dem von Ihnen gewünschten Standard-Portugiesisch.

### Anwendungsfall: Nutzer:innen nach Zeitzone ansprechen {#use-case-target-users-by-time-zone}

Sie können Nutzer:innen auch nach ihrer Zeitzone ansprechen. Senden Sie beispielsweise eine Nachricht, wenn sie sich in der EST-Zeitzone befinden, und eine andere, wenn sie in der PST-Zeitzone sind. Speichern Sie dazu die aktuelle Uhrzeit in UTC und vergleichen Sie mit einer if/else-Anweisung die aktuelle Uhrzeit der Nutzer:innen, um die richtige Nachricht für die richtige Zeitzone zu senden. Sie sollten die Campaign so einstellen, dass sie in der Ortszeit der Nutzer:innen gesendet wird, damit sie die Campaign zur richtigen Zeit erhalten.

Im folgenden Anwendungsfall sehen Sie, wie Sie eine Nachricht verfassen, die zwischen 14:00 und 15:00 Uhr zugestellt wird, mit einer spezifischen Nachricht für jede Zeitzone.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

## Nachrichten mit einer Zufallszahl senden {#send-messages-with-a-random-number}

{% raw %}
Der `{% random %}`-Tag gibt eine Zufallszahl zurück. Sie können ihn für A/B-Logik, Stichproben oder die Variation von Nachrichteninhalten verwenden.

| Tag | Beschreibung |
|-------|--------------|
| `{% random %}` | Eine Gleitkommazahl zwischen 0 und 1 (einschließlich 0, ausschließlich 1). |
| `{% random 10 %}` (ganzzahliges Argument) | Eine Ganzzahl von 0 bis, aber ausschließlich, der angegebenen Ganzzahl. Zum Beispiel gibt `{% random 10 %}` eine Ganzzahl von 0 bis 9 zurück. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nachrichten mit einer Zufallszahl senden" }

{% endraw %}

### Anwendungsfall: Nutzer:innen zufällige Varianten senden {#use-case-send-users-random-variants}

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}

## E-Commerce-Warenkorb-Tag {#shopping-cart-tag}

Der `shopping_cart`-Tag greift auf den Warenkorbinhalt von Nutzer:innen in E-Commerce-Canvas-Anwendungsfällen für [Warenkorb-Abbruch]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20cart#abandoned-cart) und [Checkout-Abbruch]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout) zu. Ersetzen Sie `CART_ID` durch den tatsächlichen Warenkorb-ID-Wert, wie z. B. {% raw %}`{{context.${cart_id}}}`{% endraw %}.

{% raw %}
```liquid
{% shopping_cart CART_ID :abort_if_not_abandoned false %}
```
{% endraw %}

Der Parameter `abort_if_not_abandoned` in diesem Beispiel gilt nur für den Anwendungsfall [Checkout-Abbruch]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout), wenn er mit dem Ereignis `ecommerce.checkout_started` verwendet wird. Er ist nicht auf Warenkorb-Abbruch-Anwendungsfälle anwendbar. Weitere Details finden Sie unter [`abort_if_not_abandoned`]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abort-if-not-abandoned).

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags