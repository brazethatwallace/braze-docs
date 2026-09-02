---
nav_title: "Compartilhamento de dados"
article_title: Compartilhamento de dados do Snowflake
page_order: 0
description: "Este artigo de referência aborda a integração de Compartilhamento Seguro de Dados do Snowflake, que permite acessar dados de engajamento e de campanhas diretamente na sua instância do Snowflake."
page_type: partner
search_tag: Partner

---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Compartilhamento de dados do Snowflake {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsnowflake-secure-data-sharing-via-braze-stylefloatrightwidth120pxborder0-classnoimgbordersnowflake-data-sharing}

> O [Compartilhamento Seguro de Dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) do Snowflake permite que a Braze forneça acesso seguro aos dados no nosso portal Snowflake sem se preocupar com atritos no fluxo de trabalho, lentidão, pontos de falha e custos desnecessários que acompanham os relacionamentos típicos com provedores de dados. O compartilhamento de dados pode ser configurado por meio da integração a seguir ou por meio das [Contas de Leitor do Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts).

O Compartilhamento de Dados do Snowflake faz parte da Distribuição de Dados da Braze. Para uma visão geral completa das opções de Distribuição de Dados, consulte [Distribuição de dados]({{site.baseurl}}/user_guide/data/distribution).

{% alert tip %}
**Quer ter acesso a dados no nível do Snowflake sem precisar de uma conta do Snowflake?**<br>Confira as [Contas de Leitor do Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts). Com as Contas de Leitor, a Braze criará e compartilhará seus dados em uma conta e fornecerá credenciais para que você faça login e acesse seus dados. Isso fará com que todo o compartilhamento de dados e a cobrança de uso sejam gerenciados inteiramente pela Braze.
{% endalert %}

## Direitos de Distribuição de Dados {#data-distribution-entitlements}

O seu direito de Distribuição de Dados determina quais tipos de eventos estão disponíveis no seu compartilhamento de dados. A Braze organiza os eventos nas seguintes categorias:

