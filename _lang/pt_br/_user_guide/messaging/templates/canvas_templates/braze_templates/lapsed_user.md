---
nav_title: Usuário inativo
article_title: Usuário inativo
page_order: 4
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para trazer os usuários de volta ao seu app com incentivos baseados em seus engajamentos anteriores."
tool: Canvas
---

# Usuário inativo {#lapsed-user}

> Use o modelo de usuário inativo para lembrar os usuários do valor que sua marca oferece a eles e incentivar seu retorno com ofertas empolgantes e incentivos baseados em seus engajamentos anteriores.

Este artigo vai guiar você por um caso de uso do modelo **Usuário inativo**, que foi projetado para a etapa de retenção e fidelidade do ciclo de vida do usuário. Ao final, você terá criado um Canvas que incentiva os usuários a retornarem ao seu app com promoções que variam de acordo com o comportamento deles, como se iniciaram uma sessão no seu app após receberem uma mensagem promocional.

## Pré-requisitos {#prerequisites}

Para usar o modelo de usuário inativo com sucesso, você precisa configurar o [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) com os parceiros e públicos que você utiliza.

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que trabalhamos para a MovieCanon, um serviço de streaming que tem conteúdo exclusivo de filmes e séries. Podemos usar o modelo de usuário inativo para promover vantagens e conteúdo premium para usuários que não visitaram nosso app nos últimos 30 dias.

Antes de criar o Canvas, configuramos a integração [Braze Audience Sync com o Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) para que possamos adicionar dados de usuários da Braze aos públicos do Google e enviar anúncios com base em gatilhos comportamentais, segmentação e muito mais.

Para acessar o modelo de usuário inativo, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Lapsing User**, selecione **Apply Template**. Agora, podemos percorrer o modelo para adaptá-lo às nossas necessidades.

### Etapa 1: Configure os detalhes {#step-1-set-up-the-details}

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele enviará mensagens aos usuários com promoções e fará uma sincronização de público para aqueles que iniciarem uma sessão.
3. Atualize a descrição para explicar que este Canvas contém vantagens e promoções.
4. Adicione a tag **Lapsing/Retention** para que possamos filtrar este Canvas na página inicial do Canvas.

![Etapa "Configurar detalhes do Canvas" com o nome "Lapsed User - Visit App" e uma breve descrição do Canvas.]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### Etapa 2: Atribua seus eventos de conversão {#step-2-assign-your-conversion-events}

Atualize o **Evento de conversão primária - A** para direcionar os usuários do nosso app (MovieCanon) e deixe o **Evento de conversão primária - B** com o padrão de realizar qualquer compra.

![Seção "Atribuir eventos de conversão" com um evento de conversão primária de um usuário iniciando uma sessão em um app específico.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### Etapa 3: Adapte o cronograma de entrada {#step-3-tailor-the-entry-schedule}

Vamos manter o cronograma de entrada como **Agendado** e as opções padrão baseadas em tempo, para que o Canvas verifique diariamente se há usuários inativos.

Faremos dois ajustes nesta etapa:

1. Selecione uma data e hora de início.
2. Selecione os parâmetros de encerramento como **On a specific date** e uma data dois meses à frente. Digamos que temos outro Canvas de usuário inativo que queremos iniciar após este.

![Etapa "Cronograma de entrada" para um Canvas agendado que insere os usuários em um horário designado.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### Etapa 4: Selecione nosso público-alvo {#step-4-select-our-target-audience}

Vamos manter as configurações padrão para o público de entrada, que está definido para usuários que não usaram nosso app há mais de 30 dias. Também manteremos os controles de entrada padrão para que os usuários possam reentrar no Canvas após quatro semanas. Isso significa que toda vez que um usuário não visitar nosso app por mais de 30 dias seguidos, ele será inserido no Canvas.

![Etapa "Público-alvo" direcionando usuários que usaram os apps pela última vez há 30 dias.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### Etapa 5: Selecione suas configurações de envio {#step-5-select-your-send-settings}

Vamos manter a maioria das configurações padrão de inscrição:

- Enviar apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações.
- Aplicar nossas [regras de limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping) para não sobrecarregar nosso público com a quantidade de mensagens que recebem. Neste caso, definimos nosso limite de frequência para limitar o número de Campaigns ou etapas do Canvas com a tag "Lapsing/Retention" que um usuário pode receber a duas por semana.
- Não enviar mensagens durante o horário de silêncio no horário local do usuário (0h às 8h).

A única configuração que vamos alterar é o que fazer quando uma mensagem é disparada durante o horário de silêncio. Em vez de cancelar a mensagem, selecione **Send at next available time** para que nossos usuários não percam nenhuma promoção.

![Seção "Horário de silêncio" com horário de início às 0h e horário de término às 8h.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### Etapa 6: Personalize seu Canvas {#step-6-customize-your-canvas}

Agora, vamos construir nosso Canvas personalizando as etapas do modelo:

1. Personalize o primeiro e-mail que será enviado a todos os usuários que não visitaram nosso app há mais de 30 dias. Para nosso caso de uso, vamos personalizar um e-mail que informa aos usuários que eles desbloquearão novas vantagens ao visitar nosso app hoje.

![Etapa de mensagem do Canvas para um e-mail que informa aos usuários para desbloquearem novas vantagens ao visitar hoje.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2. Personalize o componente de jornada de ação chamado "Start Session?" selecionando nosso app para a jornada **Started Session**.

![Jornada de ação para sessões iniciadas em um app específico.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3. Mantenha o padrão para a etapa de divisão de decisão chamada "Sessions?", que define o grupo ">1 Session" como usuários que usaram nosso app mais de uma vez no último dia do calendário.
4. Personalize a etapa de mensagem para usuários que se enquadram no grupo ">1 Session". No nosso caso de uso, vamos agradecer os usuários por visitarem nosso app e destacar as vantagens que eles desbloquearam.
5. Certifique-se de que nosso Google Audience Sync está configurado na etapa de atualização de público de anúncios, para que atualizemos e sincronizemos os dados dos usuários que tiveram múltiplas sessões após receberem nosso primeiro e-mail.
6. Mantenha o padrão para o componente de [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/#experiment-paths) chamado "A/B Test". Isso enviará aleatoriamente uma de duas promoções (que personalizaremos na próxima etapa) para usuários que tiveram menos de duas sessões.
7. Personalize as duas promoções que serão enviadas aos usuários como parte da jornada experimental. No nosso caso de uso, faremos uma promoção de 20% para uma assinatura de três meses e outra de 10% para uma assinatura de um mês.

![Etapas do Canvas com jornadas ramificadas com base em quantas sessões um usuário teve.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Etapa 7: Teste e lance o Canvas {#step-7-test-and-launch-the-canvas}

Após testar e revisar nosso Canvas para garantir que funciona conforme esperado, vamos lançá-lo selecionando **Launch Canvas**. Agora, nossos usuários que não visitaram nosso app há mais de 30 dias e que se inscreveram em nossos canais de envio de mensagens receberão e-mails incentivando-os a retornar!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}