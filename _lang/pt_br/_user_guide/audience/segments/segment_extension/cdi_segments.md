---
nav_title: Extensões de segmento CDI
article_title: Extensões de segmento CDI
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "Este artigo explica como as extensões de segmento CDI usam a Ingestão de dados na nuvem para consultar seu data warehouse e definir públicos na Braze."

---

# Extensões de segmento CDI {#cdi-segment-extensions}

> Com a [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) (CDI) da Braze, você pode configurar uma conexão direta do seu data warehouse ou sistema de armazenamento de arquivos com a Braze para sincronizar dados relevantes de usuários ou catálogos de forma recorrente.

{% alert warning %}
As extensões de segmento CDI consultam seu data warehouse diretamente, então você incorrerá em todos os custos associados à execução dessas consultas no seu data warehouse. As extensões de segmento CDI não consomem [créditos de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#monitoring-your-sql-segments-usage), não contam para o limite de extensões de segmento e não registram pontos de dados.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar os dados do seu data warehouse para segmentação dentro do seu espaço de trabalho da Braze, você precisará criar uma [fonte conectada]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) e, em seguida, criar um segmento CDI dentro das suas [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/). As extensões de segmento CDI permitem que você escreva SQL que consulta diretamente o seu próprio data warehouse usando dados disponibilizados por meio das suas conexões CDI, e crie um grupo de usuários que pode ser direcionado dentro da Braze.

## Criando um segmento CDI {#creating-a-cdi-segment}

### Etapa 1: Configure sua fonte {#step-1-set-up-your-source}

Antes de criar sua primeira extensão de segmento CDI, configure uma nova fonte conectada com seu data warehouse seguindo as etapas em [Fontes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/).

### Etapa 2: Crie um segmento {#step-2-create-a-segment}

Primeiro, crie uma nova [extensão de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) e selecione **Full refresh**.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Para a fonte de dados, escolha **CDI Data Tables**.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Como parte da configuração do CDI, você pode selecionar diferentes conexões para usar nas extensões de segmento CDI. Cada conexão possui um conjunto específico de tabelas de dados. Sua equipe de desenvolvimento pode configurar suas conexões e tabelas de dados durante a configuração do CDI.

Para visualizar as tabelas de dados disponíveis, incluindo seus esquemas e quaisquer descrições disponíveis, selecione **Reference**. Quando estiver pronto, selecione uma conexão.

![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

Em seguida, escreva o SQL para o seu segmento usando [a sintaxe SQL da Braze]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#writing-sql).

Lembre-se de que todas as extensões de segmento CDI devem usar `external_user_id` como a coluna selecionada, e seu `external_user_id` deve corresponder ao definido na Braze para os usuários.

{% alert important %}
`external_user_id` deve ser um valor do tipo **string**. Se o ID de origem estiver armazenado como número (por exemplo, `client_id` como inteiro), [converta-o para string no seu SQL](https://www.w3schools.com/sql/func_sqlserver_cast.asp) para que corresponda ao tipo `external_id` na Braze.
{% endalert %}

Se os resultados da sua consulta incluírem usuários que não existem na Braze, esses usuários serão ignorados. A Braze não cria novos usuários com base na saída da sua extensão de segmento CDI.

{% alert tip %}
Para saber como pré-visualizar suas extensões de segmento, gerenciá-las e executar atualizações automáticas de membros, consulte [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/).
{% endalert %}

Por fim, você pode [usar essa extensão de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#step-5-use-your-extension-in-a-segment) dentro de um segmento da Braze para enviar uma Campaign ou Canvas para esse público.

## Considerações {#considerations}

- Uma extensão de segmento pode referenciar dados de apenas uma conexão, não de várias.
- Uma extensão de segmento pode usar uma das seguintes opções como fonte de dados: dados CDI ou dados Braze Snowflake (Currents). Não é possível misturar fontes de dados dentro de uma extensão de segmento, mas você pode criar várias extensões de segmento para referenciar juntas dentro de um segmento.

## Solução de problemas {#troubleshooting}

- Sua consulta pode expirar ao atingir o tempo máximo de execução, que é configurado para cada sincronização de conexão na página **Cloud Data Ingestion**. O tempo máximo de execução permitido é de 60 minutos.
- Certifique-se de que seu SQL esteja escrito usando a sintaxe apropriada para o seu data warehouse.