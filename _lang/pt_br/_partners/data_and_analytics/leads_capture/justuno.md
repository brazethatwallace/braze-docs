---
nav_title: Justuno
article_title: Justuno
description: "Saiba como integrar o Justuno à Braze para que você possa aproveitar os dados do cliente em ambas as plataformas para criar experiências mais personalizadas para todos os públicos."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> O [Justuno](https://www.justuno.com/) permite criar experiências de visitantes totalmente otimizadas para todos os seus públicos com segmentos dinâmicos, oferecendo o direcionamento mais avançado disponível&#8212;tudo sem afetar a velocidade do site ou aumentar o trabalho de desenvolvimento. Analise as taxas de conversão visualizando análises de dados personalizadas, como o número de perfis criados, a taxa de visitantes de retorno influenciados e as páginas por sessão para manter uma vantagem de marketing em seu setor. O Justuno permite que você aumente a receita por visitante, estabeleça engajamentos significativos com os clientes e expanda seus negócios. Otimize toda a jornada do público de ponta a ponta com uma plataforma conectada.

## Casos de uso {#use-cases}

A Braze permite que qualquer profissional de marketing colete e aja com base em qualquer quantidade de dados de qualquer fonte, para que você possa se engajar de forma criativa com os clientes em tempo real, em todos os canais, a partir de uma única plataforma.

A integração do Justuno com a Braze oferece o melhor dos dois mundos. Você pode combinar os dados do cliente salvos na Braze com os dados do visitante e do cliente salvos no Justuno e criar experiências mais personalizadas para todos os públicos. Isso aumenta a eficácia das suas campanhas de marketing e o engajamento dos clientes.

## Pré-requisitos {#prerequisites}

| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `users.track` e `custom_attributes.get`.<br><br>Isso pode ser criado no dashboard da Braze em **Settings** > **API Keys**. |
| Endpoint REST da Braze | Seu URL do endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração do Justuno com a Braze {#integrating-justuno-with-braze}

### Etapa 1: Criar atributos personalizados na Braze {#step-1-create-custom-attributes-in-braze}

Para sincronizar atributos de usuário do Justuno para a Braze, será necessário criar esses atributos na Braze, caso ainda não o tenha feito. Você pode fazer isso acessando **Data Settings** > **Custom Attributes** e, em seguida, criando seus atributos personalizados. Para obter um passo a passo completo, consulte [Gerenciando atributos personalizados na Braze]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### Etapa 2: Adicionar o app da Braze ao Justuno {#step-2-add-the-braze-app-to-justuno}

#### Etapa 2.1: Adicione-o à sua conta {#step-21-add-it-to-your-account}

Para adicionar o app da Braze à sua conta Justuno, acesse **Account Settings** > **Apps** e, em seguida, procure e selecione o app da Braze.

![A página "Connect Apps" no Justuno com o app da Braze mostrado na lista de resultados de pesquisa.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Digite a chave de API e o URL de base [que você criou anteriormente](#prerequisites) e selecione **Connect**.

![A janela pop-up de autenticação da Braze solicitando uma chave de API da Braze e um URL de base.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Etapa 2.2: Adicione-o ao seu fluxo de trabalho {#step-22-add-it-to-your-workflow}

Para adicionar o app da Braze ao seu [fluxo de trabalho Justuno](https://hub.justuno.com/knowledge/workflows-overview), arraste e solte a ação **Sync to App** em seu fluxo de trabalho e, em seguida, escolha **Select App** > **Braze**.

![A opção "Select App" localizada na ação "Sync to App".]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Etapa 3: Conecte seus grupos de inscrições da Braze {#step-3-connect-your-braze-subscription-groups}

Para enviar dados de perfil do Justuno para um grupo de inscrições de e-mail ou SMS específico da Braze, você precisará adicionar o ID deles ao app da Braze em seu fluxo de trabalho do Justuno.

| Tipo de ID                          | Obrigatória? | Descrição                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| ID do grupo de inscrições SMS da Braze  | Sim       | Esse ID é usado para coletar o consentimento de SMS dos perfis de usuário. Se nenhum ID for inserido no Justuno, os perfis não terão consentimento quando o Justuno enviar esse perfil para a Braze. |
| ID do grupo de inscrições para e-mail da Braze | Não        | Se esse ID não for inserido no Justuno, o Justuno enviará os dados do perfil para a Braze como um usuário sem grupos de inscrições associados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 3: Conecte seus grupos de inscrições da Braze" }

#### Etapa 3.1: Localize os IDs na Braze {#step-31-locate-the-ids-in-braze}

Para localizar esses IDs no dashboard da Braze:

1. Acesse **Audience** > **Subscriptions**.
2. Para cada grupo de inscrições, anote o ID localizado na coluna ID.

#### Etapa 3.2: Adicione os IDs ao app da Braze {#step-32-add-the-ids-to-the-braze-app}

Em seu fluxo de trabalho Justuno, abra o app da Braze e insira os IDs de cada grupo de inscrições.

![O app da Braze aberto em um fluxo de trabalho Justuno com a opção de adicionar IDs de grupos de inscrições para e-mail e SMS.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Etapa 4: Configure seus atributos {#step-4-configure-your-attributes}

Os seguintes atributos são sincronizados automaticamente do Justuno para a Braze:

- E-mail
- Telefone
- Nome
- Sobrenome
- Idioma
- Gênero
- País

Para sincronizar atributos adicionais:

1. No app da Braze em seu fluxo de trabalho, selecione **Sync Another Property**.
    ![O app da Braze aberto em um fluxo de trabalho Justuno mostrando a opção "Sync Another Property".]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Escolha quais atributos da Braze você gostaria de sincronizar.
3. Combine as propriedades no Justuno com seus equivalentes na Braze (como identificadores sociais, data de aniversário, preferências de compras, respostas a pesquisas e similares). Lembre-se de que essas propriedades são consideradas dados de parte zero ou dados de primeira parte. Para saber mais, consulte [Justuno: Coleta de dados de visitantes](https://www.justuno.com/guides/zero-first-party-data/).
4. No construtor de fluxo de trabalho, escolha **Save**, **prévia** ou **Publish** para seu fluxo de trabalho.
    ![O menu "Publish" aberto com as opções de salvar, pré-visualizar ou mostrar o histórico de versões.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Informações importantes {#things-to-know}

- Você deve inserir manualmente o ID do grupo de inscrições nas configurações do app.
- Os seguintes tipos de dados da Braze **não são** suportados: Objeto, vetor de objeto.
- O consentimento implícito de SMS é fornecido quando o campo de consentimento de SMS do Justuno não é usado.
- O consentimento explícito por SMS será respeitado se o design do Justuno incluir o campo de consentimento.