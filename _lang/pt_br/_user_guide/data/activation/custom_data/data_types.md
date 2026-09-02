---
nav_title: Tipos de dados
article_title: Tipos de dados
page_order: 1
page_type: reference
description: "Referência dos tipos de dados compatíveis com atributos personalizados, propriedades de eventos e catálogos na Braze."
toc_headers: h2
---

# Tipos de dados {#data-types}

> Esta página reúne os tipos de dados compatíveis com atributos personalizados, propriedades de eventos e catálogos. Cada tipo de dado personalizado tem suporte e restrições ligeiramente diferentes.

## Definições {#definitions}

Use esta tabela para ver quais tipos de dados você pode usar para atributos de perfil de usuário, dados de eventos ou itens de catálogo. Consulte as seções a seguir para saber sobre o uso e as restrições de cada tipo.

<table role="presentation" class="definitions-table reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4 reset-td-br-5">
  <thead>
    <tr>
      <th>Tipo de dado</th>
      <th>Definição</th>
      <th>Atributos personalizados</th>
      <th>Propriedades de eventos</th>
      <th>Catálogos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Booleano</td>
      <td>Valor <code>true</code> ou <code>false</code></td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
    </tr>
    <tr>
      <td>Número</td>
      <td>Número inteiro ou decimal</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
    </tr>
    <tr>
      <td>String</td>
      <td>Texto; 255 caracteres ou menos</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
    </tr>
    <tr>
      <td>Hora</td>
      <td>Data e hora em formato padrão (<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>)</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>Lista ordenada de valores</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
    </tr>
    <tr>
      <td>Objeto</td>
      <td>Dados estruturados com campos nomeados (chave-valor aninhado)</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
      <td>✅ Compatível</td>
    </tr>
    <tr>
      <td>Array de objetos</td>
      <td>Lista de objetos</td>
      <td>✅ Compatível</td>
      <td>❌ Não compatível</td>
      <td>❌ Não compatível</td>
    </tr>
  </tbody>
</table>

### Considerações importantes {#important-considerations}

- **Array:** Atributos personalizados e propriedades de eventos têm limites de tamanho. Datas e horas não são compatíveis dentro de arrays em propriedades de eventos. Catálogos suportam apenas arrays de strings, com no máximo 100 elementos.
- **Objeto:** Na Braze, isso aparece como "atributos personalizados aninhados" para atributos personalizados, "objetos aninhados" para propriedades de eventos e "objeto JSON" para catálogos.
- **Hora:** Em propriedades de eventos, esse tipo é chamado de "Datetime".

## Tipos de dados de atributos personalizados {#custom-attribute-data-types}

