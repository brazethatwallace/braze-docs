---
nav_title: Modelos de dados
article_title: Criar um modelo de dados B2B
page_order: 0
page_type: reference
description: "Saiba como usar as ferramentas de dados da Braze para criar modelos B2B."
---

# Criar um modelo de dados B2B {#create-a-b2b-data-model}

> Este caso de uso demonstra como você pode usar as ferramentas de dados da Braze para criar um modelo de dados B2B eficaz e eficiente que ajude a direcionar, disparar, personalizar e enviar mensagens para seus usuários comerciais.

{% alert note %}
Essas recomendações podem mudar com o tempo, à medida que a Braze desenvolve seus recursos B2B.
{% endalert %}

Antes de falarmos sobre como configurar seu modelo de dados B2B, vamos abordar vários conceitos e termos que você deve conhecer.

Há quatro objetos principais de B2B que você precisa para executar campanhas de B2B.

| Objeto | Descrição |
| --- | --- |
| Leads | Um registro de clientes potenciais que demonstraram interesse em um produto ou serviço, mas ainda não foram qualificados como uma oportunidade. |
| Contatos | Normalmente, indivíduos que foram qualificados e convertidos de lead em contato para buscar uma oportunidade de vendas. |
| Oportunidades | Um registro que rastreia os detalhes de uma possível venda ou de um negócio em andamento. |
| Contas | Um registro de uma organização que é um cliente potencial qualificado, um cliente existente, um parceiro ou um concorrente que tem um relacionamento de importância semelhante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Criar um modelo de dados B2B" }

Na Braze, esses quatro objetos são combinados e reduzidos a dois objetos: perfis de usuário e objetos de negócios.

| Objeto B2B da Braze | Descrição | Objetos B2B originais  |
| --- | --- | --- |
| Perfis de usuário | Eles são mapeados diretamente para leads e contatos em seu sistema CRM de vendas. Como os leads são capturados pela Braze, eles são automaticamente criados como leads em seu sistema de CRM de vendas. À medida que são convertidos em contatos, os IDs e os detalhes dos contatos são sincronizados de volta à Braze. | Leads<br> Contatos |
| Objetos de negócios | Eles mapeiam qualquer objeto que não seja de usuário no seu sistema CRM de vendas. Isso inclui seus objetos específicos de vendas, como objetos de conta e objetos de oportunidade. | Contas<br> Oportunidades |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Criar um modelo de dados B2B" }

## Etapa 1: Crie seus objetos de negócios na Braze {#step-1-create-your-business-objects-in-braze}

Objetos de negócios são qualquer conjunto de dados não centrado no usuário. Em um contexto B2B, isso inclui os dados de contas e oportunidades e qualquer outro conjunto de dados pertinente não centrado no usuário que sua empresa rastreia.

Há dois métodos para criar e gerenciar seus objetos de negócios na Braze: catálogos e fontes conectadas.

| Método | Descrição |
| --- | --- |
| [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) | São objetos de dados independentes (objetos de dados suplementares) no perfil do usuário principal na Braze. Em um contexto B2B, você provavelmente teria catálogos para suas contas e oportunidades. |
| [Fontes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) | Isso permite que a Braze consulte diretamente seu data warehouse. É provável que você já esteja sincronizando regularmente seus objetos de lead, contato, oportunidade e conta com o data warehouse, de modo que possa apontar a segmentação da Braze diretamente para esse data warehouse e ativá-la em um ambiente de cópia zero. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Crie seus objetos de negócios na Braze" }

{% tabs %}
{% tab Catalogs %}

### Opção 1: Usar catálogos para contas e oportunidades {#option-1-use-catalogs-for-accounts-and-opportunities}

Os catálogos são tabelas de dados hospedadas e gerenciadas na Braze. Embora os dados de contas e oportunidades sejam originários do sistema de CRM de vendas de sua escolha, você os duplicaria na Braze para serem usados para fins de marketing: segmentação baseada em contas, marketing baseado em contas, gerenciamento de leads e muito mais.

Para essa opção, recomendamos criar um catálogo para suas contas e outro para suas oportunidades e atualizá-los com frequência enviando atualizações para a Braze por meio da nossa [API de catálogos]({{site.baseurl}}/api/endpoints/catalogs/) ou da [Ingestão de dados na nuvem (CDI) de catálogos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/). Ao criar esses catálogos, certifique-se de que o `id` (primeira coluna) do seu catálogo corresponda ao `id` no seu sistema CRM de vendas.

