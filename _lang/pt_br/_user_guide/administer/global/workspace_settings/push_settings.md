---
nav_title: Configurações de push
article_title: Configurações de push
page_order: 5
page_type: reference
description: "Este artigo fornece uma visão geral das configurações de push no dashboard da Braze."
channel: push

---

# Configurações de push {#push-settings}

> A página **Configurações de push** permite que você defina as principais configurações das notificações por push, incluindo o TTL (Push Time to Live) e a prioridade FCM padrão para Campaigns Android. Essas configurações ajudam a otimizar a entrega e a eficácia de suas notificações por push, garantindo uma melhor experiência para seus usuários.

## O que é Push TTL? {#what-is-push-ttl}

O TTL (Push Time to Live) controla por quanto tempo a Braze tentará entregar uma notificação por push a dispositivos que estejam offline no momento em que a Campaign for enviada. Se um dispositivo se reconectar após a expiração do TTL, a mensagem não será entregue. Essa configuração não removerá uma notificação se ela já tiver sido recebida pelo dispositivo do usuário — ela controla apenas por quanto tempo o provedor de push tenta entregar uma notificação.

## Configuração dos valores TTL padrão do push {#setting-default-push-ttl-values}

Por padrão, a Braze define o Push TTL como o máximo para cada serviço de envio de mensagens push.

| Serviço de envio de mensagens push | TTL máximo |
| --- | --- |
| Web (por meio de serviços FCM ou Push para a web) | 28 dias |
| Firebase Cloud Messaging (FCM) | 28 dias |
| Kindle (ADM) | 31 dias |
| Huawei (HMS) | 15 dias |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuração dos valores TTL padrão do push" }

Essas configurações se aplicam globalmente a todas as Campaigns de push, a menos que um TTL diferente seja definido para uma mensagem específica. Para ajustar o TTL de uma mensagem, consulte [Configurações avançadas de campanha]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#ttl).

Para definir um TTL de push padrão diferente:

1. Acesse **Settings** > **Manage Settings** > **Push Settings**.
2. Para cada plataforma Android, defina um valor padrão de TTL. Você pode definir incrementos menores, como horas ou segundos, para um controle mais preciso.
3. Selecione **Save** para aplicar suas alterações.

![Configurações de Push TTL para dispositivos Firebase, Web, Kindle e Huawei.]({% image_buster /assets/img/push_ttl.png %})

## Prioridade FCM padrão para Campaigns Android {#default-fcm-priority-for-android-campaigns}

Você pode definir a prioridade padrão do Firebase Cloud Messaging (FCM) para todas as Campaigns de push para Android. Essa prioridade determina como a notificação por push é entregue aos dispositivos dos usuários.

As opções de prioridade FCM incluem:

| Prioridade | Descrição | Caso de uso |
| --- | --- | --- |
| Normal | Prioridade de entrega padrão que otimiza o uso de bateria | Conteúdo que não exige atenção imediata |
| Alta | As mensagens são enviadas imediatamente | Notificações urgentes que exigem entrega imediata |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prioridade FCM padrão para Campaigns Android" }

Para definir a prioridade FCM padrão:

1. Acesse **Settings** > **Manage Settings** > **Push Settings**.
2. Na seção de prioridade FCM, selecione "Normal" ou "Alta" como configuração padrão.
3. Selecione **Save** para aplicar suas alterações.

![Configurações de prioridade de entrega para Android.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Essa configuração se aplica globalmente a todas as novas Campaigns de push para Android, a menos que uma prioridade diferente seja selecionada ao criar uma Campaign específica.

{% alert note %}
Se o FCM detectar que seu app envia frequentemente mensagens de alta prioridade que não resultam em notificações visíveis ao usuário ou em engajamento, essas mensagens poderão ser automaticamente rebaixadas para prioridade normal.
{% endalert %}

Para informações mais detalhadas sobre os níveis de prioridade FCM e a despriorização, consulte [Configurações avançadas de campanha]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#fcm-priority).