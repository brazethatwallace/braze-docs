---
nav_title: Contexto
article_title: Contexto
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Este artigo de referência explica como criar e usar etapas de Contexto no seu Canvas."
tool: Canvas

---

# Contexto {#context}

> As etapas de Contexto permitem criar e atualizar uma ou mais variáveis para um usuário conforme ele avança por um Canvas. Por exemplo, se você tem um Canvas que gerencia descontos sazonais, pode usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entra no Canvas.

## Como funciona {#how-it-works}

![Uma etapa de Contexto como primeira etapa de um Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

As etapas de Contexto permitem criar e usar dados temporários durante a jornada de um usuário em um Canvas específico. Esses dados existem apenas dentro daquela jornada do Canvas e não persistem em outros Canvas ou fora da sessão.

As variáveis de contexto existem apenas para aquela jornada específica do Canvas. Elas não alteram o perfil do usuário permanentemente e não aparecem em outros Canvas. Isso as torna ideais para informações temporárias que são relevantes apenas para uma campanha ou fluxo de trabalho específico.

{% alert tip %}
Para uma referência completa sobre variáveis de contexto, incluindo tipos de dados, uso e práticas recomendadas, consulte a [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).
{% endalert %}

Dentro de uma etapa de Contexto, você pode definir ou atualizar até 10 variáveis de contexto. Essas variáveis podem ser usadas para personalizar postergações, segmentar usuários dinamicamente e enriquecer o envio de mensagens em todo o Canvas. Por exemplo, você poderia criar uma variável de contexto para o horário de voo agendado de um usuário e depois usá-la para definir postergações personalizadas e enviar lembretes.

Você pode definir variáveis de contexto de duas formas:

- **Na entrada do Canvas:** As propriedades do evento personalizado ou do gatilho de API são automaticamente preenchidas como variáveis de contexto.
- **Em uma etapa de Contexto:** Defina ou atualize variáveis de contexto manualmente adicionando uma etapa de Contexto.

Cada variável de contexto requer um nome, um tipo de dado e um valor (definido usando Liquid ou a ferramenta Adicionar personalização). Quando definida, você pode referenciar variáveis de contexto em todo o Canvas usando Liquid, como {% raw %}`{{context.${flight_time}}}`{% endraw %}. No campo **Context variable name**, você também pode digitar o nome da variável de contexto ou selecioná-lo no menu suspenso do editor de etapas. Para mais detalhes, consulte a [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

Cada entrada no Canvas redefine as variáveis de contexto com base nos dados de entrada mais recentes e na configuração do Canvas, permitindo que os usuários tenham múltiplas jornadas ativas com seu próprio contexto. Por exemplo, se um cliente tem dois voos próximos, ele terá dois estados de jornada separados rodando simultaneamente&#8212;cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destino. Isso permite que você envie lembretes personalizados sobre o voo das 14h para Nova York enquanto envia atualizações diferentes sobre o voo das 8h para Los Angeles amanhã, de modo que cada mensagem permaneça relevante para a reserva específica.

### Processamento de usuários e lotes {#user-processing-and-batching}

As etapas de Contexto processam usuários em lotes para otimizar o desempenho. Quando os usuários entram em uma etapa de Contexto, a Braze os processa em lotes de 1.000 usuários por padrão. Esses lotes são processados em paralelo, mas dentro de cada lote, os usuários são processados sequencialmente.

Isso significa:

**Exemplo**: Se 3.500 usuários entram em uma etapa de Contexto com Connected Content que leva 650ms por usuário:
- A Braze cria 4 lotes de usuários (1.000, 1.000, 1.000 e 500 usuários neste exemplo).
- Cada lote processa os usuários sequencialmente, então um lote de 1.000 usuários leva aproximadamente 10,8 minutos (650 segundos; 1.000 × 650ms).
- Os lotes são concluídos em momentos diferentes, então os usuários vão chegando à próxima etapa conforme seu lote é finalizado.
- Os primeiros usuários podem alcançar a próxima etapa vários minutos antes dos últimos usuários, dependendo do tamanho do lote e dos tempos de resposta do Connected Content.

Sem Connected Content, as etapas de Contexto processam muito mais rápido porque não há chamadas de API externas para aguardar.

## Considerações {#considerations}

- Você pode definir até 10 variáveis de contexto por etapa de Contexto.
- Cada variável requer um nome único (apenas letras, números e underscores, com até 100 caracteres).
- O tamanho total de todas as variáveis em uma etapa não pode exceder 50 KB.
- Variáveis passadas por gatilhos de API compartilham o mesmo namespace das criadas em etapas de Contexto; redefinir uma variável em uma etapa de Contexto sobrescreve o valor da API.

Para mais detalhes e uso avançado, consulte a [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

## Criando uma etapa de Contexto {#creating-a-context-step}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Adicione uma etapa ao seu Canvas, depois arraste e solte o componente da barra lateral, ou selecione o botão de mais <i class="fas fa-plus-circle"></i> e selecione **Context**.

### Etapa 2: Definir as variáveis {#step-2-define-the-variables}

{% alert note %}
Você pode definir até 10 variáveis de contexto para cada etapa de Contexto.
{% endalert %}

Para definir uma variável de contexto:

1. Dê um **nome** à sua variável de contexto.
2. Selecione um [tipo de dado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types).
3. Escreva uma expressão Liquid manualmente ou use **Add Personalization** para criar um snippet Liquid a partir de atributos pré-existentes.
4. Selecione **prévia** para verificar o valor da sua variável de contexto.
5. (Opcional) Para adicionar variáveis adicionais, selecione **Add Context variable** e repita as etapas 1-4.
6. Quando terminar, selecione **Done**.

Agora você pode usar sua variável de contexto em qualquer lugar que use Liquid, como em etapas de Mensagem e Atualização de usuário, selecionando **Add Personalization**. No campo **Context variable name**, você também pode digitar o nome da variável de contexto ou selecioná-lo no menu suspenso do editor de etapas. Para um passo a passo completo, consulte a [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

{% alert important %}
Ao referenciar variáveis de contexto, sempre use o formato {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filtros de variáveis de contexto {#context-variable-filters}

Você pode criar filtros usando variáveis de contexto em etapas de [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) e [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split).

Para direcionar usuários com base na resposta de uma [etapa de Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), adicione a etapa de Agente antes da sua etapa de Jornadas do público ou Divisão de decisão. A etapa de Agente armazena sua saída no contexto do Canvas, que você pode avaliar com filtros de variáveis de contexto nessas etapas de Branch.

Se o agente retornar um objeto e você quiser filtrar por uma propriedade aninhada, insira o caminho no campo **Context variable name** usando notação de ponto em vez de apenas o nome da variável de nível superior (por exemplo, `intent_agent.persona` quando `persona` está aninhado sob `intent_agent`).

Para configuração de filtros, lógica de comparação e exemplos avançados, consulte a [Referência de variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Pré-visualizando jornadas de usuários {#previewing-user-paths}

Recomendamos testar e [pré-visualizar suas jornadas de usuários]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para garantir que suas mensagens sejam enviadas ao público certo e que as variáveis de contexto sejam avaliadas com os resultados esperados.

{% alert note %}
Se você estiver pré-visualizando seu Canvas na seção **prévia & Test Send** do editor, o timestamp na pré-visualização da mensagem de teste **não** é padronizado para UTC porque esse painel gera pré-visualizações como strings. Isso significa que, se um Canvas estiver configurado para aceitar um objeto `time`, a pré-visualização da mensagem não reflete com precisão o que ocorre quando o Canvas está ativo. Para testar seu Canvas com mais precisão, recomendamos pré-visualizar as jornadas de usuários.
{% endalert %}

Observe quaisquer cenários comuns que criam variáveis de contexto inválidas. Ao pré-visualizar a jornada do usuário, você pode ver os resultados de etapas de postergação personalizadas usando variáveis de contexto, e quaisquer comparações de etapas de público ou decisão que correspondam usuários a variáveis de contexto.

Se a variável de contexto for válida, você pode referenciá-la em todo o seu Canvas. No entanto, se a variável de contexto não foi criada corretamente, as etapas futuras do seu Canvas também não funcionarão corretamente. Por exemplo, se você criar uma etapa de Contexto para atribuir aos usuários um horário de consulta e definir o valor do horário da consulta como uma data passada, o e-mail de lembrete na sua etapa de Mensagem não será enviado.

## Convertendo strings de Connected Content para JSON {#converting-connected-content-strings-to-json}

Ao fazer uma [chamada de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) em uma etapa de Contexto, o JSON retornado da chamada é avaliado como um tipo de dado string para consistência e prevenção de erros. Se você quiser converter essa string em JSON, use `as_json_string`. Por exemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Solução de problemas {#troubleshooting}

### Variáveis de contexto inválidas {#invalid-context-variables}

Uma variável de contexto é considerada inválida quando:

- Uma chamada a um Connected Content incorporado falha.
- A expressão Liquid em tempo de execução retorna um valor que não corresponde ao tipo de dado ou está vazio (nulo).

Por exemplo, se o tipo de dado da variável de contexto for **Number**, mas a expressão Liquid retornar uma string, ela será inválida.

Nessas circunstâncias:
- O usuário avança para a próxima etapa.
- A análise de dados da etapa do Canvas conta isso como _Not Updated_.

Ao solucionar problemas, monitore a métrica _Not Updated_ para verificar se sua variável de contexto está sendo atualizada corretamente. Se a variável de contexto for inválida, seus usuários podem continuar no Canvas após a etapa de Contexto, mas podem não se qualificar para etapas posteriores.

Consulte [Tipos de dados]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types) para ver exemplos de configuração para cada tipo de dado.

### Atrasos no envio com Connected Content {#delays-in-sending-with-connected-content}

Todos os usuários em um lote são processados antes que qualquer usuário avance. Após a conclusão do processamento do lote, os usuários bem-sucedidos passam para a próxima etapa, enquanto os usuários com falha são reprocessados separadamente — os usuários bem-sucedidos não esperam que as tentativas de reprocessamento sejam concluídas antes de avançar.

#### Comportamento de reprocessamento {#retry-behavior}

Em etapas do Canvas (incluindo etapas de Contexto), a Braze usa mecanismos de reprocessamento específicos do Canvas em vez do comportamento padrão de reprocessamento do Connected Content. Se uma chamada de Connected Content falhar:

 - Para etapas de Mensagem, as chamadas de Connected Content podem ser reprocessadas até cinco vezes.
 - Para todas as outras etapas, a Braze reprocessa a etapa aproximadamente 13 vezes com backoff exponencial.

Se todas as tentativas falharem, o usuário sai do Canvas.

A tag `:retry` usada no Connected Content padrão não se aplica a chamadas de Connected Content feitas dentro de etapas do Canvas. As etapas do Canvas têm sua própria lógica de reprocessamento otimizada para fluxos de trabalho do Canvas.

O tempo necessário para processar todos os usuários em uma etapa de Contexto depende de:

- O número de usuários entrando na etapa
- Se o Connected Content é usado (e seu tempo de resposta)
- O tamanho do lote (padrão de 1.000 usuários por lote)

Se o seu endpoint de Connected Content tem limites de frequência, considere que as etapas de Contexto processam usuários sequencialmente dentro de cada lote, o que ajuda a respeitar os limites de frequência naturalmente. No entanto, múltiplos lotes são processados em paralelo, então garanta que seu endpoint possa lidar com solicitações simultâneas de múltiplos lotes.

## Padronização de consistência de fuso horário {#time-zone-consistency-standardization}

Com o Contexto do Canvas disponível de forma geral, todas as propriedades de evento de timestamp padrão em Canvas baseados em ação estão em UTC. Essa mudança faz parte de um esforço mais amplo para garantir uma experiência mais previsível e consistente ao editar etapas e mensagens do Canvas. Observe que essa mudança impacta todos os Canvas baseados em ação, independentemente de o Canvas específico estar usando uma etapa de Contexto ou não.

{% alert important %}
Em todas as circunstâncias, recomendamos fortemente o uso de [filtros Liquid time_zone]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) para que os timestamps sejam representados no fuso horário desejado. Você pode consultar esta [pergunta frequente](#faq-example) para ver um exemplo.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### O que mudou desde que o Contexto do Canvas ficou disponível de forma geral? {#what-has-changed-since-canvas-context-became-generally-available}

Agora que o Contexto do Canvas está disponível de forma geral, os seguintes detalhes se aplicam:

- Todos os timestamps com um [tipo datetime]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) de [propriedades de evento de gatilho]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) em Canvas baseados em ação estão em [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Essa mudança impacta todos os Canvas baseados em ação, independentemente de o Canvas específico estar usando uma etapa de Contexto ou não.

#### Qual é o motivo dessa mudança? {#what-is-the-reason-for-this-change}

Essa mudança faz parte de um esforço mais amplo para criar uma experiência mais previsível e consistente ao editar etapas e mensagens do Canvas.

#### Canvas disparados por API ou agendados são impactados por essa mudança? {#are-api-triggered-or-scheduled-canvases-impacted-by-this-change}

Não.

#### Essa mudança impacta as propriedades de entrada do Canvas? {#does-this-change-impact-canvas-entry-properties}

Sim, isso impacta `canvas_entry_properties` se a `canvas_entry_property` estiver sendo usada em um Canvas baseado em ação e o tipo da propriedade for `time`. Em todas as circunstâncias, recomendamos usar filtros Liquid `time_zone` para que os timestamps sejam representados no fuso horário desejado.

Veja um exemplo de como fazer isso:

| Liquid na etapa de Mensagem | Saída | Esta é a forma correta de representar fusos horários em Liquid? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Não |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Não |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Essa mudança impacta as propriedades de entrada do Canvas?" }

#### Qual é um exemplo prático de como o novo comportamento de timestamp pode afetar minhas mensagens? {#faq-example}

Digamos que temos um Canvas baseado em ação com o seguinte conteúdo em uma etapa de Mensagem:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Isso resulta na seguinte mensagem:

```
Your appointment is scheduled for 2025-08-05 4:15 PM, we’ll see you then!
```

Como nenhum fuso horário é especificado usando Liquid, o timestamp aqui está em UTC.

Para especificar um fuso horário claramente, podemos usar filtros Liquid `time_zone` assim:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Isso resulta na seguinte mensagem:

```
Your appointment is scheduled for 2025-08-05 8:15 AM, we'll see you then!
```

Como o fuso horário America/Los Angeles é especificado usando Liquid, o timestamp aqui está em PST.

O fuso horário preferido também pode ser enviado na carga útil das propriedades do evento e usado na lógica Liquid:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### Como as variáveis de contexto diferem das propriedades de entrada do Canvas? {#how-do-context-variables-differ-from-canvas-entry-properties}

As propriedades de entrada do Canvas são incluídas como variáveis de contexto do Canvas. Isso significa que você pode enviar propriedades de entrada do Canvas usando a API da Braze e referenciá-las em outras etapas, de forma semelhante ao uso de uma variável de contexto com o snippet Liquid.

### As variáveis podem referenciar umas às outras em uma única etapa de Contexto? {#can-variables-reference-each-other-in-a-singular-context-step}

Sim. Todas as variáveis em uma etapa de Contexto são avaliadas em sequência, o que significa que você poderia ter as seguintes variáveis de contexto configuradas:

| Variável de contexto | Valor | Descrição |
|---|---|---|
| `favorite_cuisine` | {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | O tipo de culinária favorita do usuário. |
| `promo_code` | {% raw %}`EATFRESH`{% endraw %} | O código de desconto disponível para o usuário. |
| `personalized_message` | {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Uma mensagem personalizada que combina as variáveis anteriores. Em uma etapa de Mensagem, você poderia usar o snippet Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para referenciar a variável de contexto e entregar uma mensagem personalizada a cada usuário. Você também poderia usar uma etapa de Contexto para salvar o valor do [código promocional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create) e usá-lo como modelo em outras etapas ao longo do Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="As variáveis podem referenciar umas às outras em uma única etapa de Contexto?" }

Isso também se aplica entre múltiplas etapas de Contexto. Por exemplo, imagine esta sequência:

1. Uma etapa de Contexto inicial cria uma variável chamada `JobInfo` com o valor `job_title`.
2. Uma etapa de Mensagem referencia {% raw %}`{{context.${JobInfo}}}`{% endraw %} e exibe `job_title` para o usuário.
3. Depois, uma etapa de Contexto atualiza a variável de contexto, alterando o valor de `JobInfo` para `job_description`.
4. Todas as etapas subsequentes que referenciam `JobInfo` agora usam o valor atualizado `job_description`.

As variáveis de contexto usam seu valor mais recente em todo o Canvas, e cada atualização afeta todas as etapas seguintes que referenciam essa variável.