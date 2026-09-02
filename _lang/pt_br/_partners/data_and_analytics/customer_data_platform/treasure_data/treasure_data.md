---
nav_title: Treasure Data
article_title: Treasure Data
description: "Este artigo de referência descreve a parceria entre a Braze e o Treasure Data, uma CDP corporativo que permite escrever os resultados do trabalho diretamente na Braze."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> O [Treasure Data](https://www.treasuredata.com/) é uma CDP (CDP) que coleta e encaminha informações de várias fontes para uma variedade de outros locais na sua pilha de marketing.

A integração entre a Braze e o Treasure Data permite escrever os resultados do trabalho do Treasure Data diretamente na Braze. Dessa forma, é possível:
* **Mapear IDs externos**: Mapeie os IDs para a conta de usuário da Braze a partir do seu sistema de CRM.
* **Gerenciar descadastramentos**: Quando um usuário final atualiza seu consentimento, optando por não participar.
* **Fazer upload do seu rastreamento de eventos, compras ou atributos personalizados de perfil**. Essas informações podem ajudá-lo a criar segmentos de clientes precisos que melhoram a experiência do usuário nas suas campanhas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta do Treasure Data | É necessário ter uma [conta do Treasure Data](https://www.treasuredata.com/custom-demo/) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `users.track`, `users.delete`, `users.alias.new` e `users.identify`.<br><br>Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Você pode sincronizar seus perfis de clientes consolidados do Treasure Data na Braze para criar segmentos de direcionamento. O Treasure Data é compatível com dados primários de cookies, IDs móveis, sistemas de terceiros (como seu CRM) e muitos outros.

## Integração {#integration}

### Etapa 1: Criar uma nova conexão {#step-1-create-a-new-connection}

No Treasure Data, navegue até **Catalog** no **Integrations Hub** e pesquise e selecione **Braze**.

No prompt **New Authentication** exibido, dê um nome à sua conexão e forneça a chave da API REST e o endpoint REST da Braze. Selecione **Done** quando terminar.

![Formulário de autenticação do Treasure Data com a Braze, com campos para chave da API REST e endpoint.]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### Etapa 2: Definir sua consulta {#step-2-define-your-query}

No Treasure Data, navegue até **Queries** no **Data Workbench** e selecione uma consulta para a qual você gostaria de exportar dados. Execute essa consulta para validar o conjunto de resultados.

{% alert note %}
Para os usuários que usam o HIVE para criar consultas, o HIVE exige que todas as colunas ou tabelas que comecem com um sublinhado sejam envolvidas por crases. Por exemplo, `_merge_objects`.
{% endalert %}

Em seguida, selecione **Export Results** e selecione uma autenticação de integração existente.

![Página de resultados de consulta do Treasure Data com Export Results e integração com a Braze selecionados.]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

Defina parâmetros adicionais de resultados de exportação, conforme descrito na [seção de personalização](#customization) a seguir. No seu conteúdo de integração de exportação, revise os parâmetros de integração.

![A página "Export Results". Nessa página, há campos para "mode", "track record type" e "pre-formatted fields". Para este exemplo, "User-Track" e "Custom Events" são definidos para esses campos, respectivamente.]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

Por fim, selecione **Done**, execute sua consulta e valide se seus dados foram movidos para a Braze.

### Personalização {#customization}

Os parâmetros dos resultados da exportação estão incluídos na tabela a seguir:

| Parâmetro | Valores | Descrição |
|---------------------------|---|---|
| `mode` | User - New Alias<br>User - Identifying<br>User - Track<br>User - Delete | Modo do conector |
| `pre_formatted_fields` | String | Use para colunas de array ou JSON para manter o formato. |
| `track_record_type` | Custom Events<br>Purchases<br>User Profile Attributes | Tipo de registro para o modo **User - Track** |
| `skip_on_invalid_records` | Booleano | Se ativado, continue e ignore quaisquer registros inválidos para a coluna JSON. <br> Caso contrário, o trabalho será interrompido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Personalização" }

{% alert note %}
Visite [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) para saber mais sobre campos pré-formatados, exemplos de consultas, detalhes de parâmetros e agendamento de tarefas de exportação de consultas.
{% endalert %}

## Webhooks

Os usuários do Treasure Data podem ingerir dados por meio da REST API pública. Você pode usar o Treasure Data para criar webhooks personalizados para seus dados. Para saber mais, visite [Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API).