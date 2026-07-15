---
nav_title: Semântica de entrega de eventos
article_title: Semântica de entrega de eventos
page_order: 2
page_type: reference
description: "Este artigo de referência descreve e define como o Currents gerencia os dados de eventos de arquivo simples que enviamos aos parceiros do Data Warehouse Storage."
tool: Currents

---

# Semântica de entrega de eventos {#event-delivery-semantics}

> Esta página descreve e define como o Currents gerencia os dados de eventos de arquivo simples que enviamos aos parceiros do Data Warehouse Storage.

O Currents for Data Storage é um fluxo contínuo de dados da nossa plataforma para um bucket de armazenamento em uma das [conexões de nossos parceiros de data warehouse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners). O Currents grava arquivos Avro no seu bucket de armazenamento em intervalos regulares, permitindo que você processe e analise os dados do evento usando seu próprio conjunto de ferramentas de business intelligence (BI).

{% alert important %}
Este conteúdo **se aplica apenas aos dados de eventos de arquivo simples que enviamos aos parceiros do Data Warehouse Storage (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage)**. <br><br>Para obter o conteúdo que se aplica a outros parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) e verifique suas respectivas páginas.
{% endalert %}

## Eventos de teste {#test-events}

Quando você configura uma integração do Currents, clique em **Enviar eventos de teste** para verificar a conexão com seu bucket de armazenamento. Esses eventos de teste validam se sua integração pode receber e processar dados corretamente.

{% alert important %}
**Formato dos dados de eventos de teste:** os eventos de teste contêm valores de espaço reservado que correspondem aos tipos de dados corretos para cada campo, mas não contêm dados realistas ou precisos. Por exemplo, um campo `timezone` pode conter uma string semelhante a UUID em vez de um identificador de fuso horário válido (como "America/Chicago"), e outros campos como `campaign_name` e `ip_pool` também podem conter valores de espaço reservado em vez de dados reais.<br>

Esse é o comportamento esperado. Os eventos de teste servem principalmente para testar a conexão e a configuração da integração, não para validar a precisão dos dados. Para ver eventos reais com dados precisos, use uma integração de teste do Currents para enviar dados de eventos reais pelo seu pipeline.
{% endalert %}

## Entrega "pelo menos uma vez" {#at-least-once-delivery}

Como um sistema de alto throughput, o Currents oferece uma entrega de eventos "pelo menos uma vez", o que significa que eventos duplicados podem ocasionalmente ser gravados no seu bucket de armazenamento. Isso pode acontecer quando os eventos são reprocessados da nossa fila por qualquer motivo.

Se seus casos de uso exigem entrega "exatamente uma vez", você pode usar o campo de identificador único enviado com cada evento (`id`) para deduplicar eventos. Como o arquivo sai do nosso controle quando é gravado no seu bucket de armazenamento, não temos como garantir a deduplicação do nosso lado.

## Timestamps {#timestamps}

Todos os timestamps exportados pelo Currents são enviados no fuso horário UTC. Para alguns eventos em que está disponível, um campo de fuso horário também é incluído, que fornece o formato da Internet Assigned Numbers Authority (IANA) do fuso horário local do usuário no momento do evento.

### Latência {#latency}

Eventos enviados para a Braze por meio do SDK ou da API podem incluir um timestamp do passado. O exemplo mais notável é quando os dados do SDK ficam em fila, como quando não há conectividade móvel. Nesse caso, o timestamp do evento refletirá quando o evento foi gerado. Isso significa que uma porcentagem dos eventos parecerá ter alta latência.

## Formato Apache Avro {#apache-avro-format}

