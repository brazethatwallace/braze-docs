---
nav_title: Comparar opções de ingestão de dados
article_title: Comparar opções de ingestão de dados persistente e zero-copy
page_order: 1
page_type: reference
description: "Compare sincronizações padrão do Cloud Data Ingestion, CDI Segments, gatilhos CDI para Canvas e a API or interface de programação do aplicativo (API) /users/track para escolher como dados do warehouse ou de aplicativos chegam aos perfis, Segments e Canvas da Braze."
---

# Comparar opções de ingestão de dados persistente e zero-copy {#compare-persistent-and-zero-copy-data-ingestion-options}

> Escolha como os dados do seu warehouse ou aplicativos chegam à Braze — se são copiados para perfis de usuário, consultados diretamente para segmentação ou passados de forma transitória para um Canvas — antes de projetar seus pipelines de ingestão.

## Sobre este exemplo {#about-this-example}

MovieCanon é um serviço fictício de streaming de filmes. Ele centraliza dados de clientes, ingressos e visualizações em um warehouse. A equipe de dados precisa decidir como alimentar a Braze para três necessidades comuns:

- **Dados de perfil:** Nível de fidelidade, valor do tempo de vida e atributos de preferência de gênero ou formato que persistem nos perfis de usuário da Braze.
- **Criação de públicos:** Segments baseados em SQL a partir de tabelas do warehouse sem copiar cada coluna para a Braze.
- **Envio de mensagens por gatilho:** Linhas do warehouse que devem entrar em um Canvas com personalização específica por linha que não precisa ficar armazenada no perfil.

A Braze oferece quatro caminhos principais de ingestão. As sincronizações padrão do Cloud Data Ingestion (CDI) e a API or interface de programação do aplicativo (API) [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) persistem dados nos perfis. CDI Segments (Connected Sources) e gatilhos CDI para Canvas são opções zero-copy: os dados do warehouse permanecem no seu warehouse e não são gravados nos perfis de usuário da Braze.

Use esta comparação quando estiver planejando a arquitetura, dimensionando a capacidade ou explicando trade-offs para stakeholders de engenharia e marketing. Ela não substitui os guias de configuração de integração de cada opção.

## Considerações {#considerations}

