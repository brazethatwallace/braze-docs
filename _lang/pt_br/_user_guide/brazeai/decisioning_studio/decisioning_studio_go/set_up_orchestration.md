---
nav_title: Configurar orquestração
article_title: Configurar orquestração
page_order: 2
description: "Aprenda como conectar o BrazeAI Decisioning Studio Go à sua plataforma de engajamento com clientes para ativar comunicações personalizadas."
toc_headers: h2
---

# Configurar orquestração {#set-up-orchestration}

> O BrazeAI Decisioning Studio™ Go precisa se conectar à sua plataforma de engajamento com clientes (CEP) para orquestrar comunicações personalizadas. Este artigo explica como configurar a integração para cada CEP compatível.

## CEPs compatíveis {#supported-ceps}

O Decisioning Studio Go é compatível com as seguintes plataformas de engajamento com clientes:

| CEP | Tipo de integração | Principais recursos |
|-----|-----------------|--------------|
| **Braze** | Campaigns disparadas por API | Integração nativa, disparo em tempo real |
| **Salesforce Marketing Cloud** | Journey Builder com eventos de API | Automação de consultas de SQL, extensões de dados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CEPs compatíveis" }

Selecione sua CEP na lista abaixo para começar a configuração da integração.

{% tabs %}
{% tab Braze %}

## Configurar a integração com a Braze {#set-up-braze-integration}

Para integrar o Decisioning Studio Go com a Braze, você criará uma chave de API, configurará uma campanha disparada por API e fornecerá os identificadores necessários ao portal do Decisioning Studio Go.

### Etapa 1: Criar uma chave da API REST {#step-1-create-a-rest-api-key}

1. No dashboard da Braze, acesse **Configurações** > **APIs e identificadores** > **Chaves de API**.
2. Selecione **Criar chave de API**.
3. Digite um nome para sua chave de API. Um exemplo é "DecisioningStudioGoEmail".
4. Selecione as permissões com base nas seguintes categorias:
    - **User Data:** selecione `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Messages:** selecione `messages.send`, `messages.schedule.create`, `messages.schedule.update`, `messages.schedule.delete`
    - **Campaigns:** selecione todas as permissões listadas
    - **Canvas:** selecione todas as permissões listadas
    - **Segments:** selecione todas as permissões listadas
    - **Templates:** selecione todas as permissões listadas

{: start="5"}
5. Selecione **Criar chave de API**.
6. Copie a chave de API e cole-a no portal do BrazeAI Decisioning Studio™ Go.

### Etapa 2: Localizar o nome de exibição do e-mail {#step-2-locate-your-email-display-name}

1. No dashboard da Braze, acesse **Configurações** > **Preferências de e-mail**.
2. Localize o nome de exibição a ser usado com o BrazeAI Decisioning Studio™ Go.
3. Copie e cole o **From Display Name** no portal do BrazeAI Decisioning Studio™ Go como **Email Display Name**.
4. Copie e cole o endereço de e-mail associado no portal do BrazeAI Decisioning Studio™ Go como **From email address**, que combina a parte local e o domínio.

### Etapa 3: Encontrar a URL da Braze e o ID do app {#step-3-find-your-braze-url-and-app-id}

**Para encontrar a URL da Braze:**
1. Acesse o dashboard da Braze.
2. Na janela do navegador, a URL da Braze começa com `https://` e termina com `braze.com`. Um exemplo de URL da Braze é `https://dashboard-01.braze.com`.

**Para encontrar o ID do app (chave de API):**

{% alert note %}
A Braze oferece IDs de app (chamados de chaves de API no dashboard da Braze) que você pode usar para fins de rastreamento, como associar atividades a um app específico no seu espaço de trabalho. Se você usar IDs de app, o BrazeAI Decisioning Studio™ Go permite associar um ID de app a cada experimentador.<br><br>Se você não usar IDs de app, pode inserir qualquer string de caracteres como espaço reservado.
{% endalert %}

1. No dashboard da Braze, acesse **Configurações** > **Configurações do app**.
2. Acesse o app que você deseja rastrear.
3. Copie e cole a **API Key** no portal do BrazeAI Decisioning Studio™ Go.

### Etapa 4: Criar uma campanha disparada por API {#step-4-create-an-api-triggered-campaign}

1. No dashboard da Braze, acesse **Envio de mensagens** > **Campaigns**.
2. Selecione **Criar campanha**.
3. Para o tipo da campanha, selecione **API Campaign**.
4. Dê um nome à campanha. Um exemplo é "Decisioning Studio Go Email".

