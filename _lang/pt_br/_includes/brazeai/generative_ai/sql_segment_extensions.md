# Extensões de Segment or segmento or segmento do SQL {#sql-segment-extensions}

> Você pode gerar uma extensão de Segment or segmento or segmento usando consultas de SQL do Snowflake de dados do [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). O SQL pode ajudar a desbloquear novos casos de uso de segmentos porque oferece a flexibilidade de descrever as relações entre os dados de maneiras que não são possíveis por meio de outros recursos de segmentação.
>
> Assim como as extensões de Segment or segmento or segmento padrão, você pode consultar eventos dos últimos dois anos (730 dias) na sua extensão de Segment or segmento or segmento SQL. Diferentemente das extensões de Segment or segmento or segmento padrão, as extensões de Segment or segmento or segmento SQL [consomem créditos](#credits).

## Pré-requisitos {#prerequisites}

Como é possível acessar dados de IPI por meio desse recurso, você deve ter permissões de IPI para executar consultas de SQL de Segment or segmento or segmento.

## Criando uma extensão de Segment or segmento or segmento {#creating-a-segment-extension}

### Etapa 1: Escolha um editor {#step-1-choose-an-editor}

Existem dois tipos de editores SQL para escolher ao criar sua extensão de Segment or segmento or segmento SQL: o Editor SQL e o Editor SQL Incremental.

- **Atualização completa:** Cada vez que seu Segment or segmento or segmento é atualizado, a Braze consultará todos os dados disponíveis para atualizar seu Segment or segmento or segmento, o que consumirá mais créditos do que atualizações incrementais. Extensões de atualização completa podem regenerar automaticamente a associação diariamente, mas não podem ser atualizadas usando atualização incremental.
- **Atualização incremental:** A atualização incremental é uma forma mais eficiente em termos de custo para configurar sua consulta, embora a configuração envolva algumas [etapas](#step-2-write-your-sql) adicionais. Se você conseguir completar essas etapas adicionais ao construir seu Segment or segmento or segmento, vale a pena escolher essa opção porque sua consulta será executada usando menos créditos.
- **Gerador de SQL com IA:** O gerador de SQL com IA permite que você escreva um prompt em linguagem simples e o transforma em uma consulta SQL para o seu Segment or segmento or segmento. É uma maneira rápida de começar sem precisar escrever o SQL você mesmo.

{% alert tip %}
Você pode fazer uma atualização completa manual em todos os Segments SQL criados em qualquer um dos editores SQL.
{% endalert %}

{% tabs local %}
{% tab Atualização completa %}

Para criar uma extensão de Segment or segmento or segmento SQL com atualização completa:

1. Acesse **Público** > **Extensões de Segment or segmento or segmento**.
2. Selecione **Criar nova extensão** e depois selecione **Atualização completa**.<br><br>
   ![Modal de criar nova extensão com opções de atualização completa e atualização incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Adicione um nome para sua extensão de Segment or segmento or segmento e insira seu SQL. Consulte a [Etapa 2](#step-2-write-your-sql) para requisitos e recursos.<br><br>
   ![Editor SQL mostrando um exemplo de extensão de Segment or segmento or segmento SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Salve sua extensão de Segment or segmento or segmento.

{% endtab %}
{% tab Atualização incremental %}

Para criar uma extensão de Segment or segmento or segmento SQL com atualização incremental:

1. Acesse **Público** > **Extensões de Segment or segmento or segmento**.
2. Selecione **Criar nova extensão** e selecione **Atualização incremental**.<br><br>
   ![Modal de criar nova extensão com opções de atualização completa e atualização incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Adicione um nome para sua extensão de Segment or segmento or segmento e insira seu SQL. Consulte a seção [Escrevendo SQL](#writing-sql) para requisitos e recursos.<br><br>
   ![Editor SQL mostrando um exemplo de extensão de Segment or segmento or segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Se desejar, selecione **Regenerar extensão diariamente**.<br><br>
   ![Caixa de seleção para regenerar a extensão diariamente.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Quando selecionado, a Braze atualizará automaticamente a associação do Segment or segmento or segmento a cada dia. Isso significa que, a cada dia à meia-noite no fuso horário da sua empresa (com um possível atraso de uma hora), a Braze verificará novos usuários no seu Segment or segmento or segmento e os adicionará automaticamente. Se uma extensão de Segment or segmento or segmento não for utilizada por 7 dias, a Braze pausará automaticamente a regeneração diária. Uma extensão de Segment or segmento or segmento não utilizada é aquela que não faz parte de uma Campaign ou Canvas (a Campaign ou Canvas não precisa estar ativa para que a extensão seja considerada "em uso").<br><br>
5. Salve sua extensão de Segment or segmento or segmento.

{% endtab %}

{% tab Gerador de SQL com IA %}

{% alert note %}
O gerador de SQL com IA está disponível atualmente como recurso beta. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse teste beta.
{% endalert %}

O gerador de SQL com IA utiliza o [GPT](https://openai.com/gpt-4), desenvolvido pela OpenAI, para recomendar SQL para o seu Segment or segmento or segmento SQL.

![Gerador de SQL com IA com o prompt "Usuários que receberam uma notificação no mês passado"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Para usar o gerador de SQL com IA, faça o seguinte:

1. Selecione **Iniciar gerador de SQL com IA** após criar um [Segment or segmento or segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) usando atualização completa ou incremental.
2. Digite seu prompt e selecione **Gerar** para transformar seu prompt em SQL.
3. Revise o SQL gerado para garantir que está correto e salve seu Segment or segmento or segmento.

#### Exemplos de prompts {#example-prompts}

- Usuários que receberam um e-mail no último mês
- Usuários que fizeram menos de cinco compras no último ano

#### Dicas {#tips}

- Familiarize-se com as [tabelas de dados do Snowflake]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) disponíveis. Solicitar dados que não existem nessas tabelas pode resultar no ChatGPT inventando uma tabela fictícia.
- Familiarize-se com as [regras de escrita SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) para este recurso. Não seguir essas regras causará um erro. Por exemplo, seu código SQL deve selecionar a coluna `user_id`. Começar seu prompt com "usuários que" pode ajudar.
- Você pode enviar até 20 prompts por minuto com o gerador de SQL com IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
Consultas SQL que levarem mais de 20 minutos para serem executadas serão encerradas por timeout.
{% endalert %}

Quando a extensão terminar o processamento, você pode [criar um Segment or segmento or segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) usando sua extensão de Segment or segmento or segmento e direcionar esse novo Segment or segmento or segmento com suas Campaigns e Canvas.

### Etapa 2: Escreva seu SQL {#step-2-write-your-sql}

Sua consulta SQL deve ser escrita usando a [sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consulte a [referência de tabelas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) para uma lista completa de tabelas e colunas disponíveis para consulta.

{% alert important %}
Observe que as tabelas disponíveis para consulta contêm apenas dados de eventos. Se você deseja consultar atributos de usuário, deve combinar seu Segment or segmento or segmento SQL com filtros de atributos personalizados do [segmentador clássico]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
{% endalert %}

{% tabs %}
{% tab Editor SQL %}

Seu SQL também deve seguir as seguintes regras:

- Escreva uma única instrução SQL. Não inclua pontos e vírgulas.
- Seu SQL deve selecionar apenas uma coluna: a coluna `user_id`. Isso significa que seu SQL deve conter:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Não é possível consultar usuários com zero eventos, o que significa que qualquer consulta para usuários que realizaram um evento menos de X vezes precisaria seguir esta solução alternativa:
   1. Escreva uma consulta para selecionar usuários que têm o evento MAIS de X vezes.
   2. Ao referenciar sua extensão de Segment or segmento or segmento no seu Segment or segmento or segmento, selecione `doesn't include` para inverter o resultado.

#### Regras adicionais {#additional-rules}

Além disso, sua consulta SQL padrão deve seguir as seguintes regras:

- Você não pode usar instruções `DECLARE`.
{% endtab %}
{% tab Editor SQL Incremental %}

Todas as consultas de atualização incremental consistem em duas partes: uma consulta e detalhes do esquema.

1. No editor, escreva uma consulta que selecione `user_id`s da tabela desejada.
2. Adicione detalhes do esquema selecionando um **Operador**, **Número de vezes** e **Período de tempo** nos campos na parte superior do editor. A consulta verificará se a soma da coluna agregada atende a uma determinada condição especificada pelos placeholders {% raw %}`{{operator}}` e `{{number of times}}`{% endraw %}. Isso funciona de forma semelhante ao fluxo de trabalho para criar extensões de Segment or segmento or segmento clássicas.<br><br>
   - **Operador:** Indique se o evento ocorreu mais vezes, menos vezes ou igual a um número de ocorrências.<br>
   ![Campo de operador com "Mais que" selecionado.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Número de vezes:** Quantas vezes você gostaria de avaliar o evento em relação ao operador.<br>
   ![Campo de número de vezes com "5" inserido.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Período de tempo:** Número de dias de 1 a 730 em que você deseja verificar instâncias do evento. Esse período de tempo se refere a dias passados em relação ao dia atual. O exemplo a seguir mostra a consulta de usuários que realizaram o evento mais de 5 vezes nos últimos 365 dias.<br>
   ![Campo de período de tempo com "365" inserido.]({% image_buster /assets/img_archive/sql_segments_period.png %})

No exemplo a seguir, o Segment or segmento or segmento resultante conteria usuários que realizaram o evento `favorited` mais de 3 vezes durante os últimos 30 dias, após uma data especificada.

![Editor SQL mostrando um exemplo de extensão de Segment or segmento or segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Prévia SQL de uma extensão de Segment or segmento or segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
Segmentos de atualização incremental consideram eventos atrasados, que são eventos ocorridos há mais de 2 dias (por exemplo, eventos do SDK or kit de desenvolvimento de software que não foram enviados no momento em que foram capturados).
{% endalert %}

#### Regras adicionais

Além disso, sua consulta de atualização incremental deve seguir as seguintes regras:

- Escreva uma única instrução SQL. Não inclua pontos e vírgulas.
- Seu Segment or segmento or segmento SQL incremental pode fazer referência a apenas um único evento. Seus menus suspensos de data e contagem são referentes ao evento escolhido.
- Seu SQL deve conter as seguintes colunas: `user_id`, `$start_date` e uma função de agregação (como `COUNT`). Qualquer SQL salvo sem esses três campos resultará em um erro.
- Você não pode usar instruções `DECLARE`.
{% endtab %}
{% endtabs %}

{% alert note %}
Se você estiver criando um Segment or segmento or segmento SQL que usa a tabela `CATALOGS_ITEMS_SHARED`, deve especificar um ID de catálogo. Por exemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Etapa 3: Visualize a consulta {#step-3-preview-the-query}

Antes de salvar, você pode executar uma prévia da sua consulta. Prévias de consultas são automaticamente limitadas a 100 linhas e terão timeout após 60 segundos. O requisito da coluna `user_id` não se aplica ao executar uma prévia.

Para extensões de Segment or segmento or segmento SQL incrementais, a prévia não incluirá os critérios adicionais do operador, número de vezes e campos de período de tempo.

### Etapa 4: Determine se você precisa inverter o SQL {#step-4-determine-if-you-need-to-invert-sql}

Em seguida, determine se você precisa inverter o SQL. Embora não seja possível consultar diretamente usuários com zero eventos, você pode usar **Inverter SQL** para direcionar esses usuários.

{% alert note %}
Por padrão, **Inverter SQL** não está ativado. No entanto, se você usar o gerador de SQL com IA para gerar uma instrução SQL que precisa ser negada, o ChatGPT pode retornar um resultado que ativa automaticamente esse recurso.
{% endalert %}

Por exemplo, para direcionar usuários que fizeram menos de três compras, primeiro escreva uma consulta para selecionar usuários que fizeram três ou mais compras. Depois, selecione **Inverter SQL** para direcionar usuários com menos de três compras (incluindo aqueles com zero compras).

{% alert important %}
A menos que você esteja especificamente direcionando usuários com zero eventos, não será necessário inverter o SQL. Se **Inverter SQL** estiver selecionado, confirme que o recurso é necessário e que o Segment or segmento or segmento corresponde ao público desejado. Por exemplo, se uma consulta direciona usuários com pelo menos um evento, ela direcionará apenas usuários com zero eventos quando invertida.
{% endalert %}

![Extensão de Segment or segmento or segmento chamada "Clicou em 1-4 e-mails nos últimos 30 dias" com a opção de inverter SQL selecionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Atualizando a associação ao Segment or segmento or segmento {#refreshing-segment-membership}

Para atualizar a associação ao Segment or segmento or segmento de qualquer extensão de Segment or segmento or segmento criada usando SQL, abra a extensão de Segment or segmento or segmento e selecione **Refresh**.

{% alert tip %}
Se você criou um Segment or segmento or segmento em que espera que os usuários entrem e saiam regularmente, atualize manualmente a extensão de Segment or segmento or segmento que ele utiliza antes de direcionar esse Segment or segmento or segmento em uma Campaign ou Canvas.
{% endalert %}

## Gerenciando suas extensões de Segment or segmento or segmento {#managing-your-segment-extensions}

Na página **Extensões de Segment or segmento or segmento**, os segmentos gerados usando SQL são indicados com <i class="fas fa-code" alt="Extensão de Segment or segmento or segmento SQL"></i> ao lado do nome.

Selecione uma extensão de Segment or segmento or segmento SQL para ver onde a extensão está sendo usada, arquivar a extensão ou [atualizar manualmente a associação ao Segment or segmento or segmento](#refreshing-segment-membership).

![Seção de uso de envio de mensagens do editor SQL mostrando onde o Segment or segmento or segmento SQL está sendo usado.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Definindo configurações de atualização {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Créditos do Snowflake {#credits}

Cada espaço de trabalho da Braze tem 5 créditos do Snowflake disponíveis por mês. Se precisar de mais créditos, entre em contato com o gerente da sua conta. Os créditos são usados sempre que você atualiza, ou salva e atualiza, a associação de um Segment or segmento or segmento SQL. Os créditos não são usados quando você executa prévias em um Segment or segmento or segmento SQL ou salva ou atualiza uma extensão de Segment or segmento or segmento clássica.

{% alert note %}
Os créditos do Snowflake não são compartilhados entre os recursos. Por exemplo, os créditos das extensões de Segment or segmento or segmento SQL e do Criador de consultas são independentes um do outro.
{% endalert %}

O uso de créditos está correlacionado ao tempo de execução da sua consulta de SQL. Quanto maior o tempo de execução, mais créditos a consulta custará. O tempo de execução pode variar de acordo com a complexidade e o tamanho das suas consultas ao longo do tempo. Quanto mais complexas e frequentes forem as consultas executadas, maior será a alocação de recursos e mais rápido será o tempo de execução.

Para economizar créditos, faça uma prévia da sua consulta para garantir que ela esteja correta antes de salvar a extensão de Segment or segmento or segmento SQL.

Seus créditos serão redefinidos para 5 no primeiro dia de cada mês, às 12h UTC. Você pode monitorar o uso dos seus créditos durante o mês no painel de uso de créditos. Na página **Extensões de Segment or segmento or segmento**, clique em <i class="fa-solid fa-chart-column"></i> **Ver uso de créditos SQL**.

![Painel de uso de créditos SQL na página de extensões de Segment or segmento or segmento SQL]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

O seguinte acontecerá quando seus créditos chegarem a zero:

- Todas as extensões de Segment or segmento or segmento SQL configuradas para atualização automática deixam de ser atualizadas, afetando a associação desses segmentos e todas as Campaigns ou Canvas direcionados a esses segmentos.
- Você só poderá salvar novas extensões de Segment or segmento or segmento SQL como rascunhos durante o restante do mês.

Todos os usuários da empresa que criaram um Segment or segmento or segmento SQL e os administradores da sua empresa receberão um e-mail de notificação quando você tiver usado 50%, 80% e 100% dos seus créditos. Depois que seus créditos forem redefinidos no início do mês seguinte, você poderá criar mais segmentos SQL, e as atualizações automáticas serão retomadas.

Se quiser comprar mais créditos de Segment or segmento or segmento SQL ou extensões de Segment or segmento or segmento adicionais, entre em contato com o gerente da sua conta.