- O Cloud Data Ingestion é um recurso abrangente. As sincronizações padrão do CDI copiam dados para os perfis da Braze (semelhante a `/users/track`). CDI Segments e gatilhos CDI para Canvas mantêm os dados do warehouse sem gravá-los nos perfis de usuário da Braze.
- As sincronizações recorrentes do CDI podem ser executadas a cada 15 minutos até uma vez por mês. Se você precisar de uma cadência maior do que 15 minutos, entre em contato com seu gerente de sucesso do cliente ou use a ingestão via REST or transferir estado representacional API or interface de programação do aplicativo (API). Consulte [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
- Os gatilhos CDI para Canvas compartilham o limite de frequência da REST or transferir estado representacional API or interface de programação do aplicativo (API) [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) com outro tráfego para esse endpoint. `/users/track` tem seus próprios limites e regras de lote. Os limites padrão podem ser elevados. Acesse **Configurações** > **APIs e identificadores** > **Limites de API or interface de programação do aplicativo (API)** e consulte [Limites de frequência da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_limits).
- Connected Sources e extensões de Segment or segmento or segmento CDI executam consultas no seu warehouse. Você incorre em custos de computação do warehouse; a Braze não registra pontos de dados para essas consultas. Consulte [Connected sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

## Configuração {#setup}

### Etapa 1: Mapeie seu caso de uso para um caminho de ingestão {#step-1-map-your-use-case-to-an-ingestion-path}

Associe seu objetivo ao caminho de ingestão recomendado e verifique se esse caminho grava nos perfis da Braze.

| Seu objetivo | Caminho recomendado | Grava nos perfis? |
| --- | --- | --- |
| Persistir atributos, eventos, compras ou itens de catálogo do warehouse | Sincronização padrão do CDI | Sim (os dados são copiados para perfis ou catálogos da Braze) |
| Criar públicos a partir de SQL do warehouse sem copiar tabelas de origem para a Braze | CDI Segments (Connected Sources) | Não (apenas associação de membros) |
| Inserir usuários em um Canvas com contexto de linha do warehouse que não deve persistir no perfil | Gatilhos CDI para Canvas | Não (propriedades de contexto transitórias do Canvas) |
| Enviar dados de apps, servidores ou pipelines de streaming em tempo quase real | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) (ou SDKs) | Sim (os dados persistem nos perfis) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mapeie seu caso de uso para um caminho de ingestão" }

### Etapa 2: Compare persistência, latência e capacidade {#step-2-compare-persistence-latency-and-throughput}

Compare como cada caminho lida com residência de dados, latência, capacidade e criação de usuários.

| Dimensão | Sincronização padrão do CDI | CDI Segments | Gatilhos CDI para Canvas | `/users/track` |
| --- | --- | --- | --- | --- |
| O que faz | Leitura agendada de uma tabela do warehouse; grava atributos, eventos, compras, exclusões de usuários ou catálogos | A Braze consulta seu warehouse para extensões de Segment or segmento or segmento SQL | Linhas do warehouse disparam entrada no Canvas com contexto de linha como propriedades de contexto do Canvas | Apps, servidores ou pipelines de streaming gravam atributos, eventos e compras nos perfis |
| Residência dos dados | Copiados e persistidos nos perfis da Braze | Permanecem no seu warehouse; nada é gravado nos perfis | As propriedades de contexto do Canvas são transitórias; não persistem nos perfis | Copiados e persistidos nos perfis da Braze |
| Latência típica | Não é em tempo real; cadência mínima de sincronização de 15 minutos (a atualidade do warehouse também se aplica) | Não é em tempo real; atualiza conforme o cronograma da extensão de Segment or segmento or segmento (a associação de membros não é atualizada a cada mudança no warehouse) | Não é em tempo real; limitada pelo cronograma de sincronização (mínimo de 15 minutos) | Tempo quase real (processamento assíncrono) |
| Notas sobre capacidade | Resultado completo da consulta por sincronização; a Braze processa internamente em lotes via `/users/track`, `/users/delete` ou endpoints de catálogo | Limite de tempo de execução de consulta de 60 minutos por connected source; sem limite de objetos por requisição | Compartilha o limite de frequência de `/canvas/trigger/send`; aproximadamente 3,75 milhões de entradas no Canvas por hora por execução de sincronização | Até 75 objetos combinados por requisição; consulte [Limites de frequência da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_limits) |
| Tamanho do lote | Sem limite de objetos no lado do CDI para leituras do warehouse | N/A (o resultado da consulta define a associação de membros) | Uma entrada no Canvas por linha do warehouse por execução de sincronização | 75 atributos, eventos e compras combinados por requisição (padrão) |
| Criação de usuários | Sim, a menos que a opção de atualizar apenas existentes esteja definida | Não (usuários desconhecidos nos resultados da consulta são ignorados) | Não (apenas usuários existentes da Braze) | Sim, a menos que `_update_existing_only` seja true |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compare persistência, latência e capacidade" }

### Etapa 3: Compare requisitos de esquema e identificadores {#step-3-compare-schema-and-identifier-requirements}

Compare as colunas obrigatórias e os identificadores compatíveis para cada caminho. Configure um tipo de dados por sincronização padrão do CDI (por exemplo, atributos em uma integração e eventos em outra).

| Dimensão | Sincronização padrão do CDI | CDI Segments | Gatilhos CDI para Canvas | `/users/track` |
| --- | --- | --- | --- | --- |
| Colunas obrigatórias / formato | Identificador do usuário + `UPDATED_AT` + `PAYLOAD` (JSON) por linha | O SQL deve retornar apenas `external_user_id` | Identificador + `UPDATED_AT` + `PROPERTIES` (JSON; use `{}` quando vazio) | Corpo de requisição padrão de `/users/track` |
| Identificadores compatíveis | `external_id`, alias de usuário, `braze_id`, e-mail ou telefone | Apenas `external_user_id` (string) | Apenas `external_id` ou alias de usuário | `external_id`, alias de usuário, `braze_id`, e-mail ou telefone |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compare requisitos de esquema e identificadores" }

### Etapa 4: Implemente o caminho selecionado {#step-4-implement-the-path-you-selected}

- **Sincronização padrão do CDI:** Crie uma tabela ou view no warehouse e siga [Integrações do Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) e [Configuração de tabelas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **CDI Segments:** Adicione uma [Connected source]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) e crie uma [extensão de Segment or segmento or segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).
- **Gatilhos CDI para Canvas:** Configure uma tabela de origem com `PROPERTIES`, crie e lance um Canvas de destino e configure uma sincronização conforme [Personalização zero-copy usando CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync).
- **`/users/track`:** Envie requisições a partir do seu aplicativo ou middleware. Formate as cargas úteis conforme [POST: Criar e atualizar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Para a MovieCanon, um padrão comum é: sincronizações padrão do CDI para enriquecimento noturno de perfis, CDI Segments para regras de público exclusivas do warehouse, gatilhos para Canvas em jornadas de status de ingresso ou visualização com contexto por linha, e `/users/track` para eventos de app em tempo real.

## Artigos relacionados {#related-articles}

- [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)
- [Connected sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)
- [Personalização zero-copy usando CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)
- [Extensões de Segment or segmento or segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)
- [Configuração de tabelas para o Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)
- [POST: Criar e atualizar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [Limites de frequência da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_limits)