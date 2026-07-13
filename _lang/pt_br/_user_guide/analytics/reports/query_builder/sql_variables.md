---
nav_title: Variáveis SQL
article_title: Variáveis SQL do Criador de consultas
page_order: 2
page_type: reference
description: "Saiba como usar variáveis no Criador de consultas para reutilizar suas consultas e evitar codificar dados diretamente no seu código."
tool: Reports
---

# Variáveis SQL do Criador de consultas {#query-builder-sql-variables}

> Saiba como usar variáveis SQL no Criador de consultas para reutilizar suas consultas e evitar codificar dados diretamente no seu código.

## Por que usar variáveis SQL? {#why-use-sql-variables}

Os benefícios de usar variáveis SQL incluem:

- Economizar tempo criando uma variável de Campaign para selecionar a partir de uma lista ao criar seu relatório, em vez de colar IDs de Campaign.
- Trocar valores adicionando variáveis que permitem reutilizar o relatório para casos de uso ligeiramente diferentes no futuro (como um evento personalizado diferente).
- Reduzir erros do usuário ao editar seu SQL, diminuindo a quantidade de edição necessária para cada relatório. Colegas mais familiarizados com SQL podem criar relatórios que colegas menos técnicos podem usar.

## Usando variáveis {#using-variables}

### Etapa 1: Adicionar uma variável {#step-1-add-a-variable}

Para adicionar uma variável à sua consulta, use a seguinte sintaxe:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Substitua o seguinte:

| Placeholder | Descrição |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type` | O tipo de variável predefinido que você deseja usar, como `campaign` ou `catalog_fields`. Para a lista completa, consulte [Tipos de variáveis suportados](#variable-types). |
| `custom_label` | O rótulo usado para identificar a variável na guia **Variables** do seu Criador de consultas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Adicionar uma variável" }

No exemplo a seguir, o número total de usuários entre o primeiro e o último dia de um mês é consultado para uma Campaign. Cada variável receberá um valor na próxima etapa.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Etapa 2: Atribuir um valor {#step-2-assign-a-value}

Por padrão, a guia **Variables** não é exibida no Criador de consultas. Ela só aparece após adicionar sua primeira variável à consulta. Lá, você poderá atribuir um valor a ela. Os valores específicos que você pode escolher dependerão do [tipo](#variable-types) daquela variável.

No exemplo a seguir, a Campaign "Summer Feature Launch" é atribuída como valor, junto com o primeiro e o último dia de junho de 2025.

![A guia "Variable" no Criador de consultas mostrando o exemplo fornecido.]({% image_buster /assets/img/query_builder_example.png %})

## Tipos de variáveis gerais {#variable-types}

### Number {#number}

`number` pode ser usado em combinação com outras variáveis que não sejam string. Aceita qualquer número positivo ou negativo, incluindo números decimais, como `5.5`.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### String {#string}

Para alterar valores de string repetitivos entre execuções de relatório. Use esta variável para evitar codificar um valor várias vezes no seu SQL.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### List {#list}

Para selecionar a partir de uma lista de opções.

{% tabs local %}
{% tab escolher uma %}
{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab escolher múltiplas %}
{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Botão de rádio {#radio-button}

Para exibir opções como botões de rádio em vez de um menu suspenso na guia **Variables**. Não pode ser usado sozinho&#8212;deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab uso %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Um exemplo de botão de rádio renderizado na Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Seleção múltipla {#multi-select}

Para definir se o menu suspenso permite seleção única ou múltipla. Não pode ser usado sozinho&#8212;deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab uso %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Um exemplo de lista de seleção múltipla renderizada na Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Opções {#options}

Para fornecer a lista de opções selecionáveis na forma de rótulo e valor. O rótulo é o que é exibido e o valor é o que substitui a variável quando a opção é selecionada. Não pode ser usado sozinho&#8212;deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab uso %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Tipos de variáveis específicos da Braze {#braze-specific-variable-types}

### Intervalo de datas {#date-range}

Para exibir um calendário para selecionar datas. Substitua `start_date` e `end_date` por um timestamp Unix em segundos para uma data especificada em UTC, como `1696517353`. Opcionalmente, você pode definir apenas um `start_date` ou `end_date` para exibir apenas uma única data no calendário. Se os rótulos do seu `start_date` e `end_date` não coincidirem, eles serão tratados como duas datas separadas, em vez de um intervalo de datas.

{% tabs %}
{% tab uso %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Você pode definir o intervalo de datas para qualquer uma das seguintes opções. Se tanto `start_date` quanto `end_date` forem usados e compartilharem o mesmo rótulo, todas as opções serão exibidas. Caso contrário, se apenas um for usado, somente a opção especificada será exibida.

| Opção | Descrição | Valores obrigatórios |
| --- | --- | --- |
| Relativo | Especifica os últimos X dias | Requer `start_date` |
| Data de início | Especifica uma data de início | Requer `start_date` |
| Data de término | Especifica uma data de término | Requer `end_date` |
| Intervalo de datas | Especifica tanto uma data de início quanto de término | Requer tanto `start_date` quanto `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Intervalo de datas" }

