---
nav_title: Melhores práticas
article_title: Melhores práticas
toc_headers: h2
page_order: 1
page_type: reference
description: "Esta página fornece uma visão geral da Ingestão de Dados na Nuvem, melhores práticas e limitações do produto."
---

# Melhores práticas {#best-practices}

> A Ingestão de Dados na Nuvem da Braze permite que você configure uma conexão direta do seu data warehouse ou sistema de armazenamento de arquivos para a Braze, sincronizando dados relevantes de usuários ou catálogos. Quando você sincroniza esses dados com a Braze, pode aproveitá-los para casos de uso como personalização, acionamento ou segmentação.

## Entendendo a coluna `UPDATED_AT` {#understanding-the-updated_at-column}

{% alert note %}
`UPDATED_AT` é relevante apenas para integrações com data warehouse, não para sincronizações com S3.
{% endalert %}

Quando uma sincronização é executada, a Braze se conecta diretamente à sua instância de data warehouse, recupera todos os novos dados da tabela especificada e atualiza os dados correspondentes no seu dashboard da Braze. Cada vez que a sincronização é executada, a Braze reflete todos os dados atualizados.

{% alert important %}
O CDI da Braze sincroniza as linhas estritamente com base no valor de `UPDATED_AT`, independentemente de o conteúdo da linha ser igual ao que está atualmente na Braze. Sendo assim, recomendamos usar `UPDATED_AT` corretamente para sincronizar apenas dados novos ou atualizados e evitar uso desnecessário de pontos de dados.
{% endalert %}

### Exemplo: sincronização recorrente {#example-recurring-sync}

Para ilustrar como `UPDATED_AT` é usado em uma sincronização CDI, considere este exemplo de sincronização recorrente para atualização de atributos de usuários:

- Fontes de armazenamento de arquivos
   - Amazon S3

## Tipos de dados compatíveis {#supported-data-types}

A Cloud Data Ingestion oferece suporte aos seguintes tipos de dados:
- Atributos de usuário, incluindo:
   - Atributos personalizados aninhados
   - Vetores de objetos
   - Status de inscrição
- Eventos personalizados
- Eventos de compra
- Itens de catálogo
- Solicitações de exclusão de usuários

### Evitando problemas com tipos de dados {#avoiding-data-type-issues}

Ao usar a CDI para sincronizar dados de fontes externas (como Databricks ou Snowflake), certifique-se de que as colunas de origem usem os tipos de dados corretos antes da sincronização. Problemas comuns incluem:

- **Timestamps armazenados como strings:** Certifique-se de que suas colunas de data usem um tipo timestamp ou datetime no banco de dados de origem, e não varchar ou string.
- **Números armazenados como strings:** Converta colunas numéricas para tipos integer ou float na sua consulta de origem antes de sincronizar.
- **Tipos inconsistentes entre sincronizações:** Se o tipo de uma coluna mudar entre sincronizações, a Braze poderá rejeitar os novos dados. Verifique se o esquema de origem permanece consistente.

