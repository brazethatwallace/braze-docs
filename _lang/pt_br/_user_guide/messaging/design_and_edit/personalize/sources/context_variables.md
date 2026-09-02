---
nav_title: Variáveis de contexto
article_title: Variáveis de contexto
page_type: reference
description: "Este artigo de referência explica as variáveis de contexto nos Canvas da Braze, incluindo seus tipos, uso e práticas recomendadas."
---

# Variáveis de contexto {#context-variables}

> Variáveis de contexto são dados temporários que você pode criar e usar durante a jornada de um usuário em um Canvas específico. Elas permitem personalizar postergações, segmentar usuários dinamicamente e enriquecer o envio de mensagens sem alterar permanentemente as informações do perfil de um usuário. As variáveis de contexto existem apenas dentro da sessão do Canvas e não persistem entre Canvas diferentes ou fora da sessão.

## Como as variáveis de contexto funcionam {#how-context-variables-work}

As variáveis de contexto podem ser definidas de duas formas:

- **Na entrada do Canvas:** quando os usuários entram em um Canvas, os dados do evento ou do gatilho de API or interface de programação do aplicativo (API) podem preencher automaticamente as variáveis de contexto.
- **Em uma etapa de Contexto:** você pode definir ou atualizar variáveis de contexto manualmente dentro do Canvas adicionando uma [etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context).

Cada variável de contexto inclui:

- Um nome (como `flight_time` ou `subscription_renewal_date`)
- Um tipo de dado (como número, string, horário ou array)
- Um valor que você atribui usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou pela ferramenta **Add Personalization**.

Depois de definida, você pode usar uma variável de contexto em todo o Canvas referenciando-a neste formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por exemplo, {% raw %}`{{context.${flight_time}}}`{% endraw %} poderia retornar o horário de voo programado do usuário.

Cada vez que um usuário entra no Canvas — mesmo que já tenha entrado antes — as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Essa abordagem com estado permite que cada entrada no Canvas mantenha seu próprio contexto independente, possibilitando que os usuários tenham múltiplos estados ativos dentro da mesma jornada, mantendo o contexto específico de cada estado.

Por exemplo, se um cliente tem dois voos próximos, ele terá dois estados de jornada separados rodando simultaneamente — cada um com suas próprias variáveis de contexto específicas do voo, como horário de partida e destino. Isso permite que você envie lembretes personalizados sobre o voo das 14h para Nova York enquanto envia atualizações diferentes sobre o voo das 8h para Los Angeles no dia seguinte, de modo que cada mensagem permaneça relevante para a reserva específica.

## Considerações {#considerations}

Você pode definir até 10 variáveis de contexto por [etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context). Cada nome de variável pode ter até 100 caracteres e deve usar apenas letras, números ou underscores.

