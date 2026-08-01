---
nav_title: Objetos de conta
article_title: Objetos de conta
page_type: reference
permalink: /account_object/
hidden: true
description: "Saiba como usar objetos de conta para criar segmentos de usuários com base na conta à qual pertencem e, em seguida, enviar mensagens personalizadas usando Liquid tags."
---

# Objetos de conta {#account-objects}

> Saiba como usar objetos de conta para criar segmentos de usuários com base na conta à qual pertencem e, em seguida, enviar mensagens personalizadas usando Liquid tags.

Para importar dados de conta, use um [arquivo CSV](#using-a-csv-file) ou a API da Braze. Usando a API da Braze, você pode [criar várias contas](#create-multiple-accounts), [criar uma conta](#create-one-account), [excluir várias contas](#delete-multiple-accounts) e [excluir uma conta](#delete-one-account).

| Público | Como você usará este artigo |
|----------|----------------------------|
| Profissionais de marketing | Importar dados de usuários e contas usando CSV, criar segmentos com base em atributos de conta e personalizar mensagens com informações de conta na Braze. |
| Desenvolvedores | Usar a REST API da Braze para criar, atualizar e excluir registros de conta de forma programática e manter a Braze sincronizada com seus dados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Os objetos de conta estão atualmente em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em participar deste beta.
{% endalert %}

## Como funciona {#how-it-works}

Objetos de conta são estruturas de dados personalizadas que representam a empresa de um usuário. Eles se conectam a perfis de usuário, permitindo que você crie Segments no estilo B2B e personalize mensagens. Use campos de conta como nome da empresa, setor, cargo ou status do negócio com catálogos da Braze, filtros de segmentação e Liquid tags.

Por exemplo, você pode direcionar usuários que trabalham na área de saúde e enviar mensagens personalizadas para médicos e administradores hospitalares, tornando sua mensagem ainda mais relevante.

Para usar objetos de conta, você importa três tipos de dados para a Braze:

- **Dados de usuários:** Perfis de usuário individuais usados para identificar cada pessoa na Braze (por exemplo, via `external_id`, e-mail, telefone ou alias de usuário). Importe dados de usuários via CSV.
- **Dados de relacionamento usuário-conta:** O relacionamento entre um usuário e uma conta, incluindo a qual empresa ele pertence e o cargo que ocupa nessa conta. Importe esses dados de relacionamento via CSV.
- **Dados de conta:** Os próprios registros da empresa, como nome da empresa, setor, receita anual e outros detalhes firmográficos. Esses são os registros que você usa para direcionamento e personalização em Segments e mensagens. Importe dados de conta via CSV ou pela REST API da Braze.

Os três tipos de dados precisam ser importados para que os objetos de conta funcionem. Os dados de usuários identificam pessoas na Braze, os dados de relacionamento usuário-conta conectam esses usuários a contas e cargos específicos, e os dados de conta fornecem os atributos no nível da empresa usados para segmentação e personalização.

## Pré-requisitos {#prerequisites}

Antes de usar esse recurso, você já deve ter usuários na Braze.

## Importar dados para a Braze {#import-data-to-braze}

Para usar objetos de conta nas suas mensagens, os dados de usuários já devem existir na Braze. A partir daí, conclua duas importações: primeiro, importe os dados de relacionamento usuário-conta para estabelecer associações e funções de conta (atualmente apenas via CSV). Em seguida, importe os dados da conta com os detalhes no nível da empresa usados para segmentação e personalização (via CSV ou REST API da Braze).

### Etapa 1: Importar dados de relacionamento usuário-conta {#step-1-import-user-account-relationship-data}

Primeiro, importe os dados de relacionamento usuário-conta para a Braze como um arquivo CSV com os campos a seguir. Isso ajuda a Braze a associar os usuários existentes às contas e funções corretas.

<style>
table td {
    word-break: break-word;
}
</style>

| Nome do campo    | Tipo do campo | Obrigatório | Descrição                                                                                           |
|------------------|---------------|-------------|-------------------------------------------------------------------------------------------------------|
| `account_id`       | String     | Sim      | A conta à qual o usuário pertence. É o mesmo que o campo `id` do objeto de conta (ID do CRM). |
| `external_id`      | String     | Sim      | O [ID externo](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) do usuário na Braze. |
| `user_alias_name`  | String     | Não*      | O [nome de alias](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases) do usuário na Braze. |
| `user_alias_label` | String     | Não*      | O [rótulo de alias](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users) do usuário na Braze. |
| `email`            | String     | Não*     | O endereço de e-mail do usuário. |
| `phone`            | String     | Não*      | O número de telefone do usuário. |
| `user_role`             | String     | Não       | A função que o usuário exerce na conta, como "diretor" ou "colaborador". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
<sup>Um dos campos `external_id`, `email`, `phone` ou `user_alias` é necessário para identificar um usuário.</sup>

#### Usando um arquivo CSV {#using-a-csv-file}

Faça upload do seu CSV com os relacionamentos usuário-conta para a Braze:

1. Acesse **Data Settings** > **Accounts**.
2. Selecione **Update data**.
3. Em **CSV upload**, selecione **Users** e faça upload do seu arquivo para a Braze.

![O menu suspenso "Upload data" na página "Accounts" na Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Etapa 2: Importar dados da conta {#step-2-import-account-data}

Contas são empresas às quais seus usuários pertencem. Importe os dados da conta para a Braze como um arquivo CSV com os campos a seguir. Lembre-se de que cada conta deve ter um ID e um nome atribuídos.

<style>
table td {
    word-break: break-word;
}
</style>

| Nome do campo                 | Tipo do campo | Obrigatório | Descrição                                                                        |
|-----------------------------|---------------|-------------|------------------------------------------------------------------------------------|
| `id`                          | String     | Sim      | O ID da conta na sua plataforma de gestão de relacionamento com o cliente (CRM). |
| `name`                        | String     | Sim      | O nome da conta.                                                                |
| `type`                        | String     | Não       | O tipo de conta, como cliente, parceiro ou revendedor.                                                                                   |
| `annual_revenue`              | String     | Não       | Receita anual da conta.                                                      |
| `industry`                    | String     | Não       | Setor no qual a conta opera.                                             |
| `number_of_employees`         | String     | Não       | Número de colaboradores, com suporte para faixas.                                           |
| `address`                     | String     | Não       | Endereço da conta.                                                      |
| `city`                        | String     | Não       | Cidade onde a conta está localizada.                                                  |
| `state`                       | String     | Não       | Estado onde a conta está localizada.                                                 |
| `postal_code`                 | String     | Não       | CEP do endereço da conta.                                              |
| `country`                     | String     | Não       | País onde a conta está localizada.                                               |
| `notes`                       | String     | Não       | Notas adicionais sobre a conta.                                                 |
| `website`                     | String     | Não       | URL do website da conta.                                                        |
| `main_phone`                  | String     | Não       | Número de telefone principal da conta.                                                  |
| `created_date`                | Time       | Não       | Data em que a conta foi criada.                                                  |
| `account_owner_email_address` | String     | Não       | Um proprietário interno da conta (como "Tom da equipe de vendas da Empresa A é responsável pela Empresa B").      |
| `parent_account_id`           | String     | Não       | ID da conta principal, se aplicável (como vincular ao ID de uma empresa controladora). |
| `sic_code`                    | String     | Não       | Código de classificação industrial padrão.                                              |
| Campos personalizados         | N/A        | Não       | Campos personalizados definidos e gerenciados por você.                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
{% alert note %}
Embora alguns campos sejam opcionais, inclua-os sempre que possível, pois são nomes de campos reservados e ajudam a manter seus dados organizados.
{% endalert %}

Em seguida, importe os dados da conta para a Braze fazendo upload de um arquivo CSV ou usando a REST API da Braze. Você pode visualizar esses dados em **Data Settings**. Não é possível editar esses dados no editor do navegador.

#### Usar um arquivo CSV

Para importar seus dados via CSV:

1. Acesse **Data Settings** > **Accounts**.
2. Selecione **Update data**.
3. Em **CSV upload**, selecione **Account Data** e faça upload do seu arquivo para a Braze.

![O menu suspenso "Upload data" na página "Accounts" na Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Solução de problemas em importações de CSV {#troubleshooting-csv-imports}

#### Linhas vazias em importações de CSV de objetos de conta {#empty-rows-in-account-objects-csv-imports}

Se você importar dados de objetos de conta e encontrar linhas vazias na página **Accounts**, verifique se os valores dos campos de conta contêm vírgulas.

Nas importações de CSV de objetos de conta, vírgulas nos valores podem ser interpretadas como separadores. Isso pode fazer com que os valores sejam analisados incorretamente e resultem em linhas vazias no dashboard.

Para corrigir esse problema, remova as vírgulas do arquivo CSV original e faça o upload novamente. Por exemplo, altere `"$5,000,000"` para `"$5000000"` ou `"$5 million"` antes de reenviar.

## Usar a API da Braze {#using-the-braze-api}

APIs (interfaces de programação de aplicativo) permitem que diferentes sistemas de software se comuniquem de forma programática. Quando você interage com a API da Braze, você envia solicitações HTTP para endpoints específicos. Endpoints são URLs estruturadas que aceitam instruções e retornam respostas. O método HTTP informa à Braze qual ação executar, e o corpo da solicitação contém os dados.

Para gerenciamento de contas, a API da Braze usa estes métodos HTTP:

| Método | Finalidade | Comportamento |
|--------|---------|----------|
| `PUT` | Criar ou atualizar recursos | Adiciona um novo registro de conta se não existir. Atualiza o registro existente se já houver um. `PUT` é projetado para ser idempotente, então você pode sincronizar os mesmos dados várias vezes sem criar duplicatas. |
| `DELETE` | Remover recursos | Remove permanentemente o registro de conta especificado e suas associações da Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

A API da Braze oferece controle programático sobre dados de conta em escala. Você pode automatizar fluxos de trabalho de gerenciamento de contas, sincronizar informações de conta diretamente das suas fontes de dados e manter a Braze alinhada com sua fonte de verdade sem uploads ou edições manuais. Isso ajuda a reduzir a sobrecarga operacional e manter dados de conta precisos e atualizados para segmentação e personalização.

Para saber mais sobre métodos HTTP e como REST APIs funcionam, consulte os seguintes recursos:
- [Métodos de solicitação HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) no MDN Web Docs
- [Tutorial de REST API](https://restapitutorial.com/)
- [Visão geral da API da Braze]({{site.baseurl}}/api/basics)

{% alert note %}
Use uma chave de API com permissões de catálogos para autenticar solicitações ao endpoint `/business/accounts`.
{% endalert %}

Esta seção aborda como usar a API da Braze para:
- [Criar várias contas](#create-multiple-accounts)
- [Criar uma conta](#create-one-account)
- [Excluir várias contas](#delete-multiple-accounts)
- [Excluir uma conta](#delete-one-account)

### Criar várias contas {#create-multiple-accounts}

Como `PUT` é idempotente, você pode enviar a mesma solicitação várias vezes e a Braze atualiza os registros existentes em vez de criar duplicatas. Isso o torna uma escolha confiável para manter os registros de conta na Braze atualizados.

O trecho de código a seguir envia uma solicitação `PUT` para o endpoint `/business/accounts`. O array `accounts` contém vários objetos de empresa, cada um mapeado para os campos de conta definidos na [Etapa 2: Importar dados de conta](#step-2-import-account-data). A Braze processa cada objeto e cria ou atualiza o registro correspondente na sua página **Accounts**. Essa operação é assíncrona. A Braze enfileira a solicitação e a processa em segundo plano, tornando-a adequada para importações em massa onde a confirmação imediata não é necessária.

Para criar várias contas, envie uma solicitação `PUT` para `/business/accounts`. Se uma conta não existir, a Braze adiciona um novo item na página **Accounts**. Cada solicitação pode suportar até 50 contas. Essa operação é assíncrona.

Sua solicitação deve ser semelhante à seguinte:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
          "accounts": [
              {
                  "id": "ACC001",
                  "name": "Acme Corporation",
                  "type": "Customer",
                  "annual_revenue": "$5,000,000",
                  "industry": "Manufacturing",
                  "number_of_employees": "150",
                  "address": "123 Industrial Way",
                  "city": "Metropolis",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA",
                  "notes": "Key client in the manufacturing sector",
                  "website": "http://www.acme.com",
                  "main_phone": "+1-212-555-1234",
                  "created_date": "2023-01-15T09:30:00Z",
                  "account_owner_email_address": "owner@example.com",
                  "parent_account_id": "",
                  "sic_code": "2011"
              },
              {
                  "id": "ACC002",
                  "name": "Global Solutions",
                  "type": "Partner",
                  "annual_revenue": "$10,000,000",
                  "industry": "Technology",
                  "number_of_employees": "500",
                  "address": "456 Tech Park",
                  "city": "Silicon Valley",
                  "state": "CA",
                  "postal_code": "94043",
                  "country": "USA",
                  "notes": "Important partner for software solutions",
                  "website": "http://www.globalsolutions.com",
                  "main_phone": "+1-650-555-5678",
                  "created_date": "2023-02-20T14:45:00Z",
                  "account_owner_email_address": "partner@example.com",
                  "parent_account_id": "ACC001",
                  "sic_code": "7372"
              },
              {
                  "id": "ACC003",
                  "name": "Oceanic Ventures",
                  "type": "Customer",
                  "annual_revenue": "$3,200,000",
                  "industry": "Retail",
                  "number_of_employees": "75",
                  "address": "789 Ocean Blvd",
                  "city": "Miami",
                  "state": "FL",
                  "postal_code": "33101",
                  "country": "USA",
                  "notes": "Expanding presence in retail markets",
                  "website": "http://www.oceanicventures.com",
                  "main_phone": "+1-305-555-6789",
                  "created_date": "2023-03-05T08:15:00Z",
                  "account_owner_email_address": "contact@example.com",
                  "parent_account_id": "",
                  "sic_code": "5941"
              }
          ]
      }'
```

### Criar uma conta {#create-one-account}

Assim como na criação de várias contas, essa operação usa o método `PUT`. A diferença é que o ID da conta é incluído diretamente na URL do endpoint em vez do corpo da solicitação. Isso oferece controle preciso sobre um único registro.

O trecho de código a seguir envia uma solicitação `PUT` para `/business/accounts/ACC001`, onde `ACC001` é o identificador único da conta. Essa operação é síncrona. A Braze processa a solicitação imediatamente e retorna uma resposta assim que é concluída. Isso é adequado para integrações em tempo real. Por exemplo, quando as informações de uma conta mudam no seu sistema, você pode refletir essa atualização na Braze imediatamente para direcionamento ou personalização.

Para criar uma conta, envie uma solicitação `PUT` para `/business/accounts/:account_id`. Se a conta não existir, a Braze cria um novo registro de conta. Essa operação é síncrona.

Sua solicitação deve ser semelhante à seguinte:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "accounts": [
            {
                "name": "Braze",
                "type": "Customer",
                "annual_revenue": "$5,000,000",
                "industry": "Manufacturing",
                "number_of_employees": "150",
                "address": "123 Industrial Way",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "notes": "Key client in the manufacturing sector",
                "website": "http://www.acme.com",
                "main_phone": "+1-212-555-1234",
                "created_date": "2023-01-15T09:30:00Z",
                "account_owner_email_address": "owner@example.com",
                "parent_account_id": "",
                "sic_code": "2011"
            }
        ]
      }'
```

### Excluir várias contas {#delete-multiple-accounts}

O método `DELETE` remove registros de conta da Braze. Diferentemente do `PUT`, as solicitações `DELETE` não são reversíveis. Uma vez que uma conta é excluída, a associação entre os usuários e essa conta é removida.

O trecho de código a seguir envia uma solicitação `DELETE` para `/business/accounts` com uma lista de IDs de conta no corpo da solicitação. A Braze processa cada ID e remove o registro de conta correspondente. Essa operação é assíncrona. A Braze enfileira as remoções e as processa em segundo plano. Use isso para tarefas de limpeza em massa, como quando um grupo de contas sofreu churn, foi consolidado ou não é mais relevante para segmentação na Braze.

Para excluir várias contas, envie uma solicitação `DELETE` para `/business/accounts` com um corpo contendo uma lista de IDs de conta. Essa operação é assíncrona.

Sua solicitação deve ser semelhante à seguinte:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "accounts": [
      { "id": "ACC001" },
      { "id": "ACC002" },
      { "id": "ACC003" }
    ]
  }'
```

### Excluir uma conta {#delete-one-account}

Assim como na criação de uma conta, essa operação direciona uma conta específica incluindo seu ID diretamente na URL do endpoint. Isso oferece controle preciso sobre um único registro sem afetar os demais.

O trecho de código a seguir envia uma solicitação `DELETE` para `/business/accounts/ACC001`. Essa operação é síncrona. A Braze processa a solicitação imediatamente e retorna uma resposta assim que é concluída. Use isso quando uma conta individual é encerrada, mesclada ou precisa ser removida da Braze por motivos de conformidade ou higiene de dados.

Para excluir uma única conta, envie uma solicitação `DELETE` para `/business/accounts/:account_id`. Essa operação é síncrona.

Sua solicitação deve ser semelhante à seguinte:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY"
```

## Usando objetos em mensagens {#using-objects-in-messages}

Depois de [importar seus dados para a Braze](#importing-data-to-braze), você pode usar objetos de conta para criar um Segment e enviar mensagens personalizadas aos usuários usando Liquid.

### Etapa 1: Criar um Segment {#step-1-build-a-segment}

Em seguida, crie um Segment que combine dados de usuários e dados de contas. Neste exemplo, você direciona diretores de empresas de saúde para aumentar as inscrições em um novo webinar da sua empresa de promoção de saúde.

1. Acesse **Público** > **Segments** e selecione **Criar Segment**.
2. Dê um nome ao seu Segment.
3. No **Criador de segmentos**, selecione o filtro **Business** e configure os seguintes filtros de segmentação. Quando terminar, selecione **Salvar**.

| Filtro                          | Descrição                                        |
|---------------------------------|--------------------------------------------------|
| `Role is exactly director`      | Direciona usuários cujo cargo é especificamente Diretor |
| `Accounts industry matches regex healthcare` | Corresponde a usuários em contas com setores relacionados à saúde |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Atualmente, para usar vários filtros de conta, selecione **Add Criteria** em vez de usar o menu suspenso **OR/AND**.
{% endalert %}

![Filtros de segmentação configurados para criar um Segment para usuários que são diretores em empresas de saúde.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/build_segment.png %})

{% alert note %}
A segmentação funciona apenas nos primeiros 1.000 registros de conta que correspondem aos critérios. Você pode ter até um filtro de negócios por Segment, e todos os critérios devem estar em um único filtro.
{% endalert %}

### Etapa 2: Usar Liquid para personalizar {#step-2-use-liquid-to-personalize}

Agora você pode personalizar sua mensagem para enviar aos usuários informações sobre oportunidades. Neste exemplo, redija uma mensagem para seus diretores e inclua um link para o webinar. Você também pode usar um catálogo da Braze para buscar imagens específicas do setor para personalização.

#### Etapa 2.1: Personalizar com informações da conta {#step-21-personalize-with-account-information}

Selecione **Business** como o tipo de personalização e, em seguida, selecione **Name** para personalizar a mensagem com o nome da empresa do usuário.

O seguinte é copiado para a área de transferência.

{% raw %}
```javascript
{% business %}
{{ business_accounts[0].name }}
```
{% endraw %}

A Braze gera a tag {% raw %}`{% business %}`{% endraw %}, que define um array chamado `business_accounts` contendo informações da conta associada.

Ajuste a saída gerada automaticamente para criar sua mensagem.

No exemplo a seguir, mova a chamada à tag {% raw %}`{% business %}`{% endraw %} para o topo da mensagem e personalize com o nome do usuário. Use o nome da conta para personalizar a mensagem. A saída do Liquid permanece a mesma, mas você a posiciona em diferentes partes da mensagem.

{% raw %}
```javascript
{% business %}

Hi {{${first_name}}},

We would love to invite you and your peers at {{ business_accounts[0].name }} to join our latest webinar named "Creating Optimal Health Outcomes for Patients".  Click the link below to register.
```
{% endraw %}

A saída é semelhante ao seguinte:

{% raw %}
```javascript
Hi John,

We would love to invite you and your peers at Sunshine Health to join our latest webinar named "Creating Optimal Health Outcomes for Patients". Click the link below to register.
```
{% endraw %}

#### Etapa 2.2: Conectar com catálogos {#step-22-connect-with-catalogs}

Em seguida, personalize ainda mais sua mensagem usando catálogos da Braze para adicionar e armazenar uma imagem que corresponda à empresa de saúde.

Para este exemplo, suponha que você tenha o seguinte:

- Um catálogo configurado chamado `industry_assets`
- O ID de cada entrada do catálogo é o nome de um setor que corresponde aos setores nas suas contas
- Os links de URL de imagem para uma imagem principal e uma imagem secundária.

A seguir, um exemplo do Liquid usado para essa personalização.
{% raw %}
```javascript
//Make a call to the business tag.  This sets the accounts array and prepares us to pull account data out.
{% business %}

//Assign the user's accounts industry to a variable called industry.  This step isn't required but it makes everything easier to read.
{% assign industry = {{business_accounts[0].industry}} %}

//Make a catalog_items call to the industry_assets catalog and ask for the industry item (in this case, it will ask for "healthcare")
{% catalog_items industry_assets industry %}

// Get the hero image for the "healthcare" industry
{{items[0].hero_image}}
```
{% endraw %}

## Perguntas frequentes (FAQ) {#faq}

### Posso adicionar campos personalizados? {#can-i-add-custom-fields}

Sim. Você pode adicionar campos personalizados às contas. Se você tem seu próprio método de pontuação de leads, também pode usar um campo personalizado no seu objeto de conta para rastrear isso.

### Um usuário pode ser associado a mais de uma conta? {#can-a-user-be-associated-with-more-than-one-account}

Não. Atualmente, cada usuário pode ter apenas uma associação de conta.

### Um perfil de usuário pode conter vários e-mails? {#can-one-user-profile-contain-multiple-emails}

Não. Um perfil de usuário não pode ter mais de um e-mail, como um e-mail pessoal e um profissional.