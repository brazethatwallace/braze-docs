---
nav_title: Clonando Canvas
article_title: Clonar Canvas
page_order: 3
alias: "/cloning_canvases/"
description: "Este artigo de referência descreve como clonar um Canvas do editor original para o fluxo de trabalho do Canvas Flow."
tool: Canvas
---

# Clonar Canvas para o Canvas Flow {#clone-canvases-to-canvas-flow}

> Se você tem um Canvas existente do editor original, é possível cloná-lo para criar uma cópia no Canvas Flow. Ao mudar para o fluxo de trabalho atual do Canvas, você ganha acesso a [componentes do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/) leves, [propriedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#canvas-entry-properties) e [edição pós-lançamento]({{site.baseurl}}/post-launch_edits/). Seu Canvas original não será alterado nem excluído.

{% alert important %}
Não é mais possível criar ou duplicar Canvas usando a experiência original do Canvas. A Braze recomenda que os clientes que usam a experiência original do Canvas migrem para o Canvas Flow, a experiência atual do Canvas.
{% endalert %}

Para clonar seu Canvas, faça o seguinte:

1. Acesse o dashboard do Canvas.
2. Identifique o Canvas do qual você deseja criar uma cópia no fluxo de trabalho do Canvas Flow. Você pode clonar Canvas com status **Draft**, **Active** ou **Stopped**.
3. Clique em <i class="fas fa-ellipsis-vertical"></i> **More actions** e selecione **Clone to Canvas Flow**.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4. Insira o nome do seu novo Canvas e clique em **Clone to Canvas Flow**.

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Agora, você tem duas versões do seu Canvas: o Canvas original e a versão do Canvas Flow. Seu Canvas original mantém o status original, e o Canvas clonado tem o status **Draft**. Você ainda pode acessar o Canvas original, mas a Braze recomenda usar o fluxo de trabalho do Canvas Flow para continuar construindo seus Canvas.

Anteriormente, alguns Canvas com ramificações não podiam ser clonados. Agora, é possível clonar Canvas com ramificações. Observe que clonar Canvas com ramificações pode resultar em etapas desconectadas. Resolva essas etapas desconectadas (etapas que não têm uma etapa anterior conectada a elas) para garantir que a jornada do seu Canvas esteja mapeada corretamente.

{% alert note %}
Se você clonar um Canvas ativo, a Braze continuará enviando usuários pelo Canvas original. Recomendamos parar um Canvas antes de cloná-lo para evitar o envio de mensagens duplicadas aos usuários de ambos os Canvas.
{% endalert %}

![Dashboard do Canvas com dois Canvas listados: Cópia V2 do Canvas V1 e Canvas V1. A Cópia V2 do Canvas V1 tem um ícone que indica que está usando o fluxo de trabalho do Canvas Flow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Você concluiu a clonagem do seu Canvas para o fluxo de trabalho do Canvas Flow. Agora, você pode continuar construindo seus Canvas nessa experiência atualizada!

## Recomendações {#recommendations}

Para permitir que os usuários existentes continuem sua jornada após você ter clonado seu Canvas original para o Canvas Flow, você pode adicionar filtros ao seu Canvas existente que impeçam novos usuários de entrar no novo Canvas.

Se a reelegibilidade estiver desativada, adicione o filtro "Entered Canvas Variation". Se a reelegibilidade estiver ativada, estes são os métodos possíveis a considerar para garantir que os usuários não entrem no mesmo Canvas duas vezes:
- Atualize o Canvas existente para incluir uma tag única. Para o novo Canvas, adicione o filtro "Last Received Message from Campaign or Canvas with Tag". Isso impede que os usuários entrem no Canvas duas vezes após uma data de entrada específica (número total de dias após o envio da última mensagem do Canvas original mais a janela de conversão).
- **O método a seguir registrará pontos de dados.** Atualize o Canvas original para incluir um webhook Braze-para-Braze que dispare um atributo personalizado com registro de data e hora na entrada. Esse atributo pode ser usado para impedir que os usuários entrem no novo Canvas após a data especificada (número total de dias após o envio da última mensagem do Canvas original mais a janela de conversão).

Para Canvas disparados por API, coordene com sua equipe de engenharia para garantir que esses Canvas estejam usando o novo ID do Canvas quando os novos Canvas estiverem prontos para lançamento.

Para saber mais sobre as diferenças entre o editor original do Canvas e a experiência do Canvas Flow, confira as [Perguntas frequentes sobre o Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).