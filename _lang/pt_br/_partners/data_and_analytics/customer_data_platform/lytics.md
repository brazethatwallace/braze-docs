---
nav_title: Lytics
article_title: Lytics
description: "Este artigo de referência aborda a integração entre a Braze e a Lytics. A Lytics é uma plataforma empresarial de dados do cliente para profissionais de marketing, analistas e tecnólogos. Essa integração permite que as marcas sincronizem e mapeiem seus dados da Lytics diretamente na Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> A [Lytics](https://www.lytics.com/) é a CDP (CDP) preferida para a próxima geração de empresas centradas no cliente. As soluções Lytics Decision Engine, Conductor e Cloud Connect oferecem aos profissionais de marketing e às equipes de dados oportunidades de realizar resolução de identidade, orquestração e otimização de campanhas em tempo real e em conformidade com a privacidade.

_Essa integração é mantida pela Lytics._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Lytics fornece uma visão unificada dos seus clientes para possibilitar uma personalização poderosa e conduzir campanhas otimizadas usando a orquestração e as decisões de próxima melhor ação.

A integração permite que as marcas:

- Exportem públicos para a Braze diretamente da Lytics
- Enviem eventos de Campaigns ou Canvas da Braze para a Lytics em tempo real para campanhas personalizadas e para criar perfis de usuários avançados

## Casos de uso {#use-cases}