As definições de variáveis de contexto podem ter até 10.240 caracteres. Se você passar variáveis de contexto para um Canvas disparado por API or interface de programação do aplicativo (API), elas compartilham o mesmo namespace das variáveis criadas em uma etapa de Contexto. Por exemplo, se você enviar uma variável `purchased_item` no objeto de contexto do [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), poderá referenciá-la como {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Se você redefinir essa variável em uma etapa de Contexto, o novo valor substituirá o valor da API or interface de programação do aplicativo (API) para a jornada daquele usuário.

Você pode armazenar até 50 KB por etapa de Contexto, distribuídos em até 10 variáveis. Se o tamanho total de todas as variáveis em uma etapa exceder 50 KB, as variáveis que ultrapassarem o limite não serão avaliadas nem armazenadas. Por exemplo, se você tiver três variáveis em uma etapa de Contexto:

- Variável 1: 30 KB
- Variável 2: 19 KB
- Variável 3: 2 KB

A Variável 3 não será avaliada nem armazenada porque a soma das variáveis anteriores excede 50 KB.

## Tipos de dados {#data-types}

As variáveis de contexto criadas ou atualizadas na etapa podem receber os seguintes tipos de dados.

{% alert note %}
As variáveis de contexto têm os mesmos formatos esperados para tipos de dados que as [propriedades de evento]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#expected-format). <br><br>Ao usar o tipo array, a Braze tenta analisar o valor como JSON, o que permite que arrays de objetos sejam criados com sucesso. Se os objetos dentro dos seus arrays não forem JSON válido, o resultado será um array simples de strings. <br><br>Para objetos aninhados e arrays de objetos, use o [filtro Liquid `as_json_string`](#converting-connected-content-strings-to-json). Se você estiver criando o mesmo objeto em uma etapa de Contexto, precisará renderizar o objeto usando `as_json_string`, como {%raw%}`{{context.${object_array} | as_json_string }}`{%endraw%}
{% endalert %}

| Tipo de dado | Exemplo de nome de variável | Exemplo de valor |
|---|---|---|
| Booleano | loyalty_program |{% raw %}<code>true</code>{% endraw %}|
| Número | credit_score |{% raw %}<code>740</code>{% endraw %}|
| String | product_name |{% raw %}<code>green_tea</code>{% endraw %} |
| Array | favorite_products |{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
| Array (de objetos) | pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
| Horário (em UTC) | last_purchase_date |{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
| Objeto (achatado) | user_profile |{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de dados" }

Por padrão, o tipo de dado de horário está em UTC. Se você usar um tipo de dado string para armazenar um valor de horário, poderá definir o horário em um fuso horário diferente, como PST.

Por exemplo, se você estiver enviando uma mensagem a um usuário no dia anterior ao aniversário dele, salvaria a variável de contexto como tipo de dado de horário, pois há lógica Liquid associada ao envio no dia anterior. No entanto, se você estiver enviando uma mensagem de feriado no Natal (25 de dezembro), não precisaria referenciar o horário como uma variável dinâmica, então usar um tipo de dado string seria preferível.

Para tipos de dados de objeto, você pode usar notação de ponto para especificar um caminho pelos dados. Por exemplo, se sua etapa de Contexto definir uma variável de contexto `order_summary` com esta estrutura:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

Em um filtro de [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split), insira o caminho como o nome da variável de contexto usando notação de ponto (por exemplo, `order_summary.shipping.carrier`). Quando o filtro for avaliado, a Braze resolverá esse caminho para o valor `overnight`.

Em Liquid (como em uma etapa de [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)), use {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %} em vez disso.

## Usando variáveis de contexto {#using-context-variables}

Você pode usar variáveis de contexto em qualquer lugar onde usar Liquid em um Canvas, como nas etapas de [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) e [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update), selecionando **Add Personalization**. Para mensagens no app e Banners nas etapas de Mensagem, você pode selecionar variáveis de contexto para determinar quando a mensagem deve expirar.

Por exemplo, digamos que você queira notificar passageiros sobre o acesso ao lounge VIP antes do próximo voo. Essa mensagem deve ser enviada apenas para passageiros que compraram passagem de primeira classe. Uma variável de contexto é uma forma flexível de rastrear essa informação.

Os usuários entrarão no Canvas quando comprarem uma passagem de avião. Para determinar a elegibilidade de acesso ao lounge, criaremos uma variável de contexto chamada `lounge_access_granted` em uma etapa de Contexto e, em seguida, referenciaremos essa variável de contexto nas etapas subsequentes da jornada do usuário.

![Variável de contexto configurada para rastrear se um passageiro se qualifica para acesso ao lounge VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Nesta etapa de Contexto, usaremos {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar se o tipo de voo comprado é `first_class`.

Em seguida, criaremos uma etapa de Mensagem para direcionar usuários onde {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} é `true`. Essa mensagem será uma notificação por push que inclui informações personalizadas do lounge. Com base nessa variável de contexto, os passageiros elegíveis receberão as mensagens relevantes antes do voo.

- Passageiros com passagem de primeira classe receberão: "Aproveite o acesso exclusivo ao lounge VIP!"
- Passageiros de classe executiva e econômica receberão: "Faça upgrade do seu voo para ter acesso exclusivo ao lounge VIP."

![Uma etapa de Mensagem com diferentes mensagens para enviar, dependendo do tipo de passagem de avião comprada.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Você pode adicionar [opções de postergação personalizadas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) com as informações da etapa de Contexto, o que significa que você pode selecionar a variável que posterga os usuários.
{% endalert %}

### Para jornadas de ação e critérios de saída {#for-action-paths-and-exit-criteria}

Você pode alavancar filtros de comparação de propriedades com variáveis de contexto ou atributos personalizados nestas ações-gatilho: **Perform Custom Event** e **Make Purchase**. Esses gatilhos de ação também suportam filtros de propriedade para propriedades básicas e aninhadas.

- Ao comparar com propriedades básicas, as comparações disponíveis corresponderão ao tipo da propriedade definida pelo evento personalizado. Por exemplo, propriedades de string terão correspondência exata e correspondência regex. Propriedades booleanas serão verdadeiro ou falso.
- Ao comparar com propriedades aninhadas, os tipos não são pré-definidos, então você pode selecionar comparações entre múltiplos tipos de dados para booleanos, números, strings, horário e dia do ano, semelhante às comparações para atributos personalizados aninhados. Se você selecionar um tipo de dado que não corresponda ao tipo de dado real da propriedade aninhada no momento da comparação, o usuário não corresponderá à jornada de ação ou aos critérios de saída.

#### Exemplos de jornada de ação {#action-path-examples}

{% alert important %}
Para comparações de atributos personalizados, usaremos o valor do atributo personalizado no momento em que a ação é realizada. Isso significa que um usuário não corresponderá ao grupo da jornada de ação se não tiver esse atributo personalizado preenchido no momento da comparação, ou se o valor do atributo personalizado não corresponder às comparações de propriedade definidas. Isso vale mesmo que o usuário tivesse correspondido quando entrou na etapa de jornada de ação.
{% endalert %}

{% tabs %}
{% tab Realizar evento personalizado %}

A seguinte jornada de ação está configurada para classificar usuários que realizaram o evento personalizado `Account_Created` com a propriedade básica `source` para a variável de contexto `app_source_variable`.

![Um exemplo de jornada de ação que referencia uma variável de contexto ao realizar um evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Fazer compra %}

A seguinte jornada de ação está configurada para corresponder a propriedade básica `brand` para o nome de produto específico `shoes` a uma variável de contexto `promoted_shoe_brand`.

![Um exemplo de jornada de ação que referencia uma variável de contexto ao fazer uma compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemplos de critérios de saída {#exit-criteria-examples}

{% tabs %}
{% tab Realizar evento personalizado %}

Os critérios de saída determinam que, em qualquer ponto da jornada do usuário no Canvas, ele sairá do Canvas se:

- Realizar o evento personalizado **Abandon Cart**, e
- A propriedade básica **Item in Cart** corresponder ao valor da string da variável de contexto `cart_item_threshold`.

![Critérios de saída configurados para remover um usuário se ele realizar um evento personalizado com base na variável de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Fazer compra %}

Os critérios de saída determinam que, em qualquer ponto da jornada do usuário no Canvas, ele sairá do Canvas se:

- Fizer uma compra específica para o nome de produto "book", e
- A propriedade aninhada dessa compra "loyalty_program" for igual ao atributo personalizado do usuário "VIP".

![Critérios de saída configurados para remover um usuário se ele fizer uma compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Definir uma expiração {#set-an-expiration}

Para [Banners]({{site.baseurl}}/user_guide/channels/banners) e [mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages) em uma etapa de [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) do Canvas, selecione **A duration after the step is available** para expiração e, em seguida, ative **Personalize duration** para controlar a janela de disponibilidade a partir de uma variável de contexto — por exemplo, para corresponder a uma promoção ou duração de reserva de uma etapa de Contexto.

**Personalize duration** se aplica a essa opção de expiração baseada em duração. Se você escolher **On a specific date and time**, defina a expiração usando os controles de data e hora.

### Postergações de jornada de ação {#action-path-delays}

Em uma etapa de [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), em **Evaluation Window**, ative **Personalize delay** para definir por quanto tempo os usuários ficam retidos na etapa a partir de uma variável de contexto. Use isso quando o período de espera deve variar por usuário com base em detalhes como nível ou região.

### Filtros de variáveis de contexto {#context-variable-filters}

Você pode criar filtros que usam variáveis de contexto declaradas anteriormente nas etapas de [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) e [divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split).

{% alert note %}
Os filtros de variáveis de contexto estão disponíveis apenas para as etapas de jornadas do público e divisão de decisão.
{% endalert %}

As variáveis de contexto são declaradas e acessíveis apenas no escopo de um Canvas, o que significa que não podem ser referenciadas em Segments. Os filtros de variáveis de contexto funcionam de forma semelhante nas etapas de jornadas do público e divisão de decisão — as etapas de jornadas do público representam múltiplos grupos, enquanto as etapas de divisão de decisão representam decisões binárias.

![Exemplo de etapa de divisão de decisão com a opção de criar um filtro com uma variável de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Assim como as variáveis de contexto do Canvas têm tipos pré-definidos, as comparações entre variáveis de contexto e valores estáticos devem ter [tipos de dados correspondentes]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). O filtro de variável de contexto permite comparações entre múltiplos tipos de dados para booleanos, números, strings, horário e dia do ano, semelhante às comparações para [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

Aqui está um exemplo de um filtro de variável de contexto comparando a variável de contexto `product_name` com o regex `/braze/`.

![Uma configuração de filtro para a variável de contexto "product_name" para corresponder ao regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Filtros de dia do ano e horário para variáveis de contexto de data {#day-of-year-and-time-filters-for-date-context-variables}

Para usar filtros de comparação de **Dia do ano** ou **Horário** com uma variável de contexto:

1. Adicione uma [etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) que defina uma variável de contexto como uma data do calendário (por exemplo, 23 de outubro de 2025).
2. Adicione uma etapa de [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) após a etapa de Contexto.
3. Na etapa de jornadas do público, adicione um filtro que divida os usuários com base nessa variável de contexto.
4. Escolha uma comparação da categoria **Dia do ano** ou **Horário**.

Se uma variável de contexto não tiver tipo declarado, a Braze mostrará todos os tipos de comparação disponíveis no menu suspenso, incluindo **Dia do ano** e **Horário**. Se a variável for declarada como tipo **horário** na etapa de Contexto, apenas as comparações de **Dia do ano** e **Horário** serão exibidas. Para outros tipos de dados com tipo conhecido (por exemplo, um atributo personalizado aninhado com tipo de horário), apenas as comparações aplicáveis a esse tipo serão exibidas.

{% alert note %}
Use o mesmo tipo de dado para sua variável de contexto e comparação. Por exemplo, se sua variável de contexto for do tipo de dado de horário, use comparações de horário (como "antes" ou "depois"). Usar tipos de dados incompatíveis (como comparações de string com uma variável de contexto de horário) pode causar comportamento inesperado.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

#### Comparando com variáveis de contexto ou atributos personalizados {#comparing-to-context-variables-or-custom-attributes}

Ao selecionar o botão **Compare to a context variable or custom attribute**, você pode construir filtros de variáveis de contexto que comparam com variáveis de contexto definidas anteriormente ou atributos personalizados do usuário. Isso pode ser útil para realizar comparações dinâmicas por usuário, como `context` disparado por API or interface de programação do aplicativo (API), ou para condensar lógica de comparação complexa definida entre variáveis de contexto.

{% tabs %}
{% tab Exemplo 1 %}

Digamos que você queira enviar um lembrete personalizado aos usuários após um período dinâmico de inatividade. Qualquer pessoa que não tenha feito login no seu app nos últimos três dias deve receber uma mensagem.

Você tem uma variável de contexto `re_engagement_date` definida como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Note que `3 days` pode ser um valor variável que também é armazenado como atributo personalizado do usuário. Então, se a `re_engagement_date` for posterior à `last_login_date` (armazenada como atributo personalizado no perfil do usuário), a mensagem será enviada.

![Uma configuração de filtro com atributos personalizados como tipo de personalização para a variável de contexto "re_engagement_date" após o atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Exemplo 2 %}

O filtro a seguir compara a variável de contexto `reminder_date` para ser anterior à variável de contexto `appointment_deadline`. Isso pode ajudar a agrupar usuários em uma etapa de jornadas do público para determinar se eles devem receber lembretes adicionais antes do prazo do compromisso.

![Uma configuração de filtro com variáveis de contexto como tipo de personalização para a variável de contexto "reminder_date" na variável de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Padronização de consistência de fuso horário {#time-zone-consistency-standardization}

Embora a maioria das propriedades de evento que usam o tipo timestamp já esteja em UTC no Canvas, existem algumas exceções. Com a adição do Contexto do Canvas, todas as propriedades de evento de timestamp padrão em Canvas baseados em ação serão consistentemente em UTC. Essa mudança faz parte de um esforço mais amplo para garantir uma experiência mais previsível e consistente ao editar etapas e mensagens do Canvas. Note que essa mudança impactará todos os Canvas baseados em ação, independentemente de o Canvas específico estar usando uma etapa de Contexto ou não.

{% alert important %}
Em todas as circunstâncias, recomendamos fortemente o uso de [filtros Liquid de time_zone]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) para que os timestamps sejam representados no fuso horário desejado. Você pode consultar esta [pergunta frequente no artigo da etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#faq-example) para ver um exemplo.
{% endalert %}

## Artigos relacionados {#related-articles}

- [Etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Personalização e conteúdo dinâmico com Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)