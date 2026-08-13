---
nav_title: Shopify para Currents
article_title: Shopify para Currents
description: "Este artigo de referência descreve a parceria entre Braze Currents e Shopify, uma empresa global de comércio que permite conectar a Braze à sua loja Shopify de forma integrada para gerar relatórios internos e rastrear melhor a atribuição de último toque para compras."
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify para Currents {#shopify-for-currents}

> [Shopify](https://www.shopify.com/) é uma empresa líder global em comércio que fornece ferramentas confiáveis para iniciar, expandir, divulgar e gerenciar negócios de qualquer porte. A plataforma e os serviços da Shopify são projetados para oferecer confiabilidade e uma experiência de compra melhor para consumidores em todos os lugares.

{% alert important %}
Essa integração está atualmente em beta. Para saber mais, entre em contato com seu gerente de sucesso do cliente da Braze.
{% endalert %}

A integração da Braze com a Shopify oferece uma solução poderosa para empresas de eCommerce que desejam aprimorar o engajamento de clientes e impulsionar esforços de marketing personalizados. Com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), você pode conectar dados à Shopify para gerar relatórios internos e rastrear melhor a atribuição de último toque para compras.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Currents | Para exportar dados para o Shopify, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado para a sua conta. |
| Loja Shopify | Certifique-se de que você já [configurou pelo menos uma loja Shopify com a Braze]({{site.baseurl}}/shopify_standard_integration). |
| Permissões de proprietário ou membro da equipe da loja Shopify | {::nomarkdown}<ul><li>Acesso a todas as configurações de <b>Geral</b> e <b>Loja Online</b>.</li><li> Permissões adicionais de administrador:</li><ul><li>Pedidos: Visualizar</li><li>Cliente: Leitura e Escrita</li><li>Visualizar Eventos do Cliente (Web Pixels)</li><li>Gerenciar Configurações</li><li>Visualizar Apps Desenvolvidos por Equipe/Colaboradores</li><li>Gerenciar/Instalar Apps e Canais</li><li>Gerenciar/Adicionar Pixels Personalizados</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Configure sua loja Shopify {#step-1-set-up-your-shopify-store}

Se ainda não tiver feito isso, siga as etapas de [configuração da integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration) para configurar pelo menos uma loja Shopify com a Braze.

### Etapa 2: Crie um Braze Current {#step-2-create-braze-current}

1. Na Braze, acesse **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**.
2. Forneça um nome de integração e um e-mail de contato.
3. Na seção **Credenciais**, selecione a loja Shopify que você configurou na [Etapa 1](#step-1-set-up-your-shopify-store).
4. Selecione os eventos que deseja rastrear. Uma lista de eventos disponíveis é fornecida.
5. Selecione **Launch Current**

![A página do Braze Shopify Currents. Esta página inclui campos para nome da integração, e-mail de contato e loja Shopify.]({% image_buster /assets/img/shopify/shopify_currents.png %})

## Sincronização de perfil de usuário {#user-profile-sync}

Além dos dados de eventos, a integração com o Shopify pode sincronizar atualizações de perfil de usuário da Braze para a sua loja Shopify. Quando o perfil de um usuário é atualizado na Braze, o Currents cria ou atualiza o cliente correspondente na sua loja.

{% alert note %}
A sincronização de perfil de usuário não é compatível com [conectores de teste do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#testing-currents-connectors). Outras exportações de eventos não são afetadas. Para sincronizar perfis de usuário, use um [conector padrão do Shopify com o Currents](#step-2-create-braze-current).
{% endalert %}

### Correspondência de usuários {#user-matching}

A Braze faz a correspondência de clientes do Shopify usando o `user_id` da Braze como um [identificador personalizado](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSet) (`customId`) do Shopify, com o namespace `braze` e a chave `user_id`. Se nenhum cliente com esse identificador existir na sua loja, um novo cliente será criado. Usuários anônimos não são sincronizados.

### Mapeamento de campos {#field-mapping}

Os seguintes campos de perfil da Braze são sincronizados com o Shopify:

| Campo da Braze | Campo do cliente Shopify | Notas |
| ----------- | ---------------------- | ----- |
| `first_name` | `firstName` | Mapeado como está. Enviado apenas quando presente na atualização do perfil. |
| `last_name` | `lastName` | Mapeado como está. Enviado apenas quando presente na atualização do perfil. |
| `email_address` | `email` | Espaços removidos e convertido para minúsculas antes do envio. |
| `phone_number` | `phone` | Enviado no formato [E.164](https://en.wikipedia.org/wiki/E.164). |
| `language` | `locale` | Convertido para um locale compatível com o Shopify. Português e chinês recebem uma variante regional (como `pt-BR`) com base no país do usuário. Se o idioma do usuário não for compatível com o Shopify, esse campo é omitido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Apenas os campos presentes em uma atualização de perfil são enviados. Campos omitidos de uma atualização permanecem inalterados no Shopify — uma sincronização nunca limpa ou exclui um campo do seu cliente Shopify.

### Campos que não são sincronizados {#fields-that-are-not-synced}

Atualmente, a integração não grava metafields do Shopify, então campos de perfil que exigiriam um metafield não são sincronizados. Em particular, atributos personalizados não são enviados para o Shopify. Os outros campos não enviados são `external_user_id`, `gender`, `dob` (data de nascimento), `timezone`, `home_city`, `country` e `archived`.

A Braze pode criar definições de metafield sob o namespace `braze` na sua loja (por exemplo, `braze.gender`). Essas definições são reservadas para uso futuro em potencial — a Braze não grava valores nelas atualmente. A exceção é `braze.user_id`, que armazena o identificador usado para fazer a correspondência dos seus clientes.