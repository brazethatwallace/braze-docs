---
nav_title: Amplitude para Currents
article_title: Amplitude para Currents
page_order: 0
description: "Este artigo de referência descreve a parceria entre o Braze Currents e a Amplitude, uma plataforma de análise de dados e business intelligence de produtos."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude para Currents {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude-for-currents}

> A [Amplitude](https://amplitude.com/) é uma plataforma de análise de dados e business intelligence de produtos.

A integração bidirecional entre a Braze e a Amplitude permite [sincronizar suas coortes da Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/), características de usuários e eventos na Braze, bem como aproveitar o Braze Currents para [exportar seus eventos da Braze para a Amplitude](#data-export-integration) a fim de realizar análises mais profundas dos dados de seu produto e marketing.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Amplitude | É necessário ter uma [conta da Amplitude](https://amplitude.com/) para usar essa parceria. |
| Currents | Para exportar dados de volta para a Amplitude, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração de exportação de dados {#data-export-integration}

Uma lista completa dos eventos e das propriedades de eventos que podem ser exportados da Braze para a Amplitude pode ser encontrada nas seções a seguir. Todos os eventos enviados à Amplitude incluirão o `external_user_id` do usuário como ID de usuário da Amplitude. As propriedades de eventos específicas da Braze serão enviadas sob a chave `event_properties` nos dados enviados à Amplitude.

{% alert important %}
Para usar esse recurso, seu ID de usuário da Amplitude deve corresponder ao ID externo da Braze.
{% endalert %}

A Braze só enviará dados de eventos para usuários que tenham o `external_user_id` definido ou para usuários anônimos que tenham o `device_id` definido. Para os usuários anônimos, será necessário sincronizar o ID do dispositivo da Amplitude com o ID do dispositivo da Braze no SDK. Por exemplo:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Você pode exportar dois tipos de eventos para a Amplitude: [Eventos de engajamento com mensagens](#supported-currents-events), que consistem nos eventos da Braze diretamente relacionados ao envio de mensagens, e [eventos de comportamento do cliente](#supported-currents-events), incluindo outras atividades do app ou do site, como sessões, eventos personalizados e compras rastreadas por meio da plataforma. Todos os eventos regulares são prefixados com `[Appboy]`, e todos os eventos personalizados são prefixados com `[Appboy] [Custom Event]`. As propriedades de eventos personalizados e de compra têm os prefixos `[Custom event property]` e `[Purchase property]`, respectivamente.

Todas as coortes nomeadas e importadas para a Braze terão o prefixo `[Amplitude]` e o sufixo `cohort_id`. Isso significa que uma coorte chamada "TEST_COHORT" com o `cohort_id` "abcd1234" terá o título `[Amplitude] TEST_COHORT: abcd1234` nos filtros da Braze.

Entre em contato com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais.

### Etapa 1: Configurar a integração da Amplitude na Braze {#step-1-configure-amplitude-integration-in-braze}

Na Amplitude, localize sua chave de API de exportação da Amplitude.

{% alert warning %}
Mantenha sua chave de API da Amplitude atualizada. Se as credenciais do conector expirarem, ele deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

### Etapa 2: Criar um Braze Current {#step-2-create-braze-current}

Na Braze, navegue até **Currents > + Create Current > Create Amplitude Export**. Forneça um nome de integração, e-mail de contato, chave de API de exportação da Amplitude e região da Amplitude nos campos listados. Em seguida, selecione os eventos que deseja rastrear; é fornecida uma lista dos eventos disponíveis. Por fim, clique em **Launch Current**.

{% alert note %}
Os eventos enviados do Braze Currents para a Amplitude contarão para sua cota de volume de eventos da Amplitude.
{% endalert %}

![A página Braze Amplitude Currents. Essa página inclui campos para nome de integração, e-mail de contato, chave de API e região dos EUA. A metade inferior da página Currents lista os eventos Currents disponíveis que você pode enviar.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
Consulte a [documentação de integração](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) da Amplitude para saber mais.
{% endtab %}

## Limites de taxa {#rate-limits}

O Currents se conecta à API HTTP da Amplitude, que tem um [limite de taxa](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 eventos/segundo por dispositivo e um limite não documentado de 500 mil eventos/dia por dispositivo. Se esses limites forem excedidos, a Amplitude limitará os eventos registrados pelo Currents. Se um dispositivo em sua integração exceder esse limite de taxa, poderá haver um atraso no momento em que os eventos de todos os dispositivos aparecerem na Amplitude.

Os dispositivos não devem relatar mais de 30 eventos/segundo ou 500 mil eventos/dia em circunstâncias normais, e esse padrão de evento só deve ocorrer caso a integração tenha sido mal configurada. Para evitar esse tipo de atraso, confirme se sua integração de SDK relata eventos a uma taxa normal, conforme especificado nas nossas instruções de integração de SDK, e evite executar testes automatizados que gerem muitos eventos para um único dispositivo.

## Eventos Currents com suporte {#supported-currents-events}

A Braze suporta a exportação dos seguintes eventos para a Amplitude:

- [Eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

Para a estrutura da carga útil de cada evento, selecione a guia **Amplitude** no [glossário de eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) e no [glossário de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).