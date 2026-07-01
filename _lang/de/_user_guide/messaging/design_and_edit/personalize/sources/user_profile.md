---
nav_title: Nutzerprofil
article_title: Nutzerprofil
page_order: 0
description: "Erfahren Sie, wie Sie Nachrichten mit Nutzerprofildaten personalisieren, einschließlich Standardattributen, angepassten Attributen und Event-Eigenschaften."
---

# Nutzerprofil {#user-profile}

> Personalisieren Sie Ihre Nachrichten mit Daten, die im Profil jedes Nutzers bzw. jeder Nutzerin gespeichert sind, einschließlich Standardattributen, angepassten Attributen und Event-Eigenschaften. Braze stellt diese Daten über [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)-Tags bereit, die Sie direkt in Ihren Nachrichteninhalt einfügen können.

## Standardattribute {#standard-attributes}

{% raw %}
Standardattribute sind vordefinierte Profilfelder, die Braze automatisch erfasst, wie z. B. `{{${first_name}}}`, `{{${email_address}}}` und `{{${city}}}`. Da diese Attribute einer einheitlichen Namenskonvention folgen, können Sie sie ohne zusätzliche Einrichtung in jeder Nachricht referenzieren.

Um beispielsweise eine Nutzerin oder einen Nutzer mit dem Vornamen zu begrüßen:

```liquid
Hi {{${first_name} | default: 'there'}}, check out our latest picks for you!
```
{% endraw %}

Eine vollständige Liste der Standardattribut-Tags finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Angepasste Attribute {#custom-attributes}

{% raw %}
Angepasste Attribute sind Profilfelder, die speziell für Ihren Workspace gelten, wie z. B. Treuestufe, Lieblingskategorie oder Kontotyp. Referenzieren Sie sie mit dem Tag `{{custom_attribute.${attribute_name}}}`.

Um beispielsweise eine Nachricht basierend auf der Mitgliedschaftsstufe zu personalisieren:

```liquid
{% if custom_attribute.${membership_tier} == 'gold' %}
  As a Gold member, you get early access to our new collection.
{% else %}
  Upgrade your membership for early access to new collections.
{% endif %}
```
{% endraw %}

Weitere Informationen zum Erstellen und Verwalten angepasster Attribute finden Sie unter [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

## Event-Eigenschaften {#event-properties}

{% raw %}
Wenn eine Kampagne oder ein Canvas durch ein angepasstes Event oder einen Kauf getriggert wird, stehen die Eigenschaften des Events für die Personalisierung zur Verfügung. Referenzieren Sie sie mit `{{event_properties.${property_name}}}`.

Wenn beispielsweise ein angepasstes Event `completed_purchase` eine Eigenschaft `product_name` enthält:

```liquid
Thanks for purchasing {{event_properties.${product_name}}}! Your order is on its way.
```
{% endraw %}

Event-Eigenschaften sind in aktionsbasierten Campaigns und im ersten Schritt eines aktionsbasierten Canvas verfügbar. Weitere Informationen finden Sie unter [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events).

## API-Trigger-Eigenschaften {#api-trigger-properties}

{% raw %}
Für Campaigns und Canvases, die über die API getriggert werden, können Sie zusätzliche Daten über das Trigger-Eigenschaften-Objekt übergeben. Referenzieren Sie diese Werte mit `{{api_trigger_properties.${property_name}}}`.

Zum Beispiel:

```liquid
Your verification code is {{api_trigger_properties.${verification_code}}}.
```
{% endraw %}

Weitere Informationen finden Sie unter [API-Trigger-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/trigger_properties_object).

## Geräteattribute {#device-attributes}

{% raw %}
Sie können auch Attribute des zuletzt verwendeten Geräts referenzieren. Beispielsweise gibt `{{most_recently_used_device.${model}}}` den Gerätemodellnamen zurück und `{{most_recently_used_device.${os}}}` das Betriebssystem.
{% endraw %}

Die vollständige Liste der Geräteattribut-Tags finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information).

## Standardwerte festlegen {#setting-default-values}

Wenn ein Profilfeld für eine bestimmte Nutzerin oder einen bestimmten Nutzer leer ist, gibt Braze standardmäßig einen leeren String aus. Um unvollständig wirkende Nachrichten zu vermeiden, legen Sie mit dem Liquid-Filter `default` einen Fallback-Wert fest.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}},
```
{% endraw %}

Weitere Informationen finden Sie unter [Standardwerte festlegen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values).