Os atributos personalizados são compatíveis com os tipos de dados listados na tabela de [Definições](#definitions). A seguir, descrevemos o uso e a segmentação para cada tipo de dado compatível.

{% tabs %}
{% tab Booleano %}

Você pode bloquear atributos personalizados individualmente no menu de ações, ou selecionar e bloquear até 100 atributos em massa. Se você bloquear um atributo personalizado, nenhum dado será coletado para esse atributo, os dados existentes ficarão indisponíveis a menos que sejam reativados, e os atributos bloqueados não aparecerão em filtros ou gráficos. Além disso, se o atributo estiver sendo referenciado por filtros ou gatilhos em outras áreas do dashboard da Braze, um modal de aviso aparecerá explicando que todas as instâncias dos filtros ou gatilhos que o referenciam serão removidas e arquivadas.

### Marcando como informação de identificação pessoal (IPI) {#marking-as-personally-identifiable-information-pii}

Administradores também podem criar atributos personalizados e marcá-los como IPI nesta página. Esses atributos são visíveis apenas para administradores e usuários do dashboard com a permissão "View Custom Attributes Marked as IPI".

### Adicionando descrições {#adding-descriptions}

Você pode adicionar uma descrição a um atributo personalizado após sua criação, se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Edite o atributo personalizado e insira o que desejar, como uma nota para sua equipe.

### Adicionando tags {#adding-tags}

Você pode adicionar tags a um atributo personalizado após sua criação, se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". Depois, você pode usar as tags para filtrar a lista de atributos.

### Removendo atributos personalizados {#removing-custom-attributes}

Existem duas formas de remover atributos personalizados dos perfis de usuário:

- Selecione o nome do atributo personalizado a ser removido em uma [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update).
- Defina o valor `null` na sua solicitação de API or interface de programação do aplicativo (API) para o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

#### Definindo o valor `null` {#setting-the-null-value}

{% alert important %}
Definir um atributo como `null` e defini-lo como `""` (string vazia) não é a mesma coisa.
{% endalert %}

- `null` remove o atributo do perfil do usuário completamente. Ele não aparece no perfil nem corresponde a nenhum filtro **IS NOT BLANK**.
- `""` define o atributo como um valor de string vazia. O atributo aparece no perfil com um valor de string vazia, mas não corresponde a filtros **IS NOT BLANK** (é tratado como vazio).

Além disso, `""` é válido apenas para atributos do tipo string. Se o tipo de dado do atributo estiver definido como um tipo não-string (como booleano, número ou hora) no dashboard, enviar `""` não limpa o valor — use `null` em vez disso.

### Exportando dados {#exporting-data}

Para exportar a lista de atributos personalizados como um arquivo CSV, selecione **Export all** no topo da página. O sistema gera um arquivo CSV e envia um link de download por e-mail.

## Visualizando relatórios de uso {#viewing-usage-reports}

O relatório de uso lista todos os Canvas, Campaigns e Segments que utilizam um atributo personalizado específico. Essa lista não inclui usos de Liquid.

Você pode visualizar até 100 relatórios de uso de uma vez selecionando as caixas de seleção ao lado dos respectivos atributos personalizados e depois selecionando **View usage report**.

### Guia Valores {#values-tab}

Ao visualizar um relatório de uso, selecione a guia **Values** para visualizar os principais valores dos atributos personalizados selecionados com base em uma amostra de aproximadamente 250.000 usuários. Como os resultados são amostrados de um subconjunto de usuários, a amostra não inclui todos os valores existentes. Isso significa que a guia **Values** não deve ser usada para solução de problemas ou para casos de uso que exigem a incorporação de dados de todos os usuários.

![Relatório de uso para atributos personalizados selecionados com uma guia "Values" aberta mostrando um gráfico de pizza com valores de atributo de país, como "US" e "PR".]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Definindo atributos personalizados {#setting-custom-attributes}

A seguir, estão listados os métodos em diversas plataformas usados para definir atributos personalizados.

{% details Expandir para documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/analytics)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/analytics?sdktab=xamarin)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Armazenamento de atributos personalizados {#custom-attribute-storage}

Todos os dados armazenados no **Perfil de usuário**, incluindo dados de atributos personalizados, são retidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Tipos de dados de atributos personalizados

Os atributos personalizados são ferramentas extremamente flexíveis que permitem um direcionamento muito eficaz.

Os seguintes tipos de dados podem ser armazenados como atributos personalizados:

- [Booleanos](#booleans)
- [Números](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Hora](#time)
- [Objetos]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)
- [Arrays de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)

### Booleanos (verdadeiro/falso) {#booleans}

Atributos booleanos são úteis para armazenar dados binários simples sobre seus usuários, como status de inscrição. Você pode encontrar usuários que tenham uma variável explicitamente definida como verdadeira ou falsa, além daqueles que ainda não possuem nenhum registro desse atributo.

Para atributos **booleanos**, as seguintes opções de segmentação estão disponíveis.

| Opções de segmentação | Filtro de dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o valor booleano **é** verdadeiro, falso, verdadeiro ou não definido, ou falso ou não definido | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** ou **FALSE OR NOT SET** | Se este filtro especificar `coffee_drinker`, um usuário corresponderá a este filtro nas seguintes circunstâncias: <br> {::nomarkdown}<ul><li>Se este filtro for <code>true</code> e o usuário tiver o valor <code>coffee_drinker</code></li><li>Se este filtro for <code>false</code> e o usuário não tiver o valor <code>coffee_drinker</code></li><li>Se este filtro for <code>true or not set</code> e o usuário tiver o valor <code>coffee_drinker</code> ou nenhum valor</li><li>Se este filtro for <code>false or not set</code> e o usuário não tiver <code>coffee_drinker</code> ou nenhum valor</li></ul>{:/} |
| Verificar se o valor booleano **existe** no perfil de um usuário e não é nulo | **IS NOT BLANK**  | **N/A** | Se este filtro especificar `coffee_drinker` e um usuário tiver um valor para o atributo `coffee_drinker`, o usuário corresponderá a este filtro. |
| Verificar se o valor booleano **não existe** no perfil de um usuário ou é nulo | **IS BLANK**  | **N/A** | Se este filtro especificar `coffee_drinker` e um usuário não tiver o atributo `coffee_drinker` ou o valor de `coffee_drinker` for nulo, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

{% endtab %}
{% tab Números %}

{% alert tip %}
Valores monetários gastos não devem ser registrados por este método. Em vez disso, devem ser registrados por meio de [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).
{% endalert %}

Para atributos **numéricos**, as seguintes opções de segmentação estão disponíveis.

| Opções de segmentação | Filtro de dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo numérico **é exatamente** um **número**| **EXACTLY** | **NUMBER** | Se este filtro especificar `10` e um perfil de usuário tiver o valor `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **não é igual a** um **número**| **DOES NOT EQUAL** | **NUMBER** | Se este filtro especificar `10` e um perfil de usuário não tiver o valor `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **é maior que** um **número**| **MORE THAN** | **NUMBER** | Se este filtro especificar `10` e um perfil de usuário tiver um valor maior que `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **é menor que** um **número**| **LESS THAN** | **NUMBER** | Se este filtro especificar `10` e um perfil de usuário tiver um valor menor que `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **existe** no perfil de um usuário e não é nulo | **IS NOT BLANK** | **N/A** | Se um perfil de usuário contiver o atributo numérico especificado, independentemente do valor, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **não existe** no perfil de um usuário ou é nulo | **IS BLANK** | **N/A** | Se um perfil de usuário não contiver o atributo numérico especificado ou o valor do atributo for nulo, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

#### Detalhes de atributos numéricos {#number-attribute-details}

- Filtros "Exatamente 0" e "Menor que" incluem usuários com campos NULL
  - Para excluir usuários sem um valor para atributos personalizados, você precisa incluir o filtro **is not blank**.

{% endtab %}
{% tab Strings %}

Atributos de string podem ter até 255 caracteres. Se você inserir valores com espaços entre, antes ou depois de palavras, a Braze também verificará esses mesmos espaços.

Para atributos de **String**, as seguintes opções de segmentação estão disponíveis.

| Opções de segmentação | Filtro de dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de string **corresponde parcialmente** a uma string inserida **OU** expressão regular | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION** <br>Não diferencia maiúsculas de minúsculas; máximo de 32.764 caracteres |
| Verificar se o atributo de string **não corresponde parcialmente** a uma string inserida **OU** expressão regular | **DOES NOT MATCH REGEX** * | **STRING** **OU** **REGULAR EXPRESSION**<br>Não diferencia maiúsculas de minúsculas; máximo de 32.764 caracteres |
| Verificar se o atributo de string **existe** no perfil de um usuário e não é uma string vazia | **IS NOT BLANK** | **N/A** | Se este filtro especificar `favorite_genre` e um perfil de usuário tiver o atributo `favorite_genre`, o usuário corresponderá a este filtro independentemente do valor do atributo. Por exemplo, o usuário pode ter `sci-fi`, `romance` ou outro valor.|
| Verificar se o atributo de string **não existe** no perfil de um usuário | **BLANK** | **N/A** | Se este filtro especificar `favorite_genre` e um perfil de usuário não tiver o atributo `favorite_genre`, o usuário corresponderá a este filtro.|
| Verificar se a string corresponde exatamente a **qualquer uma** das strings inseridas | **IS ANY OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especificar `book`, `bookmark` e `reading light`, e um perfil de usuário tiver pelo menos uma dessas strings, o usuário corresponderá a este filtro. |
| Verificar se o atributo de string **não corresponde exatamente a nenhuma** das strings inseridas | **IS NONE OF** |**STRING**<br>Diferencia maiúsculas de minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especificar `book`, `bookmark` e `reading light`, e um perfil de usuário não contiver nenhuma dessas strings, o usuário corresponderá ao filtro.|
| Verificar se o atributo de string **corresponde parcialmente a qualquer uma** das strings inseridas | **CONTAINS ANY OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especificar `gold` e um perfil de usuário contiver `gold` em qualquer string, como `gold_tier` ou `former_gold_tier`, o usuário corresponderá ao filtro. |
| Verificar se o atributo de string **não corresponde parcialmente a nenhuma** das strings inseridas | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especificar `gold` e um perfil de usuário não contiver `gold` em nenhuma string, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
Ao segmentar usando o filtro **DOES NOT MATCH REGEX**, é necessário que o perfil do usuário já tenha um atributo personalizado com um valor atribuído. A Braze sugere usar a lógica "OR" para verificar se um atributo personalizado está vazio, a fim de garantir que os usuários sejam direcionados corretamente.
{% endalert %}

{% endtab %}
{% tab Arrays %}

### Arrays {#arrays}

Arrays têm um tamanho máximo de 100&nbsp;KB. O comprimento padrão de um atributo é de até 500 itens (por exemplo, se você estiver enviando um atributo como "Filmes Assistidos" com 500 itens, quando um usuário assistir ao 501º filme, o primeiro filme será removido e o mais recente será adicionado). Se você inserir valores com espaços entre, antes ou depois de palavras, a Braze também verificará esses mesmos espaços.

Atributos personalizados do tipo array não podem ser importados via [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import). Para fazer upload de valores de array, use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou a [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

{% alert note %}
A opção de aumentar o comprimento máximo não estará disponível se o atributo estiver configurado para detectar automaticamente o tipo de dado; o tipo de dado deve ser definido como array.
{% endalert %}

#### Solução de problemas: atributo personalizado de array não exibe valor no perfil do usuário {#troubleshooting-array-custom-attribute-shows-no-value-on-a-user-profile}

Se um atributo personalizado de array aparece no perfil do usuário, mas não exibe valores, verifique se o **Max Length** do atributo está definido como `0` no dashboard.

1. Acesse **Data Settings** > **Custom Attributes**.
2. Filtre a lista por **Array**.
3. Encontre o atributo e verifique seu **Max Length**.
4. Se o **Max Length** for `0`, atualize para um valor maior que `0`.

Definir o **Max Length** como `0` impede que os valores sejam exibidos no perfil do usuário.

Para exemplos de comportamento de arrays focados em SDK or kit de desenvolvimento de software, consulte [Visão geral de análise de dados]({{site.baseurl}}/developer_guide/analytics).

Para atributos de **Array**, as seguintes opções de segmentação estão disponíveis.

| Opções de segmentação | Filtro de dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de array **inclui um valor que corresponde exatamente** a um valor inserido| **INCLUDES VALUE** | **STRING** | Se este filtro especificar `sci-fi` e um perfil de usuário tiver o valor `sci-fi`, o usuário corresponderá a este filtro.|
| Verificar se o atributo de array **não inclui um valor que corresponde exatamente** a um valor inserido| **DOESN'T INCLUDE VALUE** | **STRING** | Se este filtro especificar `sci-fi` e um perfil de usuário não tiver o valor `sci-fi`, o usuário corresponderá a este filtro.|
| Verificar se o atributo de array **contém um valor que corresponde parcialmente** a um valor inserido **OU** expressão regular | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION**<br>Máximo de 32.764 caracteres | |
| Verificar se o atributo de array **tem algum valor** ou não está vazio | **HAS A VALUE** | **N/A** | Se este filtro especificar `favorite_genres` e um perfil de usuário contiver `favorite_genres` com qualquer valor, o usuário corresponderá a este filtro. |
| Verificar se o atributo de array **está vazio** ou não existe | **IS EMPTY** | **N/A** | Se este filtro especificar `favorite_genres` e um perfil de usuário não contiver `favorite_genres` ou contiver `favorite_genres` sem nenhum valor, o usuário corresponderá a este filtro.|
| Verificar se o atributo de array **inclui um valor que corresponde exatamente a qualquer um** dos valores inseridos | **INCLUDES ANY OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário tiver qualquer combinação de `sci-fi`, `fantasy` ou `romance`, incluindo apenas um deles (como somente `sci-fi`). Um usuário pode ter `horror` ou outro valor em sua string se também tiver qualquer um de `sci-fi`, `fantasy` e `romance`.|
| Verificar se o atributo de array **não inclui um valor que corresponde exatamente a nenhum** dos valores inseridos | **INCLUDES NONE OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário não tiver nenhuma combinação de `sci-fi`, `fantasy` ou `romance`, o usuário corresponderá a este filtro. O usuário pode ter `horror` ou outro valor se não tiver nenhum de `sci-fi`, `fantasy` ou `romance`.|
| Verificar se o atributo de array **contém um valor que corresponde parcialmente a qualquer um** dos valores inseridos | **VALUES CONTAIN ANY OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especificar `gold` e um array do perfil de usuário contiver `gold` em pelo menos uma string, o usuário corresponderá a este filtro. Isso inclui valores de string como `gold_tier`, `former_gold_tier` e outros.|
| Verificar se o atributo de array **não inclui um valor que corresponde parcialmente a nenhum** dos valores inseridos | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especificar `gold` e um array do perfil de usuário não contiver `gold` em nenhuma string, o usuário corresponderá a este filtro. Isso significa que usuários com valores de string como `gold_tier` e `former_gold_tier` não corresponderão a este filtro.|
| Verificar se o atributo de array **inclui todos** os valores inseridos | **IS ALL OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário tiver todos esses valores, o usuário corresponderá a este filtro. O usuário também pode ter `horror` ou outros valores e ainda corresponder a este filtro.|
| Verificar se o atributo de array **não inclui todos** os valores inseridos | **ISN'T ALL OF** | **STRING**<br>Diferencia maiúsculas de minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especificar `sci-fi, fantasy, romance` e um perfil de usuário não tiver todos esses valores, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert tip %}
Para saber mais sobre como usar expressões regulares (regex), confira estes recursos:

- [Expressões regulares compatíveis com Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex com a Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Depurador e testador de regex](https://www.regex101.com/)
- [Tutorial de regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

{% endtab %}
{% tab Hora %}

Atributos de hora são úteis para armazenar a última vez que uma ação específica foi realizada, permitindo que você ofereça mensagens de reengajamento específicas para seus usuários.

Filtros de hora que usam datas relativas (por exemplo, mais de 1 dia atrás, menos de 2 dias atrás) medem 1 dia como 24 horas. Qualquer campanha executada usando esses filtros incluirá todos os usuários em incrementos de 24 horas. Por exemplo, `last used app more than 1 day ago` capturará todos os usuários que "usaram o app pela última vez há mais de 24 horas" a partir do momento exato em que a campanha é executada. O mesmo vale para campanhas configuradas com intervalos de datas mais longos — então, cinco dias a partir da ativação significam as 120 horas anteriores.

Para direcionar usuários que possuem um atributo de hora dentro de um intervalo de tempo, use dois filtros de público: `in more than` para o limite inferior e `in less than` para o limite superior. Um único filtro não pode expressar ambos os lados desse intervalo. Por exemplo, para direcionar usuários com um atributo de hora nas próximas 24 horas (entre agora e um dia a partir de agora), aplique `in more than 0 days` e `in less than 1 day`.

{% alert warning %}
A última data em que um evento personalizado ou evento de compra ocorreu é registrada automaticamente e não deve ser registrada novamente por meio de um atributo de hora personalizado.
{% endalert %}

Para atributos de **Hora**, as seguintes opções de segmentação estão disponíveis.

| Opções de segmentação | Filtro de dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de hora **é antes de** uma **data selecionada**| **BEFORE** | **CALENDAR DATE SELECTOR** | Se este filtro especificar `2024-01-31` e um perfil de usuário tiver uma data anterior a `2024-1-31`, o usuário corresponderá a este filtro. |
| Verificar se o atributo de hora **é depois de** uma **data selecionada**| **AFTER** | **CALENDAR DATE SELECTOR** | Se este filtro especificar `2024-01-31` e um perfil de usuário tiver uma data posterior a `2024-1-31`, o usuário corresponderá a este filtro. |
| Verificar se o atributo de hora **é mais de X número** de **dias atrás** | **MORE THAN** | **NUMBER OF DAYS AGO** | Se este filtro especificar `7` e um perfil de usuário tiver uma data há mais de sete dias, o usuário corresponderá a este filtro. |
| Verificar se o atributo de hora **é menos de X número** de **dias atrás**| **LESS THAN** | **NUMBER OF DAYS AGO** | Se este filtro especificar `7` e um perfil de usuário tiver uma data há menos de sete dias, o usuário corresponderá a este filtro.|
| Verificar se o atributo de hora **é em mais de X número** de **dias no futuro** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Se este filtro especificar `7` e um perfil de usuário tiver uma data a mais de sete dias no futuro, o usuário corresponderá a este filtro.|
| Verificar se o atributo de hora **é em menos de X número** de **dias no futuro** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Se este filtro especificar `7` e um perfil de usuário tiver uma data a menos de sete dias no futuro, o usuário corresponderá a este filtro.|
| Verificar se o atributo de hora **existe** no perfil de um usuário e não é nulo | **IS NOT BLANK** | **N/A** | Se este filtro especificar um atributo de hora que está no perfil de um usuário, o usuário corresponderá a este filtro.|
| Verificar se o atributo de hora **não existe** no perfil de um usuário ou é nulo | **IS BLANK** | **N/A** | Se este filtro especificar um atributo de hora que não está no perfil de um usuário, o usuário corresponderá a este filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert note %}
Ao usar os operadores **in less than** ou **in more than** com 90 dias ou mais, a Braze converte automaticamente o valor para semanas quando você salva o Segment or segmento. Por exemplo, 90 dias é convertido para 13 semanas.
{% endalert %}

#### Detalhes de atributos de hora {#time-attribute-details}

{% multi_lang_include data_activation/day_of_recurring_event_filter.md %}

{% endtab %}
{% tab Objetos %}

Você pode usar atributos personalizados aninhados para enviar objetos como um tipo de dado para atributos personalizados. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% endtab %}
{% tab Arrays de objetos %}

Use um array de objetos para agrupar atributos relacionados. Para mais detalhes, consulte [Array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).

{% endtab %}
{% endtabs %}

Você pode alterar o tipo de dado do seu atributo personalizado, mas deve estar ciente dos impactos. Consulte [Alterando o tipo de dado de atributos personalizados ou eventos](#changing-custom-attribute-or-event-data-type) para saber mais.

### Operadores consolidados {#consolidated-operators}

Consolidamos a lista de operadores disponíveis para uso em filtros de atributos, filtros de atributos personalizados e filtros de atributos personalizados aninhados. Se você tiver filtros existentes usando esses operadores, eles serão automaticamente atualizados para usar os novos operadores.

| Tipo de dado | Operador antigo | Novo operador | Valor |
| --- | --- | --- | --- |
| String | equals | is any of | Pelo menos 1 valor |
| String | does not equal | is none of | Pelo menos 1 valor |
| Array | includes value | includes any of | Pelo menos 1 valor |
| Array | doesn't include value | includes none of | Pelo menos 1 valor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Consolidated operators #consolidated-operators" }

## Tipos de dados de propriedades de eventos {#event-property-data-types}

Ao registrar um evento, você pode anexar informações adicionais (por exemplo, nome do produto ou preço) como propriedades de eventos. Cada propriedade tem um nome e um valor. Os valores de propriedades de eventos são compatíveis com os tipos de dados na tabela de [Definições](#definitions) (Hora é chamado de "Datetime" em propriedades de eventos).

### Formato esperado {#expected-format}

Os valores de propriedades são enviados como um objeto: as chaves são os nomes das propriedades e os valores são os valores das propriedades. Os nomes das propriedades devem ser strings não vazias, com 255 caracteres ou menos, sem cifrões (`$`) no início.

Regras específicas de propriedades de eventos:

- **Hora (Datetime):** Use o formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Não é compatível dentro de arrays.
- **Array:** Datas e horas não são compatíveis dentro de arrays.
- **Objeto aninhado:** Consulte [Objetos aninhados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).
- **Carga útil:** Objetos de propriedades de eventos que contêm valores de array ou objeto podem ter até 102.400 bytes (100&nbsp;KiB).

Você pode alterar o tipo de dado da propriedade do seu evento personalizado, mas esteja ciente dos impactos de [alterar tipos de dados](#changing-custom-attribute-or-event-data-type) após os dados terem sido coletados.

Para o comportamento completo de propriedades de eventos, chaves reservadas e uso em gatilhos e personalização, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

## Eventos de compra e receita {#purchase-events-and-revenue}

Dados de compra e receita são registrados por meio de [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) ou eventos recomendados de eCommerce.

{% alert note %}
Eventos recomendados têm esquemas pré-definidos com tipos de dados definidos. Para mais detalhes, consulte [Eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).
{% endalert %}

O registro de eventos de compra estabelece o Lifetime Value (LTV) para cada perfil de usuário, e esses dados podem ser visualizados na página de receita em séries temporais. Você pode segmentar por valor gasto, data da última compra, número de compras em um período e muito mais.

### Tipos de dados de propriedades de eventos de compra {#purchase-event-property-data-types}

Os valores de propriedades de eventos de compra (o objeto `properties` em uma compra) são compatíveis com os tipos de dados na tabela de [Definições](#definitions), com a mesma estrutura e regras de nomenclatura das [propriedades de eventos](#expected-format).

{% include data_activation/purchase_event_property_data_types.md %}

Para o esquema completo do objeto de compra e exemplos, consulte [Objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object). Para registro de eventos de compra, filtros de segmentação e detalhes completos, consulte [Eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).

## Alterando o tipo de dado de atributo personalizado ou evento {#changing-custom-attribute-or-event-data-type}

Para alterar o tipo de dado de um atributo personalizado ou evento:

1. Acesse **Data Settings** e selecione **Custom Attributes** ou **Custom Events**.
2. Encontre seu atributo ou evento na lista e selecione <i class="fa fa-ellipsis-v" aria-hidden="true"></i> **Mais ações**.
3. Selecione um novo **Data type** no dropdown.
4. Selecione **Save**.

Se você alterar o tipo de dado de um atributo personalizado ou evento (por exemplo, alterando `time` para `string`), considere o seguinte:

- **Os filtros não são atualizados automaticamente.** Segments, Campaigns, Canvas ou outros locais que usam o atributo ou evento alterado não são atualizados. Antes de alterar o tipo de dado, pare quaisquer Campaigns ou Canvas que usem o atributo em Segments ou filtros, e remova o atributo dos filtros que o referenciam.
- **Os dados existentes dos usuários não são atualizados retroativamente.** Se o atributo alterado estava no perfil de um usuário antes da alteração, esse valor permanece com o tipo de dado antigo. Os usuários podem sair de segmentos que contêm o atributo alterado porque o filtro procura o novo tipo de dado. Atualize esses perfis de usuário (por exemplo, com o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)) para que correspondam ao novo tipo e reentrem no Segment or segmento or segmento, se necessário.
- **Os novos dados devem corresponder ao novo tipo.** Chamadas de API or interface de programação do aplicativo (API) que enviam o tipo de dado anterior para o atributo alterado não são aceitas. Envie o novo tipo de dado.

{% alert important %}
A capacidade de impedir que a detecção automática atualize o tipo de dado do atributo personalizado está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar.
{% endalert %}

## Tipos de dados de catálogos {#catalog-data-types}

Os catálogos são compatíveis com os tipos listados na tabela de [Definições](#definitions). A tabela a seguir lista cada tipo, como ele pode ser criado ou atualizado, e o formato com exemplos.

| Tipo de dado | Descrição | Disponível via upload de CSV | Disponível via API or interface de programação do aplicativo (API) e CDI |
| --- | --- | --- | --- |
| String | Uma sequência de caracteres (por exemplo, nomes, descrições, IDs). | ✅ Sim | ✅ Sim |
| Número | Um valor numérico, inteiro ou decimal (por exemplo, preços, quantidades, avaliações). | ✅ Sim | ✅ Sim |
| Booleano | Um valor `true` ou `false`. | ✅ Sim | ✅ Sim |
| Hora | Data e hora no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou timestamp Unix em segundos. | ✅ Sim | ✅ Sim |
| Objeto JSON (Objeto) | Objeto aninhado com pares chave-valor. Exibido na plataforma, mas só pode ser criado ou atualizado por meio da API or interface de programação do aplicativo (API) ou CDI. | ❌ Não | ✅ Sim |
| Array de strings (Array) | Uma lista de strings. Exibido na plataforma, mas só pode ser criado ou atualizado por meio da API or interface de programação do aplicativo (API) ou CDI. Máximo de 100 elementos. | ❌ Não | ✅ Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tipos de dados de catálogos" }

### Formato e exemplos {#format-and-examples}

| Tipo de dado | Formato | Exemplo |
| --- | --- | --- |
| String | Texto | <code>"Hello World"</code> |
| Hora | ISO 8601 ou timestamp Unix (segundos) | <code>"2024-03-15T14:30:00Z"</code> |
| Booleano | <code>true</code> ou <code>false</code> | <code>true</code> |
| Número | Inteiro ou decimal | <code>42</code> ou <code>19.99</code> |
| Objeto | Objeto JSON | <code>{"key": "value", "price": 10}</code> |
| Array | Array de strings | <code>["red", "blue", "green"]</code> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Formato e exemplos" }

Para criar e atualizar catálogos, consulte [Criar um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create).