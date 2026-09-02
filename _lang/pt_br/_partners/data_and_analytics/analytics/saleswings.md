---
nav_title: SalesWings
article_title: SalesWings
description: "Este artigo de referência descreve a parceria entre a Braze e a SalesWings. A SalesWings é uma solução de operações de vendas e marketing para a Braze que ajuda a qualificar leads e contas e fornece insights e alertas de vendas dentro do CRM, como o Salesforce, bem como relatórios de atribuição B2B. Você pode aproveitar os interesses e o engajamento na Braze para personalização no Canvas e segmentação. A SalesWings também oferece uma maneira de gerar leads a partir de um site, semelhante ao Digioh."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> A [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) é uma solução de operações de marketing e vendas B2B SaaS que ajuda a gerenciar a qualificação de leads e contas por meio de pontuação e classificação holísticas de leads, além de fornecer insights e alertas de vendas e relatórios de atribuição B2B, juntamente com uma forte integração com o Salesforce CRM. Um complemento de engajamento do site, semelhante ao Digioh, permite que você gere leads no site. Você pode aproveitar os interesses e o engajamento na Braze para personalização no Canvas e segmentação.

_Essa integração é mantida pela SalesWings._

## Sobre a integração {#about-the-integration}

A SalesWings permite que as equipes de marketing e os gerentes de operações de marketing qualifiquem leads e contas para suas equipes de vendas, o que é essencial para o alinhamento entre vendas e marketing e para a eficiência operacional. Além disso, a SalesWings, juntamente com a Braze, pode apresentar aos representantes de vendas a jornada completa do cliente de um lead e da conta e os dados de engajamento de Campaigns de marketing da Braze, permitindo que você aumente as taxas de qualificação de leads por meio de conversas mais bem informadas. A SalesWings identifica necessidades e interesses juntamente com outros sinais, permitindo a transferência de compradores qualificados para as equipes de vendas dentro do seu CRM de forma automatizada. É possível usar as necessidades, os interesses e a prontidão de vendas identificados como atributos do usuário da Braze para personalização e segmentação.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta SalesWings | É necessária uma conta [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para aproveitar esta parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.export.ids` (e `users.track` se estiver usando o recurso de push de insights da SalesWings). <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Conta Segment.com (opcional) | Se você é um usuário do Segment.com, é possível enviar todos os dados de engajamento e perfis de leads e identificar eventos via Segment.com para a criação de perfis de leads. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

{% tabs %}
{% tab Lead and Account Scoring %}

A SalesWings fornece aos clientes da Braze [uma maneira flexível de qualificar leads, contatos e contas com pontuação de leads de última geração](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) e capacidades de classificação de leads. Todos os seus dados de qualificação de leads são enviados nativamente para o Salesforce CRM e outros sistemas onde você deseja gerenciar e relatar leads, contatos, contas e oportunidades.

![Exemplo de um modelo simples de pontuação de leads click-not-code na SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Exemplo de um modelo simples de pontuação de leads click-not-code na SalesWings_
{% endtab %}
{% tab Sales and Marketing Alignment %}
A SalesWings permite que as equipes de marketing rastreiem, qualifiquem e repassem leads qualificados de marketing para suas equipes de vendas. Todos os dados da SalesWings são enviados nativamente para o Salesforce e podem ser aproveitados para ajustar qualquer processo existente ou criar novos processos por meio de listas, relatórios, fluxos e mais.

![Exemplo de como a pontuação de leads da SalesWings prioriza uma lista de leads ou contatos nativamente dentro do Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Exemplo de como a pontuação de leads da SalesWings prioriza uma lista de leads ou contatos nativamente dentro do Salesforce_

![Exemplo de como a pontuação de leads da SalesWings prioriza uma lista de contas nativamente dentro do Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Exemplo de como a pontuação de leads da SalesWings prioriza uma lista de contas nativamente dentro do Salesforce_
{% endtab %}
{% tab Lead and Account Grading %}
A SalesWings permite que os clientes da Braze qualifiquem leads e contas com base em dados de perfil (normalmente dados de CRM). Isso também é conhecido como "classificação de leads", "pontuação de adequação" ou "pontuação firmográfica". Os clientes da Braze podem enviar dados de atributos diretamente para a SalesWings, e a SalesWings pode ler quaisquer dados e registros de objetos padrão ou personalizados do Salesforce CRM para uma pontuação de perfil holística.
{% endtab %}
{% tab Sales Insights for Sales Reps %}
A SalesWings permite mostrar aos seus representantes de vendas insights de vendas sobre seus leads, contatos e contas (alternativa ao Marketo Sales Insights). Essencialmente, você pode disponibilizar quaisquer dados da Braze e de engajamento na web para sua equipe de vendas. Os insights são incorporados nativamente no Salesforce CRM e podem ser enviados para outros CRMs ou sistemas ou via um e-mail da Braze como um "alerta de vendas".

![Exemplo de visualização de insights de vendas para representantes de vendas no Salesforce (também disponível para outros sistemas de CRM)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Exemplo de visualização de insights de vendas para representantes de vendas no Salesforce (também disponível para outros sistemas de CRM)_
{% endtab %}
{% tab Sales Alerts %}
A SalesWings oferece alertas nativos por e-mail e Slack, e você pode configurar assinaturas de relatórios no Salesforce que sua equipe de vendas pode acessar para obter relatórios diários, semanais e mensais por e-mail. Além disso, por meio de uma integração com o Zapier, você pode criar fluxos de trabalho adicionais com base nos dados de qualificação de leads da SalesWings.

![Exemplo de alerta de vendas via canal do Slack]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Exemplo de alerta de vendas via canal do Slack_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
Por meio da integração nativa da SalesWings com o Salesforce, é possível criar relatórios automatizados com leads, contatos, contas e oportunidades com base nos dados de engajamento na web e em qualquer engajamento de Campaigns da Braze com uma integração nativa do Braze Currents. Por exemplo, é possível exibir uma lista de leads quentes para uma equipe de vendas, com todos que clicaram em uma campanha de e-mail específica ou realizaram uma ação específica em seu app ou site.

![Exemplo de dashboard vinculado ao engajamento de e-mail e marketing da Braze no Salesforce, analisando o impacto de Campaigns da Braze nos resultados de vendas]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Exemplo de dashboard vinculado ao engajamento de e-mail e marketing da Braze no Salesforce, analisando o impacto de Campaigns da Braze nos resultados de vendas_
{% endtab %}
{% endtabs %}

## Integração {#integration}

### Etapa 1: Conta e configuração da SalesWings {#step-1-saleswings-account-and-configuration}

[Agende uma demonstração](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) com a simpática equipe da SalesWings para saber mais sobre a SalesWings.

### Etapa 2: Instale o rastreamento comportamental no seu site ou app {#step-2-installing-behavioral-tracking-on-your-website-or-app}

Há várias maneiras de coletar dados comportamentais na SalesWings para pontuação de leads e contas, identificação da intenção do comprador e insights de vendas:
* [Implante o JavaScript de rastreamento da SalesWings](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) nos sites e apps onde você deseja rastrear e identificar leads
* Ingira eventos da Braze juntamente com as propriedades do evento na SalesWings via Braze Currents
* Envie dados comportamentais de atividade de leads (e dados de perfil de leads) por meio da [integração da SalesWings com o Segment or segmento](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Envie dados diretamente para a [API or interface de programação do aplicativo (API)](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) da SalesWings a partir de uma solução de terceiros

### Etapa 3: Conectando a SalesWings à Braze {#step-3-connecting-saleswings-to-braze}

Acesse a [página **SalesWings Integrations**](https://helium.saleswings.pro/integrations) e expanda a seção **Braze Integration**.

![A seção Braze Integration na página de configurações da SalesWings.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Copie o valor da coluna **Identifier** para a nova chave criada e cole-o no campo **Braze API or interface de programação do aplicativo (API) key** da seção **Braze Integration** da SalesWings.

Adicione seu endpoint da API or interface de programação do aplicativo (API) da Braze conforme descrito no [artigo de endpoints da API or interface de programação do aplicativo (API) e do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) e insira-o no campo **Braze API or interface de programação do aplicativo (API) endpoint**. Copie o valor da coluna **REST or transferir estado representacional Endpoint** e insira-o no campo **Braze API or interface de programação do aplicativo (API) endpoint** na seção **Braze Integration** da SalesWings.

Em seguida, selecione **Save**.

### Etapa 4: Ativar o push de insights da SalesWings para a Braze (opcional) {#step-4-enable-saleswings-insights-push-to-braze-optional}

Se quiser disponibilizar os insights da SalesWings em seus perfis de usuário da Braze para segmentação, personalização ou orquestração da jornada do Canvas, visite a [página **SalesWings Integrations**](https://helium.saleswings.pro/integrations) e expanda a seção **Braze Integration**.

Clique em **Start data push** em **SalesWings-to-Braze insights data push**.

### Etapa 5: Configure uma exportação personalizada do Currents para a SalesWings (opcional) {#step-5-set-up-a-custom-currents-export-to-saleswings-optional}

Se quiser usar eventos de [comportamento do usuário]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) e de [engajamento com mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para inteligência comportamental, pontuação de leads e contas, produzir insights de vendas ou gerar relatórios em seu CRM, acesse a [página **SalesWings Integrations**](https://helium.saleswings.pro/integrations) e expanda a seção **Braze Integration**.

Selecione **Generate** em **Generate an API or interface de programação do aplicativo (API) token to setup a Custom Currents Export**.

Em seguida, [crie um novo Current]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents) e selecione **Custom Currents Export** como o tipo de Current.

Na seção **Credentials** do formulário de criação do Current, insira o token da API or interface de programação do aplicativo (API) gerado na [página **SalesWings Integrations**](https://helium.saleswings.pro/integrations) para **Bearer Token** e `https://helium.saleswings.pro/api/braze/currents/events` para **Endpoint**.

### Etapa 6: Configuração da pontuação de leads e contas da SalesWings para a Braze, integração com CRM e muito mais {#step-6-configuring-saleswings-lead-and-account-scoring-for-braze-crm-integration-and-more}

Consulte a equipe de serviços da SalesWings para obter suporte completo de integração pelo [site](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs).

## Usando essa integração {#using-this-integration}

Para vincular dados comportamentais e outros dados a leads e contas, a SalesWings deve identificar um usuário em seu site ou app, ou por meio de uma integração de terceiros. Isso pode ocorrer das seguintes maneiras:

- **Envios de formulários:** Quando um usuário envia um formulário da web, a SalesWings identificará automaticamente todos os tipos de formulários da web (como login, download, fale conosco, etc.) e resolverá a identidade de um usuário quando ele enviar um formulário.
- **Cliques em URL com ID da Braze ou ID externo:** Um usuário clica em uma ação de marketing da Braze, tipicamente cliques em e-mail, cliques em banner ou similar, levando a uma página que você está rastreando com a SalesWings.
- **Eventos Braze Currents (opcional):** Se a exportação personalizada do Currents para a SalesWings estiver configurada, a SalesWings criará um perfil identificado para cada usuário da Braze com um e-mail que tenha eventos enviados para o Current.
- **Rastreamento de e-mail de vendas via plugins do Gmail e Outlook (opcional):** Se você decidir capacitar seu representante de vendas com plugins de rastreamento de e-mail, ele poderá disparar o rastreamento completo do site dos usuários enviando links rastreáveis.
- **Evento de identificação do Segment.com (opcional):** Se você é um usuário do Segment.com, também pode resolver a identidade de um usuário com a integração do Segment.com.

### Identificando usuários a partir de cliques em URLs {#identifying-users-from-url-clicks}

Você pode identificar os usuários automaticamente quando eles clicam em uma URL rastreável (por exemplo, e-mails em massa, banners com URLs). Para tornar uma URL rastreável, existem duas maneiras de modificar as URLs do seu site em seus e-mails, banners ou SMS, adicionando o parâmetro e o ID ao final de seus links.

1. Anexando `?braze_id=` seguido por {% raw %}`{{${braze_id}}}`{% endraw %}
  - **Exemplo de link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anexando `?br_user_id=` seguido por {% raw %}`{{${user_id}}}`{% endraw %}
  - **Exemplo de link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

A variável `braze_id` é definida como um identificador do usuário gerado pela Braze e está sempre disponível. A variável `br_user_id` é definida como o identificador do usuário no seu sistema e pode estar ausente em certos cenários (por exemplo, para usuários anônimos criados pelo SDK or kit de desenvolvimento de software da Braze). Se ambos `braze_id` e `br_user_id` forem usados em um link, a SalesWings considerará apenas o parâmetro `braze_id`.

### Enviando insights da SalesWings para a Braze {#pushing-saleswings-insights-to-braze}

Se você ativar o push de insights da SalesWings para a Braze, a SalesWings atualizará os perfis de usuário da Braze com os seguintes [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types):

| Atributo personalizado | Tipo | Descrição |
| ----------- | ----------- | ----------- |
| `sw_favorite` | booleano | Se o lead foi marcado como favorito na SalesWings ou no Salesforce CRM |
| `sw_last_active_at` | data | O momento da última atividade do lead em seu site |
| `sw_lead_link_open` | string | O link para acessar um perfil de lead na SalesWings (sem uma conta no dashboard da SalesWings) |
| `sw_lead_link_protected` | string | O link para acessar um perfil de lead na SalesWings (com uma conta no dashboard da SalesWings) |
| `sw_lead_owner` | string | O proprietário definido para o lead na SalesWings ou no Salesforce CRM |
| `sw_lead_score` | float | O valor da pontuação principal do lead da SalesWings configurado no [Rule Engine](https://helium.saleswings.pro/falcon) da SalesWings |
| `sw_predictive_score` | string | O valor da [pontuação preditiva](https://support.saleswingsapp.com/en/articles/581795-the-predictive-lead-score) da SalesWings que avalia o engajamento do lead com base no número e na recência das atividades rastreadas. Os valores possíveis são `HOT`, `WARM`, `NORMAL`, `COLD` ou `FROZEN` |
| `sw_salesforce_record_id` | string | O ID do registro de lead ou contato no Salesforce CRM |
| `sw_salesforce_record_url` | string | A URL do registro de lead ou contato no Salesforce CRM |
| `sw_session_count` | inteiro | O número de sessões rastreadas em seu site para esse lead |
| `sw_tags` | array de string | As necessidades e os interesses que a SalesWings identificou, representados como "tags". Os nomes das tags da SalesWings configuradas no [Rule Engine](https://helium.saleswings.pro/falcon) da SalesWings que se aplicam a esse lead |
| Atributos adicionais de pontuação de leads | float | Um atributo personalizado para cada pontuação de lead adicional configurada no [Rule Engine](https://helium.saleswings.pro/falcon) da SalesWings. O nome do atributo é derivado do nome da pontuação da SalesWings; por exemplo, uma pontuação chamada `Likeliness to meet` é enviada como atributo personalizado `sw_likeliness_to_meet`. Se você renomear uma pontuação depois que o sistema a criar, a SalesWings continuará sincronizando com o nome inicial do atributo personalizado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Enviando insights da SalesWings para a Braze" }

Quando o push é ativado, a SalesWings começa imediatamente a enviar atributos personalizados para a Braze assim que os pontos de dados subjacentes mudam nos perfis de leads da SalesWings e sincroniza progressivamente todos os leads existentes, mesmo que eles não tenham novas atualizações.

A SalesWings atualiza todos os usuários da Braze com um e-mail que corresponde ao endereço de e-mail do perfil de lead da SalesWings. Se não houver usuários correspondentes na Braze, a SalesWings não criará um novo usuário.

### Usando eventos Braze Currents em seu CRM {#using-braze-currents-events-in-your-crm}

Se você conectar um Braze Current à SalesWings, a SalesWings criará perfis de leads identificados para cada usuário da Braze com um e-mail e registrará os eventos suportados pela Braze como atividade de lead. Em seu CRM, todos os dados podem ser automaticamente agregados no nível da conta do lead. A atividade e os dados registrados podem ser combinados ainda mais com os dados comportamentais coletados com o script de rastreamento da SalesWings ou Segment.com, ou enviando outros dados para a API or interface de programação do aplicativo (API) da SalesWings, e depois usados para identificar as necessidades e a prontidão de vendas de seus clientes potenciais para seus processos de gerenciamento de leads e contas.

A tabela a seguir mostra os tipos de eventos da Braze suportados pela SalesWings e sua representação no histórico de atividades de leads e no mecanismo de regras da SalesWings:

| Categoria do evento | Tipo de evento | Nome do evento na SalesWings |
| ----------- | ----------- | ----------- |
| Eventos do Canvas | Entradas | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| Eventos de comportamento do cliente | Eventos personalizados | `[Custom Event tracked] $name` |
| Eventos de comportamento do cliente | Primeira sessão | `[User Action] Today marks the user's first session` |
| Eventos de comportamento do cliente | Atribuição da instalação | `[User Action] User installed app from $source` |
| Eventos de comportamento do cliente | Eventos de compra | `[Purchase] Customer purchased $product_id for $price $currency` |
| Eventos de mensagem | Clique no cartão de conteúdo | `[Content Card engagement] Clicked on $campaign_name content card` |
| Eventos de mensagem | Bounce de e-mail | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| Eventos de mensagem | Clique no e-mail | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| Eventos de mensagem | Entrega de e-mail | `[Nurturing] Received email $campaign_name` |
| Eventos de mensagem | Abertura de e-mail | `[Email campaign engagement] Opened email $campaign_name` |
| Eventos de mensagem | Cancelamento de inscrição de e-mail | `[Subscription status change] Unsubscribed from $campaign_name` |
| Eventos de mensagem | Clique em mensagem no app | `[In-app campaign engagement] Clicked on message $campaign_name` |
| Eventos de mensagem | Abertura de push | `[Push notification engagement] Clicked on notification $campaign_name` |
| Eventos de mensagem | SMS/MMS de entrada recebidos | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Eventos de mensagem | Clique em link encurtado de SMS/MMS | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Eventos de mensagem | WhatsApp de entrada recebido | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Eventos de mensagem | Leitura de WhatsApp | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Inscrições | Alteração de estado de inscrição global | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Inscrições | Alteração de estado do grupo de inscrições | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Usando eventos Braze Currents em seu CRM" }

Em seguida, você pode configurar as condições de **Custom Event** > **Event Name** e **Custom Event** > **Event Property** para as tags e pontuações da SalesWings em relação aos nomes de eventos da SalesWings da tabela nesta seção. A lista de propriedades de eventos disponíveis para condições é pré-preenchida com algumas das entradas mais usadas, e você sempre pode adicionar novas na seção **Event Property** da [página de configuração do Rule Engine](https://helium.saleswings.pro/falcon).

![Exemplo de uma condição de nome de evento.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

Para configuração e solução de problemas, entre em contato com a [equipe de serviços da SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para suporte de integração.