#### Mapeie seus campos de CRM {#map-over-your-crm-fields}

As tabelas abaixo incluem alguns exemplos de campos que você pode mapear a partir dos objetos de conta e oportunidade do seu CRM.

{% subtabs %}
{% subtab Account catalog %}

Neste caso de uso, o Salesforce é o sistema de CRM de exemplo. Você pode mapear qualquer campo incluído nos objetos do seu CRM.

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

{% endsubtab %}
{% subtab Opportunity catalog %}

Neste caso de uso, o Salesforce é o sistema de CRM de exemplo. Você pode mapear qualquer campo incluído nos objetos do seu CRM.

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

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Opção 2: Usar fontes conectadas para contas e oportunidades {#option-2-use-connected-sources-for-accounts-and-opportunities}

Fontes conectadas são tabelas de dados hospedadas por você em seu próprio data warehouse e consultadas pelas [extensões de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) da Braze. Ao contrário dos catálogos, em vez de duplicar seus objetos de negócios (contas e oportunidades) na Braze, você os manteria em seu data warehouse e os usaria como a fonte da verdade.

Para configurar fontes conectadas, consulte [Integração de fontes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Etapa 2: Relacione seus objetos de negócios aos perfis de usuário {#step-2-relate-your-business-objects-to-user-profiles}

Os perfis de usuário são o principal objeto na Braze, que alimenta a maior parte da sua segmentação demográfica, disparo e personalização. Os perfis de usuários incluem [dados de usuários padrão]({{site.baseurl}}/user_guide/data/unification/user_data/) coletados pelo nosso SDK e outras fontes, incluindo [dados personalizados]({{site.baseurl}}/user_guide/data/activation/), que assumem a forma de atributos (dados demográficos), eventos (dados comportamentais) ou compras (dados transacionais).

### Etapa 2.1: Mapear IDs de CRM de vendas para a Braze {#step-21-map-sales-crm-ids-to-braze}

Primeiro, certifique-se de que a Braze e o CRM de sua escolha tenham um identificador comum para compartilhar dados. Sugerimos usar a tabela a seguir para mapear os campos de ID do CRM de vendas de volta para o objeto de usuário da Braze. A tabela abaixo tem o Salesforce como sistema de CRM, mas isso pode ser feito com qualquer CRM.

#### Objeto da Braze: Usuário {#braze-object-user}

| Campo da Braze | Objeto CRM (Salesforce) | Campo CRM (Salesforce) | Informações adicionais |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` | - Rótulo de alias de usuário: `salesforce_lead_id` <br>- Nome do alias do usuário: `lead_id` |
| `Aliases.salesforce_contact_id` | Contato | `id` | - Rótulo de alias de usuário: `salesforce_contact_id` <br>- Nome do alias do usuário: `contact_id` |
| `AccountId` | Contato | `AccountId` |
| `OpportunityId` (opcional, escalar) <br>ou<br> `Opportunities` (opcional, array) | Oportunidade | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objeto da Braze: Usuário" }

{% alert note %}
Recomendamos o uso de [aliases]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases) em vez de `external_id` para mapear os identificadores de leads e contatos do Salesforce de volta à Braze. Isso reduz a quantidade de pesquisas necessárias ao identificar e executar suas iniciativas de crescimento lideradas por produtos.
{% endalert %}

Depois de sincronizar seus IDs, é necessário relacionar os perfis de usuário da Braze com seus objetos de negócios.

### Etapa 2.2: Crie uma relação entre os perfis de usuário e seus objetos de negócios {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab Catalogs %}

#### Opção 1: Ao usar catálogos {#option-1-when-using-catalogs}

Agora que os detalhes da oportunidade e da conta estão registrados como catálogos da Braze, é necessário criar um relacionamento entre esses catálogos e os perfis de usuário para os quais você deseja enviar mensagens. Atualmente, isso requer duas etapas:

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

Uma das tabelas da sua fonte conectada deve incluir um `user_id` que corresponda ao `external_user_id` definido na Braze para seus usuários. A configuração do perfil de usuário acima usa seu lead e `contact_ids` como seu `external_id`, portanto, você deve garantir que suas tabelas de lead/contato incluam esses IDs.

Além de garantir a correspondência dos IDs, recomendamos gravar dados básicos no nível da conta, como `account_id`, `opportunity_id` e até mesmo atributos firmográficos comuns, como `industry`, nos perfis de usuários para uma segmentação e personalização eficientes.

{% endtab %}
{% endtabs %}