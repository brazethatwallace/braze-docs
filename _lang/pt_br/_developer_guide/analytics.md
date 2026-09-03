---
nav_title: Análise de dados
article_title: Sobre a análise de dados do SDK da Braze
page_order: 2.6
description: "Saiba mais sobre a análise de dados do SDK da Braze, para que você possa entender melhor quais dados a Braze coleta, a diferença entre eventos personalizados e atributos personalizados, e as melhores práticas para gerenciar a análise de dados."
platform:
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - .NET MAUI
---

# Análise de dados {#analytics}

> Saiba mais sobre a análise de dados do SDK da Braze, para que você possa entender melhor quais dados a Braze coleta, a diferença entre eventos personalizados e atributos personalizados, e as melhores práticas para gerenciar a análise de dados.

{% alert tip %}
Durante a sua implementação da Braze, certifique-se de discutir as metas de marketing com sua equipe, para que você possa decidir da melhor forma quais dados deseja rastrear e como deseja rastreá-los com a Braze. Como exemplo, veja nosso estudo de caso de [aplicativo de táxi/viagem por aplicativo](#example-case) no final deste guia.
{% endalert %}

## Dados coletados automaticamente {#automatically-collected-data}

Certos dados de usuários são coletados automaticamente pelo nosso SDK — por exemplo, Primeiro Uso do App, Último Uso do App, Contagem Total de Sessões, Sistema Operacional do Dispositivo, etc. Se você seguir nossos guias de integração para implementar nossos SDKs, poderá aproveitar essa [coleta de dados padrão]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection). Verificar essa lista pode ajudar você a evitar armazenar a mesma informação sobre os usuários mais de uma vez. Com exceção do início e do fim da sessão, todos os outros dados rastreados automaticamente não contam para o seu uso de pontos de dados.

Consulte nosso artigo [Introdução ao SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) para adicionar processos à lista de permissões que bloqueiam a coleta padrão de determinados itens de dados.

## Eventos personalizados {#custom-events}

Eventos personalizados são ações realizadas pelos seus usuários; eles são ideais para rastrear interações de alto valor dos usuários com o seu aplicativo. Registrar um evento personalizado pode disparar qualquer número de campanhas de acompanhamento com atrasos configuráveis, e habilita os seguintes filtros de segmentação em torno da recência e frequência desse evento:

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o evento personalizado ocorreu **mais de X vezes** | **MORE THAN** | **NUMBER** |
| Verificar se o evento personalizado ocorreu **menos de X vezes** | **LESS THAN** | **NUMBER** |
| Verificar se o evento personalizado ocorreu **exatamente X vezes** | **EXACTLY** | **NUMBER** |
| Verificar se o evento personalizado ocorreu pela última vez **após a data X** | **AFTER** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **antes da data X** | **BEFORE** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **há mais de X dias** | **MORE THAN** | **NUMBER OF DAYS AGO** (Número positivo) |
| Verificar se o evento personalizado ocorreu pela última vez **há menos de X dias** | **LESS THAN** | **NUMBER OF DAYS AGO** (Número positivo) |
| Verificar se o evento personalizado ocorreu **mais de X (Máx = 50) vezes** | **MORE THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **menos de X (Máx = 50) vezes** | **LESS THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **exatamente X (Máx = 50) vezes** | **EXACTLY** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eventos personalizados" }

A Braze registra o número de vezes que esses eventos ocorreram, bem como a última vez que foram realizados por cada usuário para fins de segmentação. Na página de análise de dados de **Custom Events**, você pode visualizar de forma agregada a frequência com que cada evento personalizado ocorre, bem como por Segment ao longo do tempo para uma análise mais detalhada. Isso é particularmente útil para visualizar como suas campanhas afetaram a atividade de eventos personalizados, observando as linhas cinzas que a Braze sobrepõe na série temporal para indicar a última vez que uma campanha foi enviada.

