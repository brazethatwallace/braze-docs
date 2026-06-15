---
nav_title: Profil utilisateur
article_title: Profil utilisateur
page_order: 0
description: "Découvrez comment personnaliser vos messages avec les données du profil utilisateur, y compris les attributs standard, les attributs personnalisés et les propriétés d'événement."
---

# Profil utilisateur

> Personnalisez vos messages avec les données stockées sur le profil de chaque utilisateur, y compris les attributs standard, les attributs personnalisés et les propriétés d'événement. Braze met ces données à disposition via des balises [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) que vous insérez directement dans le contenu de vos messages.

## Attributs standard

{% raw %}
Les attributs standard sont des champs de profil prédéfinis que Braze suit automatiquement, tels que `{{${first_name}}}`, `{{${email_address}}}` et `{{${city}}}`. Comme ces attributs suivent une convention de nommage cohérente, vous pouvez les référencer dans n'importe quel message sans configuration supplémentaire.

Par exemple, pour saluer un utilisateur par son prénom :

```liquid
Hi {{${first_name} | default: 'there'}}, check out our latest picks for you!
```
{% endraw %}

Pour une liste complète des balises d'attributs standard, consultez [Balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## Attributs personnalisés

{% raw %}
Les attributs personnalisés sont des champs de profil propres à votre espace de travail, tels que le niveau de fidélité, la catégorie préférée ou le type de compte. Référencez-les à l'aide de la balise `{{custom_attribute.${attribute_name}}}`.

Par exemple, pour personnaliser un message en fonction du niveau d'adhésion d'un utilisateur :

```liquid
{% if custom_attribute.${membership_tier} == 'gold' %}
  As a Gold member, you get early access to our new collection.
{% else %}
  Upgrade your membership for early access to new collections.
{% endif %}
```
{% endraw %}

Pour en savoir plus sur la création et la gestion des attributs personnalisés, consultez [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

## Propriétés d'événement

{% raw %}
Lorsqu'une campagne ou un Canvas est déclenché par un événement personnalisé ou un achat, les propriétés de l'événement sont disponibles pour la personnalisation. Référencez-les à l'aide de `{{event_properties.${property_name}}}`.

Par exemple, si un événement personnalisé `completed_purchase` inclut une propriété `product_name` :

```liquid
Thanks for purchasing {{event_properties.${product_name}}}! Your order is on its way.
```
{% endraw %}

Les propriétés d'événement sont disponibles dans les campagnes par événement et dans la première étape d'un Canvas par événement. Pour en savoir plus, consultez [Événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/).

## Propriétés de déclenchement API

{% raw %}
Pour les campagnes et les Canvas déclenchés via l'API, vous pouvez transmettre des données supplémentaires à l'aide de l'objet de propriétés de déclenchement. Référencez ces valeurs avec `{{api_trigger_properties.${property_name}}}`.

Par exemple :

```liquid
Your verification code is {{api_trigger_properties.${verification_code}}}.
```
{% endraw %}

Pour en savoir plus, consultez [Objet de propriétés de déclenchement API]({{site.baseurl}}/api/objects_filters/trigger_properties_object/).

## Attributs de l'appareil

{% raw %}
Vous pouvez également référencer les attributs du dernier appareil utilisé. Par exemple, `{{most_recently_used_device.${model}}}` renvoie le nom du modèle de l'appareil, et `{{most_recently_used_device.${os}}}` renvoie le système d'exploitation.
{% endraw %}

Pour la liste complète des balises d'attributs d'appareil, consultez [Balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#most-recently-used-device-information).

## Définir des valeurs par défaut

Si un champ de profil est vide pour un utilisateur donné, Braze affiche par défaut une chaîne de caractères vide. Pour éviter des messages d'apparence incomplète, définissez une valeur de repli à l'aide du filtre Liquid `default`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}},
```
{% endraw %}

Pour en savoir plus, consultez [Définir des valeurs par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/).