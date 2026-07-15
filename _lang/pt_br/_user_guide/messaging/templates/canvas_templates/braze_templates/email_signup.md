---
nav_title: Cadastro de e-mail com double opt-in
article_title: Cadastro de e-mail com double opt-in
page_order: 2
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para expandir seu alcance com cadastros de e-mail verificados."
tool: Canvas
---

# Cadastro de e-mail com double opt-in {#email-sign-up-with-double-opt-in}

> Use o modelo de cadastro de e-mail com double opt-in para expandir seu alcance com cadastros de e-mail verificados. Direcione novos usuários para capturar seus e-mails, confirmar suas inscrições e receber um código de promoção, tudo em uma única jornada integrada.

Este artigo vai guiar você por um caso de uso do modelo **Cadastro de e-mail com double opt-in**, projetado para a etapa de consideração do ciclo de vida do usuário. Ao final, você terá criado um Canvas que envia e-mails e mensagens no app para os usuários quando eles iniciam uma sessão ou quando não concluíram sua integração.

## Pré-requisitos {#prerequisites}

Para usar este modelo com sucesso, você precisa do seguinte:

- Uma [mensagem no app com várias páginas]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page) com uma página para capturar os e-mails dos seus usuários e outra para comunicar uma mensagem de sucesso.
- Um e-mail de confirmação para os usuários verificarem seu endereço de e-mail.
- Um e-mail de boas-vindas com um código de promoção exclusivo para os usuários que fizerem o double opt-in.

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que você trabalha para a Steppington, um app de saúde conhecido por recursos como rastreamento de calorias, aulas de exercícios digitais e maratonas relâmpago. Antes de criar o Canvas, você [configura mensagens no app e no navegador com várias páginas]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page) que incluem uma série de perguntas envolventes para determinar a experiência e a impressão da primeira interação do usuário com o app.

Para acessar o modelo, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Email sign-up with double opt-in**, selecione **Apply Template**. Agora, podemos percorrer o modelo para adaptá-lo às nossas necessidades.

### Etapa 1: Configure os detalhes {#step-1-set-up-the-details}

Ajuste os detalhes do Canvas para refletir seu objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele é direcionado a novos usuários quando eles usam o app pela primeira vez.
3. Atualize a descrição para explicar que este Canvas contém mensagens personalizadas para os usuários fazerem o double opt-in.
4. Adicione a tag **Email** para que possamos filtrá-lo na página inicial do Canvas.

![O novo nome, descrição e tag do Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Etapa 2: Atribua eventos de conversão {#step-2-assign-conversion-events}

Em seguida, atribua nossos eventos de conversão. Eventos de conversão são um tipo de métrica que você pode usar para medir o sucesso do Canvas. Para **Conversion event type**, selecione **Performs Custom Event**. Em seguida, selecione **email_opt_in** para o **Custom event name**.

![Seção "Assign Conversion Events" para o tipo de evento de conversão de opt-in de e-mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Mantenha o prazo de conversão de três dias do modelo, pois você deseja direcionar seus usuários mais recentes.

### Etapa 3: Adapte o cronograma de entrada {#step-3-tailor-the-entry-schedule}

Mantenha o cronograma de entrada como **Action-Based** para que os usuários entrem no seu Canvas quando iniciarem uma sessão no app. Dessa forma, você pode começar a construir seu relacionamento com engajamento oportuno.

Além disso, considere manter as **Action Based Options** como estão, para que os usuários entrem no Canvas apenas quando iniciarem uma sessão.

![Um cronograma de entrada baseado em ação para inserir no Canvas os usuários que iniciam qualquer sessão.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Para o **Entry Window**, atualize o **Started Time (Required)** para a data e hora desejadas.

![Um período de entrada com horário de início em 16 de janeiro de 2025 às 12h30. Os usuários entrarão nesta mensagem no fuso horário local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Etapa 4: Selecione o público-alvo {#step-4-select-the-target-audience}

Defina seu público-alvo como usuários da Steppington que não possuem um endereço de e-mail em seu perfil de usuário, mantendo o [filtro de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) padrão do modelo `Email Available is false`.

![Público de entrada com o filtro "Email Available is false".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Etapa 5: Selecione suas configurações de envio {#step-5-select-your-send-settings}

Mantenha as configurações de inscrição padrão para enviar apenas para usuários que se inscreveram ou fizeram opt-in para receber mensagens ou notificações, e pule as outras configurações (limite de frequência, horário de silêncio e grupos de teste).

![Opções de envio padrão para enviar apenas para usuários inscritos ou que fizeram opt-in.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Etapa 6: Personalize seu Canvas {#step-6-customize-your-canvas}

Em seguida, construa o Canvas personalizando os canais e o conteúdo que você deseja enviar aos usuários. Como o foco é verificar cadastros de e-mail, você não precisa adicionar ou remover nenhuma das etapas e canais do modelo do Canvas.

1. Selecione a primeira etapa de Mensagem chamada **Email Sign-up**. É aqui que você atualiza o modelo para usar nossa mensagem no app (e no navegador) com várias páginas.

- A página 1 captura os e-mails.
- A página 2 exibe uma mensagem de confirmação.

![Duas páginas de uma mensagem no app para capturar e-mails dos usuários e exibir uma mensagem de sucesso.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2. A partir daqui, mantenha a etapa de Jornada de ação **Subscribed** como está. Esta etapa divide nossos usuários em dois grupos em um período de um dia:

- Usuários que se inscreveram na Steppington com seu e-mail
- Usuários que não se inscreveram na Steppington com seu e-mail

{:start="3"}
3. Em seguida, substitua o corpo do e-mail pelo nosso e-mail de confirmação com a marca para a etapa de Mensagem **Verify Email**. Isso enviará um e-mail para nossos usuários inscritos e os solicitará a confirmar seu endereço de e-mail e fazer opt-in no nosso envio de mensagens.
4. Mantenha a etapa de Jornada de ação **Confirm Subscription** como está. Esta etapa divide ainda mais nossos usuários entre aqueles que confirmaram seu e-mail e aqueles que não confirmaram, com um período de uma semana.
5. Por fim, atualize a etapa de Mensagem **Welcome + Discount** com nosso e-mail de confirmação que inclui um código de promoção exclusivo.

{% alert note %}
A etapa de Mensagem **Verify Email** é disparada na segunda sessão do usuário. Isso ocorre porque o primeiro evento de início de sessão acionaria o Canvas, mas um segundo início de sessão após o usuário ter alcançado a primeira etapa de Mensagem **Email Sign-up** é necessário para que o usuário seja elegível para acionar a segunda mensagem no app.
{% endalert %}

### Etapa 7: Teste e lance seu Canvas {#step-7-test-and-launch-your-canvas}

Após testar e revisar seu Canvas para garantir que ele funciona conforme esperado, lance-o selecionando **Launch Canvas**.

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para itens a considerar antes e depois de lançar um Canvas.
{% endalert %}