Conecte a Braze à Lytics para [importar](#importing-data-from-braze-to-lytics) atividades de e-mail, SMS e push para enriquecer os perfis de usuário da Lytics. Usando a Braze e a Lytics em conjunto, você também pode [exportar](#integration) os públicos orientados por comportamento e entre canais da Lytics para criar jornadas de clientes altamente personalizadas na Braze usando dados primários.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Lytics | É necessário ter uma conta da Lytics para aproveitar essa integração. |
| Número da conta da Lytics | É necessário um número de conta da Lytics para configurar a URL do endpoint do webhook. |
| Token da API da Lytics | Um token da REST API da Lytics com permissões de gerenciamento de dados. <br><br> Isso pode ser criado no dashboard da Lytics em **Account Settings Console** > **Access Tokens** > **Create New Token**. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissão `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Instância da Braze | Sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Entre em contato com o gerente de integração da Braze para obter essas informações se não tiver certeza. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Esta seção descreve como exportar dados da Lytics para a Braze.

### Etapa 1: Criar uma autorização {#step-1-create-an-authorization}

Na Lytics, navegue até o dashboard **Authorization** no console **Data** na barra de navegação. Selecione **Create New Authorization**, procure e selecione **Braze**.

No prompt **Configure Authorization** exibido, forneça um rótulo e uma descrição e insira sua chave da API REST e a instância da Braze. Selecione **Complete** quando terminar.

![Prompt de configuração de autorização da Lytics para a Braze com campos para rótulo, descrição, chave da API REST e instância da Braze.]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### Etapa 2: Criar um novo trabalho {#step-2-create-a-new-job}

Na Lytics, navegue até o dashboard **Jobs** no console **Data** na barra de navegação. Selecione **Create New Job**, procure e selecione **Braze**. No prompt **Select Job Type** exibido, selecione **Export Audience**.

![Prompt de seleção de tipo de trabalho da Lytics para um novo trabalho da Braze com Export Audience selecionado.]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

Em seguida, escolha uma autorização nas opções **Select Authorization**.

![Etapa de seleção de autorização da Lytics mostrando a autorização da Braze a ser usada para o trabalho de exportação.]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### Etapa 3: Configurar o trabalho {#step-3-configure-the-job}

No prompt **Configure Job**, forneça um rótulo e uma descrição opcional. Em seguida, no campo **Braze External User ID Field**, selecione o campo na Lytics que contém o ID de usuário externo da Braze (`braze_id`). A próxima etapa é a mais importante — na mesma caixa de diálogo, selecione os públicos a serem exportados para a Braze usando o seletor de públicos.

Por fim, escolha a opção preferível para a caixa de seleção **Existing Users**. Deixar essa caixa marcada adicionará usuários que já existem no público selecionado da Lytics. Se desmarcada, os usuários só serão exportados para a Braze quando entrarem ou saírem do público após o início do fluxo de trabalho.

{% alert note %}
Ao marcar essa caixa, todos os usuários existentes no público selecionado serão enviados para a Braze. Se o preço da Braze incluir pontos de dados, monitore o uso de pontos de dados adequadamente.
{% endalert %}

Selecione **Complete** quando terminar para iniciar a exportação e salvar.

![Resumo do trabalho de exportação da Lytics mostrando o controle Complete e opções para salvar ou executar a exportação de público para a Braze.]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

Depois que o trabalho de exportação for configurado, a Lytics enviará os públicos selecionados para a Braze por meio da integração nativa. A seguir, mostramos um exemplo de público com a estrutura JSON do público enviado à Braze.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Um novo usuário será criado na Braze para qualquer `external_id` incluído na exportação do público que ainda não exista na Braze.

## Importação de dados da Braze para a Lytics {#importing-data-from-braze-to-lytics}

Você pode importar dados de público da Braze para a Lytics usando os seguintes métodos:

- [Usando webhooks](#using-webhooks)
- [De um arquivo CSV](#from-a-csv-file)

### Usando webhooks {#using-webhooks}

#### Etapa 1: Criar um token da API da Lytics {#step-1-create-a-lytics-api-token}

Navegue até o menu da conta da Lytics selecionando o nome da sua conta e selecione **Access Tokens** no menu suspenso. Em seguida, selecione **Create API Token**.

![Tela de tokens de acesso da Lytics com Create API Token selecionado no menu da conta.]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

Insira um nome, uma descrição opcional e um período de expiração do token. Em seguida, ative o escopo **Data Manager** para permissões de API e selecione **Generate Token**. Copie o token e armazene-o em um local seguro.

![Permissões do token da API da Lytics com o escopo Data Manager ativado antes de gerar o token.]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### Etapa 2: Configurar a URL do webhook da Lytics {#step-2-configure-the-lytics-webhook-url}

A URL do webhook da Lytics é usada pela Braze para enviar uma mensagem para a API da Lytics a partir da Braze. Essa mensagem pode ser usada para personalizar suas campanhas na Lytics ou para enriquecer seu perfil de cliente da Lytics. Os dois parâmetros a seguir devem ser adicionados à URL do webhook da Lytics:

- Número da conta da Lytics
- Token da API da Lytics

Configure a URL do webhook da seguinte forma:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Substitua `<ACCOUNT-NUMBER>` pelo número da sua conta e `<LYTICS-API-TOKEN>` pelo token da API da Lytics.

#### Etapa 3: Criar um webhook na Braze {#step-3-create-a-webhook-on-braze}

Na Braze, crie uma nova [campanha de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook). Adicione a URL do webhook da Lytics no campo **Webhook URL**.

Após definir o tipo de solicitação (método HTTP `POST`) e configurar o restante dos detalhes do webhook, o webhook estará pronto para testes e implantação. Aqui está um exemplo de corpo da solicitação POST após a configuração do webhook na Braze:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "Alex",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@example.com",
  "braze_id": "xxxxxx"
}
```

### De um arquivo CSV {#from-a-csv-file}

Esta seção descreve como importar dados de usuários da Braze de um Segment para a Lytics.

#### Etapa 1: Criar uma autorização

Na Lytics, navegue até o dashboard **Authorization** no console **Data** na barra de navegação. Selecione **Create New Authorization**, procure e selecione **Custom Integrations**.

Selecione o tipo preferido de autorização SFTP com base nos seus requisitos comerciais e de segurança. Os seguintes tipos de autorização são compatíveis com a importação de arquivos para a Lytics via SFTP:

- Autorização do servidor SFTP do cliente
- Autorização do servidor SFTP do cliente com chave privada PGP
- Autorização do servidor SFTP gerenciado da Lytics

As autorizações SFTP de chave pública são apenas para exportação SFTP.

![Opções de método de autorização SFTP da Lytics para importação de Custom Integrations, incluindo opções de servidor do cliente e gerenciado pela Lytics.]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

No prompt **Configure Authorization** exibido, forneça um rótulo e uma descrição e preencha o restante dos requisitos de configuração. Selecione **Complete** quando terminar.

#### Etapa 2: Exportar seus dados de Segment para CSV {#step-2-export-your-segment-data-to-csv}

Na Braze, navegue até **Público** > **Segments**. Localize o Segment que deseja exportar e selecione <i class="fas fa-gear" aria-label="Configurações"></i> e, em seguida, **Exportar dados de usuários em CSV**. É possível exportar até 500.000 usuários em um Segment. Para obter detalhes, consulte [Exportação de dados de Segment para CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

#### Etapa 3: Configurar um trabalho de importação de CSV {#step-3-configure-a-csv-import-job}

Na Lytics, navegue até o dashboard **Jobs** no console **Data** na barra de navegação. Selecione **Create New Job**, procure e selecione **Custom Integrations**.

Em seguida, selecione o tipo de trabalho. Para importar arquivos CSV da Braze para a Lytics, selecione **Import CSV** como o tipo de trabalho.

![Configuração de trabalho de Custom Integrations da Lytics com Import CSV selecionado como tipo de trabalho.]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

Por fim, insira um rótulo e uma descrição opcional para o trabalho e configure outros detalhes necessários. Selecione **Complete** para iniciar e salvar o trabalho.