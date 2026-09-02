---
nav_title: Integração padrão do Shopify com tag de terceiros
article_title: Integração padrão do Shopify com tag de terceiros
description: "Este artigo de referência descreve como configurar a integração padrão do Shopify com uma ferramenta de tag de terceiros."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Integração padrão do Shopify com ferramenta de tag de terceiros {#shopify-standard-integration-with-third-party-tagging-tool}

> Esta página orienta você no uso de ferramentas de terceiros, como o Google Tag Manager, com a [integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration) para inicializar e carregar o Braze Web SDK or kit de desenvolvimento de software.

Para lojas on-line do Shopify, recomendamos usar o método de integração padrão da Braze para oferecer suporte aos SDKs da Braze em seu site. No entanto, entendemos que você pode preferir usar uma ferramenta de terceiros, como o Google Tag Manager. Se você optar por usar uma ferramenta de terceiros com o conector Shopify da Braze, lembre-se de que a integração da Braze e a incorporação do app gerenciarão o SDK or kit de desenvolvimento de software durante o processo de checkout.

## Requisitos {#requirements}

- **Chave de API or interface de programação do aplicativo (API) consistente entre sua ferramenta de terceiros e o conector do Shopify:** A chave de API or interface de programação do aplicativo (API) deve ser consistente tanto na Braze quanto em sua ferramenta de terceiros. Isso evita a criação de usuários duplicados e mantém a compatibilidade entre os SDKs.
  - **Local da chave de API or interface de programação do aplicativo (API):** Depois de concluir a integração padrão, a integração criará automaticamente um app web da Braze chamado "Shopify". Recupere a chave de API or interface de programação do aplicativo (API) dentro da integração que é usada com a configuração da ferramenta de terceiros.
- **Versões consistentes do SDK or kit de desenvolvimento de software entre sua ferramenta de terceiros e o conector do Shopify:** Novos clientes são provisionados na versão mais recente do SDK or kit de desenvolvimento de software durante a configuração. Sua ferramenta de terceiros deve usar a mesma versão do SDK or kit de desenvolvimento de software configurada nas configurações de integração da Braze. Clientes existentes são notificados quando uma versão mais recente está disponível e podem fazer upgrade por conta própria nas configurações de integração.
- **Tempo de inicialização consistente do SDK or kit de desenvolvimento de software:** Nas configurações de integração padrão do Shopify, você pode selecionar os SDKs a serem inicializados no início da sessão ou quando ocorrer um login na conta. Essa configuração deve ser consistente entre sua ferramenta de terceiros e a Braze. Inconsistências podem levar a problemas posteriores para o usuário e para a sincronização de dados.

{% alert note %}
Recomendamos usar exclusivamente o método de integração padrão em vez de usá-lo em conjunto com gerenciadores de tags de terceiros, o que pode causar conflitos entre o Braze SDK or kit de desenvolvimento de software e as ferramentas de terceiros. Se você usar uma ferramenta de terceiros, faça um teste para confirmar que tudo funciona conforme o esperado.
{% endalert %}

## Configuração da integração com uma ferramenta de terceiros {#setting-up-the-integration-with-a-third-party-tool}

Desviar-se das etapas fornecidas pode levar a problemas inesperados, portanto, certifique-se de segui-las à risca.

1. Siga as etapas fornecidas na [configuração da integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration). Ao [ativar os Braze Web SDKs]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-2-enable-braze-web-sdks), marque a caixa que indica que você está usando uma ferramenta de terceiros para adicionar o Braze Web SDK or kit de desenvolvimento de software ao seu site do Shopify.
2. Acesse **Settings** > **App Settings**, selecione o app web **Shopify** e copie a **API or interface de programação do aplicativo (API) key for Shopify on Web**.
3. Cole a chave de API or interface de programação do aplicativo (API) na configuração do SDK or kit de desenvolvimento de software web da sua ferramenta de terceiros e defina a versão do SDK or kit de desenvolvimento de software para corresponder à integração Shopify da Braze.

{% alert note %}
Se você estiver usando o Google Tag Manager, mantenha as versões do SDK or kit de desenvolvimento de software alinhadas tanto no GTM quanto na configuração da integração Shopify da Braze.
{% endalert %}

## Captura de dados do Shopify e sincronização de usuários {#capturing-shopify-data-and-syncing-users}

Desde que o Web SDK or kit de desenvolvimento de software esteja acessível no front-end do seu site do Shopify por meio de uma ferramenta de terceiros, a integração padrão capturará os dados do Shopify e sincronizará os usuários conforme esperado.

## Considerações e isenções de responsabilidade {#considerations-and-disclaimers}

- **Configurações de inicialização:** Se você modificar as configurações de inicialização por meio da ferramenta de terceiros, a sincronização de usuários e dados poderá ser afetada. Por exemplo, se você optar por inicializar o SDK or kit de desenvolvimento de software quando um formulário de consentimento de cookie for aceito, a Braze não receberá rastreamento de usuários anônimos ou dados até que o usuário consinta.
- **Não há suporte para a definição de atributos diretamente pelo `dataLayer`:** Use `window.braze` em vez de `dataLayer` para definir atributos.
- **Usuários duplicados em potencial:** Se a chave de API or interface de programação do aplicativo (API) não corresponder entre a Braze e sua ferramenta de terceiros, poderão ser criados usuários duplicados.
- **Incompatibilidade de SDK or kit de desenvolvimento de software:** O uso de um número de versão incorreto pode causar problemas com os métodos do SDK or kit de desenvolvimento de software.