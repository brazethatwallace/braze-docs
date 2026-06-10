---
nav_title: SmarterSends
article_title: SmarterSends
description: "Este artigo de referência descreve a parceria entre a Braze e a SmarterSends, uma interface fácil de usar projetada para que até profissionais que não sejam da área de marketing possam criar, programar e implementar campanhas de e-mails alinhadas com a marca."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> A [SmarterSends](https://smartersends.com) impulsiona a personalização com campanhas de marketing que as empresas podem criar, programar e implementar para reforçar a conformidade legal e da marca com controle sobre o conteúdo e os dados usados.

_Essa integração é mantida pela SmarterSends._

## Sobre a integração {#about-the-integration}

A parceria entre a Braze e a SmarterSends permite combinar o poder da Braze com o conteúdo hiperlocalizado de propriedade de seus usuários distribuídos para elevar suas campanhas de marketing.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta SmarterSends | É necessário ter uma [conta SmarterSends](https://smartersends.com) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com estas permissões: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. Para aumentar a segurança, coloque na lista de permissões o endereço IP da SmarterSends (disponível em sua instância). |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| ID da campanha da API da Braze | O [ID da campanha da API da Braze]({{site.baseurl}}/api/api_campaigns/) é o identificador exclusivo de todas as campanhas enviadas por meio da SmarterSends. Isso pode ser criado no dashboard da Braze em **Messaging** > **Campaigns**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Com a integração da Braze e da SmarterSends, você pode tirar proveito do marketing distribuído criando e executando campanhas de marketing em vários canais e locais. Essas vantagens incluem:

1. **Maior alcance:** usar vários canais e locais para atingir um público mais amplo e direcionar clientes em diferentes locais, resultando em maior exposição da marca.
2. **Envio de mensagens direcionadas:** adaptar o envio de mensagens em todos os canais e locais para que repercutam no público local, a fim de obter uma comunicação e um engajamento mais eficazes com os clientes.
3. **Melhoria da consistência da marca:** alinhar o envio de mensagens e a imagem da sua marca em todos os canais e locais, o que é importante para a criação de uma marca forte e reconhecível.
4. **Melhores insights:** coletar dados de vários canais e locais, fornecendo insights valiosos sobre o comportamento e as preferências dos clientes, que podem ser usados para refinar as estratégias e táticas de marketing, tanto em nível local quanto global.
5. **Aumento da eficiência:** aproveitar os pontos fortes de diferentes canais e locais, o que pode resultar em um uso mais eficiente dos recursos e, ao mesmo tempo, atingir as metas de marketing desejadas.

## Integração {#integration}

### Etapa 1: Criar uma chave da API REST {#step-1-create-a-rest-api-key}

1. Na Braze, acesse **Configurações** > **Chaves de API** e clique em **Criar nova chave de API**.
2. Digite um nome para a chave de API.
3. Selecione as seguintes permissões para essa chave para permitir que a SmarterSends interaja com seu espaço de trabalho na Braze.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Adicione o endereço IP da SmarterSends à seção **Whitelist IPs**.
5. Clique em **Save API Key**.
6. Copie e cole a chave de API com as permissões apropriadas nas configurações do **Braze Email Service Provider** na SmarterSends.

### Etapa 2: Criar ou copiar um ID de aplicativo {#step-2-create-or-copy-an-application-id}

1. Em seu espaço de trabalho da Braze, acesse **Configurações** > **Configurações do app**.
2. Configure um novo app ou use o ID do aplicativo de um aplicativo existente em seu espaço de trabalho. Note que o ID do aplicativo é rotulado como **API Key**.
3. Copie e cole esse ID no campo **App ID** na SmarterSends.

### Etapa 3: Criar uma campanha de API {#step-3-create-an-api-campaign}

Uma campanha de API permite o rastreamento de métricas para todos os e-mails da SmarterSends na Braze e capacita a SmarterSends a disparar essas campanhas baseadas em API.

1. Na Braze, [crie uma campanha de API]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Clique em **Email** em **Select Message Channel** para adicionar um canal de envio de mensagens e começar a rastrear as métricas.
3. Em seguida, copie e cole o ID da campanha da Braze no campo **Campaign ID** da SmarterSends.
4. Copie e cole o ID da variante da mensagem da Braze no campo **Message Variant ID** da SmarterSends. Esse será o ID de mensagem padrão usado se você decidir não criar um ID de mensagem para cada grupo na SmarterSends.
5. Para cada grupo que você criar na SmarterSends, adicione uma variante de mensagem à sua campanha de API na Braze. Em seguida, copie o ID da variante da mensagem para o ID da variante da mensagem do grupo na SmarterSends.

{% alert tip %}
Crie um ID de variante de mensagem para cada grupo que você criar na SmarterSends para visualizar as métricas dos envios de cada grupo separadamente em seu espaço de trabalho da Braze. Isso pode ser útil para identificar tendências entre grupos ao criar relatórios na Braze.
{% endalert %}

## Personalização {#customization}

Cada instância da SmarterSends é totalmente personalizável com as cores do logotipo da sua marca e o nome de domínio personalizado, criando um ambiente familiar. Além disso, para maior personalização, é possível definir os atributos e os atributos personalizados para direcionamento de usuários em campanhas com base nos segmentos dentro do seu espaço de trabalho da Braze.