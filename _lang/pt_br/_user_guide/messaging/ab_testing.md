---
nav_title: Testes A/B
article_title: Testes A/B
page_order: 6
layout: dev_guide
guide_top_header: "Testes A/B"
guide_top_text: "Execute experimentos para otimizar seu envio de mensagens. Um teste A/B compara as respostas dos usuários a múltiplas versões da mesma Campaign, enquanto um teste multivariante estende isso a duas ou mais variáveis. Na Braze, os termos são usados de forma intercambiável porque o processo de configuração é o mesmo. Use <a href=\"/docs/user_guide/brazeai/intelligence_suite/variant_selection\">Otimizar com BrazeAI<sup>TM</sup></a> para otimizar automaticamente seus resultados."

page_type: landing
description: "Configure e analise testes A/B e experimentos multivariantes na Braze."

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Conceitos
    link: /docs/user_guide/messaging/ab_testing/concepts
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: Criar testes
    link: /docs/user_guide/messaging/ab_testing/create_tests
    image: /assets/img/braze_icons/plus-circle.svg
  - name: Otimizações
    link: /docs/user_guide/messaging/ab_testing/optimizations
    image: /assets/img/braze_icons/settings-01.svg
  - name: Análise de dados
    link: /docs/user_guide/messaging/ab_testing/analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: FAQ
    link: /docs/user_guide/messaging/ab_testing/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Quando usar testes A/B {#when-to-use-ab-tests}

- **Experimentando um novo tipo de mensagem:** Experimente e descubra o que funciona melhor com seus usuários.
- **Campanhas de integração ou envios recorrentes:** Garanta que as campanhas de alto tráfego sejam o mais eficazes possível.
- **Múltiplas ideias de mensagem:** Execute um teste e tome uma decisão orientada por dados.
- **Desafiando suposições:** Teste se as táticas de marketing convencionais realmente funcionam para o seu público específico.

## Dicas para executar testes eficazes {#tips-for-running-effective-tests}

- **Use amostras grandes** para garantir que os resultados reflitam seu usuário médio e não sejam distorcidos por valores atípicos.
- **Randomize os grupos de teste** para que as diferenças nas taxas de resposta reflitam diferenças nas mensagens, e não diferenças nas amostras.
- **Saiba o que você está testando.** Isolar uma única alteração identifica qual elemento teve o maior impacto; testar múltiplas diferenças permite comparar abordagens mais amplas.
- **Defina a duração do teste antecipadamente** e não encerre o teste antes do prazo, mesmo que os resultados iniciais pareçam promissores.
- **Adicione testes antes do lançamento.** Adicionar um teste a uma Campaign em andamento produz resultados imprecisos. Clone a Campaign, interrompa a original e adicione o teste ao clone.
- **Inclua um [grupo de controle]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#including-a-control-group)** para medir o impacto em comparação com não enviar nenhuma mensagem.