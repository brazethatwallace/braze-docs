---
nav_title: Shopify checkout e Liquid
page_order: 7
description: "Este artigo explica a descontinuação do Shopify checkout&#46;liquid, incluindo o impacto na sua integração com a Shopify e orientações para desenvolvedores."
page_type: update

---

# Descontinuação do Shopify checkout&#46;liquid {#shopify-checkout46liquid-deprecation}

A Shopify informou a todos os comerciantes sobre a descontinuação de `checkout.liquid` e a migração para o [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), uma nova base para criar experiências de checkout personalizadas.

A Shopify descontinuará `checkout.liquid` em duas fases:

1. **[13 de agosto de 2024](#phase-one-august-13-2024):** Prazo para fazer upgrade das suas páginas de informações, envio e pagamento.
2. **[28 de agosto de 2025](#phase-two-august-28-2025):** Prazo para fazer upgrade das suas páginas de agradecimento e status de pedido, incluindo seus apps que usam tags de script e scripts adicionais.

Para informações gerais sobre como fazer upgrade para o Checkout Extensibility, consulte o [guia de upgrade da Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Impacto na sua integração {#impact-to-your-integration}

A integração da Braze com a Shopify usa [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) para carregar o SDK or kit de desenvolvimento de software da Braze para web em sites que não são headless. Estamos planejando lançar uma nova versão da integração antes do prazo de 2025 para dar suporte a todos os clientes antes que o `checkout.liquid` seja totalmente descontinuado.

Para as mudanças previstas para 13 de agosto de 2024, confira os detalhes a seguir para verificar se a sua equipe de desenvolvimento será impactada.

### Fase um: 13 de agosto de 2024 {#phase-one-august-13-2024}

A integração padrão da Braze com a Shopify não utiliza as páginas de informações, envio e pagamento dentro da experiência de checkout. Portanto, a integração padrão não será impactada.

#### Shopify Plus

Para clientes Shopify Plus, quaisquer snippets de código personalizados do SDK or kit de desenvolvimento de software que modificam o `checkout.liquid` para as páginas de informações, envio ou pagamento ficarão inativos após essa data. Por exemplo, código personalizado que registra eventos dessas páginas deixará de funcionar. Se você tem código personalizado do SDK or kit de desenvolvimento de software, consulte nossa [orientação para desenvolvedores](#developer-guidance) sobre migração.

#### Não Shopify Plus {#non-shopify-plus}

Para clientes que não são Shopify Plus, se você precisa personalizar as páginas de informações, pagamento e envio, é necessário [fazer upgrade para o Shopify Plus](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) e então seguir a [orientação para desenvolvedores](#developer-guidance).

### Fase dois: 28 de agosto de 2025 {#phase-two-august-28-2025}

A Shopify vai descontinuar o suporte para [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) nas páginas de `checkout.liquid`, que são usadas na integração. Em resposta, estamos construindo ativamente uma nova versão da integração com a Shopify, que planejamos lançar bem antes do prazo de agosto de 2025. Fique atento para mais informações da equipe de produto da Braze.

## Orientações para desenvolvedores {#developer-guidance}

Estas orientações se aplicam a clientes do Shopify Plus que adicionaram snippets de código personalizados do SDK or kit de desenvolvimento de software às páginas de informações, envio ou pagamento no `checkout.liquid`. Se você não fez essas personalizações, pode desconsiderar estas orientações.

Você não poderá mais adicionar snippets de código personalizados do SDK or kit de desenvolvimento de software às páginas de informações, envio ou pagamento no `checkout.liquid`. Em vez disso, será necessário adicionar snippets de código personalizados do SDK or kit de desenvolvimento de software às páginas de agradecimento ou de status de pedido. Isso permite reconciliar os usuários que concluíram o checkout.
1. Carregue o SDK or kit de desenvolvimento de software web da Braze nas páginas de agradecimento e de status de pedido.
2. Recupere o e-mail do usuário.
3. Chame `setEmail`.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. Na Braze, mescle os perfis de usuário com base no e-mail.

Se você encontrar perfis de usuário duplicados, pode usar nossa [ferramenta de mesclagem em massa]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#bulk-merging) para ajudar a otimizar seus dados.