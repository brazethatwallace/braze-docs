---
nav_title: Propriedades de contexto e evento
article_title: Propriedades de contexto e evento
page_order: 4.2
page_type: reference
description: "Este artigo de referência descreve as diferenças entre propriedades de contexto e de evento, e quando usar cada uma."
tool: Canvas
---

# Propriedades de contexto e evento {#context-and-event-properties}

> Este artigo de referência aborda informações sobre `context` e `event_properties`, incluindo quando usar cada propriedade e as diferenças de comportamento. <br><br> Para informações gerais sobre propriedades de eventos personalizados, confira [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

As propriedades de contexto e as propriedades de evento funcionam de maneira diferente nos seus fluxos de trabalho do Canvas. As propriedades de eventos ou chamadas de API que disparam a entrada de um usuário em um Canvas são conhecidas como `context`. As propriedades de eventos que ocorrem enquanto um usuário avança em uma jornada do Canvas são conhecidas como `event_properties`. A diferença principal é que `context` vai além dos eventos, acessando também as propriedades das cargas úteis de entrada em Canvas disparados por API.

Consulte a tabela a seguir para um resumo das diferenças entre propriedades de contexto e de evento.

| | Propriedades de contexto | Propriedades de evento |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistência** | Podem ser referenciadas por todas as etapas de [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) durante toda a duração de um Canvas criado usando o Canvas. | - Só podem ser referenciadas uma vez. <br> - Não podem ser referenciadas por etapas de Mensagem subsequentes. |
| **Comportamento no Canvas** | Podem referenciar `context` em qualquer etapa de um Canvas. Para o comportamento pós-lançamento, consulte [Editando Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/#canvas-entry-properties). | - Podem referenciar `event_properties` na primeira etapa de Mensagem **após** uma etapa de [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) em que a ação realizada é um evento personalizado ou evento de compra. <br> - Não podem estar após a jornada Restante do público da etapa de Jornadas de ação. <br> - Podem ter outros componentes que não sejam de Mensagem entre as etapas de Jornadas de ação e Mensagem. Se um desses componentes que não são de Mensagem for uma etapa de Jornadas de ação, o usuário pode passar pela jornada Restante do público dessa etapa. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Context and event properties" }

{% details Detalhes do editor original do Canvas %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Observe que o contexto do Canvas não é compatível com o editor original do Canvas, então esta seção está disponível como referência ao usar propriedades de entrada do Canvas e propriedades de evento no fluxo de trabalho anterior do Canvas.

**Propriedades de entrada do Canvas:**
- É necessário ter as propriedades de entrada persistentes ativadas.
- Só podem referenciar `canvas_entry_properties` na primeira etapa completa de um Canvas. O Canvas deve ser baseado em ação ou disparado por API.

**Propriedades de entrada:**
- Podem referenciar `event_properties` em qualquer etapa completa que use entrega baseada em ação em um Canvas.
- Não podem ser usadas em etapas completas agendadas, exceto na primeira etapa completa de um Canvas baseado em ação. No entanto, se um usuário estiver usando um [componente do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/), o comportamento segue as regras atuais do fluxo de trabalho do Canvas para `event_properties`.

**Propriedades de evento:**
- Não é possível usar `event_properties` na etapa de Mensagem inicial. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de Jornadas de ação com o evento correspondente **antes** da etapa de Mensagem que inclui `event_properties`.

{% enddetails %}

### Informações importantes {#things-to-know}

- O contexto está disponível apenas para referência em Liquid. Para filtrar pelas propriedades dentro do Canvas, use a [segmentação por propriedade de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/).
- Para canais de mensagem no app, você pode referenciar `context` e `event_properties` em um Canvas. `event_properties` podem ser acessadas quando incluídas na primeira etapa do Canvas, pois são baseadas em gatilho.
- Não é possível usar `event_properties` na etapa de Mensagem inicial. Em vez disso, você pode usar `context` ou adicionar uma etapa de Jornadas de ação com o evento correspondente **antes** da etapa de Mensagem que inclui `event_properties`.
- Quando uma etapa de Jornadas de ação contém um gatilho "Enviou uma mensagem de entrada por SMS" ou "Enviou uma mensagem de entrada por WhatsApp", as etapas subsequentes do Canvas podem incluir uma propriedade Liquid de SMS ou WhatsApp. Isso reflete o funcionamento das propriedades de evento em Canvas. Dessa forma, você pode aproveitar suas mensagens para salvar e referenciar dados primários em perfis de usuário e no envio de mensagens conversacionais.

{% alert note %}
A elegibilidade do público é avaliada uma vez na entrada do Canvas. Se um usuário for mesclado durante a entrada, o usuário identificado continua pelo Canvas e não é reavaliado em relação aos critérios de segmento do Canvas.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Timestamps para gatilhos {#timestamps-for-triggers}

Se você estiver usando timestamps com um [tipo datetime]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/) de eventos que disparam Canvas baseados em ação, que são referenciados usando [contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/), os timestamps são normalizados para UTC.

Considerando esse comportamento, a Braze recomenda fortemente que você use um filtro de fuso horário do Liquid como no exemplo a seguir para garantir que suas mensagens sejam enviadas com o [fuso horário de sua preferência]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

## Caso de uso {#use-case}

![Uma etapa de Jornadas de ação seguida por uma etapa de postergação e uma etapa de Mensagem para usuários que adicionaram um item à lista de desejos, e uma jornada para o restante do público.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para entender melhor as diferenças entre `context` e `event_properties`, vamos considerar este cenário em que os usuários entram em um Canvas baseado em ação ao realizarem o evento personalizado "adicionar item à lista de desejos".

O contexto é configurado na etapa [Cronograma de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) da criação de um Canvas e corresponde ao momento em que um usuário entra em um Canvas. O contexto também pode ser referenciado em qualquer etapa de Mensagem.

Neste Canvas, temos uma jornada de usuário que começa com uma etapa de Jornadas de ação para determinar se um usuário adicionou um item à lista de desejos. A partir daí, se o usuário adicionou um item, ele passa por uma postergação antes de receber a mensagem "Novo item na sua lista de desejos!" da etapa de Mensagem.

A primeira etapa de Mensagem em uma jornada de usuário tem acesso às `event_properties` personalizadas da sua etapa de Jornadas de ação. Neste caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` nesta etapa de Mensagem como parte do conteúdo da nossa mensagem. Se um usuário não adicionar um item à lista de desejos, ele segue pela jornada Restante do público, o que significa que as `event_properties` não podem ser referenciadas e resultam em um erro de configuração inválida.

Observe que você só terá acesso às `event_properties` se sua etapa de Mensagem puder ser rastreada até uma jornada que não seja Restante do público em uma etapa de Jornadas de ação. Se a etapa de Mensagem estiver conectada a uma jornada Restante do público, mas puder ser rastreada até uma etapa de Jornadas de ação na jornada do usuário, você ainda terá acesso às `event_properties`. Para saber mais sobre esses comportamentos, consulte [Etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/).