Seu Liquid será usado para exibir um calendário dentro do intervalo de datas fornecido:

![Um exemplo de calendário renderizado na Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campaigns

{% tabs local %}
{% tab uma Campaign %}
Para selecionar uma Campaign. Compartilhar o mesmo rótulo com um Canvas resultará em um botão de rádio na guia **Variables** para selecionar Canvas ou Campaign.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiplas Campaigns %}
Para selecionar múltiplas Campaigns. Compartilhar o mesmo rótulo com um Canvas resultará em um botão de rádio na guia **Variables** para selecionar Canvas ou Campaign.

- **Valor de substituição:** IDs BSON de Campaigns

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes de Campaign %}
Para selecionar variantes de Campaign que pertencem à Campaign selecionada. Deve ser usado em conjunto com uma variável de Campaign ou Campaigns.

- **Valor de substituição:** IDs de API de variantes de Campaign, strings delimitadas por vírgulas, como `api-id1, api-id2`.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas as variáveis de Campaign e Canvas devem usar os mesmos identificadores para sincronizar estados dentro de um único grupo.
{% endalert %}

### Canvas {#canvases}

{% tabs local %}
{% tab um Canvas %}
Para selecionar um Canvas. Compartilhar o mesmo rótulo com uma Campaign resultará em um botão de rádio na guia **Variables** para selecionar Canvas ou Campaign.

- **Valor de substituição:** ID BSON do Canvas

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiplos Canvas %}
Para selecionar múltiplos Canvas. Compartilhar o mesmo rótulo com uma Campaign resultará em um botão de rádio na guia **Variables** para selecionar Canvas ou Campaign.

- **Valor de substituição:** IDs BSON de Canvas

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes de Canvas %}
Para selecionar variantes de Canvas que pertencem a um Canvas escolhido. Deve ser usado com uma variável de Canvas. Defina para um ou mais IDs de API de variantes de Canvas, como uma string separada por vírgulas, como em `api-id1, api-id2`.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab uma etapa do Canvas %}
Para selecionar uma etapa do Canvas que pertence a um Canvas escolhido. Deve ser usado com uma variável de Canvas.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiplas etapas do Canvas %}
Para selecionar etapas do Canvas que pertencem a Canvas escolhidos. Deve ser usado com uma variável de Canvas.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas as variáveis de Campaign e Canvas devem usar os mesmos identificadores para sincronizar estados dentro de um único grupo.
{% endalert %}

### Produtos {#products}

