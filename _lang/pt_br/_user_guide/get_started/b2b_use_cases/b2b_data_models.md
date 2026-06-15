---
nav_title: Modelos de dados
article_title: Criar um modelo de dados B2B
page_order: 0
page_type: reference
description: "Saiba como usar as ferramentas de dados da Braze para criar modelos B2B."
---

# Criar um modelo de dados B2B {#create-a-b2b-data-model}

> Este caso de uso demonstra como você pode usar as ferramentas de dados da Braze para criar um modelo de dados B2B eficaz e eficiente que ajude a segmentar, disparar, personalizar e enviar mensagens para seus usuários comerciais.

{% alert note %}
Essas recomendações podem mudar com o tempo, à medida que a Braze desenvolve seus recursos B2B.
{% endalert %}

Antes de falarmos sobre como configurar seu modelo de dados B2B, vamos abordar alguns conceitos e termos que você deve conhecer.

Há quatro objetos principais de B2B necessários para executar campanhas B2B.

| Objeto | Descrição |
| --- | --- |
| Leads | Um registro de clientes potenciais que demonstraram interesse em um produto ou serviço, mas ainda não foram qualificados como uma oportunidade. |
| Contatos | Normalmente, indivíduos que foram qualificados e convertidos de lead em contato para buscar uma oportunidade de vendas. |
| Oportunidades | Um registro que rastreia os detalhes de uma possível venda ou de um negócio em andamento. |
| Contas | Um registro de uma organização que é um cliente potencial qualificado, um cliente existente, um parceiro ou um concorrente com um relacionamento de importância semelhante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Criar um modelo de dados B2B" }

Na Braze, esses quatro objetos são combinados e reduzidos a dois: perfis de usuário e objetos de negócios.

| Objeto B2B da Braze | Descrição | Objetos B2B originais  |
| --- | --- | --- |
| Perfis de usuário | Mapeiam diretamente para leads e contatos no seu sistema CRM de vendas. Como os leads são capturados pela Braze, eles são automaticamente criados como leads no seu sistema CRM de vendas. Quando são convertidos em contatos, os IDs e os detalhes dos contatos são sincronizados de volta para a Braze. | Leads<br> Contatos |
| Objetos de negócios | Mapeiam qualquer objeto que não seja de usuário no seu sistema CRM de vendas. Isso inclui objetos específicos de vendas, como objetos de conta e objetos de oportunidade. | Contas<br> Oportunidades |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Criar um modelo de dados B2B" }

## Etapa 1: Crie seus objetos de negócios na Braze {#step-1-create-your-business-objects-in-braze}

Objetos de negócios são qualquer conjunto de dados não centrado no usuário. Em um contexto B2B, isso inclui dados de contas e oportunidades, além de qualquer outro conjunto de dados pertinente não centrado no usuário que sua empresa rastreia.

Há dois métodos para criar e gerenciar seus objetos de negócios na Braze: catálogos e fontes conectadas.

| Método | Descrição |
| --- | --- |
| [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) | São objetos de dados independentes (objetos de dados suplementares) no perfil de usuário principal na Braze. Em um contexto B2B, você provavelmente teria catálogos para suas contas e oportunidades. |
| [Fontes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) | Permitem que a Braze consulte diretamente seu data warehouse. É provável que você já esteja sincronizando regularmente seus objetos de lead, contato, oportunidade e conta com o data warehouse. Assim, você pode apontar a segmentação da Braze diretamente para esse data warehouse e ativá-la em um ambiente de cópia zero. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Crie seus objetos de negócios na Braze" }

{% tabs %}
{% tab Catalogs %}

### Opção 1: Usar catálogos para contas e oportunidades {#option-1-use-catalogs-for-accounts-and-opportunities}

Os catálogos são tabelas de dados hospedadas e gerenciadas na Braze. Embora os dados de contas e oportunidades sejam originários do sistema CRM de vendas de sua escolha, você os duplicaria na Braze para fins de marketing: segmentação baseada em contas, marketing baseado em contas, gerenciamento de leads e muito mais.

Para essa opção, recomendamos criar um catálogo para suas contas e outro para suas oportunidades, atualizando-os com frequência por meio da nossa [API de catálogos]({{site.baseurl}}/api/endpoints/catalogs/) ou da [Ingestão de dados na nuvem (CDI) de catálogos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/). Ao criar esses catálogos, certifique-se de que o `id` (primeira coluna) do seu catálogo corresponda ao `id` no seu sistema CRM de vendas.

#### Mapeie seus campos de CRM {#map-over-your-crm-fields}

As tabelas abaixo incluem alguns exemplos de campos que você pode mapear a partir dos objetos de conta e oportunidade do seu CRM.

{% subtabs %}
{% subtab Account catalog %}

Neste caso de uso, o Salesforce é o sistema CRM de exemplo. Você pode mapear qualquer campo incluído nos objetos do seu CRM.

