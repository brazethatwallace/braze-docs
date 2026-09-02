---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "Este artigo de referência descreve a parceria entre a Braze e a Antavo, um programa de fidelidade de última geração que vai além de recompensas por compras."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [A Antavo](https://antavo.com/) é um provedor de tecnologia de fidelidade SaaS de nível empresarial que cria programas de fidelidade abrangentes para promover o amor à marca e mudar o comportamento do cliente.

_Essa integração é mantida pela Antavo._

## Sobre a integração {#about-the-integration}

A integração entre a Antavo e a Braze permite que você use dados relacionados ao programa de fidelidade para criar campanhas personalizadas e aprimorar a experiência do cliente. A Antavo oferece suporte à sincronização de dados de fidelidade entre as duas plataformas — essa é uma sincronização de dados unidirecional apenas, da Antavo para a Braze. A integração oferece suporte ao campo `external_id` da Braze, que a Antavo usa para sincronizar o ID do membro de fidelidade.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conta Antavo | Para aproveitar essa parceria, é necessário ter uma conta [Antavo](https://antavo.com/) com a integração Braze ativada. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as seguintes permissões: `users.track`, `events.list`, `events.data_series` e `events.get`.<br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Identificador do app Braze | A chave do identificador do seu app. <br><br>Para localizar essa chave no dashboard da Braze, acesse **Configurações** > **Chaves de API or interface de programação do aplicativo (API)** e encontre a seção **Identification**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar a Braze na Antavo {#step-1-connect-braze-in-antavo}

Na Antavo, acesse **Modules** > **Braze** e clique em **Configure**. Ao navegar pela primeira vez para a página de configuração da integração da Braze na Antavo, a interface solicitará que você conecte os dois sistemas.

Forneça as seguintes credenciais:

- **Instance URL:** O endpoint REST or transferir estado representacional da Braze da instância para a qual você está provisionado.
- **API or interface de programação do aplicativo (API) Token (Identifier):** A chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze que a Antavo deve usar ao enviar solicitações para a Braze.
- **App Identifier:** O identificador do app Braze.

Depois de inserir as credenciais, clique em **Connect**.

![Tela de conexão da Braze na Antavo com URL da instância, token da API e identificador do app.]({% image_buster /assets/img/antavo/connect_braze.png %})

### Etapa 2: Configurar o mapeamento de campos {#step-2-configure-field-mapping}

Depois que a conexão for estabelecida, você será redirecionado automaticamente para a página **Sync Fields** na Antavo para configurar a sincronização de campos entre os dois sistemas. Você pode acessar essa página a qualquer momento em **Modules** > **Braze**.

Para configurar o mapeamento de campos na Antavo:

1. Clique em **Add new field** <i class="fas fa-plus" alt=""></i>.
2. Use o campo suspenso para selecionar o **Loyalty field** da Antavo que você deseja sincronizar com a Braze.
3. Informe o **Remote field** que representa o atributo personalizado equivalente na Braze no qual os dados serão preenchidos.

{% alert note %}
Você pode encontrar sua lista de atributos personalizados na Braze em **Configurações de dados** > **Atributos personalizados**. Se o campo que você inserir não estiver definido na Braze, um novo campo será gerado automaticamente com a primeira sincronização.
{% endalert %}

{:start="4"}
4. Para adicionar outros pares de campos, repita as etapas 1 a 3.
5. Para remover um campo da lista de dados sincronizados, clique em <i class="fa-solid fa-rectangle-xmark" title="Excluir"></i> no final da linha.
6. Clique em **Save**.

Quando qualquer valor dos campos configurados é alterado na Antavo, não apenas a sincronização desse valor único é disparada, mas todos os campos adicionados ao mapeamento de campos são incluídos na solicitação.

![Página Sync Fields na Antavo.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
Para minimizar o uso de pontos de dados, recomendamos mapear apenas os campos que serão acionados na Braze.
{% endalert %}

#### Tipos de dados compatíveis {#supported-data-types}

A integração é compatível com todos os [tipos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) de atributos personalizados da Braze, a saber: número (inteiro, flutuante), string, array, booleano, objeto, array de objetos e data.

![Perfil da Braze mostrando diferentes atributos personalizados.]({% image_buster /assets/img/antavo/braze_profile.png %})

Os campos de dados são preenchidos com base no mapeamento de campos configurado.

## Gatilhos {#triggers}

Além de configurar o mapeamento de campos, a integração oferece recursos adicionais por meio da ferramenta [Workflows](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) da Antavo. Todos os [tipos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) de atributos personalizados da Braze e os [tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#event-property-data-types) de propriedades de eventos personalizados também podem ser sincronizados por meio de workflows.

### Sincronizar dados de fidelidade ocasionalmente {#synchronizing-loyalty-data-occasionally}

Use essa opção se os dados não estiverem armazenados em campos de fidelidade na Antavo ou se os dados não forem adicionados à lista de campos mapeados. A sincronização dos dados solicitados é disparada quando os critérios de workflow configurados são atendidos.

Visite o guia passo a passo para saber como configurar a sincronização dos [dados de fidelidade relacionados à última compra](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase).

### Sincronizar eventos do programa de fidelidade {#synchronizing-loyalty-program-events}

Use eventos sincronizados da Antavo para inserir membros de fidelidade em Canvas da Braze baseados em ações. A integração pode sincronizar qualquer evento da Antavo (incluindo eventos de compra) que apareça na Braze como eventos personalizados.

Visite o guia passo a passo para saber como configurar a sincronização do [evento de inscrição no programa de fidelidade](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) e a sincronização do [evento de ganho de benefícios do programa de fidelidade](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!).