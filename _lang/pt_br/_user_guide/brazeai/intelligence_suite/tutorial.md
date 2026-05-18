---
nav_title: "Tutorial: Restaurante de serviço rápido"
article_title: Tutorial do Intelligence Suite
page_order: 10
search_rank: 12
description: "Novo no Intelligence Suite da Braze? Comece com este tutorial."
tool:
  - Dashboard
---

# Tutorial do Intelligence Suite {#intelligence-suite-tutorial}

> Novo no Intelligence Suite da Braze? Comece com este tutorial! Para mais informações gerais, consulte [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Tutorial: Restaurante de serviço rápido {#tutorial-quick-service-restaurant}

Vamos imaginar que trabalhamos no SandwichEmperor, um restaurante de fast food que tem um novo item de menu por tempo limitado: o Royal Roast. Usaremos dois recursos do Intelligence Suite para enviar promoções personalizadas em um Canvas.

### Etapa 1: Use o Intelligent Timing para saber quando enviar notificações {#step-1-use-intelligent-timing-for-when-to-send-notifications}

Usaremos o Intelligent Timing para analisar as interações anteriores dos nossos usuários com o nosso app e cada canal de envio de mensagens e, em seguida, selecionar automaticamente o melhor momento para promover o Royal Roast para cada usuário. Alguns usuários podem receber a promoção à tarde, enquanto outros podem recebê-la à noite.

Forneceremos um horário de fallback para usuários que não têm interações anteriores suficientes para análise: o horário mais popular para usar o app entre todos os usuários.

![Configurações de entrega do Intelligent Timing para uma etapa de Mensagem.]({% image_buster /assets/img/intelligence_suite1.png %})

### Etapa 2: Use a Seleção inteligente para selecionar a promoção {#step-2-use-intelligent-selection-to-select-the-promotion}

Para as mensagens promocionais em si, usaremos a Seleção inteligente para testar três mensagens diferentes (notificação por push, e-mail e SMS) para o Royal Roast. A Seleção inteligente analisará o desempenho de todas as nossas mensagens promocionais duas vezes por dia e, em seguida, enviará gradualmente mais das mensagens com melhor desempenho e menos das demais.

Depois que a Seleção inteligente reunir dados suficientes para determinar a mensagem com melhor desempenho, ela usará essa mensagem em 100% dos envios futuros.

![Seção de Testes A/B de um Canvas com a Seleção inteligente ativada.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Etapa 3: Lance o Canvas {#step-3-launch-the-canvas}

Com o Intelligent Timing e a Seleção inteligente, configuramos nossas promoções do Royal Roast para serem otimizadas em termos de horário e envio de mensagens. Podemos lançar nosso Canvas e observar como nossos envios se ajustam para acomodar as preferências dos usuários.