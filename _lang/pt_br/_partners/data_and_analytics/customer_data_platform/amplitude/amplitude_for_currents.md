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

A integração bidirecional entre a Braze e a Amplitude permite [sincronizar suas coortes da Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences), características de usuários e eventos na Braze, bem como aproveitar o Braze Currents para [exportar seus eventos da Braze para a Amplitude](#data-export-integration) a fim de realizar análises mais profundas dos dados de seu produto e marketing.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta na Amplitude | É necessária uma [conta na Amplitude](https://amplitude.com/) para aproveitar essa parceria. |
| Currents | Para exportar dados de volta para a Amplitude, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração de exportação de dados {#data-export-integration}

Uma lista completa dos eventos e propriedades de eventos que podem ser exportados da Braze para o Amplitude pode ser encontrada nas seções a seguir. Todos os eventos enviados ao Amplitude incluirão o `external_user_id` do usuário como o ID de usuário do Amplitude. As propriedades de eventos específicas da Braze serão enviadas sob a chave `event_properties` nos dados enviados ao Amplitude.

{% alert important %}
Para usar esse recurso, o ID de usuário do Amplitude deve corresponder ao ID externo da Braze.
{% endalert %}

A Braze enviará dados de eventos apenas para usuários que tenham o `external_user_id` definido ou para usuários anônimos que tenham o `device_id` definido. Para os usuários anônimos, será necessário sincronizar o ID de dispositivo do Amplitude com o ID de dispositivo da Braze no SDK or kit de desenvolvimento de software. Por exemplo:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Você pode exportar dois tipos de eventos para o Amplitude: [Eventos de engajamento com mensagem](#supported-currents-events), que consistem nos eventos da Braze diretamente relacionados ao envio de mensagens, e [Eventos de comportamento do cliente](#supported-currents-events), que incluem outras atividades no app ou website, como sessões, eventos personalizados e compras rastreadas pela plataforma. Todos os eventos regulares são prefixados com `[Appboy]`, e todos os eventos personalizados são prefixados com `[Appboy] [Custom Event]`. As propriedades de eventos personalizados e de compra são prefixadas com `[Custom event property]` e `[Purchase property]`, respectivamente.

{% alert note %}
O Braze Currents aplica o prefixo `[Appboy]` ao exportar eventos para o Amplitude. Esse rótulo faz referência ao nome legado do produto da Braze. Esse é o comportamento esperado e não indica um problema com o SDK or kit de desenvolvimento de software ou com a integração.
{% endalert %}

Todas as coortes nomeadas e importadas para a Braze serão prefixadas com `[Amplitude]` e terão como sufixo o `cohort_id`. Isso significa que uma coorte chamada "TEST_COHORT" com o `cohort_id` "abcd1234" será intitulada `[Amplitude] TEST_COHORT: abcd1234` nos filtros da Braze.

Entre em contato com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) se precisar de acesso a direitos adicionais de eventos.

### Etapa 1: Configurar a integração do Amplitude na Braze {#step-1-configure-amplitude-integration-in-braze}

No Amplitude, localize sua chave de API or interface de programação do aplicativo (API) de exportação do Amplitude.

{% alert warning %}
Mantenha sua chave de API or interface de programação do aplicativo (API) do Amplitude atualizada. Se as credenciais do seu conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão permanentemente perdidos.
{% endalert %}

### Etapa 2: Criar um Braze Current {#step-2-create-braze-current}

Na Braze, navegue até **Currents > + Create Current > Create Amplitude Export**. Forneça um nome de integração, e-mail de contato, chave de API or interface de programação do aplicativo (API) de exportação do Amplitude e região do Amplitude nos campos indicados. Em seguida, selecione os eventos que deseja rastrear; uma lista de eventos disponíveis será fornecida. Por último, clique em **Launch Current**.

{% alert note %}
Os eventos enviados do Braze Currents para o Amplitude contarão para a sua cota de volume de eventos do Amplitude.
{% endalert %}

![A página do Braze Amplitude Currents. Esta página inclui campos para nome da integração, e-mail de contato, chave de API e região dos EUA. A metade inferior da página do Currents lista os eventos disponíveis do Currents que você pode enviar.]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
Se você receber um erro "Invalid API or interface de programação do aplicativo (API) key" ao colar sua chave de API or interface de programação do aplicativo (API) do Amplitude, tente digitar a chave manualmente. Alguns navegadores podem adicionar caracteres ocultos ao copiar e colar, o que pode causar erros de validação.
{% endalert %}

{% tab note %}
Para saber mais, consulte a documentação do Amplitude sobre a [Integração Appboy Amplitude](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration).
{% endtab %}

## Limites de frequência {#rate-limits}

O Currents se conecta à API or interface de programação do aplicativo (API) HTTP da Amplitude, que possui um [limite de frequência](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 eventos/segundo por dispositivo e um limite não documentado de 500 mil eventos/dia por dispositivo. Se esses limites forem excedidos, a Amplitude fará o throttling dos eventos registrados pelo Currents. Se um dispositivo na sua integração exceder esse limite de frequência, você poderá perceber uma postergação no momento em que os eventos de todos os dispositivos aparecerão na Amplitude.

Os dispositivos não devem reportar mais de 30 eventos/segundo ou 500 mil eventos/dia em circunstâncias normais, e esse padrão de eventos só deve ocorrer devido a uma integração mal configurada. Para evitar esse tipo de postergação, certifique-se de que sua integração SDK or kit de desenvolvimento de software reporte eventos em uma taxa normal, conforme especificado em nossas instruções de integração SDK or kit de desenvolvimento de software, e evite executar testes automatizados que gerem muitos eventos para um único dispositivo.

## Eventos do Currents compatíveis {#supported-currents-events}

A Braze oferece suporte à exportação dos seguintes eventos para o Amplitude:

- [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Para ver a estrutura da carga útil de cada evento, selecione a guia **Amplitude** no [glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) e no [glossário de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).