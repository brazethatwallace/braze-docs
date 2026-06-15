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

A integração da Braze com a Shopify oferece uma solução poderosa para empresas de eCommerce que desejam aprimorar o engajamento de clientes e impulsionar esforços de marketing personalizados. Com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), você pode conectar dados à Shopify para gerar relatórios internos e rastrear melhor a atribuição de último toque para compras.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Currents | Para exportar dados para a Shopify, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado na sua conta. |
| Loja Shopify | Certifique-se de que você já [configurou pelo menos uma loja Shopify com a Braze]({{site.baseurl}}/shopify_standard_integration/). |
| Permissões de proprietário ou membro da equipe da loja Shopify | {::nomarkdown}<ul><li>Acesso a todas as configurações de <b>General</b> e <b>Online Store</b>.</li><li> Permissões adicionais de administrador:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Configure sua loja Shopify {#step-1-set-up-your-shopify-store}

Se ainda não fez isso, siga as etapas de [configuração da integração padrão da Shopify]({{site.baseurl}}/shopify_standard_integration/) para configurar pelo menos uma loja Shopify com a Braze.

### Etapa 2: Crie um Braze Current {#step-2-create-braze-current}

1. Na Braze, acesse **Integrações de parceiros** > **Currents** > **+ Criar nova** > **Exportar para Shopify**.
2. Forneça um nome para a integração e um e-mail de contato.
3. Na seção **Credentials**, selecione a loja Shopify que você configurou na [Etapa 1](#step-1-set-up-your-shopify-store).
4. Selecione os eventos que deseja rastrear. Uma lista de eventos disponíveis é fornecida.
5. Selecione **Launch Current**.

![A página Braze Shopify Currents. Esta página inclui campos para nome da integração, e-mail de contato e loja Shopify.]({% image_buster /assets/img/shopify/shopify_currents.png %})