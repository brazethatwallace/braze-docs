---
nav_title: Envio de mensagens para usuários
article_title: Usuários-alvo para previsão de churn
description: "Este artigo de referência aborda as possíveis próximas etapas após a criação de uma previsão de churn, como a implementação de filtros e considerações estratégicas."
page_order: 1.2

---

# Usuários de envio de mensagens {#what-do-next}

> Este artigo de referência aborda as próximas etapas após a criação de uma previsão de churn, incluindo como direcionar usuários com filtros e considerações estratégicas para o envio de mensagens.

{% alert note %}
As previsões prévias e de demonstração não permitirão que os usuários sejam direcionados para envio de mensagens, e os botões **Create Segment** e **Create Campaign** serão desativados. Para adquirir essa funcionalidade, entre em contato com o gerente da sua conta.
{% endalert %}

## Implementação de filtros {#filters}

Depois de decidir qual intervalo de _Pontuação de risco de churn_ ou categoria deseja segmentar, você pode usar os botões **Create Segment** ou **Create Campaign** para criar um novo **Segment** ou **Campaign** que filtre os usuários com a _Pontuação de risco de churn_ ou a categoria selecionada com o controle deslizante.

Também é possível usar filtros em **Campaigns** ou **Segments** para direcionar os usuários de acordo com esse limite. Você pode filtrar os usuários por "Pontuação de churn" ou "Categoria de churn" em **Campaigns**, **Canvas** e **Segments**, da mesma forma que usa qualquer outro filtro na Braze.

![Os filtros de churn disponíveis ao definir um público incluem Categoria de probabilidade de compra e Pontuação de probabilidade de compra.]({% image_buster /assets/img_archive/predictive_churn_filters.png %})

## Considerações estratégicas {#strategic-considerations}

Agora que você identificou e selecionou o grupo de usuários em risco de churn que precisa de alguns incentivos ou de uma nova série de envios de mensagens para mantê-los ativos e engajados, o que fazer? Você simplesmente os adiciona proativamente à sua série de usuários passivos atuais? Ou cria uma série totalmente nova de **Canvases** e **Campaigns**?

**Aqui estão algumas ideias a serem consideradas:**

- Direcione seus usuários de médio a alto risco previstos com um desconto especial, mercadoria gratuita (presente físico ou créditos digitais), conteúdo exclusivo ou acesso antecipado a uma nova experiência (produto, recurso de app, nível).<br><br>
- Coloque esses usuários em um **Canvas** diário por uma semana, enviando mensagens no canal que eles mais preferem, faça um envio concentrado por três dias, alcançando os clientes em todos os canais, do e-mail ao Facebook, ou envie uma mensagem de uma pessoa real, solicitando feedback sobre a marca ou oferecendo uma dica profissional.<br><br>
- Talvez você só precise de uma maneira nova e divertida de reiterar o valor da sua marca e todas as maneiras pelas quais esses clientes já encontraram valor nela antes. Isso pode ser um boletim informativo semanal específico para uma persona, uma série de histórias reais de usuários reais sobre sua marca ou alguma outra estratégia de marketing de conteúdo.

Lembre-se de que é possível enviar mensagens para diferentes níveis de usuários em risco de forma diferente! Assim, os clientes de maior risco poderiam receber descontos mais altos do que os clientes de médio risco, enquanto os clientes de menor risco simplesmente recebem novos tipos de envio de mensagens ou conteúdo, mas nenhum incentivo maior. Você também pode adicionar outros filtros nesses **Segments** para qualificar ainda mais quem recebe quais ofertas ou mensagens.