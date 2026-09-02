---
nav_title: Survicate
article_title: Survicate
description: "Este artigo de referência descreve a parceria entre a Braze e a Survicate, uma plataforma de feedback do cliente que ajuda a coletar, analisar e agir com base nos insights do cliente em vários canais e durante toda a jornada do usuário."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [A Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) é uma plataforma de feedback do cliente que coleta, analisa e age com base nos insights do cliente em vários canais e durante toda a jornada do usuário. [Assista a uma demonstração rápida](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Essa integração é mantida pela Survicate._

## Sobre a integração {#about-the-integration}

Use a integração nativa da Survicate e da Braze para sincronizar as respostas de pesquisas por e-mail, no app, no celular ou na web com os perfis de clientes da Braze. As respostas da pesquisa são sincronizadas automaticamente com os perfis de usuário da Braze como atributos personalizados ou eventos. Os insights de feedback em tempo real facilitam o rastreamento e a análise do feedback juntamente com os dados de clientes e a criação de acompanhamentos direcionados e segmentos hiperpersonalizados.

## Casos de uso {#use-cases}

A Braze e a Survicate trabalham juntas para cobrir uma série de casos de uso de feedback, ajudando você a coletar insights práticos sobre o usuário e a melhorar a experiência do cliente:

- Melhore as taxas de resposta das pesquisas com pesquisas incorporadas que podem ser respondidas diretamente da caixa de entrada de e-mail.
- Reúna insights em estágios críticos da jornada do cliente por meio de In-App Messages da Braze.
- Use o feedback armazenado na Survicate para criar segmentos mais inteligentes na Braze.
- Automatize campanhas de acompanhamento com base no feedback do cliente.
- Use os insights dos clientes para disparar fluxos de trabalho personalizados.
- Alcance um público mais amplo com pesquisas traduzidas automaticamente.
- Envie eventos para os perfis de contato da Braze quando alguém responder à sua pesquisa.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Survicate | Você precisa de uma conta Survicate para ativar essa integração. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com a permissão `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **APIs e identificadores**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Principais recursos da integração {#key-features-of-the-integration}

A integração entre a Survicate e a Braze oferece sincronização de dados em tempo real, de modo que as informações mais atualizadas das pesquisas da Survicate ficam imediatamente disponíveis na Braze. Com base nas respostas da pesquisa, você pode usar esses dados para tomar ações oportunas e personalizadas.

- **Envie as respostas da pesquisa para a Braze como atributos personalizados do usuário**: Enriqueça os perfis de usuários da Braze com dados de respostas de pesquisas.
- **Dispare eventos personalizados na Braze**: Use eventos baseados nas respostas da pesquisa para direcionar grupos específicos ou iniciar campanhas de acompanhamento.
- **Crie segmentos detalhados**: Crie segmentos na Braze usando dados das pesquisas da Survicate para personalizar ainda mais seu alcance.

## Integração {#integration}

### Criando suas pesquisas na Survicate {#creating-your-surveys-in-survicate}

#### Incorpore sua pesquisa em um e-mail ou crie uma pesquisa com link compartilhável {#embed-your-survey-in-an-email-or-create-a-shareable-link-survey}

1.  Na Survicate, clique em **+ Create new survey**, selecione qualquer método de criação (um modelo, usando a criação de pesquisa por IA ou adicionando suas próprias perguntas) e o tipo de pesquisa Email ou Shareable link:
![Braze é selecionado no criador da pesquisa.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2. Na guia **Configure** da pesquisa, selecione **Braze** como a ferramenta para identificar os respondentes:
![Braze é selecionado na guia Configure da pesquisa.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3. Depois de configurar sua pesquisa, acesse a guia **Share** e decida como enviar sua pesquisa por e-mail. Há duas opções: você pode enviar a **pesquisa como um link** ou **incorporar a primeira pergunta no e-mail** para que os respondentes comecem a responder à pesquisa diretamente do e-mail.

{% details Survey link option %}

1. Pegue um link para sua pesquisa no botão Copy survey link:

![Pegue um link para sua pesquisa no botão Copy survey link.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2. Oculte o link da pesquisa atrás de um botão de CTA ou hiperlink no seu e-mail da Braze.

![Oculte o link da pesquisa atrás de um botão de CTA ou hiperlink no seu e-mail da Braze.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Exiba a primeira pergunta diretamente no corpo do e-mail para iniciar a pesquisa a partir do e-mail. Os respondentes são então redirecionados para uma landing page para responder ao restante da pesquisa.

1. Clique em **Get email code** e, em seguida, **Copy the HTML code**:

![Obter código de e-mail]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2. Acesse a Campaign da Braze que deseja usar para a pesquisa, clique em **Edit email body** e adicione um bloco HTML ao seu modelo:

![Obter código do bloco HTML]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3. Substitua o código pelo que você copiou da sua pesquisa Survicate. Você verá a primeira pergunta da pesquisa no modelo:

![Substitua o código pelo que você copiou da sua pesquisa Survicate]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. Programe o envio do e-mail, escolha seu grupo-alvo e sua Campaign estará pronta para ser enviada.

{% enddetails %}

### Pesquisa de In-App Message da Braze {#braze-in-app-message-survey}

1. Clique em **+ Create new survey**, selecione qualquer método de criação (um modelo, usando a criação de pesquisa por IA ou adicionando suas próprias perguntas) e, em seguida, escolha In-platform surveys e o tipo de pesquisa Braze In-App Message:

![Clique em + Create new survey e selecione qualquer método de criação]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2. Inicie sua pesquisa de In-App Message da Braze navegando até sua conta Braze e, em seguida, em **Messaging > Campaigns > Create campaign > In-app message**:
![Inicie sua pesquisa de In-App Message da Braze]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Inicie sua pesquisa de In-App Messenger da Braze pelo editor tradicional {#launch-your-braze-in-app-messenger-survey-via-the-traditional-editor}

1. Se você usar o editor tradicional, no tipo de mensagem, selecione **Custom code**:

![Selecione Custom code]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2. Em seguida, cole o código da guia **Launch** da sua pesquisa no campo HTML:

![Cole o código da guia Launch da sua pesquisa no campo HTML]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Por padrão, a Braze exibe mensagens no app em um iframe enquanto o plano de fundo do app está bloqueado. Para permitir a interação com seu app enquanto as pesquisas da Survicate são exibidas, você deve:<br><br>

- Adicionar `opts.useBrazeIframeClipper = true` ao seu snippet Survicate-Braze.
- Instalar o [pacote](https://www.npmjs.com/package/@survicate/braze-bridge-npm) `@survicate/braze-bridge-npm` no arquivo em que você inicializa a Braze e usar a função `initBrazeBridge`.

Você pode encontrar um snippet de exemplo e a implementação em React [no site de desenvolvedores da Survicate](https://developers.survicate.com/javascript/installation/#braze).
{% endalert %}

{: start="3"}
3. Na sua Campaign da Braze, configure as etapas **Target** e **Assign**. Quando concluída, sua Campaign estará pronta para ser lançada. Na etapa **Review**, você pode ver a aparência da Campaign. A pesquisa aparece no seu site no local especificado no painel da Survicate, conforme descrito na etapa 1.

### Ativando a integração da Braze {#enabling-the-braze-integration}

1. Para ativar a integração da Braze, acesse **Integrations**, pesquise e selecione "Braze".

![Selecione Braze]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2. Clique em **Connect** para configurar a autorização.

3. Insira a chave de API or interface de programação do aplicativo (API) do espaço de trabalho da sua conta Braze e a URL da instância da Braze:

![Insira a chave de API do espaço de trabalho da sua conta Braze e a URL da instância da Braze]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Para conectar a Survicate à Braze, a chave de API or interface de programação do aplicativo (API) da Braze precisa ter as permissões `users.track`.
{% endalert %}

### Conectando suas pesquisas à Braze {#connecting-your-surveys-to-braze}

Agora que a integração da Braze está conectada, você pode definir configurações individuais para cada pesquisa. Acesse sua pesquisa, selecione a guia **Connect** e escolha **Braze** na lista de integrações disponíveis.

![Acesse sua pesquisa, selecione a guia Connect e escolha Braze]({% image_buster /assets/img/survicate/survicate_14.png %})

### Envio de respostas à Braze como atributos personalizados {#sending-responses-to-braze-as-custom-attributes}

Configure as respostas da pesquisa para fluírem para a Braze como atributos personalizados, enriquecendo os perfis de usuários da Braze com os dados coletados.

1. Na guia **Settings** da integração da Braze, encontre a seção **Update fields**.

![Selecione a seção Update fields]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2. Selecione a pergunta da qual você deseja atualizar os campos. Para evitar a sobrecarga dos perfis de usuários da Braze com dados, você pode enviar respostas apenas para as perguntas escolhidas.

![Selecione a pergunta da qual você deseja atualizar os campos]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
As perguntas de classificação e de matriz não são compatíveis com essa integração da Braze.
{% endalert %}

{: start="3"}
3. Adicione o nome do atributo personalizado que deseja atualizar no campo **User**:

![Adicione o nome do atributo personalizado que deseja atualizar no campo User]({% image_buster /assets/img/survicate/survicate_17.png %})

Por padrão, a Survicate envia o conteúdo de uma resposta de pesquisa como um valor de atributo. Você pode alterar o rótulo para torná-lo mais curto ou ajustá-lo à sua estrutura de dados, clicando em **Edit mapping** para modificar esses valores:

![Resposta da pesquisa como um valor de atributo]({% image_buster /assets/img/survicate/survicate_18.png %})

![Clique em Edit mapping para modificar esses valores]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Para o Net Promoter Score (NPS), a Survicate envia valores mapeados com base no grupo de resposta para a pergunta do Net Promoter Score (NPS)®. No entanto, se quiser receber valores numéricos, você pode ativar a opção Send Answers as 0-10 values.
{% endalert %}

![A Survicate envia valores mapeados com base no grupo de resposta]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. Conecte mais perguntas à sua integração clicando em **+ Add new** e aplicando as mesmas etapas.

![Conecte mais perguntas à sua integração]({% image_buster /assets/img/survicate/survicate_21.png %})

### Envio de eventos para os perfis dos contatos da Braze {#sending-events-to-braze-contacts-profiles}

Além das configurações anteriores, cada vez que um respondente responde a uma pergunta da pesquisa, a Survicate pode enviar um evento personalizado na Braze chamado `survicate-question-answered`.
No painel da Survicate, em Send responses as custom attributes, você pode escolher se deseja enviar o evento para todas as perguntas, para as perguntas escolhidas na guia Update fields ou para nenhuma:

![Você pode escolher se deseja enviar o evento para todas as perguntas]({% image_buster /assets/img/survicate/survicate_22.png %})

Se você optar por enviar os eventos, poderá ver nos perfis dos usuários quantas vezes eles responderam às pesquisas da Survicate e quando foi a última vez que responderam:

![Respostas]({% image_buster /assets/img/survicate/survicate_23.png %})

O evento contém propriedades de evento com a resposta à pergunta e informações sobre a pesquisa, a pergunta e o respondente. Você pode usar esse evento para criar segmentos. Por exemplo, crie um Segment or segmento or segmento de usuários que responderam a uma pesquisa após uma determinada data ou um determinado número de vezes:

![O evento contém propriedades de evento com a resposta]({% image_buster /assets/img/survicate/survicate_24.png %})

Você também pode usar esses dados ao criar uma Campaign na Braze.

![Você também pode usar esses dados ao criar uma Campaign na Braze]({% image_buster /assets/img/survicate/survicate_25.png %})

### Teste a integração {#test-the-integration}

Quando sua pesquisa estiver pronta e a integração configurada, você pode testá-la sem sair da Survicate, clicando no botão **Test Integration** ao lado de qualquer atributo, tag ou configuração de novo contato que tenha sido criada. A Survicate cria um contato de teste (`braze-test@survicate.com`) na sua conta Braze. O perfil do contato inclui campos atualizados de acordo com a configuração.

![Clique no botão Test Integration]({% image_buster /assets/img/survicate/survicate_26.png %})

Na Braze, você vê dados de amostra dos campos mapeados no contato fictício da Survicate:

![Dados de amostra dos campos mapeados no contato fictício da Survicate]({% image_buster /assets/img/survicate/survicate_27.png %})

### Análise dos resultados da pesquisa {#analyzing-your-survey-results}

Depois de coletar as respostas por meio da sua pesquisa da Braze, é hora de analisar o feedback e os insights que os respondentes compartilharam. A Survicate permite que você analise facilmente os resultados, as estatísticas e as tendências para tomar ações adicionais.

### Feedback na Survicate {#feedback-in-survicate}

Depois que sua pesquisa começar a coletar respostas, elas serão imediatamente exibidas na guia **Analyze** da pesquisa.

![Respostas na guia Analyze]({% image_buster /assets/img/survicate/survicate_28.png %})

A guia **Analyze** mostra os resultados gerais com estatísticas e dados ao longo do tempo, bem como respostas individuais para examinar detalhadamente cada envio de pesquisa.

### Feedback na Braze {#feedback-in-braze}

Se você atualizar os campos de usuários com as respostas da pesquisa ou enviar respostas como eventos personalizados, poderá ver os dados da pesquisa sincronizados em tempo real. Na Braze, acesse um contato específico que respondeu à sua pesquisa. Você verá os dados baseados em resposta e os eventos na visualização principal do contato.

![Dados da pesquisa sincronizados em tempo real]({% image_buster /assets/img/survicate/survicate_29.png %})