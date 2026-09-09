# Extensões de Segment do SQL {#sql-segment-extensions}

> Você pode gerar uma extensão de Segment usando consultas de SQL do Snowflake de dados do [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). O SQL pode ajudar a desbloquear novos casos de uso de segmentos porque oferece a flexibilidade de descrever as relações entre os dados de maneiras que não são possíveis por meio de outros recursos de segmentação.
>
> Assim como as extensões de Segment padrão, você pode consultar eventos dos últimos dois anos (730 dias) na sua extensão de Segment SQL. Diferentemente das extensões de Segment padrão, as extensões de Segment SQL [consomem créditos](#credits).

## Pré-requisitos {#prerequisites}

Como é possível acessar dados de IPI por meio desse recurso, você deve ter permissões de IPI para executar consultas de SQL de Segment.

## Criando uma extensão de Segment {#creating-a-segment-extension}

### Etapa 1: Escolha um editor {#step-1-choose-an-editor}

Existem dois tipos de editores SQL para escolher ao criar sua extensão de Segment SQL: o Editor SQL e o Editor SQL Incremental.

- **Atualização completa:** Cada vez que seu Segment é atualizado, a Braze consultará todos os dados disponíveis para atualizar seu Segment, o que usará mais créditos do que atualizações incrementais. Extensões de atualização completa podem regenerar automaticamente a associação diariamente, mas não podem ser atualizadas usando atualização incremental.
- **Atualização incremental:** A atualização incremental é uma forma mais eficiente em termos de custo para configurar sua consulta, embora a configuração envolva algumas [etapas](#step-2-write-your-sql) adicionais. Se você conseguir completar essas etapas adicionais ao construir seu Segment, vale a pena escolher essa opção porque sua consulta será executada usando menos créditos.
- **Gerador de SQL com IA:** O Gerador de SQL com IA permite que você escreva um prompt em linguagem natural e o transforme em uma consulta SQL para o seu Segment. É uma maneira rápida de começar sem precisar escrever o SQL você mesmo.

{% alert tip %}
Você pode fazer uma atualização completa manual em todos os Segments SQL criados em qualquer editor SQL.
{% endalert %}

{% tabs local %}
{% tab Atualização completa %}

Para criar uma extensão de Segment SQL com atualização completa:

1. Acesse **Público** > **Extensões de Segment**.
2. Selecione **Criar nova extensão** e, em seguida, selecione **Atualização completa**.<br><br>
   ![Modal de Criar nova extensão com opções de Atualização completa e Atualização incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Adicione um nome para sua extensão de Segment e insira seu SQL. Consulte a [Etapa 2](#step-2-write-your-sql) para requisitos e recursos.<br><br>
   ![Editor SQL mostrando um exemplo de extensão de Segment SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Salve sua extensão de Segment.

{% endtab %}
{% tab Atualização incremental %}

Para criar uma extensão de Segment SQL com atualização incremental:

1. Acesse **Público** > **Extensões de Segment**.
2. Selecione **Criar nova extensão** e selecione **Atualização incremental**.<br><br>
   ![Modal de Criar nova extensão com opções de Atualização completa e Atualização incremental.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Adicione um nome para sua extensão de Segment e insira seu SQL. Consulte a seção [Escrevendo SQL](#writing-sql) para requisitos e recursos.<br><br>
   ![Editor SQL mostrando um exemplo de extensão de Segment SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Se desejar, selecione **Regenerar extensão diariamente**.<br><br>
   ![Caixa de seleção para regenerar a extensão diariamente.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Quando selecionada, a Braze atualizará a associação do Segment automaticamente a cada dia. Isso significa que todos os dias à meia-noite no fuso horário da sua empresa (com um possível atraso de uma hora), a Braze verificará se há novos usuários no seu Segment e os adicionará automaticamente ao seu Segment. Se uma extensão de Segment não for usada por 7 dias, a Braze pausará automaticamente a regeneração diária. Uma extensão de Segment não utilizada é aquela que não faz parte de uma Campaign ou Canvas (a Campaign ou Canvas não precisa estar ativa para que a extensão seja considerada "em uso").<br><br>
5. Salve sua extensão de Segment.

{% endtab %}

{% tab Gerador de SQL com IA %}

{% alert note %}
O gerador de SQL com IA está atualmente disponível como um recurso beta. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar dessa versão beta.
{% endalert %}

O gerador de SQL com IA utiliza o [GPT](https://openai.com/gpt-4), desenvolvido pela OpenAI, para recomendar SQL para o seu Segment SQL.

![Gerador de SQL com IA com o prompt "Usuários que receberam uma notificação no último mês"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Para usar o gerador de SQL com IA, faça o seguinte:

1. Selecione **Iniciar gerador de SQL com IA** após criar um [Segment SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) usando atualização completa ou incremental.
2. Digite seu prompt e selecione **Gerar** para traduzir seu prompt em SQL.
3. Revise o SQL gerado para verificar se está correto e, em seguida, salve seu Segment.

#### Exemplos de prompts {#example-prompts}

- Usuários que receberam um e-mail no último mês
- Usuários que fizeram menos de cinco compras no último ano

#### Dicas {#tips}

- Familiarize-se com as [tabelas de dados do Snowflake]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) disponíveis. Pedir dados que não existem nessas tabelas pode fazer com que o ChatGPT invente uma tabela falsa.
- Familiarize-se com as [regras de escrita SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) para este recurso. Não seguir essas regras causará um erro. Por exemplo, seu código SQL deve selecionar a coluna `user_id`. Começar seu prompt com "usuários que" pode ajudar.
- Você pode enviar até 20 prompts por minuto com o gerador de SQL com IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
Consultas SQL que levam mais de 20 minutos para serem executadas atingirão o tempo limite.
{% endalert %}

Quando a extensão terminar de ser processada, você pode [criar um Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) usando sua extensão de Segment e direcionar esse novo Segment com suas Campaigns e Canvas.

### Etapa 2: Escreva seu SQL {#step-2-write-your-sql}

Sua consulta SQL deve ser escrita usando a [sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consulte a [referência de tabelas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) para uma lista completa de tabelas e colunas disponíveis para consulta.

{% alert important %}
Observe que as tabelas disponíveis para consulta contêm apenas dados de eventos. Se você deseja consultar atributos de usuário, deve combinar seu Segment SQL com filtros de atributos personalizados do [segmentador clássico]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
{% endalert %}

{% tabs %}
{% tab Editor SQL %}

Seu SQL também deve seguir as seguintes regras:

- Escreva uma única instrução SQL. Não inclua ponto e vírgula.
- Seu SQL deve selecionar apenas uma coluna: a coluna `user_id`. Isso significa que seu SQL deve conter:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Não é possível consultar usuários com zero eventos, o que significa que qualquer consulta para usuários que realizaram um evento menos de X vezes precisaria seguir esta solução alternativa:
   1. Escreva uma consulta para selecionar usuários que realizaram o evento MAIS de X vezes.
   2. Ao referenciar sua extensão de Segment no seu Segment, selecione `doesn't include` para inverter o resultado.

#### Regras adicionais {#additional-rules}

Além disso, sua consulta SQL padrão deve seguir as seguintes regras:

- Você não pode usar instruções `DECLARE`.
{% endtab %}
{% tab Editor SQL Incremental %}

Todas as consultas de atualização incremental consistem em duas partes: uma consulta e detalhes do esquema.

1. No editor, escreva uma consulta que selecione `user_id`s da tabela desejada.
2. Adicione detalhes do esquema selecionando um **Operador**, **Número de vezes** e **Período de tempo** nos campos na parte superior do editor. A consulta verifica se a soma da coluna agregada atende à condição que você definiu com esses campos. Isso funciona de maneira similar ao fluxo de trabalho para criar extensões de Segment clássicas.<br><br>
   - **Operador:** Indique se o evento aconteceu mais do que, menos do que ou igual a um número de ocorrências.<br>
   ![Campo do operador com "Mais do que" selecionado.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Número de vezes:** Quantas vezes você gostaria de avaliar o evento em relação ao operador.<br>
   ![Número de vezes com "5" inserido.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Período de tempo:** Número de dias de 1 a 730 em que você deseja verificar instâncias do evento. Esse período de tempo refere-se a dias passados em relação ao dia atual. O exemplo a seguir mostra a consulta de usuários que realizaram o evento mais de 5 vezes nos últimos 365 dias.<br>
   ![Campo de período de tempo com "365" inserido.]({% image_buster /assets/img_archive/sql_segments_period.png %})

No exemplo a seguir, o Segment resultante conteria usuários que realizaram o evento `favorited` mais de 3 vezes durante os últimos 30 dias, após uma data especificada.

![Editor SQL mostrando um exemplo de extensão de Segment SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Prévia SQL de uma extensão de Segment SQL incremental.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
A atualização incremental considera eventos atrasados — eventos que chegam após a janela de atualização diária, como eventos do SDK que não foram enviados quando foram capturados. Quando o Segment é atualizado, a Braze reprocessa as datas às quais esses eventos atrasados pertencem.
{% endalert %}

#### Como a atualização incremental rastreia usuários ao longo do tempo {#how-incremental-refresh-tracks-users-over-time}

Quando você usa a atualização incremental, a Braze armazena contagens diárias para cada usuário em uma tabela de contagens interna para poder avaliar seu Segment ao longo de todo o período de tempo sem precisar reconsultar todos os dados históricos a cada dia.

**O que é armazenado:** A Braze mantém uma tabela de contagens (similar a uma tabela de coortes de Segment) que acumula contagens diárias de qualificação de usuários no formato `(date, user_id, count)`. Essa tabela persiste dados históricos fora da janela de atualização contínua de dois dias.

**O que acontece em cada atualização:** Quando uma atualização incremental é executada, a Braze limpa apenas os registros da janela de atualização contínua de dois dias da tabela de contagens. Em seguida, reexecuta sua consulta SQL com parâmetros de tempo atualizados (usando `$start_date`) para inserir novas linhas para essas datas. As linhas históricas fora da janela de atualização contínua de dois dias permanecem intactas na tabela de contagens.

**Como a Braze decide quem está no Segment:** A Braze avalia os critérios de associação do seu Segment em relação a toda a tabela de contagens acumulada, não apenas à carga útil mais recente da janela de atualização contínua de dois dias. Isso significa que os usuários que se qualificaram há mais de dois dias permanecem no Segment, a menos que as contagens agregadas não atendam mais aos seus critérios.

**Escrevendo SQL que atualiza de forma confiável:** Ao escrever SQL para atualização incremental, evite padrões de consulta que possam produzir resultados inconsistentes durante atualizações parciais. Por exemplo, agregações com janela como `MAX(time)` que dependem de dados entre os limites de `$start_date` podem alterar o estado da linha inesperadamente quando apenas um subconjunto de datas é recalculado. Estruture suas consultas de modo que a saída de cada data dependa apenas dos eventos daquela data, o que mantém resultados consistentes independentemente de a consulta processar dois dias ou 730 dias de dados.

#### Regras adicionais

Além disso, sua consulta de atualização incremental deve seguir as seguintes regras:

- Escreva uma única instrução SQL. Não inclua ponto e vírgula.
- Seu Segment SQL incremental pode referenciar apenas um evento. Seus menus suspensos de data e contagem se aplicam a esse evento.
- Seu SQL deve incluir o alias `$date()` (por exemplo, `$date(time)`), selecionar `user_id` e uma agregação `COUNT()`, agrupar por data e `user_id`, e filtrar com `$start_date` na sua coluna de tempo (por exemplo, `time > $start_date`). Salvar SQL sem `$date()` ou esses campos retornará um erro.
- Você não pode usar instruções `DECLARE`.
{% endtab %}
{% endtabs %}

{% alert note %}
Se você estiver criando um Segment SQL que usa a tabela `CATALOGS_ITEMS_SHARED`, você deve especificar um ID de catálogo. Por exemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Etapa 3: Visualize a consulta {#step-3-preview-the-query}

Antes de salvar, você pode executar uma prévia da sua consulta. As prévias de consulta são automaticamente limitadas a 100 linhas e atingirão o tempo limite após 60 segundos. O requisito da coluna `user_id` não se aplica ao executar uma prévia.

Para extensões de Segment SQL incrementais, a prévia não incluirá os critérios adicionais dos seus campos de operador, número de vezes e período de tempo.

### Etapa 4: Determine se você precisa inverter o SQL {#step-4-determine-if-you-need-to-invert-sql}

Em seguida, determine se você precisa inverter o SQL. Embora não seja possível consultar diretamente usuários com zero eventos, você pode usar **Inverter SQL** para direcionar esses usuários.

{% alert note %}
Por padrão, **Inverter SQL** não está ativado. No entanto, se você usar o gerador de SQL com IA para gerar uma instrução SQL que precisa ser negada, o ChatGPT pode retornar uma saída que ativa automaticamente esse recurso.
{% endalert %}

Por exemplo, para direcionar usuários que têm menos de três compras, primeiro escreva uma consulta para selecionar usuários que têm três ou mais compras. Em seguida, selecione **Inverter SQL** para direcionar usuários com menos de três compras (incluindo aqueles com zero compras).

{% alert important %}
A menos que você esteja especificamente tentando direcionar usuários com zero eventos, você não precisará inverter o SQL. Se **Inverter SQL** estiver selecionado, confirme que o recurso é necessário e que o Segment corresponde ao público desejado. Por exemplo, se uma consulta direciona usuários com pelo menos um evento, ela direcionará apenas usuários com zero eventos quando invertida.
{% endalert %}

![Extensão de Segment chamada "Clicaram em 1 a 4 e-mails nos últimos 30 dias" com a opção de inverter SQL selecionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Atualizando a associação ao segmento {#refreshing-segment-membership}

Para atualizar a associação ao segmento de qualquer extensão de segmento criada usando SQL, abra a extensão de segmento e selecione **Refresh**.

{% alert tip %}
Se você criou um segmento em que espera que os usuários entrem e saiam regularmente, atualize manualmente a extensão de segmento utilizada antes de direcionar esse segmento em uma Campaign ou Canvas.
{% endalert %}

## Gerenciando suas extensões de segmento {#managing-your-segment-extensions}

Na página **Extensões de Segment**, os segmentos gerados usando SQL são indicados com <i class="fas fa-code" alt="Extensão de Segment SQL"></i> ao lado do nome.

Selecione uma extensão de Segment SQL para ver onde a extensão está sendo usada, arquivar a extensão ou [atualizar manualmente a associação do segmento](#refreshing-segment-membership).

![Seção de uso de envio de mensagens do editor SQL mostrando onde o segmento SQL está sendo usado.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Definindo configurações de atualização {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Créditos do Snowflake {#credits}

Cada espaço de trabalho da Braze tem 5 créditos do Snowflake disponíveis por mês. Se precisar de mais créditos, entre em contato com o gerente da sua conta. Os créditos são usados sempre que você atualiza, ou salva e atualiza, a associação de um Segment SQL. Os créditos não são usados quando você executa prévias em um Segment SQL ou salva ou atualiza uma extensão de Segment clássica.

{% alert note %}
Os créditos do Snowflake não são compartilhados entre os recursos. Por exemplo, os créditos das extensões de Segment SQL e do Criador de consultas são independentes um do outro.
{% endalert %}

O uso de créditos está correlacionado ao tempo de execução da sua consulta de SQL. Quanto maior o tempo de execução, mais créditos a consulta custará. O tempo de execução pode variar de acordo com a complexidade e o tamanho das suas consultas ao longo do tempo. Quanto mais complexas e frequentes forem as consultas executadas, maior será a alocação de recursos e mais rápido será o tempo de execução.

Para economizar créditos, faça uma prévia da sua consulta para garantir que ela esteja correta antes de salvar a extensão de Segment SQL.

Seus créditos serão redefinidos para 5 no primeiro dia de cada mês, às 12h UTC. Você pode monitorar o uso dos seus créditos durante o mês no painel de uso de créditos. Na página **Extensões de Segment**, clique em <i class="fa-solid fa-chart-column"></i> **Ver uso de créditos SQL**.

![Painel de uso de créditos SQL na página de extensões de Segment SQL]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

O seguinte acontecerá quando seus créditos chegarem a zero:

- Todas as extensões de Segment SQL configuradas para atualização automática deixam de ser atualizadas, afetando a associação desses segmentos e todas as Campaigns ou Canvas direcionados a esses segmentos.
- Você só poderá salvar novas extensões de Segment SQL como rascunhos durante o restante do mês.

Todos os usuários da empresa que criaram um Segment SQL e os administradores da sua empresa receberão um e-mail de notificação quando você tiver usado 50%, 80% e 100% dos seus créditos. Depois que seus créditos forem redefinidos no início do mês seguinte, você poderá criar mais segmentos SQL, e as atualizações automáticas serão retomadas.

Se quiser comprar mais créditos de Segment SQL ou extensões de Segment adicionais, entre em contato com o gerente da sua conta.