| Direito | Categoria do evento | Descrição | Referência do glossário de eventos |
|------------|----------------|-------------|--------------------------|
| **Eventos de engajamento** | Eventos de engajamento com mensagem | Eventos relacionados a envios, entregas, aberturas, cliques, bounces e outras interações com canais de envio de mensagens | [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **Eventos de comportamento do cliente** | Eventos de engajamento com mensagem e eventos de comportamento do cliente | Inclui todos os eventos de engajamento com mensagem, além de eventos relacionados a compras, eventos personalizados, sessões, atribuição e ações do usuário no app | [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Eventos de comportamento do cliente e do usuário]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **Perfis e atributos de usuário** | Eventos de engajamento com mensagem, eventos de comportamento do cliente e eventos de perfil de usuário | Inclui eventos de engajamento com mensagem e eventos de comportamento do cliente, além de eventos relacionados a alterações em perfis e atributos de usuário | [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Eventos de comportamento do cliente e do usuário]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [Eventos de perfil de usuário]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Direitos de Distribuição de Dados" }

Para dúvidas sobre quais eventos estão incluídos no seu direito, entre em contato com o gerente da sua conta ou gerente de sucesso do cliente na Braze.

## Sobre o compartilhamento seguro de dados {#about-secure-data-sharing}

Com o compartilhamento de dados, nenhum dado é de fato copiado ou transferido entre contas. Todo o compartilhamento é feito por meio da camada de serviços e do armazenamento de metadados exclusivos do Snowflake. Esse é um conceito importante porque os dados compartilhados não ocupam espaço de armazenamento na sua conta e, portanto, não contribuem para as cobranças mensais de armazenamento de dados. As **únicas** cobranças são pelos recursos de computação (como warehouses virtuais) usados para consultar os dados compartilhados.

Além disso, usando os recursos integrados de funções e permissões do Snowflake, o acesso aos dados compartilhados pela Braze pode ser controlado e governado por meio dos controles de acesso já existentes na sua conta do Snowflake e nos dados contidos nela. O acesso pode ser restringido e monitorado da mesma forma que seus próprios dados.

- **Reduza o tempo até os insights**<br>Diga adeus aos processos de ETL que levam semanas para serem construídos. As arquiteturas exclusivas da Braze e do Snowflake tornam todos os dados de engajamento do cliente e de Campaign imediatamente acessíveis e consultáveis a partir do instante em que chegam ao data lake. Nenhum dado é copiado ou movido, então você pode entregar experiências do cliente com base apenas nas informações mais relevantes e atualizadas.
- **Elimine os silos de dados**<br>Crie uma visão holística dos seus clientes em todos os canais e plataformas. O compartilhamento de dados facilita mais do que nunca a junção dos seus dados de engajamento do cliente da Braze com todos os outros dados do Snowflake, gerando insights mais ricos em uma única fonte confiável de verdade.
- **Veja como seu engajamento se compara**<br>Otimize suas estratégias de engajamento do cliente com o Braze Benchmarks. Essa ferramenta interativa, desenvolvida pela Braze e pelo Snowflake, permite comparar os dados de engajamento da sua marca com benchmarks de canais, setores e plataformas de dispositivos.

Para saber mais sobre o compartilhamento de dados do Snowflake, consulte [Introdução ao compartilhamento seguro de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso à Braze | Entre em contato com o gerente de conta ou gerente de sucesso do cliente da Braze para configurar o Compartilhamento de Dados. |
| Conta Snowflake | Uma conta Snowflake com permissões de `admin`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Configurando o Secure Data Sharing {#setting-up-secure-data-sharing}

Para o Snowflake, o compartilhamento de dados acontece entre um [provedor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) e um [consumidor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Nesse contexto, sua conta da Braze é o provedor de dados, pois ela cria e envia o compartilhamento de dados&#8212;enquanto sua conta do Snowflake é o consumidor de dados, pois utiliza o compartilhamento de dados para criar um banco de dados. Para mais detalhes, consulte [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Etapa 1: Enviar o compartilhamento de dados a partir da Braze {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Etapa 2: Criar o banco de dados no Snowflake {#step-2-create-the-database-in-snowflake}

1. Após alguns minutos, você deverá receber o compartilhamento de dados de entrada na sua conta do Snowflake.
2. Usando o compartilhamento de dados de entrada, crie um banco de dados para visualizar e consultar as tabelas. Por exemplo:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Conceda privilégios para consultar o novo banco de dados.

{% alert warning %}
Se você excluir e recriar um compartilhamento no dashboard da Braze, será necessário descartar o banco de dados criado anteriormente e recriá-lo usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar o compartilhamento de entrada.
Se você tiver vários espaços de trabalho compartilhando dados com a mesma conta do Snowflake, consulte as [Perguntas frequentes sobre Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) para orientações sobre como gerenciar configurações com vários espaços de trabalho.
{% endalert %}

## Uso e visualização {#usage-and-visualization}

Após o compartilhamento de dados ser provisionado, crie um banco de dados a partir do compartilhamento de dados recebido, fazendo com que todas as tabelas compartilhadas apareçam na sua instância do Snowflake e possam ser consultadas como qualquer outro dado armazenado na sua instância. No entanto, tenha em mente que os dados compartilhados são somente leitura e só podem ser consultados, não sendo possível modificá-los ou excluí-los de nenhuma forma.

Assim como com o Currents, você pode usar o Snowflake Secure Data Sharing para:

{% multi_lang_include partners/data_sharing_use_cases.md %}

[Baixe os esquemas brutos das tabelas.](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

{% alert note %}
O download do esquema bruto não inclui as visualizações de atributos do perfil de usuário. Para os esquemas completos e orientações de uso de `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`, `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` e visualizações de atributos de usuário relacionadas, consulte [Atributos do perfil de usuário]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

### Esquema de ID do usuário {#user-id-schema}

Observe as seguintes diferenças entre as convenções de nomenclatura da Braze e do Snowflake para IDs de usuário.

| Esquema Braze | Esquema Snowflake | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador único atribuído automaticamente pela Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador único do perfil de um usuário, definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de ID do usuário" }

## Informações importantes e limitações {#important-information-and-limitations}

### Alterações com e sem quebra de compatibilidade {#breaking-versus-non-breaking-changes}

#### Alterações sem quebra de compatibilidade {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Como novas colunas são consideradas alterações sem quebra de compatibilidade, a Braze recomenda fortemente listar explicitamente as colunas de interesse em cada consulta, em vez de usar consultas `SELECT *`. Alternativamente, você pode criar views que nomeiem explicitamente as colunas e então consultar essas views em vez das tabelas diretamente.
{% endalert %}

#### Alterações com quebra de compatibilidade {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Regiões do Snowflake {#snowflake-regions}

Atualmente, a Braze hospeda todos os dados em nível de usuário nestas regiões AWS do Snowflake:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Northeast-1 (Tóquio)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jacarta)

Para usuários fora dessas regiões, a Braze pode fornecer compartilhamento de dados para clientes em comum que hospedam sua infraestrutura Snowflake em qualquer região AWS, Azure ou GCP.

### Retenção de dados {#data-retention}

#### Política de retenção {#retention-policy}

Quaisquer dados com mais de dois anos serão arquivados e movidos para armazenamento de longo prazo. Como parte do processo de arquivamento, todos os eventos são anonimizados e quaisquer campos sensíveis com informações de identificação pessoal (IPI) são removidos (isso inclui campos opcionalmente IPI, como `properties`). Os dados arquivados ainda contêm o campo `user_id`, o que permite análises por usuário em todos os dados de eventos.

Você poderá consultar os dois anos mais recentes de dados de cada evento na view `USERS_*_SHARED` correspondente. Além disso, cada evento terá uma view `USERS_*_SHARED_ALL` que pode ser consultada para retornar dados anonimizados e não anonimizados.

#### Dados históricos {#historical-data}

O arquivo de dados históricos de eventos no Snowflake remonta a abril de 2019. Nos primeiros meses em que a Braze armazenava dados no Snowflake, foram feitas alterações no produto que podem ter resultado em alguns desses dados parecendo ligeiramente diferentes ou tendo alguns valores nulos (já que não estávamos passando dados para todos os campos disponíveis naquela época). É melhor presumir que quaisquer resultados que incluam dados anteriores a agosto de 2019 podem parecer ligeiramente diferentes do esperado.

### Conformidade com o Regulamento Geral de Proteção de Dados (GDPR) {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### Velocidade, desempenho e custo das consultas {#speed-performance-cost-of-queries}

A velocidade, o desempenho e o custo de qualquer consulta executada sobre os dados são determinados pelo tamanho do warehouse que você usa para consultar os dados. Em alguns casos, dependendo da quantidade de dados que você está acessando para análise, pode ser necessário usar um warehouse de tamanho maior para que a consulta seja bem-sucedida. O Snowflake tem excelentes recursos disponíveis sobre como determinar o melhor tamanho a ser usado, incluindo [Visão geral dos warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) e [Considerações sobre warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Para um conjunto de consultas de exemplo para referência ao configurar o Snowflake, confira nossos exemplos de [consultas de exemplo]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) e [configuração de pipeline ETL de eventos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).
{% endalert %}