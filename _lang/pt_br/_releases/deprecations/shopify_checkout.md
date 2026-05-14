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
2. **[28 de agosto de 2025](#phase-two-august-28-2025):** Prazo para fazer upgrade das suas páginas de agradecimento e status do pedido, incluindo seus apps que usam tags de script e scripts adicionais.

Para informações gerais sobre como fazer upgrade para o Checkout Extensibility, consulte o [guia de upgrade da Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Impacto na sua integração {#impact-to-your-integration}

A integração da Braze com a Shopify usa [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) para carregar o SDK da Braze para web em sites não headless. Estamos planejando lançar uma nova versão da integração antes do prazo de 2025 para dar suporte a todos os clientes antes que `checkout.liquid` seja totalmente descontinuado.

Para as mudanças previstas para 13 de agosto de 2024, confira os detalhes abaixo para verificar se a sua equipe de desenvolvimento será impactada.

### Fase um: 13 de agosto de 2024 {#phase-one-august-13-2024}

A integração padrão da Braze com a Shopify não usa as páginas de informações, envio e pagamento dentro da experiência de checkout. Como resultado, a integração padrão não será afetada.

#### Shopify Plus

Para clientes do Shopify Plus, quaisquer trechos de código SDK personalizados que modifiquem `checkout.liquid` para as páginas de informações, envio ou pagamento se tornarão inativos após essa data. Por exemplo, código personalizado que registra eventos dessas páginas não funcionará mais. Se você tiver código SDK personalizado, consulte nossas [orientações para desenvolvedores](#developer-guidance) sobre migração.

#### Não-Shopify Plus {#non-shopify-plus}

Para clientes que não são do Shopify Plus, se você precisar personalizar as páginas de informações, pagamento e envio, será necessário [fazer upgrade para o Shopify Plus](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) e então seguir as [orientações para desenvolvedores](#developer-guidance).

### Fase dois: 28 de agosto de 2025 {#phase-two-august-28-2025}

A Shopify descontinuará o suporte para [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) em páginas `checkout.liquid`, que são usadas na integração. Em resposta, estamos construindo ativamente uma nova versão da integração com a Shopify, que planejamos lançar bem antes do prazo de agosto de 2025. Fique atento para mais informações da equipe de produtos da Braze.

## Orientações para desenvolvedores {#developer-guidance}

Estas orientações se aplicam a clientes do Shopify Plus que adicionaram trechos de código SDK personalizados às páginas de informações, envio ou pagamento em `checkout.liquid`. Se você não fez essas personalizações, pode desconsiderar estas orientações.

Você não poderá mais adicionar trechos de código SDK personalizados às páginas de informações, envio ou pagamento em `checkout.liquid`. Em vez disso, será necessário adicionar trechos de código SDK personalizados às páginas de agradecimento ou de status do pedido. Isso permite que você reconcilie os usuários que concluíram o checkout.
1. Carregue o SDK da Braze para web nas páginas de agradecimento e status do pedido.
2. Recupere o e-mail do usuário.
3. Chame `setEmail`.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. Na Braze, mescle os perfis de usuário pelo e-mail.

Se você encontrar perfis de usuário duplicados, pode usar nossa [ferramenta de mesclagem em massa]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) para ajudar a simplificar seus dados.