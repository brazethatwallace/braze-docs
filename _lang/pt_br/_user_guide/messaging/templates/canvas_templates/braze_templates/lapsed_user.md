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

Digamos que você trabalha para a MovieCanon, um serviço de streaming com conteúdo exclusivo de filmes e séries. Você pode usar o modelo de usuário inativo para promover vantagens e conteúdo premium para usuários que não visitaram seu app nos últimos 30 dias.

Antes de criar o Canvas, configure a integração [Braze Audience Sync com o Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) para que você possa adicionar dados de usuários da Braze aos públicos do Google e enviar anúncios com base em gatilhos comportamentais, segmentação e muito mais.

Para acessar o modelo de usuário inativo, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Lapsing User**, selecione **Apply Template**. Agora você pode percorrer o modelo para adaptá-lo às suas necessidades.

### Etapa 1: Configure os detalhes {#step-1-set-up-the-details}

Ajuste os detalhes do Canvas para refletir seu objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele envia mensagens aos usuários com promoções e faz uma sincronização de público para aqueles que iniciarem uma sessão.
3. Atualize a descrição para explicar que este Canvas contém vantagens e promoções.
4. Adicione a tag **Lapsing/Retention** para que você possa filtrar este Canvas na página inicial do Canvas.

### Etapa 2: Atribua seus eventos de conversão {#step-2-assign-your-conversion-events}

Atualize o **Evento de conversão primária - A** para direcionar os usuários do seu app (MovieCanon) e deixe o **Evento de conversão primária - B** com o padrão de realizar qualquer compra.

### Etapa 3: Adapte o cronograma de entrada {#step-3-tailor-the-entry-schedule}

Mantenha o cronograma de entrada como **Agendado** e as opções padrão baseadas em tempo, para que o Canvas verifique diariamente se há usuários inativos.

Faça dois ajustes nesta etapa:

1. Selecione uma data e hora de início.
2. Selecione os parâmetros de encerramento como **On a specific date** e uma data dois meses à frente. Neste exemplo, há outro Canvas de usuário inativo que começa após o término deste.

### Etapa 4: Selecione seu público-alvo {#step-4-select-your-target-audience}

Mantenha as configurações padrão para o público de entrada, que direciona usuários que não usaram seu app há mais de 30 dias. Também mantenha os controles de entrada padrão para que os usuários possam reentrar no Canvas após quatro semanas. Isso significa que toda vez que um usuário não visitar seu app por mais de 30 dias seguidos, ele será inserido no Canvas.

### Etapa 5: Selecione suas configurações de envio {#step-5-select-your-send-settings}

Mantenha a maioria das configurações padrão de inscrição:

- Enviar apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações.
- Aplicar suas [regras de limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping) para não sobrecarregar seu público com a quantidade de mensagens que recebem. Neste caso, defina seu limite de frequência para limitar o número de Campaigns ou etapas do Canvas com a tag "Lapsing/Retention" que um usuário pode receber a duas por semana.
- Não enviar mensagens durante o horário de silêncio no horário local do usuário (0h às 8h).

A única configuração a alterar é o que acontece quando uma mensagem é disparada durante o horário de silêncio. Em vez de cancelar a mensagem, selecione **Send at next available time** para que seus usuários não percam nenhuma promoção.

### Etapa 6: Personalize seu Canvas {#step-6-customize-your-canvas}

Agora, construa seu Canvas personalizando as etapas do modelo:

1. Personalize o primeiro e-mail que será enviado a todos os usuários que não visitaram seu app há mais de 30 dias. Neste caso de uso, personalize um e-mail que informa aos usuários que eles desbloquearão novas vantagens ao visitar seu app hoje.

{: start="2"}
2. Personalize o componente de jornada de ação chamado "Start Session?" selecionando seu app para a jornada **Started Session**.

{: start="3"}
3. Mantenha o padrão para a etapa de divisão de decisão chamada "Sessions?", que define o grupo ">1 Session" como usuários que usaram seu app mais de uma vez no último dia do calendário.
4. Personalize a etapa de mensagem para usuários que se enquadram no grupo ">1 Session". Neste caso de uso, agradeça os usuários por visitarem seu app e destaque as vantagens que eles desbloquearam.
5. Certifique-se de que seu Google Audience Sync está configurado na etapa de atualização de público de anúncios, para que você atualize e sincronize os dados dos usuários que tiveram múltiplas sessões após receberem o primeiro e-mail.
6. Mantenha o padrão para o componente de [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/#experiment-paths) chamado "A/B Test". Isso enviará aleatoriamente uma de duas promoções (que você personaliza na próxima etapa) para usuários que tiveram menos de duas sessões.
7. Personalize as duas promoções que serão enviadas aos usuários como parte da jornada experimental. Neste caso de uso, faça uma promoção de 20% para uma assinatura de três meses e outra de 10% para uma assinatura de um mês.

![Etapas do Canvas com jornadas ramificadas com base em quantas sessões um usuário teve.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Etapa 7: Teste e lance o Canvas {#step-7-test-and-launch-the-canvas}

Após testar e revisar seu Canvas para garantir que funciona conforme esperado, lance-o selecionando **Launch Canvas**. Usuários que não visitaram seu app há mais de 30 dias e que se inscreveram em seus canais de envio de mensagens agora receberão e-mails incentivando-os a retornar!

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}