As integrações de armazenamento de dados do Braze Currents geram dados no formato `.avro`. Escolhemos o [Apache Avro](https://avro.apache.org/) porque é um formato de dados flexível que suporta nativamente a evolução de esquemas e é compatível com uma ampla variedade de produtos de dados:

- O Avro é compatível com quase todos os principais data warehouses.
- Caso você deseje manter seus dados no S3, o Avro compacta melhor do que CSV e JSON, então você paga menos pelo armazenamento e potencialmente pode usar menos CPU para processar os dados.
- O Avro exige esquemas quando os dados são gravados ou lidos. Os esquemas podem evoluir ao longo do tempo para lidar com a adição de campos sem causar quebras.

O Currents criará um arquivo para cada tipo de evento usando o seguinte formato:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Não consegue ver o código por causa da barra de rolagem? Saiba como corrigir isso [na página inicial do Guia do Usuário da Braze]({{site.baseurl}}/user_guide).
{% endalert %}

Por exemplo, o caminho de um evento de envio de push pode ser assim:

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

O segmento de caminho `version` é um valor inteiro simples da versão do Currents, como `version=6`.

| Segmento do nome do arquivo | Definição |
|---|---|
| `<your-bucket-prefix>` | O prefixo definido para esta integração do Currents. |
| `<cluster-identifier>` | Para uso interno da Braze. Será uma string como "prod-01", "prod-02", "prod-03" ou "prod-04". Todos os arquivos terão o mesmo identificador de cluster. |
| `<connection-type-identifier>` | O identificador do tipo de conexão. As opções são "S3", "AzureBlob" ou "GCS". |
| `<integration-id>` | O ID único desta integração do Currents. |
| `<event-type>` | O tipo do evento no arquivo. |
| `<date>` | A hora em que os eventos são enfileirados no nosso sistema para processamento no fuso horário UTC. Formatado como AAAA-MM-DD-HH. |
| `version=<currents_version>` | A versão do Currents para o caminho do pipeline. Esse valor é um inteiro simples como `6`. |
| `<environment>` | Para uso interno da Braze. |
| `<partition>` | Para uso interno da Braze. Inteiro. |
| `<offset>` | Para uso interno da Braze. Inteiro. Note que arquivos diferentes enviados dentro da mesma hora terão um parâmetro `<offset>` diferente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Formato Apache Avro" }

{% alert tip %}
As convenções de nomenclatura de arquivos podem mudar. A Braze recomenda pesquisar todas as chaves no seu bucket que tenham o prefixo &lt;your-bucket-prefix&gt;.
{% endalert %}

### Limite de gravação do Avro {#avro-write-threshold}

Em circunstâncias normais, a Braze gravará arquivos de dados no seu bucket de armazenamento a cada 5 minutos ou 15.000 eventos, o que ocorrer primeiro. Sob carga pesada, podemos gravar arquivos de dados maiores com até 100.000 eventos por arquivo.

{% alert important %}
O Currents nunca gravará arquivos vazios.
{% endalert %}

### Alterações no esquema Avro {#avro-schema-changes}

De tempos em tempos, a Braze pode fazer alterações no esquema Avro quando campos são adicionados, alterados ou removidos. Para nossos propósitos aqui, existem dois tipos de alterações: com quebra e sem quebra. Todas as alterações de esquema são agrupadas em releases do Currents, e cada release avança o segmento `version=<currents_version>` no caminho de armazenamento (por exemplo, de `version=6` para `version=7`). Os eventos do Currents gravados no Azure Blob Storage, Google Cloud Storage e Amazon S3 usam o seguinte formato de caminho:

```
<your-bucket-prefix>/<currents-integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/<avro-file>
```

#### Alterações sem quebra {#non-breaking-changes}

Quando um campo é adicionado ao esquema Avro, consideramos isso uma alteração sem quebra. Os campos adicionados sempre serão campos Avro "opcionais" (como com um valor padrão de `null`), então eles "corresponderão" a esquemas mais antigos de acordo com a [especificação de resolução de esquema Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Essas adições não devem afetar os processos existentes de Extract, Transform e Load (ETL), pois o campo será simplesmente ignorado até ser adicionado ao seu processo de ETL.

{% alert important %}
Recomendamos que sua configuração de ETL seja explícita sobre os campos que processa para evitar quebras no fluxo quando novos campos são adicionados.
{% endalert %}

#### Alterações com quebra {#breaking-changes}

Quando um campo é removido ou alterado no esquema Avro, consideramos isso uma alteração com quebra. Alterações com quebra podem exigir modificações nos processos de ETL existentes, pois campos que estavam em uso podem não ser mais registrados conforme esperado.

Todas as alterações com quebra serão comunicadas com antecedência antes do release.

Para um histórico completo de alterações por versão, consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).