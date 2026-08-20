---
nav_title: Aquecimento de IP automatizado
article_title: Aquecimento de IP automatizado
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o aquecimento de IP automatizado e como monitorar seu aquecimento de IP."
channel: email
---

# Aquecimento de IP automatizado {#automated-ip-warming}

> Use o aquecimento de IP automatizado para aumentar gradualmente o volume de e-mails de novos IPs dedicados e construir a reputação do remetente com os provedores de caixa de entrada. Para perguntas frequentes, consulte as [Perguntas frequentes sobre aquecimento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

## Como funciona {#how-it-works}

Você pode usar o aquecimento de IP automatizado para aumentar gradualmente seu volume de envio diário, permitindo que os provedores de caixa de entrada aprendam e confiem nos seus padrões de envio. Ao adicionar um domínio ao seu espaço de trabalho, você pode selecionar o bloco **Automated IP Warming** na seção **Pick up where you left off** do seu dashboard inicial. Esse bloco permanece visível por 60 dias enquanto seu espaço de trabalho está na janela de integração de novo remetente, e fica oculto depois que você conclui pelo menos um plano.

Cada plano de aquecimento de IP automatizado está vinculado a um endereço de remetente. Esse endereço de remetente é mapeado para um subdomínio de envio e um pool de IP. Se o pool contiver vários IPs dedicados, a Braze faz o aquecimento de todos juntos em um único plano.

A Braze envia primeiro para seus inscritos com maior engajamento, o que permite que o volume diário cresça em um ritmo alinhado às melhores práticas. Em seguida, a Braze monitora sinais de engajamento e entregabilidade. Se a Braze detectar algum problema, o sistema ajusta seu cronograma automaticamente.

Depois de concluir pelo menos um plano, você pode visualizar os planos concluídos em **Settings** > **Email Preferences** > **Automated IP warming**.

## Pré-requisitos {#prerequisites}

Para realizar o aquecimento de IP automatizado, você precisa ter o seguinte:

- Subdomínio verificado e endereços IP ativos
- Permissões para visualizar e configurar um plano:
    - "View Email Settings" para visualizar planos de aquecimento de IP e o widget do dashboard principal
    - "View Email Templates" para selecionar modelos de e-mail
    - "View Segments" para selecionar Segments
- Permissões para iniciar um plano:
    - "Edit Email Settings"
    - "Edit Campaigns"
    - "Launch Campaigns"
    - "Approve Campaigns"

{% alert note %}
Se o fluxo de trabalho de aprovação de Campaigns estiver ativado, a Braze aprova automaticamente as Campaigns criadas pelo aquecimento de IP automatizado em seu nome.
{% endalert %}

## Configure um plano automatizado de aquecimento de IP {#set-up-an-automated-ip-warming-plan}

### Etapa 1: Defina um cronograma {#step-1-set-a-schedule}

1. Insira um **Nome do plano** exclusivo. Os nomes de plano podem conter apenas letras, números, hifens e underscores, e devem ser exclusivos no seu espaço de trabalho. É necessário informar um nome de plano antes de fazer o lançamento.
2. Na seção **Informações de envio**, selecione o **Endereço de remetente** para aquecer os endereços IP. A Braze exibe o **Pool de IP** associado e o número de **Endereços IP no pool** para esse endereço de remetente.
3. Insira o **Volume de envio diário atual** e o **Volume de envio desejado**. A Braze sugere um volume de envio desejado de até 2 milhões de envios por IP no pool selecionado. Se o seu volume de envio diário atual for 0, o primeiro dia do seu cronograma começa com até 50 envios por IP, limitado a 500 no total.
4. Selecione a data de início do aquecimento de IP automatizado. Essa data deve ser pelo menos um dia após o lançamento do plano.
5. Insira o horário de envio. As mensagens são enviadas no fuso horário do espaço de trabalho (ou no fuso horário da empresa, caso o espaço de trabalho não tenha uma substituição configurada).
6. Selecione **Próximo: Segments** para continuar a configuração.

![Exemplo de detalhes do cronograma.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Etapa 2: Selecione e classifique os segments {#step-2-select-and-rank-segments}

1. Em seguida, selecione os segments a serem direcionados. Durante o aquecimento de IP, a Braze começa enviando para os usuários com maior engajamento e aumenta gradualmente o volume de envio ao longo do tempo, adicionando lentamente segments com menor engajamento.
2. Depois, arraste e solte os segments para classificá-los do maior para o menor engajamento. Alto engajamento inclui destinatários que abrem e clicam consistentemente nos seus e-mails. Baixo engajamento inclui destinatários que são inconsistentes no engajamento com seus e-mails ou que não interagem com seus e-mails há muito tempo.
3. Selecione **Próximo: Mensagens** para continuar a configuração.

![Dois segments selecionados para direcionar no aquecimento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Etapa 3: Selecione as mensagens a serem enviadas {#step-3-select-the-messages-to-send}

1. Selecione **Selecionar modelos de e-mail**.
2. Escolha os modelos de e-mail para as mensagens a serem enviadas. O conteúdo que você envia durante o aquecimento de IP deve incentivar aberturas e cliques. Recomendamos escolher conteúdos que tiveram boa recepção no passado. Por exemplo, você pode usar ofertas promocionais para incentivar engajamento e compras imediatas.
3. Selecione **Selecionar modelos**. A Braze calcula o número de modelos necessários antes de você poder fazer o lançamento. Recomendamos fornecer mais modelos do que o mínimo necessário para permitir que o sistema se ajuste a problemas de entregabilidade sem interromper o processo.
4. Após adicionar o número necessário de modelos, selecione **Próximo: Resumo**.

{% alert important %}
Alterações feitas nas Campaigns criadas a partir da ferramenta de aquecimento de IP (como alterar a data agendada, o segment ou o volume) não são refletidas na página de **Resumo** do aquecimento de IP.
{% endalert %}

### Etapa 4: Selecione os eventos de conversão {#step-4-select-conversion-events}

Você pode definir até quatro dos seguintes eventos de conversão para rastrear. Esses eventos de conversão não podem ser atualizados após o lançamento do plano automatizado de aquecimento de IP.

- Inicia sessão
- Faz pedido
- Realiza evento personalizado
- Faz upgrade do app
- Abre e-mail
- Clica no e-mail

Em seguida, selecione o prazo de conversão, que é o tempo máximo que pode passar entre a entrada de um usuário em uma Campaign e o evento de conversão.

![Configurações de conversão mostrando a seleção de evento de conversão e o prazo de conversão.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Etapa 5: Revise e lance {#step-5-review-and-launch}

Revise os detalhes do seu plano de aquecimento de IP. Em seguida, selecione **Lançar**.

## Aquecimento de múltiplos IPs {#multiple-ip-warming}

Use vários planos automatizados de aquecimento de IP quando precisar aquecer mais de um endereço de remetente ou pool de IP.

| Cenário | Recomendação |
| --- | --- |
| Múltiplos IPs dedicados em um pool de IP | Crie um plano e selecione o endereço de remetente para esse pool |
| Múltiplos pools de IP ou endereços de remetente | Crie um plano separado para cada endereço de remetente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cenários de aquecimento de múltiplos IPs" }

### Aquecer múltiplos IPs em um pool {#warm-multiple-ips-in-one-pool}

Quando você seleciona um endereço de remetente na [Etapa 1: Definir um cronograma](#step-1-set-a-schedule), a Braze exibe o pool de IP associado e os endereços IP no pool. A Braze usa a contagem de IPs ao compilar seu cronograma de ramp-up e sugere o volume de envio desejado.

Se o seu **Volume de envio diário atual** for 0, o primeiro dia agendado começa com até 50 envios por IP no pool, limitado a 500 no total. A Braze sugere um **Volume de envio desejado** de até 2 milhões de envios por IP no pool.

### Aquecer múltiplos pools de IP {#warm-multiple-ip-pools}

Para aquecer mais de um endereço de remetente ou pool de IP:

1. Acesse **Configurações** > **Preferências de e-mail** > **Aquecimento automatizado de IP**.
2. Selecione **Novo plano de aquecimento de IP**.
3. Insira um **Nome do plano** exclusivo.
4. Conclua a configuração para esse endereço de remetente.
5. Repita para cada endereço de remetente ou pool de IP adicional que você precisa aquecer.

Acompanhe cada plano na tabela **Aquecimento automatizado de IP**. Cada plano tem seu próprio cronograma, Segments, modelos, Campaigns e rastreador. Os planos podem estar com status **Rascunho**, **Em andamento**, **Concluído** ou **Parado**.

{% alert important %}
Evite enviar Campaigns grandes que não sejam de aquecimento a partir do mesmo endereço de remetente ou pool de IP enquanto um plano automatizado de aquecimento de IP estiver ativo. Envios adicionais durante o aquecimento podem afetar os sinais de entregabilidade e dificultar o isolamento de problemas.
{% endalert %}

## Durante o aquecimento ativo de IP {#during-active-ip-warming}

As campanhas de aquecimento de IP são criadas à meia-noite no fuso horário efetivo para o dia atual e o dia seguinte (0 a 1 dias antes do envio). Ao iniciar um plano, as campanhas futuras também são criadas imediatamente. Essas campanhas são nomeadas automaticamente com o seguinte formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Quando a meta diária de envio é atingida, o sistema para de enviar naquele dia para proteger sua reputação.

A Braze avalia a entregabilidade das campanhas enviadas entre 12 e 20 horas atrás. Se algum dos seguintes limites for ultrapassado, a Braze mantém o volume para o próximo dia de envio em vez de aumentá-lo:

- Taxa de entrega abaixo de 90%
- Taxa de abertura abaixo de 10%
- Taxa de bounce acima de 5%
- Taxa de reclamação de SPAM acima de 0,04%

Para saber o que acontece quando o volume é mantido, consulte [O que acontece quando o volume é mantido?]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq#what-happens-when-volume-is-held).

## Parar um plano de aquecimento de IP {#stop-an-ip-warmup-plan}

Você pode parar um plano de aquecimento de IP para impedir a criação de futuras Campaigns. Parar um plano também desativa todas as Campaigns associadas. Depois de parar um plano, não é possível retomá-lo. Configure um novo plano para continuar de onde parou:

- Baixe os dados existentes do plano interrompido para manter em seus registros
- Atualize o **Volume de envio diário atual** para o volume mais recente
- Adicione um filtro a um Segment se você planeja usar o mesmo Segment do último aquecimento de IP, excluindo os usuários que já receberam Campaigns anteriores

## Quando um aquecimento de IP é concluído {#when-an-ip-warming-completes}

O aquecimento de IP é marcado como concluído quando o último dia do aquecimento de IP termina à meia-noite no fuso horário do seu espaço de trabalho (ou no fuso horário da empresa, se o espaço de trabalho não tiver uma substituição). Por exemplo, se a última Campaign do plano é enviada às 20h, o plano é marcado como concluído à meia-noite, quatro horas depois.

Os planos concluídos permanecem disponíveis em **Settings** > **Email Preferences** > **Automated IP warming**. O rastreador também permanece no dashboard inicial por 90 dias após o término do plano. Após 90 dias, o rastreador do dashboard inicial é removido.

O download dos dados inclui estas métricas padrão de e-mail:

- _Sent_
- _Delivered_
- _Bounces_
- _Spam reports_
- _Total opens_
- _Unique opens_
- _Clicked_
- _Unsubscribed_

Se um dia incluir múltiplas Campaigns usadas para atender aos requisitos de volume, elas serão agregadas na visualização diária.

![Rastreador de aquecimento de IP com volume de envio para a semana de 16 de janeiro.]({% image_buster /assets/img/automated_ip_warming_example.png %})