![Uma campanha da API chamada "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. Para o canal de envio de mensagens, selecione **Email**.

![Opção para selecionar o canal de envio de mensagens para a campanha da API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. Em **Opções adicionais**, marque a caixa de seleção **Allow users to become re-eligible to receive campaign**.
7. Para o tempo de re-elegibilidade, insira **1** e selecione **Hours** no menu suspenso.

![Re-elegibilidade para a campanha da API selecionada.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. Selecione **Salvar campanha**.

### Etapa 5: Copiar os IDs da campanha e da mensagem {#step-5-copy-your-campaign-and-message-ids}

1. Na sua campanha da API, copie o **Campaign ID**. Em seguida, acesse o portal do BrazeAI Decisioning Studio™ Go e cole o **Campaign ID**.

![Um exemplo de ID de variação de mensagem para copiar e colar.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2. Copie o **Message Variation ID**. Em seguida, acesse o portal do BrazeAI Decisioning Studio™ Go e cole o **Message Variation ID**.

### Etapa 6: Localizar um ID de usuário teste {#step-6-locate-a-test-user-id}

Para testar sua integração, você precisará de um ID de usuário:

Se o seu espaço de trabalho usa [criptografia em nível de campo de identificador]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption), qualquer novo usuário teste criado com o endpoint `/users/track` deve seguir os requisitos de e-mail para espaços de trabalho criptografados. Envie o campo `email` como o hash HMAC-SHA256 codificado em Base64 do valor do e-mail em letras minúsculas, e envie `email_encrypted` como o valor de e-mail criptografado gerado com suas chaves de criptografia de IPI configuradas.

1. No dashboard da Braze, acesse **Público** > **Pesquisar usuários**.
2. Pesquise o usuário pelo ID de usuário externo, alias, e-mail, número de telefone ou token por push.
3. Copie o ID do usuário para referência na sua configuração.

![Exemplo de perfil de usuário ao localizar um usuário pelo ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurar a integração com o SFMC {#set-up-sfmc-integration}

Para integrar o Decisioning Studio Go com o Salesforce Marketing Cloud, você configurará um pacote de app, criará uma automação de consulta de dados e construirá uma jornada para gerenciar envios disparados.

### Parte 1: Configurar um pacote de app do SFMC {#part-1-set-up-an-sfmc-app-package}

1. Acesse a página inicial do Marketing Cloud.
2. Abra o menu no cabeçalho global e selecione **Setup**.
3. Acesse **Apps** em **Platform Tools** na navegação do painel lateral e selecione **Installed Packages**.
4. Selecione **New** para criar um pacote de app.
5. Dê um nome e uma descrição ao pacote de app.

![Um pacote de app com o nome "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. Selecione **Add Component**.
7. Para o **Component Type**, selecione **API Integration**. Em seguida, selecione **Next**.
8. Para o **Integration Type**, selecione **Server-to-server**. Em seguida, selecione **Next**.
9. Selecione os seguintes escopos recomendados apenas para o seu pacote de app:
    - Channels > Email > Read, Write, Send
    - Channels > OTT > Read
    - Channels > Push > Read
    - Channels > SMS > Read
    - Channels > Social > Read
    - Channels > Web > Read
    - Assets > Documents and Images > Read, Write
    - Assets > Saved Content > Read, Write
    - Automation > Automations > Read, Write, Execute
    - Automation > Journeys > Read, Write, Execute, Activate/Stop/Pause/Send/Schedule
    - Contacts > Audiences > Read
    - Contacts > List and Subscribers > Read, Write
    - Cross Cloud Platform > Market Audience > View
    - Cross Cloud Platform > Market Audience Member > View
    - Cross Cloud Platform > Marketing Cloud Connect > Read
    - Data > Data Extensions > Read, Write
    - Data > File Locations > Read
    - Data > Tracking Events > Read, Write
    - Event notifications > Callbacks > Read
    - Event notifications > Subscriptions > Read

{% details Mostrar imagem dos escopos recomendados %}

![Os escopos recomendados para o pacote de app do Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. Selecione **Save**.
11. Copie e cole os seguintes campos no portal do BrazeAI Decisioning Studio™ Go: **Client Id**, **Client Secret**, **Authentication Base URI**, **REST Base URI**, **SOAP Base URI**.

### Parte 2: Configurar uma automação de consulta de dados {#part-2-set-up-a-data-query-automation}

#### Etapa 1: Criar uma nova automação {#step-1-create-a-new-automation}

1. Na página inicial do Salesforce Marketing Cloud, acesse **Journey Builder** e selecione **Automation Studio**.

![Opção Automation Studio na navegação do Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. Selecione **New Automation**.
3. Arraste e solte um nó **Schedule** como a **Starting Source**.

!["Schedule" como a fonte inicial de uma jornada.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. No nó **Schedule**, selecione **Configure**.
5. Defina o seguinte para o agendamento:
    - **Start Date:** dia do calendário de amanhã
    - **Time:** **12:00 AM**
    - **Time Zone:** **(GMT-05:00) Eastern (US & Canada)**
6. Para **Repeat**, selecione **Daily**.
7. Defina este agendamento para nunca terminar.
8. Selecione **Done** para salvar o agendamento.

![Um agendamento de exemplo definido para 25 de janeiro de 2024 às 12h ET, para repetir todos os dias.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Etapa 2: Criar suas consultas de SQL {#step-2-create-your-sql-queries}

Em seguida, crie 2 consultas de SQL: uma consulta de assinantes e uma consulta de engajamento. Essas consultas permitem que o BrazeAI Decisioning Studio™ Go recupere dados para preencher o público e ingerir eventos de engajamento.

**Consulta de assinantes:**

1. Arraste e solte uma **SQL Query** no canvas.
2. Selecione **Choose**.
3. Selecione **Create New Query Activity**.
4. Dê um nome e uma chave externa à consulta. Recomendamos usar o nome sugerido e a chave externa para a consulta de assinantes fornecidos no portal do BrazeAI Decisioning Studio™ Go.

![Um exemplo "OFE_Subscribers_query_Test5" e a chave externa.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. Selecione **Next**.
6. No portal do BrazeAI Decisioning Studio™ Go, localize a consulta SQL de dados do sistema em **Subscriber Query Resources**.
7. Copie e cole a consulta na caixa de texto e selecione **Next**.

![Um exemplo de consulta na seção de consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. No portal do BrazeAI Decisioning Studio™ Go, na seção **Resources to use**, localize a chave externa da extensão de dados alvo. Em seguida, cole-a na barra de pesquisa para buscar.

![Uma chave externa colada na barra de pesquisa.]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. Selecione a extensão de dados que corresponde à chave externa pesquisada. O nome da extensão de dados alvo também é fornecido no portal do BrazeAI Decisioning Studio™ Go para referência cruzada. A **Data Extension** para a consulta de assinantes deve terminar com o sufixo `BASE_AUDIENCE_DATA`.

![O nome da extensão de dados que corresponde à chave externa do exemplo.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. Selecione **Overwrite** e depois **Next**.

**Consulta de engajamento:**

1. Arraste e solte uma **SQL Query** no canvas.

!["SQL Query" adicionada como uma atividade na jornada.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. Selecione **Choose**.
3. Selecione **Create New Query Activity**.
4. Dê um nome e uma chave externa à consulta. Recomendamos usar o nome sugerido e a chave externa para a consulta de engajamento fornecidos no portal do BrazeAI Decisioning Studio™ Go.

![Um exemplo "OFE_Engagement_query" e a chave externa.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. Selecione **Next**.
6. No portal do BrazeAI Decisioning Studio™ Go, localize a consulta SQL de dados do sistema em **Engagement Query Resources**.
7. Copie e cole a consulta na caixa de texto e selecione **Next**.

![Um exemplo de consulta na seção de consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. Localize e selecione a extensão de dados alvo para a consulta de engajamento especificada no portal do BrazeAI Decisioning Studio™ Go.

{% alert tip %}
O nome da extensão de dados alvo também é fornecido no portal do BrazeAI Decisioning Studio™ Go para referência cruzada. Certifique-se de que você está olhando para a extensão de dados alvo da consulta de engajamento. A **Data Extension** para a consulta de engajamento deve terminar com o sufixo ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9. Selecione **Overwrite** e depois **Next**.

![O nome da extensão de dados que corresponde à chave externa do exemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Etapa 3: Executar a automação {#step-3-run-the-automation}

1. Dê um nome à automação e selecione **Save**.

![Uma automação de exemplo "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. Em seguida, selecione **Run Once** para confirmar que tudo está funcionando como esperado.
3. Selecione ambas as consultas e clique em **Run**.

![Uma automação "OFE_Experimenter_Test5_Automation" com uma lista de atividades de consulta SQL selecionadas para executar.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. Selecione **Run Now**.

![Uma atividade de consulta SQL selecionada.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Agora você pode verificar se a automação está sendo executada com sucesso. Entre em contato com o suporte da Braze para mais assistência se a automação não estiver funcionando como esperado.

### Parte 3: Criar sua jornada no SFMC {#part-3-create-your-sfmc-journey}

#### Etapa 1: Configurar a jornada {#step-1-set-up-the-journey}

1. No Salesforce Marketing Cloud, acesse **Journey Builder** > **Journey Builder**.
2. Selecione **Create New Journey**.
3. Para o tipo de jornada, selecione **Multi-Step Journey** e selecione **Create**.

![Uma fonte de entrada de evento de API conectada a um nó de divisão de decisão e múltiplos nós de e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Etapa 2: Construir a jornada {#step-2-build-the-journey}

**Criar uma fonte de entrada:**

1. Para a fonte de entrada, arraste **API Event** para o Journey Builder.

!["API Event" selecionado como a fonte de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2. No **API Event**, selecione **Create an event**.

![A opção "criar um evento" no evento de API.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. Selecione **Select Data Extension**. Localize e selecione a extensão de dados na qual o BrazeAI Decisioning Studio™ Go gravará as recomendações.
4. Selecione **Summary** para salvar suas alterações.
5. Selecione **Done** para salvar o evento de API.

![Resumo do evento de API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Adicionar uma divisão de decisão:**

1. Arraste e solte uma **Decision Split** após o **API Entry Event**.
2. Nos detalhes da **Decision Split**, selecione **Edit** para o primeiro caminho.

![Detalhes da divisão de decisão com o botão "Edit".]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. Atualize a **Decision Split** para usar o ID do modelo passado pela extensão de dados de recomendações. Localize o campo apropriado em **Journey Data**.

![A seção de dados da jornada no caminho 1 da divisão de decisão.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. Selecione seu evento de entrada e localize o campo de ID do modelo desejado, depois arraste-o para o espaço de trabalho.

![O ID do modelo de e-mail a incluir.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. Insira o ID do modelo do seu primeiro modelo de e-mail e selecione **Done**.
6. Selecione **Summary** para salvar este caminho.
7. Adicione um caminho para cada um dos seus modelos de e-mail e repita as etapas 4-6 da sequência anterior para definir os critérios de filtro de modo que o ID do modelo corresponda ao valor de ID de cada modelo.
8. Selecione **Done** para salvar o nó da **Decision Split**.

![Dois caminhos em uma divisão de decisão para cada ID de modelo de e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Adicionar um e-mail para cada divisão de decisão:**

1. Arraste um nó de **Email** para cada caminho da **Decision Split**.
2. Selecione **Email** e escolha o modelo apropriado para cada caminho (ou seja, o modelo cujo valor de ID corresponda à lógica da sua divisão de decisão).

![Um nó de e-mail adicionado à jornada.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Etapa 3: Ativar a jornada {#step-3-activate-the-journey}

Após configurar sua jornada, ative-a e compartilhe os seguintes detalhes com a equipe do BrazeAI Decisioning Studio™ Go:

* ID da jornada
* Nome da jornada
* Chave de definição do evento de API
* Chave externa da extensão de dados de recomendações

{% alert note %}
O portal do BrazeAI Decisioning Studio™ Go mostra a automação do SFMC provisionada para exportar os dados de assinantes e engajamento uma vez por dia. Se você abrir essa automação no SFMC, certifique-se de despausar e reativá-la.
{% endalert %}

1. No portal do BrazeAI Decisioning Studio™ Go, copie o **Nome da jornada**.
2. Em seguida, no Salesforce Marketing Cloud Journey Builder, cole o nome da jornada na barra de pesquisa.
3. Selecione o nome da jornada. Observe que a jornada está atualmente em status de rascunho.
4. Selecione **Validate**.

![A jornada concluída para ativar.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. Em seguida, revise os resultados da validação e selecione **Activate**.

![Recomendações listadas na seção de regras de validação.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. No resumo de **Activate Journey**, selecione **Activate** novamente.

![Resumo da jornada.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Tudo pronto! Agora você pode começar a disparar envios pelo BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Próximos passos {#next-steps}

Agora que você configurou a orquestração, prossiga para projetar seu agente:

- [Projetar seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent)