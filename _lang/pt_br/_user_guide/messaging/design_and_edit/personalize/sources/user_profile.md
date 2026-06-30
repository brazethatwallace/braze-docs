---
nav_title: Perfil de usuário
article_title: Perfil de usuário
page_order: 0
description: "Saiba como personalizar mensagens com dados do perfil de usuário, incluindo atributos padrão, atributos personalizados e propriedades de eventos."
---

# Perfil de usuário {#user-profile}

> Personalize suas mensagens com dados armazenados no perfil de cada usuário, incluindo atributos padrão, atributos personalizados e propriedades de eventos. A Braze disponibiliza esses dados por meio de tags [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) que você insere diretamente no conteúdo da sua mensagem.

## Atributos padrão {#standard-attributes}

{% raw %}
Atributos padrão são campos de perfil predefinidos que a Braze rastreia automaticamente, como `{{${first_name}}}`, `{{${email_address}}}` e `{{${city}}}`. Como esses atributos seguem uma convenção de nomenclatura consistente, você pode referenciá-los em qualquer mensagem sem configuração adicional.

Por exemplo, para cumprimentar um usuário pelo nome:

```liquid
Hi {{${first_name} | default: 'there'}}, check out our latest picks for you!
```
{% endraw %}

Para ver a lista completa de tags de atributos padrão, consulte [Tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Atributos personalizados {#custom-attributes}

{% raw %}
Atributos personalizados são campos de perfil exclusivos do seu espaço de trabalho, como nível de fidelidade, categoria favorita ou tipo de conta. Referencie-os usando a tag `{{custom_attribute.${attribute_name}}}`.

Por exemplo, para personalizar uma mensagem com base no nível de assinatura de um usuário:

```liquid
{% if custom_attribute.${membership_tier} == 'gold' %}
  As a Gold member, you get early access to our new collection.
{% else %}
  Upgrade your membership for early access to new collections.
{% endif %}
```
{% endraw %}

Para saber mais sobre como criar e gerenciar atributos personalizados, consulte [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

## Propriedades de eventos {#event-properties}

{% raw %}
Quando uma Campaign ou um Canvas é disparado por um evento personalizado ou uma compra, as propriedades do evento ficam disponíveis para personalização. Referencie-as usando `{{event_properties.${property_name}}}`.

Por exemplo, se um evento personalizado `completed_purchase` inclui uma propriedade `product_name`:

```liquid
Thanks for purchasing {{event_properties.${product_name}}}! Your order is on its way.
```
{% endraw %}

As propriedades de eventos estão disponíveis em Campaigns baseadas em ação e na primeira etapa de um Canvas baseado em ação. Para saber mais, consulte [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events).

## Propriedades de disparo via API {#api-trigger-properties}

{% raw %}
Para Campaigns e Canvas disparados pela API, você pode enviar dados adicionais usando o objeto de propriedades de disparo. Referencie esses valores com `{{api_trigger_properties.${property_name}}}`.

Por exemplo:

```liquid
Your verification code is {{api_trigger_properties.${verification_code}}}.
```
{% endraw %}

Para saber mais, consulte [Objeto de propriedades de disparo da API]({{site.baseurl}}/api/objects_filters/trigger_properties_object).

## Atributos do dispositivo {#device-attributes}

{% raw %}
Você também pode referenciar atributos do dispositivo usado mais recentemente pelo usuário. Por exemplo, `{{most_recently_used_device.${model}}}` retorna o nome do modelo do dispositivo, e `{{most_recently_used_device.${os}}}` retorna o sistema operacional.
{% endraw %}

Para ver a lista completa de tags de atributos de dispositivo, consulte [Tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information).

## Definindo valores padrão {#setting-default-values}

Se um campo de perfil estiver vazio para um determinado usuário, a Braze renderiza uma string vazia por padrão. Para evitar mensagens com aparência incompleta, defina um valor de fallback usando o filtro Liquid `default`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}},
```
{% endraw %}

Para saber mais, consulte [Definindo valores padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values).