![Um gráfico de análise de dados de eventos personalizados mostrando estatísticas sobre usuários que adicionaram um cartão de crédito e fizeram uma pesquisa ao longo de um período de trinta dias.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
[Atributos personalizados incrementais]({{site.baseurl}}/api/endpoints/messaging) podem ser usados para manter um contador de ações do usuário de forma semelhante a um evento personalizado. No entanto, você não poderá visualizar dados de atributos personalizados em uma série temporal. Ações do usuário que não precisam ser analisadas em série temporal devem ser registradas por esse método.
{% endalert %}

### Armazenamento de eventos personalizados {#custom-event-storage}

Todos os dados de perfil de usuário (eventos personalizados, atributos personalizados, dados personalizados) são armazenados enquanto esses perfis estiverem ativos.

### Propriedades de eventos personalizados {#custom-event-properties}

Com as propriedades de eventos personalizados, a Braze permite que você defina propriedades em eventos personalizados e compras. Essas propriedades podem então ser usadas para qualificar ainda mais as condições de disparo, aumentar a personalização no envio de mensagens e gerar análises mais sofisticadas por meio da exportação de dados brutos. Os valores das propriedades podem ser string, número, booleano ou objetos de tempo. No entanto, os valores das propriedades não podem ser objetos de array.

Por exemplo, se um aplicativo de e-commerce quisesse enviar uma mensagem a um usuário quando ele abandonasse o carrinho, poderia melhorar ainda mais seu público-alvo e permitir maior personalização da campanha adicionando uma propriedade de evento personalizado do `cart_value` dos carrinhos dos usuários.

![Um exemplo de evento personalizado que enviará uma campanha para um usuário que abandonou o carrinho e deixou o valor do carrinho acima de 100 e abaixo de 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

As propriedades de eventos personalizados também podem ser usadas para personalização dentro do modelo de mensagem. Qualquer campanha que use [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) com um evento-gatilho pode usar propriedades de eventos personalizados desse evento para personalização de mensagens. Se um aplicativo de jogos quisesse enviar uma mensagem a usuários que completaram uma fase, poderia personalizar ainda mais a mensagem com uma propriedade para o tempo que os usuários levaram para completar essa fase. Neste exemplo, a mensagem é personalizada para três Segments diferentes usando [lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic). A propriedade de evento personalizado chamada ``time_spent`` pode ser incluída na mensagem chamando ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players from around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

As propriedades de eventos personalizados são projetadas para ajudar você a personalizar suas mensagens ou criar campanhas granulares de entrega baseada em ação. Se você deseja criar Segments com base na recência e frequência de propriedades de eventos, entre em contato com seu gerente de sucesso do cliente ou nossa equipe de suporte.

## Atributos personalizados {#custom-attributes}

Atributos personalizados são ferramentas extremamente flexíveis que permitem segmentar usuários com maior especificidade do que seria possível com atributos padrão. Atributos personalizados são ótimos para armazenar informações específicas da sua marca sobre seus usuários. Tenha em mente que não armazenamos informações de séries temporais para atributos personalizados, então você não terá gráficos baseados neles como no exemplo anterior de eventos personalizados.

### Armazenamento de atributos personalizados {#custom-attribute-storage}

Todos os dados do perfil de usuário (eventos personalizados, atributos personalizados, dados personalizados) são armazenados enquanto esses perfis estiverem ativos.

### Tipos de dados de atributos personalizados {#custom-attribute-data-types}

Os seguintes tipos de dados podem ser armazenados como atributos personalizados:

#### Strings (caracteres alfanuméricos) {#strings-alphanumeric-characters}

Atributos de string são úteis para armazenar entradas do usuário, como uma marca favorita, um número de telefone ou a última string de busca dentro do seu aplicativo. Atributos de string estão sujeitos às [restrições de comprimento](#length-constraints) para dados personalizados (479 bytes; aproximadamente 479 caracteres de byte único ou aproximadamente 160 caracteres para scripts multibyte, como japonês).

A tabela a seguir descreve as opções de segmentação disponíveis para atributos de string.

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o atributo de string **corresponde exatamente** a uma string inserida | **EQUALS** | **STRING** |
| Verificar se o atributo de string **corresponde parcialmente** a uma string inserida **OU** expressão regular | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION** |
| Verificar se o atributo de string **não corresponde parcialmente** a uma string inserida **OU** expressão regular | **DOES NOT MATCH REGEX** | **STRING** **OU** **REGULAR EXPRESSION** |
| Verificar se o atributo de string **não corresponde** a uma string inserida | **DOES NOT EQUAL** | **STRING** |
| Verificar se o atributo de string **existe** no perfil de um usuário | **IS BLANK** | **N/A** |
| Verificar se o atributo de string **não existe** no perfil de um usuário | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Strings (caracteres alfanuméricos)" }

{% alert important %}
Ao segmentar usando o filtro **DOES NOT MATCH REGEX**, é necessário que já exista um atributo personalizado com um valor atribuído no perfil desse usuário. A Braze sugere usar a lógica "OR" para verificar se um atributo personalizado está em branco, a fim de segmentar os usuários corretamente.
{% endalert %}

{% alert tip %}
Para saber mais sobre como usar nosso filtro de expressões regulares, confira esta documentação sobre [expressões regulares compatíveis com Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Mais recursos sobre regex:
- [Regex com a Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Depurador e testador de regex](https://regex101.com/)
- [Tutorial de regex](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Arrays {#arrays}

Atributos de array são bons para armazenar listas de informações relacionadas sobre seus usuários. Por exemplo, armazenar os últimos 100 conteúdos que um usuário assistiu em um array permitiria segmentação por interesses específicos.

Arrays de atributos personalizados são conjuntos unidimensionais; arrays multidimensionais não são suportados. **Adicionar um elemento a um array de atributo personalizado insere o elemento no final do array, a menos que ele já esteja presente, caso em que ele é movido da posição atual para o final do array.** Por exemplo, se um array `['hotdog','hotdog','hotdog','pizza']` fosse importado, ele apareceria no atributo de array como `['hotdog', 'pizza']`, pois apenas valores únicos são suportados.

Se o array contiver o número máximo de elementos, o primeiro elemento será descartado e o novo elemento será adicionado ao final. A lista a seguir mostra um exemplo de código demonstrando o comportamento do array no SDK web:

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

O número padrão e máximo de elementos em um array é 500. Você pode atualizar o número máximo de arrays no dashboard da Braze, em **Data Settings** > **Custom Attributes**. Arrays que excedem o número máximo de elementos são truncados para conter o número máximo de elementos.

{% alert note %}
Se um atributo personalizado de array aparece no perfil de um usuário, mas não mostra valores, verifique o **Max Length** do atributo em **Data Settings** > **Custom Attributes**. Um **Max Length** de `0` impede que os valores sejam exibidos no perfil. Para etapas de solução de problemas, consulte [Tipos de dados de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays).
{% endalert %}

A tabela a seguir descreve as opções de segmentação disponíveis para atributos de array.

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o atributo de array **inclui um valor que corresponde exatamente** a um valor inserido | **INCLUDES VALUE** | **STRING** |
| Verificar se o atributo de array **não inclui um valor que corresponde exatamente** a um valor inserido | **DOESN'T INCLUDE VALUE** | **STRING** |
| Verificar se o atributo de array **contém um valor que corresponde parcialmente** a um valor inserido **OU** expressão regular | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION** |
| Verificar se o atributo de array **possui algum valor** | **HAS A VALUE** | **N/A** |
| Verificar se o atributo de array **está vazio** | **IS EMPTY** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Arrays" }

{% alert note %}
Usamos [expressões regulares compatíveis com Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Datas {#dates}

Atributos de tempo são úteis para armazenar a última vez que uma ação específica foi realizada, permitindo que você ofereça mensagens de reengajamento com conteúdo específico para seus usuários.

{% alert note %}
A última data em que um evento personalizado ou evento de compra ocorreu é registrada automaticamente e não deve ser registrada em duplicidade por meio de um atributo de tempo personalizado.
{% endalert %}

Filtros de data que usam datas relativas (por exemplo, mais de 1 dia atrás, menos de 2 dias atrás) medem 1 dia como 24 horas. Qualquer campanha que você executar usando esses filtros incluirá todos os usuários em incrementos de 24 horas. Por exemplo, "último uso do app há mais de 1 dia" capturará todos os usuários que "usaram o app pela última vez há mais de 24 horas" a partir do momento exato em que a campanha é executada. O mesmo se aplica a campanhas configuradas com intervalos de datas mais longos — cinco dias a partir da ativação significará as 120 horas anteriores.

A tabela a seguir descreve as opções de segmentação disponíveis para atributos de tempo.

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o atributo de tempo **é anterior** a uma **data selecionada** | **BEFORE** | **CALENDAR DATE SELECTOR** |
| Verificar se o atributo de tempo **é posterior** a uma **data selecionada** | **AFTER** | **CALENDAR DATE SELECTOR** |
| Verificar se o atributo de tempo é **mais de X número** de **dias atrás** | **MORE THAN** | **NUMBER OF DAYS AGO** |
| Verificar se o atributo de tempo é **menos de X número** de **dias atrás** | **LESS THAN** | **NUMBER OF DAYS AGO** |
| Verificar se o atributo de tempo é **em mais de X número** de **dias no futuro** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** |
| Verificar se o atributo de tempo é **menos de X número** de **dias no futuro** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  |
| Verificar se o atributo de tempo **existe** no perfil de um usuário | **BLANK** | **N/A** |
| Verificar se o atributo de tempo **não existe** no perfil de um usuário | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Datas" }

#### Números {#integers}

Atributos numéricos têm uma ampla variedade de casos de uso. Atributos personalizados de números incrementais são úteis para armazenar o número de vezes que uma determinada ação ou evento ocorreu. Números padrão têm todos os tipos de usos, como registrar tamanho de calçado, medida de cintura ou o número de vezes que um usuário visualizou um determinado recurso ou categoria de produto.

{% alert note %}
Valores monetários gastos não devem ser registrados por este método. Em vez disso, devem ser registrados por meio dos nossos [métodos de compra]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#purchase-events--revenue-tracking).
{% endalert %}

A tabela a seguir descreve as opções de segmentação disponíveis para atributos numéricos.

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o atributo numérico **é maior que** um **número** | **MORE THAN** | **NUMBER** |
| Verificar se o atributo numérico **é menor que** um **número** | **LESS THAN** | **NUMBER** |
| Verificar se o atributo numérico **é exatamente** um **número** | **EXACTLY** | **NUMBER** |
| Verificar se o atributo numérico **não é igual a** um **número** | **DOES NOT EQUAL** | **NUMBER** |
| Verificar se o atributo numérico **existe** no perfil de um usuário | **EXISTS** | **N/A** |
| Verificar se o atributo numérico **não existe** no perfil de um usuário | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Números #integers" }

#### Booleanos (verdadeiro/falso) {#booleans-truefalse}

Atributos booleanos são úteis para armazenar status de inscrição e outros dados binários simples sobre seus usuários. As opções de entrada que fornecemos permitem encontrar usuários que tiveram uma variável explicitamente definida como booleana, além daqueles que ainda não possuem nenhum registro desse atributo.

A tabela a seguir descreve as opções de segmentação disponíveis para atributos booleanos.

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o valor booleano **é** | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** ou **FALSE OR NOT SET** |
| Verificar se o valor booleano **existe** no perfil de um usuário | **EXISTS**  | **N/A** |
| Verificar se o valor booleano **não existe** no perfil de um usuário | **DOES NOT EXIST**  | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Booleanos (verdadeiro/falso)" }

## Eventos de compra / rastreamento de receita {#purchase-events-revenue-tracking}

Usar nossos métodos de compra para registrar compras no app estabelece o Valor do Tempo de Vida (LTV) para cada perfil de usuário individual. Esses dados podem ser visualizados na nossa página de receita em gráficos de séries temporais.

A tabela a seguir descreve as opções de segmentação disponíveis para eventos de compra.

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o valor total em dólares gasto **é maior que** um **número** | **GREATER THAN** | **NUMBER** |
| Verificar se o valor total em dólares gasto **é menor que** um **número** | **LESS THAN** | **NUMBER** |
| Verificar se o valor total em dólares gasto **é exatamente** um **número** | **EXACTLY** | **NUMBER** |
| Verificar se a última compra ocorreu **após a data X** | **AFTER** | **TIME** |
| Verificar se a última compra ocorreu **antes da data X** | **BEFORE** | **TIME** |
| Verificar se a última compra ocorreu **há mais de X dias** | **MORE THAN** | **TIME** |
| Verificar se a última compra ocorreu **há menos de X dias** | **LESS THAN** | **TIME** |
| Verificar se a compra ocorreu **mais de X (Máx = 50) vezes** | **MORE THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se a compra ocorreu **menos de X (Máx = 50) vezes** | **LESS THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se a compra ocorreu **exatamente X (Máx = 50) vezes** | **EXACTLY** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eventos de compra / rastreamento de receita" }

{% alert note %}
Se você deseja segmentar pelo número de vezes que uma compra específica ocorreu, também deve registrar essa compra individualmente como um [atributo personalizado incremental](#integers).
{% endalert %}

## Caso de uso de táxi/viagem por aplicativo {#example-case}

Para este exemplo, vamos considerar um app de viagem por aplicativo que deseja decidir quais dados de usuários coletar. As seguintes perguntas e processo de brainstorming são um ótimo modelo para as equipes de marketing e desenvolvimento seguirem. Até o final deste exercício, ambas as equipes devem ter uma compreensão sólida de quais eventos e atributos personalizados fazem sentido coletar para ajudar a alcançar seu objetivo.

**Questão do estudo de caso 1: Qual é o objetivo?**

O objetivo deles é simples: eles querem que os usuários chamem táxis pelo app.

**Questão do estudo de caso 2: Quais são as etapas intermediárias no caminho para esse objetivo a partir da instalação do app?**

1. Eles precisam que os usuários comecem o processo de registro e preencham suas informações pessoais.
2. Eles precisam que os usuários concluam e verifiquem o processo de registro inserindo um código no app que recebem via SMS.
3. Eles precisam tentar chamar um táxi.
4. Para chamar um táxi, ele deve estar disponível quando for procurado.

Essas ações poderiam então ser marcadas como os seguintes eventos personalizados:

- Início do registro
- Registro concluído
- Chamadas de táxi bem-sucedidas
- Tentativas de táxi malsucedidas

Depois de implementar os eventos, você pode executar as seguintes campanhas:

1. Envie mensagens para os usuários que começaram o registro, mas não dispararam o evento de registro concluído em um determinado período de tempo.
2. Envie mensagens de parabéns aos usuários que completam o registro.
3. Envie desculpas e crédito promocional aos usuários que tiveram tentativas de chamar táxi malsucedidas que não foram seguidas por uma tentativa bem-sucedida dentro de um determinado período de tempo.
4. Envie promoções para usuários avançados com muitas chamadas de táxi bem-sucedidas para agradecê-los por sua fidelidade.

E muito mais!

**Questão do estudo de caso 3: Que outras informações podemos querer saber sobre nossos usuários para orientar nosso envio de mensagens?**

- Se eles têm ou não algum crédito promocional?
- A avaliação média que eles dão aos seus motoristas?
- Códigos promocionais únicos para o usuário?

Essas características poderiam então ser marcadas como os seguintes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Classificação média do motorista (tipo numérico)
- Código promocional único (tipo string)

Adicionar esses atributos daria a você a capacidade de enviar campanhas para os usuários, como:

1. Lembrar os usuários que não fizeram login em sete dias, mas que têm um crédito promocional, que seu crédito existe e que eles devem voltar ao app para usá-lo!
2. Enviar mensagens aos usuários que dão baixas avaliações aos motoristas para obter feedback direto dos clientes e entender por que eles não gostaram de suas viagens.
3. Usar nossos [recursos de modelo de mensagem e personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) para incluir o atributo de código promocional exclusivo no envio de mensagens direcionadas aos usuários.

## Boas práticas {#best-practices}

### Boas práticas gerais {#general-best-practices}

#### Use propriedades de eventos {#use-event-properties}

- Nomeie um evento personalizado com algo que descreva uma ação que o usuário realiza.
- Faça uso generoso de propriedades de eventos personalizados para representar dados importantes sobre um evento.
- Por exemplo, em vez de capturar um evento personalizado separado para assistir a cada um de 50 filmes diferentes, seria mais eficaz capturar simplesmente "assistir a um filme" como evento e incluir uma propriedade de evento com o nome do filme.

### Boas práticas de desenvolvimento {#development-best-practices}

#### Defina IDs de usuário para todos os usuários {#set-user-ids-for-every-user}

IDs de usuário devem ser definidos para cada um dos seus usuários. Eles devem ser imutáveis e acessíveis quando o usuário abre o app. **Recomendamos fortemente** fornecer esse identificador, pois ele permitirá que você:

- Rastreie seus usuários em diferentes dispositivos e plataformas, melhorando a qualidade dos seus dados comportamentais e demográficos.
- Importe dados sobre seus usuários usando nossa [API de dados de usuários]({{site.baseurl}}/api/endpoints/user_data).
- Direcione usuários específicos com nossa [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) para mensagens gerais e transacionais.

Os IDs de usuário devem ter menos de 512 caracteres e devem ser privados e não facilmente obtidos (por exemplo, não um endereço de e-mail simples ou nome de usuário). Se esse identificador não estiver disponível, a Braze atribuirá um identificador único aos seus usuários, mas você não terá as funcionalidades listadas para IDs de usuário. Evite definir IDs de usuário para usuários para os quais você não possui um identificador único vinculado a eles como indivíduo. Passar um identificador de dispositivo não oferece nenhum benefício em comparação com o rastreamento automático de usuários anônimos que a Braze oferece por padrão. A seguir, alguns exemplos de IDs de usuário adequados e inadequados.

Boas opções para IDs de usuário:

- Endereço de e-mail com hash ou nome de usuário único
- Identificador único de banco de dados

Estes não devem ser usados como IDs de usuário:

- ID do dispositivo
- Número aleatório ou ID de sessão
- Qualquer ID não único
- Endereço de e-mail
- ID de usuário de outro fornecedor terceiro

{% multi_lang_include alerts/important_alerts.md alert='SDK auth' %}

#### Dê nomes legíveis a eventos e atributos personalizados {#give-custom-events-and-attributes-readable-names}

Imagine que você é um profissional de marketing que começa a usar a Braze um ou dois anos após a implementação. Ler uma lista suspensa cheia de nomes como "usr_no_acct" sem contexto adicional pode ser intimidador. Dar nomes identificáveis e legíveis aos seus eventos e atributos facilitará as coisas para todos os usuários da sua plataforma. Considere as seguintes boas práticas:

- Não comece um evento personalizado com um caractere numérico. A lista suspensa é ordenada alfabeticamente e começar com um caractere numérico torna mais difícil segmentar pelo filtro desejado.
- Tente não usar abreviações obscuras ou jargão técnico quando possível.
  - Exemplo: `usr_ctry` pode ser aceitável como nome de variável para o país de um usuário em um trecho de código, mas o atributo personalizado deve ser enviado à Braze como algo como `user_country` para dar mais clareza a um profissional de marketing que usará o dashboard futuramente.

#### Registre atributos apenas quando eles mudarem {#only-log-attributes-when-they-change}

Contamos cada atributo enviado à Braze como um ponto de dados, mesmo que o atributo enviado contenha o mesmo valor salvo anteriormente. Registrar dados apenas quando eles mudam ajuda a evitar o uso redundante de pontos de dados e proporciona uma experiência mais fluida ao evitar chamadas de API desnecessárias.

#### Evite gerar nomes de eventos programaticamente {#avoid-programmatically-generating-event-names}

Se você está constantemente criando novos nomes de eventos, será impossível segmentar seus usuários de forma significativa. De modo geral, você deve capturar eventos genéricos ("Assistiu a um vídeo" ou "Leu um artigo") em vez de eventos altamente específicos como ("Assistiu Gangnam Style" ou "Leu artigo: Melhores 10 lugares para almoçar em Midtown Manhattan"). Os dados específicos sobre o evento devem ser incluídos como uma propriedade de evento, não como parte do nome do evento.

### Limitações e restrições técnicas {#technical-limitations-and-constraints}

Esteja atento às seguintes limitações e restrições ao implementar eventos personalizados:

#### Restrições de comprimento {#length-constraints}

A Braze impõe um limite de comprimento em bytes (479 bytes) para nomes de eventos personalizados, nomes de atributos personalizados (chaves) e valores de string de eventos personalizados. Valores que excedem esse limite são truncados. Quando expresso em caracteres, isso equivale a aproximadamente 479 caracteres de byte único (por exemplo, ASCII), ou aproximadamente 160 caracteres para scripts multibyte como japonês (assumindo cerca de 3 bytes por caractere em UTF-8). Idealmente, mantenha nomes e valores o mais curtos possível para melhorar o desempenho de rede e bateria do seu app — se possível, limite-os a 50 caracteres.

#### Restrições de conteúdo {#content-constraints}

O conteúdo a seguir será removido programaticamente dos seus atributos e eventos. Tome cuidado para não usar o seguinte:

- Espaços em branco no início e no final
- Quebras de linha
- Todos os não dígitos em números de telefone
  - Exemplo: "(732) 178-1038" será condensado para "7321781038"
- Caracteres que não são espaços em branco devem ser convertidos em espaços
- $ não deve ser usado como prefixo para nenhum evento personalizado
- Quaisquer valores de codificação UTF-8 inválidos
  - "My \x80 Field" seria condensado para "My Field"

#### Chaves reservadas {#reserved-keys}

As seguintes chaves são reservadas e não podem ser usadas como propriedades de eventos personalizados:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Definições de valores {#value-definitions}

- Valores inteiros são de 64 bits
- Decimais têm 15 dígitos decimais por padrão

### Analisando um campo de nome genérico {#parsing-a-generic-name-field}

Se existir apenas um único campo de nome genérico para um usuário (por exemplo, 'JohnDoe'), você pode atribuir esse título inteiro ao atributo de nome do seu usuário. Além disso, você pode tentar separar o primeiro e o último nome do usuário usando espaços, mas esse último método traz o risco potencial de nomear incorretamente alguns dos seus usuários.