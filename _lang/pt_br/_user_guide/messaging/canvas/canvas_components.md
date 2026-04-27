---
nav_title: Componentes do Canvas
article_title: Componentes do Canvas
page_order: 3
alias: "/user_guide/messaging/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Componentes do Canvas"
guide_top_text: "Aprimore sua jornada no Canvas com os componentes do Canvas. Os componentes do Canvas podem ser usados para simplificar o processo de determinar a eficácia do seu Canvas, substituindo etapas completas excessivas por apenas uma. Os componentes no Canvas referem-se à jornada personalizada do usuário nos ramos do seu Canvas."

page_type: landing
description: "Esta landing page reúne artigos sobre componentes do Canvas que ajudarão você a criar Canvas mais avançados. Alguns desses componentes incluem a etapa de mensagem, a etapa de postergação, a etapa de divisão de decisão e muito mais."
tool: Canvas

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Etapa de Jornadas de ação
    link: /docs/user_guide/messaging/canvas/canvas_components/action_paths
    image: /assets/img/braze_icons/zap.svg
  - name: Etapa de agente
    link: /docs/user_guide/messaging/canvas/canvas_components/agent_step
    image: /assets/img/braze_icons/briefcase-01.svg
  - name: Etapa de Jornadas do público
    link: /docs/user_guide/messaging/canvas/canvas_components/audience_paths
    image: /assets/img/braze_icons/users-01.svg 
  - name: Etapa de sincronização de público
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Etapa de Otimizador de conteúdo
    link: /docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step
    image: /assets/img/braze_icons/target-04.svg
  - name: Etapa de contexto
    link: /docs/user_guide/messaging/canvas/canvas_components/context
    image: /assets/img/braze_icons/file-search-02.svg
  - name: Etapa de Divisão de decisão
    link: /docs/user_guide/messaging/canvas/canvas_components/decision_split
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Etapa de postergação
    link: /docs/user_guide/messaging/canvas/canvas_components/delay_step
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Etapa de Jornadas do experimento
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step
    image: /assets/img/braze_icons/columns-01.svg
  - name: Feature Flags
    link: /docs/user_guide/messaging/canvas/canvas_components/feature_flags
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Etapa de mensagem
    link: /docs/user_guide/messaging/canvas/canvas_components/message_step
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Etapa de enviar para destino
    link: /docs/user_guide/messaging/canvas/canvas_components/send_to_destination
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Etapa de Atualização de usuário
    link: /docs/user_guide/messaging/canvas/canvas_components/user_update
    image: /assets/img/braze_icons/user-check-01.svg
---

## Sobre os componentes do Canvas

Com os componentes do Canvas, você pode desbloquear novas jornadas de usuário para melhorar seu processo e aumentar a eficácia do alcance do seu público.

### Personalizando jornadas de usuário

![Exemplo de uma jornada de usuário no Canvas com uma etapa de Divisão de decisão seguida por etapas de postergação e etapas de mensagem.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Use [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para dividir a jornada do usuário com base em ações e eventos de engajamento, como realizar uma compra. Se você quiser filtrar e direcionar seus públicos, as [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ajudam a simplificar o direcionamento de usuários, enviando-os por diferentes jornadas do Canvas com base em critérios de público.

Os componentes de [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) usam uma lógica simples de "sim ou não" para criar duas jornadas mutuamente exclusivas para seus usuários, com base em uma ação ou um atributo de usuário. Isso pode ajudar a identificar e direcionar seus grupos de usuários.

Os componentes de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) permitem que você adie uma única etapa no seu Canvas. Essa etapa de postergação independente no seu Canvas é ideal para enviar mensagens aos seus usuários em um momento específico. Além disso, os componentes de postergação também podem aumentar o alcance do seu público, permitindo mais tempo para que ele atenda aos critérios do componente.

### Testes

Ao criar suas jornadas de usuário, você também pode querer testar qual é a jornada mais eficaz no Canvas. Com as [Jornadas do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step), você pode testar múltiplas jornadas do Canvas em qualquer etapa. Você também pode usar as conexões entre etapas como uma pré-visualização de alto nível. Conexões em laranja indicam que a etapa anterior avançará os usuários imediatamente para a próxima etapa.

### Integração

Quer sincronizar com os dados primários de usuários da sua marca? Aproveite as opções de sincronização de público disponíveis para [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) e [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).