`products` é usado para selecionar um ou mais produtos do dashboard da Braze.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab exemplo %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Eventos personalizados {#custom-events}

Selecione um ou mais eventos personalizados ou propriedades de eventos personalizados a partir de uma lista.

{% tabs local %}
{% tab evento %}
`custom_events` é usado para selecionar um ou mais eventos personalizados do dashboard da Braze.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab exemplo %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}});
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab propriedades %}
`custom_event_properties` é usado para selecionar uma ou mais propriedades do evento personalizado atualmente selecionado. Requer uma variável `custom_events` definida.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Espaço de trabalho {#workspace}

`workspace` é usado para selecionar um único espaço de trabalho do dashboard da Braze.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Catálogos {#catalogs}

Selecione um ou mais catálogos ou campos de catálogo a partir de uma lista.

{% tabs local %}
{% tab catálogos %}
`catalogs` é usado para selecionar um ou mais catálogos do dashboard da Braze.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campos de catálogo %}
`catalog_fields` é usado para definir um ou mais campos do catálogo atualmente selecionado. Requer uma variável `catalogs` definida.

{% subtabs %}
{% subtab uso %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segments

Para selecionar Segments que tenham o [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) ativado. Defina como o ID de análise de dados do Segment, que corresponde aos IDs armazenados na coluna `user_segment_membership_ids` nas tabelas onde essa coluna está disponível.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Tags {#tags}

Para selecionar tags para Campaigns e Canvas. Defina para Campaigns e Canvas com IDs BSON separados por vírgulas e entre aspas simples que estejam associados às tags selecionadas.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Metadados de variáveis {#variable-metadata}

Metadados podem ser anexados a uma variável para alterar seu comportamento, adicionando os metadados com um caractere de pipe ( &#124; ) após o rótulo da variável. A ordem dos metadados não importa e você pode adicionar qualquer quantidade deles. Além disso, todos os tipos de metadados podem ser usados para qualquer variável, exceto metadados especiais que são específicos de certas variáveis (isso será indicado nesses casos). O uso de todos os metadados é opcional e serve para alterar o comportamento padrão da variável.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Booleano {#boolean}

Para saber se o valor de uma variável está preenchido. Isso é útil para variáveis opcionais onde você deseja encurtar uma condição se o valor de uma variável não estiver preenchido. Pode ser definido como `true` ou `false` dependendo do valor da outra variável.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` e `name` referem-se à variável referenciada. Por exemplo, para encurtar a seguinte variável opcional: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Visível {#visible}

Para definir se as variáveis são visíveis. Todas as variáveis são visíveis por padrão na guia **Variables**, onde você pode inserir valores.

Existem várias variáveis especiais cujo valor depende de outra variável, como se outra variável tem um valor. Essas variáveis especiais são marcadas como não visíveis para que não apareçam na guia **Variables**.

{% tabs %}
{% tab uso %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Obrigatória {#required}

Para definir se as variáveis são obrigatórias por padrão. Um valor vazio para uma variável geralmente leva a uma consulta incorreta.

{% tabs %}
{% tab uso %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Ordem {#order}

Para selecionar a posição da variável na guia **Variables**.

{% tabs %}
{% tab uso %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Incluir aspas {#include-quotes}

{% tabs local %}
{% tab aspas simples %}
Para envolver os valores de uma variável com aspas simples.

{% subtabs %}
{% subtab uso %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab aspas duplas %}
Para envolver os valores de uma variável com aspas duplas.

{% subtabs %}
{% subtab uso %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Placeholder {#placeholder}

Para especificar o texto de placeholder exibido no campo de entrada da variável.

{% tabs %}
{% tab uso %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Descrição {#description}

Para especificar o texto de descrição exibido abaixo do campo de entrada da variável.

{% tabs %}
{% tab uso %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Valor padrão {#default-value}

Para especificar o valor padrão da variável quando nenhum valor é especificado.

{% tabs %}
{% tab uso %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Ocultar rótulo {#hide-label}

Para ocultar o rótulo da variável.

{% tabs %}
{% tab uso %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}