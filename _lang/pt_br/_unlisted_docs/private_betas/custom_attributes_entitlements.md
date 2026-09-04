---
article_title: Atributos personalizados
permalink: "/custom_attributes_entitlements/"
hidden: true
---

# [![Curso do Braze Learning]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Atributos personalizados {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> Esta página aborda os atributos personalizados, que são uma coleção de características únicas dos seus usuários. Os atributos personalizados são ideais para armazenar informações sobre seus usuários ou dados sobre ações de baixo valor dentro do seu aplicativo.

Quando armazenados na Braze, os atributos personalizados podem ser usados para criar segmentos de público e personalizar o envio de mensagens usando Liquid. Tenha em mente que não armazenamos informações de séries temporais para atributos personalizados, então você não pode gerar gráficos com base neles como faz com eventos personalizados.

## Direitos de uso {#entitlements}

Os direitos de uso determinam a capacidade de atributos personalizados, que rastreia o número de nomes de atributos diferentes que você define. Você pode ter até 1.000 atributos personalizados por espaço de trabalho. Se precisar aumentar sua capacidade, entre em contato com o gerente de conta da Braze para saber mais.

Conforme seu espaço de trabalho se aproxima do número máximo de atributos personalizados, você receberá notificações no dashboard e por e-mail para ajudar a manter o controle.

Mesmo após atingir a capacidade máxima, os atributos personalizados existentes ainda podem ser recebidos. No entanto, você não poderá criar novos atributos personalizados. Quaisquer dados recebidos para atributos personalizados que ainda não existam não serão processados.

## Gerenciamento de atributos personalizados {#managing-custom-attributes}

Para criar e gerenciar atributos personalizados no dashboard, acesse **Data Settings** > **Custom Attributes**.

![Quatro atributos personalizados que são booleanos.]({% image_buster /assets/unlisted_docs/img/custom_attributes_entitlements/export_custom_attributes.png %})

A coluna **Last updated** mostra a última vez que o atributo personalizado foi editado, como quando foi definido pela última vez como blocklist ou ativo.

{% alert important %}
Para um direcionamento de mensagens adequado, certifique-se de que o tipo de dados do seu atributo personalizado corresponda ao atributo personalizado real.
{% endalert %}

Nesta página, você pode visualizar, gerenciar, criar ou adicionar à blocklist atributos personalizados existentes. Selecione o menu ao lado de um atributo personalizado para as seguintes ações:

### Adição à blocklist {#blocklisting}

Atributos personalizados podem ser adicionados à blocklist individualmente no menu de ações, ou até 100 atributos podem ser selecionados e adicionados à blocklist em massa. Se você bloquear um atributo personalizado, nenhum dado será coletado para esse atributo, os dados existentes ficarão indisponíveis a menos que sejam reativados, e os atributos na blocklist não aparecerão em filtros ou gráficos. Além disso, se o atributo estiver sendo referenciado por filtros ou gatilhos em outras áreas do dashboard da Braze, um modal de alerta aparecerá explicando que todas as instâncias dos filtros ou gatilhos que o referenciam serão removidas e arquivadas.

### Marcação como informação pessoalmente identificável (IPI) {#marking-as-personally-identifiable-information-pii}

Os administradores também podem criar atributos personalizados e marcá-los como IPI nesta página. Esses atributos serão visíveis apenas para administradores e usuários do dashboard com a permissão "View Custom Attributes Marked as IPI".

### Adição de descrições {#adding-descriptions}

Você pode adicionar uma descrição a um atributo personalizado após sua criação, caso tenha a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Edite o atributo personalizado e insira o que desejar, como uma nota para sua equipe.

### Adição de tags {#adding-tags}

Você pode adicionar tags a um atributo personalizado após sua criação, caso tenha a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". As tags podem então ser usadas para filtrar a lista de atributos.

### Remoção de atributos personalizados {#removing-custom-attributes}

Existem duas formas de remover atributos personalizados dos perfis de usuário:

* Selecione o nome do atributo personalizado a ser removido em uma [etapa de Atualização de Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update#removing-custom-attributes).
* Defina o valor `null` na sua solicitação de API para o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Visualização de relatórios de uso {#viewing-usage-reports}

O relatório de uso lista todos os Canvas, Campaigns e Segments que utilizam um atributo personalizado específico. Essa lista não inclui usos de Liquid.

Você pode visualizar até 100 relatórios de uso por vez marcando as caixas de seleção ao lado dos respectivos atributos personalizados e selecionando **View usage report**.

### Exportação de dados {#exporting-data}

Para exportar a lista de atributos personalizados como um arquivo CSV, selecione **Export all** no topo da página. O arquivo CSV será gerado e um link para download será enviado por e-mail para você.

## Definição de atributos personalizados {#setting-custom-attributes}

A lista a seguir apresenta os métodos em diversas plataformas usados para definir atributos personalizados.

{% details Expandir para ver a documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Armazenamento de atributos personalizados {#custom-attribute-storage}

Todos os dados armazenados no **Perfil de Usuário**, incluindo dados de atributos personalizados, são retidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Tipos de dados de atributos personalizados {#custom-attribute-data-types}

Atributos personalizados são ferramentas extremamente flexíveis que permitem um grande poder de direcionamento.

Os seguintes tipos de dados podem ser armazenados como atributos personalizados:

- [Booleanos](#booleans)
- [Números](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Data e hora](#time)
- [Objetos]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)
- [Arrays de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)

### Booleanos (verdadeiro/falso) {#booleans}

Atributos booleanos são úteis para armazenar dados binários simples sobre seus usuários, como status de inscrição. Você pode encontrar usuários que possuem explicitamente uma variável definida como verdadeira ou falsa, além daqueles que ainda não possuem nenhum registro desse atributo.

| Opções de segmentação | Filtro do dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o valor booleano **é** verdadeiro, falso, verdadeiro ou não definido, ou falso ou não definido | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** ou **FALSE OR NOT SET** | Se este filtro especifica `coffee_drinker`, um usuário corresponderá a este filtro nas seguintes circunstâncias: <br> {::nomarkdown}<ul><li>Se este filtro for <code>true</code> e o usuário tiver o valor <code>coffee_drinker</code></li><li>Se este filtro for <code>false</code> e o usuário não tiver o valor <code>coffee_drinker</code></li><li>Se este filtro for <code>true or not set</code> e o usuário tiver o valor <code>coffee_drinker</code> ou nenhum valor</li><li>Se este filtro for <code>false or not set</code> e o usuário não tiver <code>coffee_drinker</code> ou qualquer valor</li></ul>{:/} |
| Verificar se o valor booleano **existe** no perfil de um usuário e não é nulo | **IS NOT BLANK**  | **N/A** | Se este filtro especifica `coffee_drinker` e um usuário possui um valor para o atributo `coffee_drinker`, o usuário corresponderá a este filtro. |
| Verificar se o valor booleano **não existe** no perfil de um usuário ou é nulo | **IS BLANK**  | **N/A** | Se este filtro especifica `coffee_drinker` e um usuário não possui o atributo `coffee_drinker` ou o valor de `coffee_drinker` é nulo, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Números {#numbers}

Atributos numéricos incluem [inteiros](https://en.wikipedia.org/wiki/Integer) e [números de ponto flutuante](https://en.wikipedia.org/wiki/Floating-point_arithmetic), e possuem uma grande variedade de casos de uso. Atributos personalizados numéricos incrementais são úteis para armazenar o número de vezes que uma determinada ação ou evento ocorreu sem contar contra o seu limite de dados. Números padrão possuem todos os tipos de uso, como registrar:

- Tamanho do calçado
- Medida da cintura
- Número de vezes que um usuário visualizou um determinado recurso ou categoria de produto

{% alert tip %}
Valores gastos não devem ser registrados por este método. Em vez disso, devem ser registrados através dos nossos [métodos de compra](#purchase-revenue-tracking).
{% endalert %}

| Opções de segmentação | Filtro do dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo numérico **é exatamente** um **número**| **EXACTLY** | **NUMBER** | Se este filtro especifica `10` e um perfil de usuário possui o valor `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **não é igual a** um **número**| **DOES NOT EQUAL** | **NUMBER** | Se este filtro especifica `10` e um perfil de usuário não possui o valor `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **é maior que** um **número**| **MORE THAN** | **NUMBER** | Se este filtro especifica `10` e um perfil de usuário possui um valor maior que `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **é menor que** um **número**| **LESS THAN** | **NUMBER** | Se este filtro especifica `10` e um perfil de usuário possui um valor menor que `10`, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **existe** no perfil de um usuário e não é nulo | **IS NOT BLANK** | **N/A** | Se um perfil de usuário contém o atributo numérico especificado, independentemente do valor, o usuário corresponderá a este filtro. |
| Verificar se o atributo numérico **não existe** no perfil de um usuário ou é nulo | **IS BLANK** | **N/A** | Se um perfil de usuário não contém o atributo numérico especificado ou o valor do atributo é nulo, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalhes de atributos numéricos {#number-attribute-details}

- Filtros "Exatamente 0" e "Menor que" incluem usuários com campos NULL
  - Para excluir usuários sem um valor para atributos personalizados, você precisa incluir o filtro **is not blank**.

### Strings (caracteres alfanuméricos) {#strings}

Atributos de string são úteis para armazenar entrada do usuário, como uma marca favorita, um número de telefone ou a última string de pesquisa dentro do seu aplicativo. Atributos de string podem ter até 255 caracteres.

Se você inserir quaisquer valores com espaços entre, antes ou depois das palavras, a Braze também verificará os mesmos espaços.

| Opções de segmentação | Filtro do dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de string **corresponde exatamente** a uma string inserida| **EQUALS** | **STRING**<br>Diferencia maiúsculas e minúsculas | Se este filtro especifica `book` e um perfil de usuário possui um atributo de string para `last_item_purchased` que contém `book`, o usuário corresponderá a este filtro. |
| Verificar se o atributo de string **corresponde parcialmente** a uma string inserida **OU** expressão regular | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION** <br>Não diferencia maiúsculas e minúsculas; máximo de 32.764 caracteres |
| Verificar se o atributo de string **não corresponde parcialmente** a uma string inserida **OU** expressão regular | **DOES NOT MATCH REGEX** * | **STRING** **OU** **REGULAR EXPRESSION**<br>Não diferencia maiúsculas e minúsculas; máximo de 32.764 caracteres |
| Verificar se o atributo de string **não corresponde** a uma string inserida| **DOES NOT EQUAL** | **STRING**<br>Não diferencia maiúsculas e minúsculas  | Se este filtro especifica `book` e um perfil de usuário possui um atributo de string para `last_item_purchased` que não contém `book`, o usuário corresponderá a este filtro.|
| Verificar se o atributo de string **existe** no perfil de um usuário e não é uma string vazia | **IS NOT BLANK** | **N/A** | Se este filtro especifica `favorite_genre` e um perfil de usuário possui o atributo `favorite_genre`, o usuário corresponderá a este filtro independentemente do valor do atributo. Por exemplo, o usuário pode ter `sci-fi`, `romance` ou outro valor.|
| Verificar se o atributo de string **não existe** no perfil de um usuário | **BLANK** | **N/A** | Se este filtro especifica `favorite_genre` e um perfil de usuário não possui o atributo `favorite_genre`, o usuário corresponderá a este filtro.|
| Verificar se a string corresponde exatamente a **qualquer uma** das strings inseridas | **IS ANY OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especifica `book`, `bookmark` e `reading light`, e um perfil de usuário possui pelo menos uma dessas strings, o usuário corresponderá a este filtro. |
| Verificar se o atributo de string **não corresponde exatamente a nenhuma** das strings inseridas | **IS NONE OF** |**STRING**<br>Diferencia maiúsculas e minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especifica `book`, `bookmark` e `reading light`, e um perfil de usuário não contém nenhuma dessas strings, o usuário corresponderá ao filtro.|
| Verificar se o atributo de string **contém parcialmente qualquer uma** das strings inseridas | **CONTAINS ANY OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especifica `gold` e um perfil de usuário contém `gold` em qualquer string, como `gold_tier` ou `former_gold_tier`, o usuário corresponderá ao filtro. |
| Verificar se o atributo de string **não contém parcialmente nenhuma** das strings inseridas | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplas strings permitidas (máximo de 256) | Se este filtro especifica `gold` e um perfil de usuário não contém `gold` em nenhuma string, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Uma string de data como "12-1-2021" ou "12/1/2021" será convertida em um objeto de data e hora e tratada como um [atributo de data e hora]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time).
{% endalert %}

{% alert important %}
Ao segmentar usando o filtro **DOES NOT MATCH REGEX**, você já deve ter um atributo personalizado com um valor atribuído naquele perfil de usuário. A Braze sugere usar a lógica "OR" para verificar se um atributo personalizado está em branco para garantir que os usuários estejam sendo direcionados corretamente.
{% endalert %}

### Arrays {#arrays}

Atributos de array são bons para armazenar listas de informações relacionadas sobre seus usuários. Por exemplo, armazenar os últimos 100 conteúdos que um usuário assistiu dentro de um array permitiria segmentação por interesses específicos.

Por padrão, o comprimento máximo de um array para um atributo é definido como 25 e pode ser aumentado para 100 para um array individual. Por exemplo, se você estiver enviando um atributo como "Filmes Assistidos" e ele estiver definido como 100, quando um usuário assistir a um 101º filme, o primeiro filme será removido do array e o filme mais recente será adicionado.

Se você quiser que esse máximo seja aumentado, entre em contato com seu CSM. Seu administrador do dashboard poderá então aumentar o comprimento máximo para arrays individuais para mais de 100 na guia **Custom Attributes** da página **Manage Settings**.

Se você inserir quaisquer valores com espaços entre, antes ou depois das palavras, a Braze também verificará os mesmos espaços.

{% alert note %}
A opção de aumentar o comprimento máximo não estará disponível se o atributo estiver configurado para detectar automaticamente o tipo de dados; o tipo de dados deve ser definido como array.
{% endalert %}

| Opções de segmentação | Filtro do dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de array **inclui um valor que corresponde exatamente** a um valor inserido| **INCLUDES VALUE** | **STRING** | Se este filtro especifica `sci-fi` e um perfil de usuário possui o valor `sci-fi`, o usuário corresponderá a este filtro.|
| Verificar se o atributo de array **não inclui um valor que corresponde exatamente** a um valor inserido| **DOESN'T INCLUDE VALUE** | **STRING** | Se este filtro especifica `sci-fi` e um perfil de usuário não possui o valor `sci-fi`, o usuário corresponderá a este filtro.|
| Verificar se o atributo de array **contém um valor que corresponde parcialmente** a um valor inserido **OU** expressão regular | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION**<br>Máximo de 32.764 caracteres | |
| Verificar se o atributo de array **possui algum valor** ou não está vazio | **HAS A VALUE** | **N/A** | Se este filtro especifica `favorite_genres` e um perfil de usuário contém `favorite_genres` com qualquer valor, o usuário corresponderá a este filtro. |
| Verificar se o atributo de array **está vazio** ou não existe | **IS EMPTY** | **N/A** | Se este filtro especifica `favorite_genres` e um perfil de usuário não contém `favorite_genres` ou contém `favorite_genres` mas sem valores, o usuário corresponderá a este filtro.|
| Verificar se o atributo de array **inclui um valor que corresponde exatamente a qualquer um** dos valores inseridos | **INCLUDES ANY OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especifica `sci-fi, fantasy, romance` e um perfil de usuário possui qualquer combinação de `sci-fi`, `fantasy` ou `romance`, incluindo apenas um deles (como somente `sci-fi`). Um usuário pode ter `horror` ou outro valor na sua string se também possuir qualquer um entre `sci-fi`, `fantasy` e `romance`.|
| Verificar se o atributo de array **não inclui um valor que corresponde exatamente a nenhum** dos valores inseridos | **INCLUDES NONE OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especifica `sci-fi, fantasy, romance` e um perfil de usuário não possui nenhuma combinação de `sci-fi`, `fantasy` ou `romance`, o usuário corresponderá a este filtro. O usuário pode ter `horror` ou outro valor se não possuir nenhum entre `sci-fi`, `fantasy` ou `romance`.|
| Verificar se o atributo de array **contém um valor que corresponde parcialmente a qualquer um** dos valores inseridos | **VALUES CONTAIN ANY OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especifica `gold` e um array de perfil de usuário contém `gold` em pelo menos uma string, o usuário corresponderá a este filtro. Isso inclui valores de string como `gold_tier`, `former_gold_tier` e outros.|
| Verificar se o atributo de array **não inclui um valor que corresponde parcialmente a nenhum** dos valores inseridos | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especifica `gold` e um array de perfil de usuário não contém `gold` em nenhuma string, o usuário corresponderá a este filtro. Isso significa que usuários com valores de string como `gold_tier` e `former_gold_tier` não corresponderão a este filtro.|
| Verificar se o atributo de array **inclui todos** os valores inseridos | **IS ALL OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplos valores permitidos (máximo de 256) | Se este filtro especifica `sci-fi, fantasy, romance` e um perfil de usuário possui todos esses valores, o usuário corresponderá a este filtro. O usuário também pode ter `horror` ou outros valores e ainda corresponder a este filtro.|
| Verificar se o atributo de array **não inclui todos** os valores inseridos | **ISN'T ALL OF** | **STRING**<br>Diferencia maiúsculas e minúsculas; múltiplos valores permitidos (máximo de 256)| Se este filtro especifica `sci-fi, fantasy, romance` e um perfil de usuário não possui todos esses valores, o usuário corresponderá a este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Para saber mais sobre como usar expressões regulares (regex), confira estes recursos:
- [Expressões regulares compatíveis com Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex com a Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Depurador e testador de regex](https://www.regex101.com/)
- [Tutorial de regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Data e hora {#time}

Atributos de data e hora são úteis para armazenar a última vez que uma ação específica foi realizada, permitindo que você ofereça mensagens de reengajamento específicas para seus usuários.

Filtros de data e hora que usam datas relativas (por exemplo, mais de 1 dia atrás, menos de 2 dias atrás) medem 1 dia como 24 horas. Qualquer Campaign que você executar usando esses filtros incluirá todos os usuários em incrementos de 24 horas. Por exemplo, `last used app more than 1 day ago` capturará todos os usuários que "usaram o app pela última vez há mais de 24 horas" a partir do momento exato em que a Campaign é executada. O mesmo vale para Campaigns com intervalos de datas mais longos — cinco dias a partir da ativação significarão as 120 horas anteriores.

Por exemplo, para criar um Segment que direciona usuários com um atributo de data e hora entre 24 e 48 horas no futuro, aplique os filtros `in more than 1 day in the future` e `in less than 2 days in the future`.

{% alert warning %}
A última data em que um evento personalizado ou evento de compra ocorreu é registrada automaticamente e não deve ser registrada novamente por meio de um atributo personalizado de data e hora.
{% endalert %}

| Opções de segmentação | Filtro do dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o atributo de data e hora **é antes de** uma **data selecionada**| **BEFORE** | **CALENDAR DATE SELECTOR** | Se este filtro especifica `2024-01-31` e um perfil de usuário possui uma data antes de `2024-1-31`, o usuário corresponderá a este filtro. |
| Verificar se o atributo de data e hora **é depois de** uma **data selecionada**| **AFTER** | **CALENDAR DATE SELECTOR** | Se este filtro especifica `2024-01-31` e um perfil de usuário possui uma data depois de `2024-1-31`, o usuário corresponderá a este filtro. |
| Verificar se o atributo de data e hora é **há mais de X** **dias atrás** | **MORE THAN** | **NUMBER OF DAYS AGO** | Se este filtro especifica `7` e um perfil de usuário possui uma data de mais de sete dias atrás, o usuário corresponderá a este filtro. |
| Verificar se o atributo de data e hora é **há menos de X** **dias atrás**| **LESS THAN** | **NUMBER OF DAYS AGO** | Se este filtro especifica `7` e um perfil de usuário possui uma data de menos de sete dias atrás, o usuário corresponderá a este filtro.|
| Verificar se o atributo de data e hora é **em mais de X** **dias no futuro** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Se este filtro especifica `7` e um perfil de usuário possui uma data de mais de sete dias no futuro, o usuário corresponderá a este filtro.|
| Verificar se o atributo de data e hora é **em menos de X** **dias no futuro** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Se este filtro especifica `7` e um perfil de usuário possui uma data de menos de sete dias no futuro, o usuário corresponderá a este filtro.|
| Verificar se o atributo de data e hora **existe** no perfil de um usuário e não é nulo | **IS NOT BLANK** | **N/A** | Se este filtro especifica um atributo de data e hora que está em um perfil de usuário, o usuário corresponderá a este filtro.|
| Verificar se o atributo de data e hora **não existe** no perfil de um usuário ou é nulo | **IS BLANK** | **N/A** | Se este filtro especifica um atributo de data e hora que não está em um perfil de usuário, o usuário corresponderá a este filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalhes de atributos de data e hora {#time-attribute-details}

{% multi_lang_include data_activation/day_of_recurring_event_filter.md %}

### Objetos {#objects}

Você pode usar atributos personalizados aninhados para enviar objetos como tipo de dados para atributos personalizados. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

### Arrays de objetos {#arrays-of-objects}

Use um array de objetos para agrupar atributos relacionados. Para mais detalhes, consulte nosso artigo sobre [Array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).

### Operadores consolidados {#consolidated-operators}

Consolidamos a lista de operadores disponíveis para uso em filtros de atributos, filtros de atributos personalizados e filtros de atributos personalizados aninhados. Se você possui filtros existentes usando esses operadores, eles serão atualizados automaticamente para usar os novos operadores.

| Tipo de dados | Operador antigo | Novo operador | Valor |
| --- | --- | --- | --- |
| String | equals | is any of | Pelo menos 1 valor |
| String | does not equal | is none of | Pelo menos 1 valor |
| Array | includes value | includes any of | Pelo menos 1 valor |
| Array | doesn't include value | includes none of | Pelo menos 1 valor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Rastreamento de compras e receita {#purchase-revenue-tracking}

Usar nossos métodos de compra para registrar compras no app estabelece o valor do tempo de vida (LTV) para cada perfil de usuário individual. Esses dados são visualizáveis na nossa página de receita em séries temporais.

| Opções de segmentação | Filtro dropdown | Opções de entrada | Exemplos |
| ---------------------| --------------- | ------------- | -------- |
| Verificar se o total de dólares gastos **é maior que** um **número** | **GREATER THAN** | **NUMBER** | Se este filtro especifica `500` e um perfil de usuário tem um valor maior que `500`, o usuário corresponderá a este filtro. |
| Verificar se o total de dólares gastos **é menor que** um **número** | **LESS THAN** | **NUMBER** | Se este filtro especifica `500` e um perfil de usuário tem um valor menor que `500`, o usuário corresponderá a este filtro. |
| Verificar se o total de dólares gastos **é exatamente** um **número** | **EXACTLY** | **NUMBER** | Se este filtro especifica `500` e um perfil de usuário tem o valor `500`, o usuário corresponderá a este filtro. |
| Verificar se a compra ocorreu pela última vez **após a data X** | **AFTER** | **TIME** | Se este filtro especifica `2024/31/1` e a última compra de um usuário foi após `2024/31/1`, o usuário corresponderá a este filtro. |
| Verificar se a compra ocorreu pela última vez **antes da data X** | **BEFORE** | **TIME** | Se este filtro especifica `2024/31/1` e a última compra de um usuário foi antes de `2024/31/1`, o usuário corresponderá a este filtro. |
| Verificar se a compra ocorreu pela última vez **há mais de X dias** | **MORE THAN** | **TIME** | Se este filtro especifica `7` e a última compra de um usuário foi há mais de sete dias a partir de hoje, o usuário corresponderá a este filtro. |
| Verificar se a compra ocorreu pela última vez **há menos de X dias** | **LESS THAN** | **TIME** | Se este filtro especifica `7` e a última compra de um usuário foi há menos de sete dias a partir de hoje, o usuário corresponderá a este filtro. |
| Verificar se a compra ocorreu **mais de X (máx. = 50) vezes** | **MORE THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** | Se este filtro especifica `7` vezes e `21` dias, e um usuário fez mais de sete compras nos últimos 21 dias, o usuário corresponderá a este filtro. |
| Verificar se a compra ocorreu **menos de X (máx. = 50) vezes** | **LESS THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** | Se este filtro especifica `7` vezes e `21` dias, e um usuário fez menos de sete compras nos últimos 21 dias, o usuário corresponderá a este filtro. |
| Verificar se a compra ocorreu **exatamente X (máx. = 50) vezes** | **EXACTLY** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** | Se este filtro especifica `7` vezes e `21` dias, e um usuário fez sete compras nos últimos 21 dias, o usuário corresponderá a este filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Se você quiser segmentar pelo número de vezes que uma compra específica ocorreu, também deve registrar essa compra individualmente como um [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes#incrementingdecrementing-custom-attributes).
{% endalert %}

Você pode alterar o tipo de dados do seu atributo personalizado, mas deve estar ciente dos impactos da [alteração de tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type).