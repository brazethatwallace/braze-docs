---
nav_title: Integração
article_title: Integração
page_order: 5
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para criar jornadas de integração que promovam uma adoção inicial sólida e incentivem relacionamentos duradouros com seus usuários."
tool: Canvas
---

# Integração {#onboarding}

> Inicie a jornada dos seus usuários com este modelo de integração. Este modelo foi projetado para promover uma adoção inicial sólida e incentivar relacionamentos duradouros com seus usuários. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, você pode apresentar seus usuários à sua marca de forma fluida e dar início a um relacionamento duradouro.

Neste artigo, vamos guiar você por um caso de uso do modelo **Integração**, destinado à etapa de consideração do ciclo de vida do usuário, para criar uma jornada de integração fluida para novos usuários. Ao final deste artigo, você terá personalizado este modelo de Canvas da Braze com mensagens personalizadas para esses novos usuários.

## Pré-requisitos {#prerequisites}

Antes de usar este modelo, você precisa criar os seguintes [modelos de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template/) para referenciá-los no Canvas:

- Um e-mail de boas-vindas para todos os usuários do seu app
- Um e-mail com dicas sobre como usar seu app
- Um e-mail de feedback que inclua uma pesquisa com o usuário

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que trabalhamos na PantsLabyrinth e nosso objetivo é aumentar o engajamento dos usuários, construir confiança e fidelidade com eles e incentivá-los a permanecer engajados. Para isso, queremos focar na criação de mensagens direcionadas a novos usuários que ainda não interagiram com o app.

Para acessar o modelo de integração, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Onboarding**, selecione **Apply Template**. Vamos começar a personalizar este modelo para o nosso caso de uso.

### Etapa 1: Configure os detalhes {#step-1-set-up-the-details}

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele é destinado à integração de novos usuários.
3. Atualize a descrição para especificar que o Canvas mapeia uma jornada do usuário que promove confiança e fidelidade.
4. Adicione a tag **Onboarding** para que possamos filtrá-lo na página inicial do Canvas.

![O novo nome, descrição e tag do Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Etapa 2: Atribua seus eventos de conversão {#step-2-assign-your-conversion-events}

Em seguida, vamos atribuir nossos eventos de conversão. Eventos de conversão são um tipo de métrica que pode ser usada para medir o sucesso do Canvas. Em **Custom event name**, selecione **Email Click** como o evento personalizado.

![Evento de conversão primária - A com o tipo de conversão "Performs Custom Event" com o nome de evento personalizado "Email Click". Há um prazo de conversão de 4 dias.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Isso significa que os novos usuários têm até quatro dias para clicar no e-mail de boas-vindas. Neste caso, queremos que nossos novos usuários sintam um senso de urgência para interagir com a PantsLabyrinth e assinar uma entrega recorrente de roupas sazonais.

### Etapa 3: Defina um cronograma de entrada {#step-3-set-an-entry-schedule}

Como o objetivo é direcionar novos usuários da PantsLabyrinth, manteremos o Canvas como baseado em ação. Em **Start Session**, selecione **Start Session in Any App** para permitir que usuários que iniciem uma sessão em qualquer app entrem no Canvas.

Em seguida, ajuste o **Entry Window** para determinar quando os usuários podem entrar no Canvas. Digamos que há um lançamento de assinatura da PantsLabyrinth previsto para o final de outubro. É aqui que definiremos o horário de início como **28/10/2024 às 8h**. Opcionalmente, também podemos permitir que os usuários entrem no Canvas no horário local deles.

![Um período de entrada com horário de início em 28 de outubro de 2024 às 8h. Os usuários entrarão nesta mensagem no horário local deles.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Etapa 4: Direcione seu público {#step-4-target-your-audience}

Ao direcionar o público certo, podemos interagir de forma eficaz com novos usuários. Por exemplo, este modelo direciona todos os usuários que usaram um app pela primeira vez há menos de um dia, o que é adequado para o nosso caso de uso. Então, vamos manter esta seção como está.

### Etapa 5: Defina as configurações de envio {#step-5-set-send-settings}

Por padrão, este Canvas é enviado para usuários que estão inscritos ou que optaram por receber mensagens e segue as regras do limite de frequência. Vamos manter essas configurações como estão.

### Etapa 6: Personalize seu Canvas {#step-6-customize-your-canvas}

Agora, vamos construir o Canvas personalizando as etapas do modelo.

#### Configure o e-mail de boas-vindas {#set-up-the-welcome-email}

1. Selecione a etapa de mensagem chamada "Welcome Email".
2. Selecione **Edit message** para substituir o e-mail do modelo pelo nosso e-mail de boas-vindas.
3. Selecione **Done**.

Agora, nossos usuários receberão este e-mail de boas-vindas depois de iniciarem uma sessão no nosso app. Para não sobrecarregar os usuários com mensagens repetidas, recomendamos usar a etapa de postergação como parte da jornada do usuário.

#### Personalize a jornada do público {#customize-the-audience-path}

Na etapa de jornada do público chamada **Audience Split**, podemos personalizar o filtro para nossos usuários engajados. No modelo, o filtro é **Has clicked email for step Welcome Email**, o que significa que os usuários são divididos em dois grupos: usuários que clicaram no e-mail de boas-vindas e aqueles que não clicaram.

![Uma etapa de divisão de público com uma jornada para usuários engajados e outra para o restante do público.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

Como varejista de roupas online, a PantsLabyrinth também tem um grupo ativo de usuários mobile. Então, em um Canvas de integração separado, também podemos selecionar o seguinte filtro para identificar e dividir nossos usuários mobile nesses segmentos:

- **Has clicked content card for step Welcome Content Card**
- **Everyone Else**

#### Direcione mais usuários com jornadas do público {#target-more-users-with-audience-paths}

A partir do conjunto de usuários que não interagiram com nosso app, podemos direcionar ainda mais esses usuários editando a etapa "Check for Clicks" e a etapa "Winback Nudge".

### Etapa 7: Teste e lance seu Canvas {#step-7-test-and-launch-your-canvas}

Depois de testar e revisar nosso Canvas para garantir que ele funciona como esperado, selecione **Launch Canvas** para lançar o Canvas. Agora, podemos oferecer aos nossos novos usuários uma experiência de integração personalizada para incentivar um relacionamento duradouro!

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}