Para forçar ou alterar tipos de dados de atributos personalizados no dashboard da Braze, consulte [Gerenciar dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#forcing-data-type-comparisons).

Você pode atualizar dados de usuários por ID externo, alias de usuário, ID da Braze, e-mail ou número de telefone. Você pode excluir usuários por ID externo, alias de usuário ou ID da Braze.

## O que é sincronizado {#what-gets-synced}

Cada vez que uma sincronização é executada, a Braze procura linhas que não foram sincronizadas anteriormente. Isso é verificado por meio da coluna `UPDATED_AT` na sua tabela ou visualização. A Braze seleciona e importa todas as linhas em que `UPDATED_AT` é posterior ao último valor de `UPDATED_AT` sincronizado. Linhas que estejam exatamente no timestamp limite também podem ser ressincronizadas se novas linhas forem adicionadas com esse mesmo timestamp entre as execuções.

{% alert important %}
O CDI rastreia o número de linhas no último valor de `UPDATED_AT` sincronizado. Se novas linhas forem adicionadas com esse mesmo timestamp entre as execuções, o CDI muda para um limite inclusivo (`>=`) e ressincroniza todas as linhas com esse timestamp, incluindo as que já foram processadas. Para evitar sincronizações duplicadas e consumo desnecessário de pontos de dados, use valores de `UPDATED_AT` únicos entre as execuções de sincronização. Para saber mais, consulte [Evitar ressincronizar linhas com timestamps duplicados](#avoid-resyncing-rows-with-duplicate-timestamps).
{% endalert %}

No seu data warehouse, adicione os seguintes usuários e atributos à sua tabela, definindo o horário de `UPDATED_AT` como o momento em que você adiciona esses dados:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Durante a próxima sincronização agendada, a Braze sincroniza todas as linhas com um timestamp de `UPDATED_AT` posterior ao timestamp sincronizado mais recente. A Braze atualiza ou adiciona campos, então você não precisa sincronizar o perfil de usuário completo a cada vez. Após a sincronização, os perfis de usuário refletem as novas atualizações:

**Sincronização recorrente, segunda execução em 20 de julho de 2022 às 12h**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Uma nova linha foi adicionada para `customer_9012`, mas seu valor de `UPDATED_AT` (`2022-07-16 00:25:30`) é anterior ao timestamp armazenado (`2022-07-19 09:07:23`), então ela não será sincronizada. No entanto, a linha existente para `customer_5678` tem um valor de `UPDATED_AT` igual ao timestamp armazenado, então ela é ressincronizada devido ao limite inclusivo. Para saber mais sobre esse comportamento, consulte [Certifique-se de que o horário de UPDATED_AT não seja o mesmo horário da sua sincronização](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync). O `UPDATED_AT` armazenado permanece como `2022-07-19 09:07:23`.

**Sincronização recorrente, terceira execução em 21 de julho de 2022 às 12h**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Nessa terceira execução, outra nova linha foi adicionada para `customer_1234` com um valor de `UPDATED_AT` (`2022-07-21 08:30:00`) posterior ao timestamp armazenado. Essa nova linha e a linha existente para `customer_5678` (que tem um `UPDATED_AT` igual ao timestamp armazenado) são ambas sincronizadas. O `UPDATED_AT` armazenado agora é definido como `2022-07-21 08:30:00`.

{% alert note %}
Os valores de `UPDATED_AT` podem ser até mesmo posteriores ao horário de início da execução de uma determinada sincronização. No entanto, isso não é recomendado, pois empurra o último timestamp de `UPDATED_AT` "para o futuro", e sincronizações subsequentes não sincronizarão valores anteriores.
{% endalert %}

## Use um timestamp UTC para a coluna `UPDATED_AT` {#use-a-utc-timestamp-for-the-updated_at-column}

A coluna `UPDATED_AT` deve estar em UTC para evitar problemas com o horário de verão. Prefira funções exclusivamente UTC, como `SYSDATE()` em vez de `CURRENT_DATE()`, sempre que possível.

## Evitar a ressincronização de linhas com timestamps duplicados {#avoid-resyncing-rows-with-duplicate-timestamps}

A CDI rastreia o número de linhas no último timestamp `UPDATED_AT` sincronizado. Se a CDI detectar que novas linhas foram adicionadas com o mesmo timestamp desde a última execução, ela usa um limite inclusivo (`>=`) para resselecionar todas as linhas naquele timestamp, incluindo as já processadas. Caso contrário, a CDI usa um limite exclusivo (`>`) e seleciona apenas linhas estritamente posteriores ao último valor sincronizado.

Por exemplo, se uma sincronização processa cinco linhas com `UPDATED_AT = 2025-04-01 00:00:00`, e uma sexta linha é adicionada posteriormente com o mesmo timestamp, a próxima sincronização detecta a mudança na contagem e ressincroniza todas as seis linhas. Isso pode resultar em dados duplicados e consumo desnecessário de pontos de dados.

Para evitar isso:

- Se você estiver configurando uma sincronização contra uma `VIEW`, não use `CURRENT_TIMESTAMP` como valor padrão. Isso faz com que todos os dados sejam sincronizados toda vez que a sincronização for executada, porque o campo `UPDATED_AT` é avaliado no momento em que a consulta é executada.
- Se você tiver pipelines ou consultas de longa duração gravando dados na sua tabela de origem, evite executá-los simultaneamente com uma sincronização, ou evite usar o mesmo timestamp para cada linha inserida.
- Use uma transação para gravar todas as linhas que compartilham o mesmo timestamp.
- Use valores `UPDATED_AT` únicos e monotonicamente crescentes para evitar que linhas sejam resselecionadas após terem sido processadas.

### Exemplo: gerenciando atualizações subsequentes {#example-managing-subsequent-updates}

Este exemplo mostra o processo geral para sincronizar dados pela primeira vez e depois atualizar apenas os dados que mudam (deltas) nas atualizações subsequentes. Digamos que temos uma tabela `EXAMPLE_DATA` com alguns dados de usuários. No dia 1, ela tem os seguintes valores:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table aria-label="Exemplo: gerenciando atualizações subsequentes">
  <caption>Exemplo: gerenciando atualizações subsequentes</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Para obter esses dados no formato que a CDI espera, você pode executar a seguinte consulta:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Nada disso foi sincronizado com a Braze antes, então adicione tudo à tabela de origem da CDI:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

Uma sincronização é executada, e a Braze registra que você sincronizou todos os dados disponíveis até "2023-03-16 15:00:00". Então, na manhã do dia 2, você tem um ETL que é executado e alguns campos na sua tabela de usuários são atualizados (marcados com *):

<table aria-label="Exemplo: gerenciando atualizações subsequentes">
  <caption>Exemplo: gerenciando atualizações subsequentes. * indica um campo atualizado desde a última sincronização.</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145*</td>
            <td style="background-color: #FFFF00;">red*</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE*</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15*</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495*</td>
            <td style="background-color: #FFFF00;">FALSE*</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green*</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693*</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Agora você precisa adicionar apenas os valores alterados na tabela de origem da CDI. Essas linhas podem ser anexadas em vez de atualizar as linhas antigas. A tabela agora fica assim:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

A CDI sincronizará apenas as novas linhas, então a próxima sincronização que ocorrer sincronizará apenas as últimas cinco linhas.

## Dicas adicionais {#additional-tips}

### Grave apenas atributos novos ou atualizados para minimizar o consumo {#only-write-new-or-updated-attributes-to-minimize-consumption}

Cada vez que uma sincronização é executada, a Braze procura por linhas que não foram sincronizadas anteriormente. Verificamos isso usando a coluna `UPDATED_AT` na sua tabela ou view. A Braze seleciona e importa quaisquer linhas em que o `UPDATED_AT` seja posterior ao último valor de `UPDATED_AT` sincronizado, independentemente de serem iguais ao que está atualmente no perfil de usuário. Linhas no limite do timestamp também podem ser sincronizadas novamente se novas linhas compartilharem esse timestamp. Sendo assim, recomendamos sincronizar apenas os atributos que você deseja adicionar ou atualizar.

O uso de pontos de dados é idêntico ao usar CDI ou outros métodos de ingestão, como REST or transferir estado representacional APIs ou SDKs, então cabe a você garantir que está adicionando apenas atributos novos ou atualizados às suas tabelas de origem.

### Separe o `EXTERNAL_ID` da coluna `PAYLOAD` {#separate-external_id-from-payload-column}

O objeto `PAYLOAD` não deve incluir um ID externo ou outro tipo de identificador.

### Remova um atributo {#remove-an-attribute}

Você pode defini-lo como `null` se quiser omitir um atributo do perfil de um usuário. Se quiser que um atributo permaneça inalterado, não o envie para a Braze até que tenha sido atualizado. Para remover completamente um atributo, use `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Faça atualizações incrementais {#make-incremental-updates}

Faça atualizações incrementais nos seus dados para evitar substituições não intencionais quando atualizações simultâneas são realizadas.

{% alert important %}
* **Atualizações em atributos diferentes:** Na grande maioria dos casos, se duas atualizações não impactam os mesmos atributos de um usuário, elas têm resultados totalmente independentes. Por exemplo, se você atualizar o atributo `Color` de um usuário e separadamente atualizar o atributo `Size`, ambas as atualizações devem ser aplicadas corretamente, mesmo que ocorram com poucos segundos de diferença.
* **Atualizações no mesmo atributo:** Condições de corrida podem ocorrer quando múltiplas atualizações atingem o mesmo atributo dentro de uma única execução de sincronização. Nesses casos raros, uma atualização pode sobrescrever outra. A melhor forma de prevenir esse comportamento é garantir que os dados de origem da sua sincronização CDI reflitam apenas o estado mais recente de cada usuário, ou que todas as atualizações para um determinado usuário ou par usuário+atributo estejam contidas em uma única linha.
* **Operadores de vetor de objeto:** As únicas exceções para atualizações independentes são os operadores `$add`, `$remove` e `$update` para vetores de objeto, em que atualizações no mesmo vetor podem interagir entre si.
* **Eventos:** Condições de corrida não afetam eventos, pois cada evento é único e possui um timestamp associado a ele.
{% endalert %}

A melhor forma de prevenir esse comportamento é garantir que os dados de origem da sua sincronização CDI reflitam apenas o estado mais recente de cada usuário, ou que todas as atualizações para um determinado usuário ou par usuário+atributo estejam contidas em uma única linha.

### Crie uma string JSON a partir de outra tabela {#create-a-json-string-from-another-table}

Se você preferir armazenar cada atributo em sua própria coluna internamente, precisa converter essas colunas em uma string JSON para preencher a sincronização com a Braze. Para isso, você pode usar uma consulta como:

{% tabs local %}
{% tab Snowflake %}
Use esta consulta no Snowflake para formatar colunas de origem em campos CDI.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
Use esta consulta no Redshift para formatar colunas de origem em campos CDI.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
Use esta consulta no BigQuery para formatar colunas de origem em campos CDI.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
Use esta consulta no Databricks para formatar colunas de origem em campos CDI.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
Use esta consulta no Microsoft Fabric para formatar colunas de origem em campos CDI.
```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Use o timestamp `UPDATED_AT` {#use-the-updated_at-timestamp}

A Braze usa o timestamp `UPDATED_AT` para rastrear quais dados foram sincronizados com sucesso. O CDI também rastreia o número de linhas no último timestamp sincronizado. Se novas linhas forem adicionadas com o mesmo timestamp entre execuções, o CDI ressincroniza todas as linhas naquele timestamp, o que pode levar a dados duplicados. Para mais detalhes e dicas, consulte [Evitar a ressincronização de linhas com timestamps duplicados](#avoid-resyncing-rows-with-duplicate-timestamps).

### Configuração da tabela {#table-configuration}

Temos um [repositório público no GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) para que clientes compartilhem melhores práticas ou snippets de código. Para contribuir com seus próprios snippets, crie um pull request!

### Formatação de dados {#data-formatting}

Os requisitos de configuração de tabela e formatação de carga útil para Cloud Data Ingestion estão documentados em [Configuração de tabela para Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Use essa página para distinguir:

- Requisitos da tabela de origem (colunas obrigatórias, colunas de identificador e comportamento do `UPDATED_AT`)
- Requisitos da carga útil (quais campos devem corresponder ao formato do objeto `/users/track` para cada tipo de dados)

### Evite timeouts nas consultas do data warehouse {#avoid-timeouts-for-data-warehouse-queries}

Recomendamos que as consultas sejam concluídas em até uma hora para desempenho ideal e para evitar possíveis erros. Se as consultas excederem esse prazo, considere revisar a configuração do seu data warehouse. Otimizar os recursos alocados ao seu warehouse pode ajudar a melhorar a velocidade de execução das consultas.

## Limitações do produto {#product-limitations}

| Limitação              | Descrição                                                                                                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integrações  | Não há limite para a quantidade de integrações que você pode configurar. No entanto, só é possível configurar uma integração por tabela ou visualização.                            |
| Número de linhas       | Por padrão, cada execução pode sincronizar até 500 milhões de linhas. A Braze interrompe qualquer sincronização com mais de 500 milhões de novas linhas. Se você precisar de um limite maior, entre em contato com seu gerente de sucesso do cliente ou com o suporte da Braze. |
| Atributos por linha    | Cada linha deve conter um único ID de usuário e um objeto JSON com até 250 atributos. Cada chave no objeto JSON conta como um atributo (ou seja, um vetor conta como um atributo). |
| Tamanho da carga útil  | Cada linha pode conter uma carga útil de até 1 MB. A Braze rejeita cargas úteis maiores que 1&nbsp;MB e registra o erro "Payload was greater than 1MB" no registro de sincronização, juntamente com o ID externo associado e a carga útil truncada. |
| Tipo de dados          | Você pode sincronizar atributos de usuário, eventos e compras por meio da ingestão de dados na nuvem.                                                                             |
| Região da Braze        | Este produto está disponível em todas as regiões da Braze. Qualquer região da Braze pode se conectar a qualquer região de dados de origem.                                        |
| Região de origem       | A Braze se conectará ao seu data warehouse ou ambiente de nuvem em qualquer região ou provedor de nuvem.                                                                           |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitações do produto" }

<br><br>