<table aria-label="Mapeie seus campos de CRM" border="1">
  <caption>Mapeie seus campos de CRM</caption>
  <thead>
  <tr>
    <th><b>Objeto da Braze</b></th>
    <th><b>Campo da Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo CRM (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Catálogo &gt; Catálogo de contas</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tbody>
</table>

##### Exemplo de tabela de campos de conta mapeados {#example-table-of-mapped-account-fields}

![Tabela de contas do Salesforce com as respectivas informações, como endereço de cobrança e proprietário da conta.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

Neste caso de uso, o Salesforce é o sistema CRM de exemplo. Você pode mapear qualquer campo incluído nos objetos do seu CRM.

<table aria-label="Exemplo de tabela de campos de conta mapeados" border="1">
  <caption>Exemplo de tabela de campos de conta mapeados</caption>
  <thead>
  <tr>
    <th><b>Objeto da Braze</b></th>
    <th><b>Campo da Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo CRM (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Catálogo &gt; Catálogo de oportunidades</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
  </tbody>
</table>

##### Exemplo de tabela de campos de oportunidade mapeados {#example-table-of-mapped-opportunity-fields}

![Tabela de oportunidades do Salesforce com as respectivas informações, como endereço de cobrança e proprietário da conta.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Opção 2: Usar fontes conectadas para contas e oportunidades {#option-2-use-connected-sources-for-accounts-and-opportunities}

Fontes conectadas são tabelas de dados hospedadas por você no seu próprio data warehouse e consultadas pelas [Extensões de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) da Braze. Ao contrário dos catálogos, em vez de duplicar seus objetos de negócios (contas e oportunidades) na Braze, você os manteria no seu data warehouse e o usaria como fonte da verdade.

Para configurar fontes conectadas, consulte [Integração de fontes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Etapa 2: Relacione seus objetos de negócios aos perfis de usuário {#step-2-relate-your-business-objects-to-user-profiles}

Os perfis de usuário são o objeto principal na Braze, responsáveis pela maior parte da segmentação demográfica, disparo e personalização. Os perfis de usuário incluem [dados de usuário padrão]({{site.baseurl}}/user_guide/data/unification/user_data/) coletados pelo nosso SDK e outras fontes, além de [dados personalizados]({{site.baseurl}}/user_guide/data/activation/), que podem ser atributos (dados demográficos), eventos (dados comportamentais) ou compras (dados transacionais).

### Etapa 2.1: Mapear IDs do CRM de vendas para a Braze {#step-21-map-sales-crm-ids-to-braze}

Primeiro, certifique-se de que a Braze e o CRM de sua escolha tenham um identificador comum para compartilhar dados. Sugerimos usar a tabela a seguir para mapear os campos de ID do CRM de vendas de volta para o objeto de usuário da Braze. A tabela abaixo usa o Salesforce como sistema CRM, mas isso pode ser feito com qualquer CRM.

#### Objeto da Braze: Usuário {#braze-object-user}

| Campo da Braze | Objeto CRM (Salesforce) | Campo CRM (Salesforce) | Informações adicionais |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` | - Rótulo de alias de usuário: `salesforce_lead_id` <br>- Nome do alias de usuário: `lead_id` |
| `Aliases.salesforce_contact_id` | Contato | `id` | - Rótulo de alias de usuário: `salesforce_contact_id` <br>- Nome do alias de usuário: `contact_id` |
| `AccountId` | Contato | `AccountId` |
| `OpportunityId` (opcional, escalar) <br>ou<br> `Opportunities` (opcional, array) | Oportunidade | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objeto da Braze: Usuário" }

{% alert note %}
Recomendamos o uso de [aliases]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases) em vez de `external_id` para mapear os identificadores de leads e contatos do Salesforce de volta para a Braze. Isso reduz a quantidade de buscas necessárias ao identificar e executar suas iniciativas de crescimento orientado pelo produto.
{% endalert %}

Depois de sincronizar seus IDs, é necessário relacionar os perfis de usuário da Braze com seus objetos de negócios.

### Etapa 2.2: Crie um relacionamento entre os perfis de usuário e seus objetos de negócios {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab Catalogs %}

#### Opção 1: Ao usar catálogos {#option-1-when-using-catalogs}

Agora que os detalhes de oportunidade e conta estão registrados como catálogos da Braze, é necessário criar um relacionamento entre esses catálogos e os perfis de usuário para os quais você deseja enviar mensagens. Atualmente, isso requer duas etapas:

1. Inclua a conta (como `account_id (string)`), o ID da oportunidade (como `opportunity_ids (array)`) ou ambos no perfil do usuário como atributos.
2. Registre um evento (como `account_linked`) que inclua o ID da conta como uma propriedade do evento.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### Opção 2: Ao usar fontes conectadas {#option-2-when-using-connected-sources}

Uma das tabelas da sua fonte conectada deve incluir um `user_id` que corresponda ao `external_user_id` definido na Braze para seus usuários. A configuração do perfil de usuário acima usa seus IDs de lead e `contact_ids` como `external_id`, portanto, você deve garantir que suas tabelas de lead/contato incluam esses IDs.

Além de garantir a correspondência dos IDs, recomendamos gravar dados básicos no nível da conta, como `account_id`, `opportunity_id` e até mesmo atributos firmográficos comuns, como `industry`, nos perfis de usuário para uma segmentação e personalização eficientes.

{% endtab %}
{% endtabs %}