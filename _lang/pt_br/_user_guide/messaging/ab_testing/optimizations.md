---
nav_title: Otimizações
article_title: Otimizando testes A/B
page_order: 1
page_type: reference
description: "Aprenda a otimizar testes multivariantes e A/B de Campaigns com BrazeAI."
---

# Otimizando testes A/B {#optimizing-ab-tests}

> Use **Otimizar com BrazeAI<sup>TM</sup>** para otimizar automaticamente uma Campaign com múltiplas variantes.

Na etapa **Públicos-alvo**, acesse **A/B Testing** e ative **Otimizar com BrazeAI<sup>TM</sup>**.

Para uma Campaign de envio único, a BrazeAI<sup>TM</sup> envia um teste inicial e depois envia a variante de melhor desempenho para o público restante. Para uma Campaign de múltiplos envios, a BrazeAI<sup>TM</sup> analisa o desempenho a cada 12 horas e direciona mais usuários para as variantes de melhor desempenho.

Para pré-requisitos, opções de configuração e detalhes de relatórios, consulte [Otimizando testes A/B com BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

{% alert note %}
Campaigns existentes que usam Variante Personalizada continuam a oferecer suporte a essa otimização e à sua análise de dados. A Variante Personalizada não está disponível ao criar uma nova Campaign.
{% endalert %}

A Braze verifica a elegibilidade do usuário novamente antes do segundo envio em uma otimização de envio único. Usuários que não eram elegíveis para o teste inicial podem entrar no público restante, enquanto usuários que não são mais elegíveis não recebem o envio de acompanhamento.

Para informações sobre os resultados da Campaign, consulte [Análise de dados de testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).