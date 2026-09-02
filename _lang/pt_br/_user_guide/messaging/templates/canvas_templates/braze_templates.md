---
nav_title: Usar modelos da Braze
article_title: Usar modelos de Canvas da Braze
alias: "/canvas_templates/templates/"
page_order: 2
description: "Este artigo de referência aborda como criar modelos de Canvas disponíveis."
page_type: reference
---

# Usar modelos de Canvas da Braze {#use-braze-canvas-templates}

> A Braze tem uma seleção de modelos de Canvas disponíveis para você consultar e usar como práticas recomendadas para casos de uso comuns. Embora esses modelos não possam ser editados, você pode visualizá-los em **Conteúdo** > **Canvas** > **Modelos da Braze** ou usá-los nos seus Canvas.

![Modelos da Braze na seção de modelos de Canvas com treze modelos disponíveis.]({% image_buster /assets/img/braze_canvas_templates.png %})

Selecione entre os modelos disponíveis a seguir para consultar ou usar como seu Canvas.

## Modelos padrão de Canvas {#standard-canvas-templates}

{% tabs %}
{% tab Abandoned Intent %}

### Intenção abandonada {#abandoned-intent}

Engaje os usuários em tempo real para incentivá-los a concluir suas compras.

Considere o seguinte ao usar este modelo:

- O cronograma de entrada é disparado por API or interface de programação do aplicativo (API). Use o [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) para inserir usuários quando eles abandonarem um carrinho, ou mude para um cronograma baseado em ação com um gatilho como **Realizar evento personalizado** ou **Realizar evento de atualização de carrinho**, se isso se adequar à sua configuração.
- A conversão padrão rastreia **Realizar qualquer compra (Legado)**. Adapte os eventos de conversão e as etapas de jornadas de ação **Realizou compra?** para produtos específicos, se necessário.
- Os usuários saem do Canvas quando realizam uma compra nas etapas de jornadas de ação **Realizou compra?**. Este modelo pressupõe que você tenha uma jornada pós-compra separada.
- O Canvas inclui um e-mail para **Lembrete detalhado**, uma etapa de postergação, uma divisão de canal inteligente para e-mail e SMS, mensagens de canal com Content Cards (e-mail, SMS e mensagem no app) e uma etapa de Audience Sync. Configure o **Redirecionamento de anúncios** com seus parceiros e públicos.

Para um passo a passo detalhado, consulte [Intenção abandonada]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/abandoned_cart).

{% endtab %}
{% tab Back In Stock %}

### De volta ao estoque {#back-in-stock}

Impulsione compras notificando seus usuários quando um item está de volta ao estoque com mensagens personalizadas. Considere o seguinte ao usar este modelo:

- Em **Cronograma de entrada**, selecione um catálogo para usar. Isso permite que você acesse dados, como produtos, descontos e promoções, para direcionar ainda mais seus usuários.
- Em **Público-alvo**, adicione um Segment or segmento or segmento para direcionar usuários que indicaram interesse em um determinado item.
- Nas etapas de Mensagem ao longo do Canvas, atualize o Liquid para referenciar seu catálogo.

{% endtab %}
{% tab Feature Adoption %}

### Adoção de funcionalidades {#feature-adoption}

Entregue mensagens personalizadas e oportunas para destacar os benefícios e dicas de uso. Considere o seguinte ao usar este modelo:

- Exclua usuários que já adotaram a funcionalidade. Por exemplo, em **Público-alvo**, adicione um filtro para um evento personalizado como "Funcionalidade ativada" que já tenha ocorrido.
- Para usar a etapa de jornada experimental, defina um evento de conversão. Esse evento deve ser o evento que sinaliza a adoção da funcionalidade.
- Configure a etapa de jornada de ação no modelo com eventos personalizados para "Funcionalidade ativada" e "Tour realizado".
- Configure os atributos personalizados na etapa de Mensagem chamada "Pesquisa de feedback" para capturar o sentimento do feedback.

{% endtab %}
{% tab Lapsed User %}

### Usuário inativo {#lapsed-user}

Traga os usuários de volta ao seu app com incentivos baseados em seus engajamentos anteriores. Considere o seguinte ao usar este modelo:

- Em **Básico**, selecione um app específico para rastrear conversões.
- No editor de Canvas, adicione apps específicos para as etapas de jornadas de ação.
- Configure a etapa de Audience Sync com os parceiros e públicos para o seu caso de uso.

{% endtab %}
{% tab Onboarding %}

### Integração {#onboarding}

Crie jornadas de integração que promovam uma adoção inicial sólida e incentivem relacionamentos duradouros com seus usuários. Considere o seguinte ao usar este modelo:

- Na etapa de jornadas do público chamada "Divisão de público", considere personalizar as ações-chave para usuários engajados. No modelo, o filtro de Segment or segmento or segmento é "Clicou no e-mail da etapa E-mail de boas-vindas".

{% endtab %}
{% tab Post-Purchase Feedback %}

### Feedback pós-compra {#post-purchase-feedback}

Orquestre experiências personalizadas que permitam responder ao feedback e construir um relacionamento com seus usuários. Considere o seguinte ao usar este modelo:

- Na primeira etapa do editor de Canvas:
    - Especifique os atributos personalizados na mensagem no app para indicar o sentimento do feedback com base na opção de pesquisa selecionada.
    - Especifique atributos nos links para cada chamada para ação para capturar qual opção foi selecionada. Esses atributos são referenciados na jornada do público subsequente.
- Personalize a jornada do público com os atributos da primeira etapa deste modelo.
- Configure a etapa de Audience Sync chamada "Redirecionamento de anúncios".

{% endtab %}
{% endtabs %}

## Modelos de Canvas para eCommerce {#ecommerce-canvas-templates}

Os modelos de Canvas para eCommerce são feitos especificamente para profissionais de marketing de eCommerce, facilitando a implementação de estratégias essenciais.

{% multi_lang_include canvas/ecommerce_templates.md %}