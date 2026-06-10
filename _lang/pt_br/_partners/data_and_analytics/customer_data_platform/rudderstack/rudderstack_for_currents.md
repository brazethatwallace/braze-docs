---
nav_title: RudderStack para Currents
article_title: RudderStack para Currents
description: "Este artigo descreve a parceria entre o Braze Currents e o RudderStack, uma infraestrutura de dados de clientes de código aberto que oferece uma integração perfeita da Braze para seus apps Android, iOS e da web."
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack para Currents {#rudderstack-for-currents}

> O [RudderStack](https://www.rudderstack.com/) permite coletar, transformar e ativar os dados de seus clientes em toda a sua pilha, aproveitando seu data warehouse na nuvem como a fonte central da verdade. Este artigo fornece uma visão geral de como configurar uma conexão entre o Braze Currents e o RudderStack.

A integração entre a Braze e o RudderStack permite usar o Braze Currents para exportar seus eventos da Braze para o RudderStack a fim de gerar análises de dados mais profundas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta do RudderStack | É necessário ter uma [conta RudderStack](https://app.rudderstack.com/login) para usar essa parceria. |
| Destino da Braze | Sugerimos que você tenha [configurado a Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) no RudderStack. |
| Currents | Para exportar dados de volta para o RudderStack, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado para sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar uma fonte de dados para a Braze no RudderStack {#step-1-create-a-data-source-for-braze-within-rudderstack}

Primeiro, crie uma fonte da Braze no app web do RudderStack. As instruções para criar uma fonte de dados podem ser encontradas no site do [RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Depois de concluído, o RudderStack fornecerá uma URL de webhook, incluindo a chave de gravação, que você precisará usar na próxima etapa. Você pode encontrar a URL do webhook na guia **Settings** da sua fonte Braze.

### Etapa 2: Criar Current {#step-2-create-current}

Na Braze, navegue até **Currents > + Create Current > RudderStack Export**. Forneça um nome de integração, e-mail de contato, URL do webhook do RudderStack (no campo de chave) e região do RudderStack.

### Etapa 3: Exportar eventos {#step-3-export-events}

Em seguida, selecione os eventos que você deseja exportar. Por fim, clique em **Launch Current**.

Todos os eventos enviados ao RudderStack incluirão o `external_user_id` do usuário. No momento, a Braze não envia dados de eventos ao RudderStack para usuários que não possuem o `external_user_id` definido.

## Detalhes da integração {#integration-details}

A Braze suporta a exportação de todos os dados listados nos [glossários de eventos do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) para o RudderStack.

A estrutura da carga útil dos dados exportados é a mesma dos conectores HTTP personalizados, que pode ser visualizada no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).