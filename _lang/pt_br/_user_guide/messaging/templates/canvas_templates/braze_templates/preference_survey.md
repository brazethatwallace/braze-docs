---
nav_title: Integração com pesquisa de preferências
article_title: Integração com pesquisa de preferências
page_order: 5.5
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para impulsionar a adoção inicial com um fluxo de integração guiado que apresenta novos usuários à sua marca e coleta preferências para mantê-los engajados a longo prazo."
tool: Canvas
---

# Integração com pesquisa de preferências {#onboarding-with-preferences-survey}

> Use o modelo de integração com pesquisa de preferências para criar um fluxo de integração guiado que direciona novos usuários. Apresente-os à sua marca, ajude-os a começar e colete suas preferências para mantê-los engajados a longo prazo.

Este artigo vai guiar você por um caso de uso do modelo **Onboarding with preferences survey**, projetado para a etapa de consideração do ciclo de vida do usuário. Ao final, você terá criado um Canvas que envia e-mails e mensagens no app para os usuários quando eles iniciam uma sessão e quando não concluíram sua integração.

## Pré-requisitos {#prerequisites}

Para usar este modelo com sucesso, você vai precisar do seguinte:

- Um e-mail de boas-vindas que incentive os usuários a iniciar a integração.
- Um e-mail de acompanhamento com dicas para começar a usar o app, destinado aos usuários que concluíram a integração.
- Um e-mail de acompanhamento para incentivar os usuários a concluir a integração.
- Uma [pesquisa]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/simple_survey/) com múltiplas perguntas para determinar as preferências dos usuários.

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que trabalhamos para a StyleRyde, um app de transporte sob demanda que leva as pessoas aonde precisam ir. Antes de criar o Canvas, [configuramos uma pesquisa simples]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) que inclui uma série de perguntas envolventes para determinar a experiência e a impressão da primeira corrida do usuário com o app.

Para acessar o modelo, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Onboarding with preferences survey**, selecione **Apply Template**. Agora podemos percorrer o modelo e adaptá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes {#step-1-set-up-the-details}

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele é direcionado a novos usuários quando usam o app pela primeira vez.
3. Atualize a descrição para explicar que este Canvas contém mensagens personalizadas.
4. Adicione a tag **Onboarding** para que possamos filtrá-lo na página inicial do Canvas.

![O novo nome, descrição e tag do Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Etapa 2: Atribuir eventos de conversão {#step-2-assign-conversion-events}

Atualize o **Primary Conversion Event - A** para **Performs Custom Event**. Em seguida, selecione **Last Used App** como o evento personalizado.

![Last Used App como o nome do evento personalizado selecionado para o evento de conversão.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Etapa 3: Adaptar o cronograma de entrada {#step-3-tailor-the-entry-schedule}

Vamos manter o cronograma de entrada como **Action-Based** para que os usuários entrem no Canvas quando iniciarem uma sessão no app. Dessa forma, podemos começar a construir nosso relacionamento com engajamento oportuno.

Faremos uma atualização nesta seção, ajustando o **Entry Window** para a data e hora desejadas.

![Seção "Entry Window" com o horário de início em 30 de janeiro de 2025 às 12h.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Etapa 4: Selecionar o público-alvo {#step-4-select-the-target-audience}

Vamos manter o público-alvo como está para direcionar nossos usuários que usaram o app StyleRyde pela primeira vez há menos de um dia.

![O filtro "First used these apps less than 1 days ago" selecionado para direcionar o público de entrada.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Etapa 5: Selecionar as configurações de envio {#step-5-select-your-send-settings}

Vamos manter as configurações de inscrição padrão, enviando apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações, com o horário de silêncio ativado, e pular as outras configurações (limite de frequência e grupos de teste).

![Seção "Send Settings" com as configurações de inscrição para usuários inscritos ou que optaram por receber, com horário de silêncio ativado entre 0h e 20h.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Etapa 6: Personalizar seu Canvas {#step-6-customize-your-canvas}

Agora vamos construir nosso Canvas personalizando o conteúdo que será enviado aos usuários.

1. Na primeira etapa de mensagem **Welcome Email**, vamos atualizar esta etapa para incluir nosso e-mail de boas-vindas da StyleRyde.
2. Em seguida, vamos manter a etapa de jornada de ação como está. Essa etapa divide nossos usuários em dois grupos em um período de três dias:

- Usuários que iniciaram uma sessão ou clicaram no e-mail de integração
- Usuários que não iniciaram uma sessão nem clicaram no e-mail de integração

![Uma etapa de jornada de ação dividida em duas jornadas, uma para usuários que iniciaram uma sessão e outra para o restante do público.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

A partir daqui, vamos direcionar nossos usuários e mensagens com base nos grupos mencionados.

#### Direcionar seus usuários engajados {#target-your-engaged-users}

Para os usuários que iniciaram uma sessão ou interagiram com nosso e-mail de integração da primeira etapa de mensagem, vamos atualizar a etapa de mensagem **Getting Started Tips** para incluir as dicas essenciais de viagem e segurança para nossos novos usuários da StyleRyde.

Depois que um usuário concluir a integração, ele sairá do Canvas.

Em seguida, atualize a etapa de mensagem **Content Preferences Survey** para incluir nossa pesquisa de preferências que solicita aos usuários que selecionem os tópicos sobre os quais desejam receber informações no futuro.

![Uma pré-visualização da pesquisa de preferências que solicita aos usuários que selecionem todos os interesses aplicáveis.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Incentivar usuários que não iniciaram a integração {#nudge-users-who-havent-started-onboarding}

Para os demais usuários, vamos atualizar a etapa de mensagem **Winback Nudge** com nosso e-mail de acompanhamento para incentivar os usuários a concluir a integração.

Como nossa última etapa de reengajamento, vamos renomear **Step 2** para **Final Winback Nudge** e atualizar a etapa com nossa mensagem no app para incentivar nossos novos usuários a concluir a integração.

### Etapa 7: Testar e lançar seu Canvas {#step-7-test-and-launch-your-canvas}

Depois de testar e revisar nosso Canvas para garantir que funciona como esperado, vamos lançá-lo selecionando **Launch Canvas**.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}