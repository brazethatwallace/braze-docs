---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Este artigo de referência descreve a parceria entre a Braze e a Iterate, permitindo que você enriqueça os dados de clientes usando pesquisas para acrescentar insights adicionais."
page_type: partner
search_tag: Partner

---

# Iterate

> A [Iterate](https://iteratehq.com) fornece ferramentas de pesquisa e feedback para ajudá-lo a aprender com seus clientes, oferecendo experiências de pesquisa fáceis de usar que correspondem à sua marca.

_Essa integração é mantida pela Iterate._

## Sobre a integração {#about-the-integration}

A integração da Iterate com a Braze permite que você entregue pesquisas da Iterate de forma nativa e prática em seu produto ou campanhas. As respostas da pesquisa podem ser registradas como atributos personalizados do usuário na Braze, permitindo que você construa uma imagem completa dos seus usuários ou crie novos e poderosos públicos e segmentos.

Com o SDK or kit de desenvolvimento de software da Braze instalado em seu aplicativo ou site, você pode usar as ferramentas de segmentação e direcionamento disponíveis na Braze para entregar pesquisas por meio de mensagens no app a uma parte específica do seu público com base em qualquer gatilho ou Segment or segmento or segmento personalizado. As pesquisas da Iterate também podem ser incorporadas diretamente em suas campanhas de e-mail ou incluídas como links em seu push ou em outros tipos de campanha.

## Pré-requisitos {#prerequisites}

| Requisito | Origem |
|---|---|
| Conta da Iterate | É necessário ter uma [conta da Iterate](https://iteratehq.com) para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. Para enviar pesquisas por meio de mensagens no app da Braze, você também precisará da permissão `kpi.mau.data_series`.<br><br> Isso pode ser criado no dashboard da Braze em **Settings** > **API or interface de programação do aplicativo (API) Keys**. |
| Endpoint REST or transferir estado representacional da Braze | Sua URL de endpoint REST or transferir estado representacional. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Com a Iterate, você pode coletar praticamente qualquer tipo de dados. Desde informações pessoais (nome, idade, e-mail), dados de desempenho (Net Promoter Score (NPS), satisfação do cliente, classificação por estrelas), preferências (dispositivo preferido, frequência preferida de comunicação) ou personalidade (livro favorito, cachorro ou gato). O que você pergunta depende inteiramente de você e do tipo de dados que deseja coletar ou do público que deseja construir.

## Integração {#integration}

### Como começar: conectar a Braze com a Iterate {#getting-started-connect-braze-with-iterate}

Faça login na sua conta da Iterate e adicione seu endpoint REST or transferir estado representacional da Braze e a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional na página **Company Settings**.

### Envie pesquisas como uma mensagem no app {#deliver-surveys-as-an-in-app-message}

#### Etapa 1: crie sua pesquisa {#step-1-create-your-survey}

Antes de criar sua pesquisa, ative a opção **Enable in-app message surveys** nas configurações da Iterate.

Em seguida, crie uma nova pesquisa na Iterate e adicione perguntas relevantes. Se apropriado, também é possível incluir uma mensagem de aviso a ser exibida antes da pesquisa. Selecione **Send via Braze In-App Message** como o tipo de pesquisa.

Quando a pesquisa estiver concluída, na guia **Publish**, copie o snippet de código em **Copy and paste your embed code**.

#### Etapa 2: compartilhe sua pesquisa {#step-2-share-your-survey}

Na Braze, crie uma nova campanha de mensagens no app, selecione **Custom Code** como o tipo de mensagem e cole o snippet de código na mensagem. Em seguida, selecione **Wait for User to Dismiss** como o comportamento ao clicar na mensagem.

Continue configurando sua campanha como faria com qualquer outra campanha de mensagens no app, escolhendo um método de entrega e direcionando um público.

### Envie pesquisas por e-mail ou push {#deliver-surveys-through-email-or-push}

#### Etapa 1: crie sua pesquisa

Crie uma nova pesquisa por e-mail ou link na Iterate e adicione perguntas relevantes. Depois que as perguntas tiverem sido escritas e você tiver personalizado o design, selecione **Send survey** > **Integrations** > **Braze**.

Em seguida, você verá as opções de configuração para enviar respostas à Braze. Ative a integração para habilitar o envio de respostas dessa pesquisa para a Braze.

#### Etapa 2: compartilhe sua pesquisa

Sua pesquisa pode ser compartilhada de duas maneiras: incorporando a primeira pergunta em sua mensagem ou incluindo um link direto para a pesquisa na plataforma Iterate.

![Opções de link da Iterate]({% image_buster /assets/img/iterate.png %})

- **Incorporar o código**
  - Copie o snippet de código em **Email embed code** na seção de integração da Braze na guia **Send survey**. Insira o código no HTML do seu e-mail da Braze onde deseja que o início da pesquisa apareça.
  - Se estiver tendo dificuldades para renderizar as perguntas da pesquisa ou se elas parecerem formatadas incorretamente, será necessário acessar a guia **Sending Info** no criador de mensagens e desmarcar **Inline CSS**.
- **Incluir um link**
  - Copie o link em **Survey Link** na seção de integração da Braze na guia **Send survey**. Note que o Liquid incluído no link {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} será automaticamente substituído para cada usuário após o envio.

### Próximos passos: crie campanhas de acompanhamento {#next-steps-build-follow-up-campaigns}

À medida que os usuários respondem, você verá o preenchimento dos perfis deles com dados em tempo real. Esses dados podem ser usados para segmentar usuários e enviar campanhas de acompanhamento personalizadas. Por exemplo, se você enviar a pergunta "Você gosta dos nossos produtos?", poderá criar segmentos de usuários que tenham o atributo personalizado `Do you enjoy our products?` e que tenham respondido "Sim" ou "Não" e direcionar esses usuários.

## Eventos personalizados da Braze {#braze-custom-events}

Quando um usuário responde a uma pergunta da pesquisa, a Iterate dispara um evento personalizado na Braze chamado `survey-question-response`. Os eventos personalizados permitem que você dispare qualquer número e tipo de campanhas de acompanhamento.

## Personalizar nomes de atributos de usuários {#customize-user-attribute-names}

Por padrão, o atributo de usuário criado para uma pergunta é o mesmo que o prompt.
Em alguns casos, você pode querer personalizar isso. Para fazer isso, clique no menu suspenso **Customize user attribute names** na etapa **Create your Survey** e insira os nomes personalizados que desejar.