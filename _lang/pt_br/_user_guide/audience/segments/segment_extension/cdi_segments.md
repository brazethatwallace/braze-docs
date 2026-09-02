---
nav_title: Extensões de segmento CDI
article_title: Extensões de segmento CDI
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "Este artigo explica como as extensões de segmento CDI usam a ingestão de dados na nuvem para consultar seu data warehouse e definir públicos na Braze."

---

# Extensões de segmento CDI {#cdi-segment-extensions}

> Com a [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) (CDI) da Braze, você pode configurar uma conexão direta do seu data warehouse ou sistema de armazenamento de arquivos com a Braze para sincronizar dados relevantes de usuários ou catálogos de forma recorrente.

{% alert warning %}
As extensões de segmento CDI consultam seu data warehouse diretamente, então você incorrerá em todos os custos associados à execução dessas consultas no seu data warehouse. As extensões de segmento CDI não consomem [créditos de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits), não contam para o limite de extensões de segmento e não registram pontos de dados.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar os dados do seu data warehouse para segmentação dentro do seu espaço de trabalho da Braze, você precisará criar uma [fonte conectada]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) e, em seguida, criar um segmento CDI dentro das suas [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension). As extensões de segmento CDI permitem que você escreva SQL que consulta diretamente o seu próprio data warehouse usando dados disponibilizados por meio das suas conexões CDI, e crie um grupo de usuários que pode ser direcionado dentro da Braze.

## Criando um segmento CDI {#creating-a-cdi-segment}

### Etapa 1: Configure sua fonte {#step-1-set-up-your-source}

Antes de criar sua primeira extensão de segmento CDI, configure uma nova fonte conectada com seu data warehouse seguindo as etapas em [Fontes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

### Etapa 2: Crie um segmento {#step-2-create-a-segment}

1. Acesse **Público** > **Extensões de Segmento** e selecione **Criar Nova Extensão**.
2. No menu **Selecione sua experiência de criação de extensão de segmento**, selecione **Atualização completa (incluindo Segments CDI)**.

![O menu "Selecione sua experiência de criação de extensão de segmento" com as opções de criação.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

{: start="3"}
3. No menu **Selecione a fonte de dados para esta extensão de segmento**, escolha **Tabelas de Dados CDI**. Esse menu aparece somente depois que você configura pelo menos uma [fonte conectada]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

![O menu "Selecione a fonte de dados para esta extensão de segmento" com a opção Tabelas de Dados CDI.]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

{: start="4"}
4. Selecione uma conexão para usar e escreva sua consulta. Cada conexão tem um conjunto específico de tabelas de dados. Sua equipe de desenvolvimento pode configurar suas conexões e tabelas de dados durante a configuração do CDI.
5. Visualize as tabelas de dados disponíveis, incluindo seus esquemas e descrições disponíveis, selecionando **Explorador de Fontes**.

![O Explorador de Fontes mostrando as tabelas de dados disponíveis, incluindo seus esquemas e descrições disponíveis.]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

{: start="6"}
6. Escreva o SQL para seu segmento usando [a sintaxe SQL da Braze]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql). Lembre-se de que todas as extensões de segmento CDI devem usar `external_user_id` como a coluna selecionada, e seu `external_user_id` deve corresponder ao definido na Braze para os usuários.<br><br>
Se os resultados da sua consulta incluírem usuários que não existem na Braze, esses usuários serão ignorados. A Braze não cria novos usuários com base na saída da sua extensão de segmento CDI.

{% alert important %}
`external_user_id` deve ser um valor da string. Se o ID da sua fonte estiver armazenado como número (por exemplo, `client_id` como um inteiro), [converta-o para string no seu SQL](https://www.w3schools.com/sql/func_sqlserver_cast.asp) para que corresponda ao tipo `external_id` na Braze.
{% endalert %}

{: start="7"}
7. [Use esta extensão de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment) dentro de um Segment da Braze para enviar uma Campaign ou Canvas para esse público.

{% alert tip %}
Para saber como você pode pré-visualizar suas extensões de segmento, gerenciá-las e executar atualizações automáticas de participação, consulte [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).
{% endalert %}

## Considerações {#considerations}

- Uma extensão de segmento pode referenciar dados de apenas uma conexão, não de várias.
- Uma extensão de segmento pode usar uma das seguintes opções como fonte de dados: dados de CDI ou dados da Braze Snowflake (Currents). Não é possível misturar fontes de dados dentro de uma extensão de segmento, mas você pode criar várias extensões de segmento para referenciar juntas dentro de um Segment.

## Solução de problemas {#troubleshooting}

- Sua consulta pode expirar ao atingir o tempo máximo de execução, que é configurado para cada sincronização de conexão na página **Cloud Data Ingestion**. O tempo máximo de execução permitido é de 60 minutos.
- Verifique se o SQL está escrito usando a sintaxe apropriada para o seu data warehouse.