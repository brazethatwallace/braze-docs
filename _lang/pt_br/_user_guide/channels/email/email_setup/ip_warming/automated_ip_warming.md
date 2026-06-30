---
nav_title: Aquecimento de IP automatizado
article_title: Aquecimento de IP automatizado
page_order: 1
page_type: reference
description: "Este artigo de referência cobre o aquecimento de IP automatizado e como monitorar seu aquecimento de IP."
channel: email
---

# Aquecimento de IP automatizado {#automated-ip-warming}

> Use o aquecimento de IP automatizado para aumentar gradualmente o volume de e-mails de um novo endereço IP e construir a reputação do remetente com os provedores de caixa de entrada.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Automated IP warming' %}

## Como funciona {#how-it-works}

Você pode usar o aquecimento de IP automatizado para aumentar gradualmente seu volume diário de envios, permitindo que os provedores de caixa de entrada aprendam e confiem em seus padrões de envio. Quando você adiciona um domínio ao seu espaço de trabalho, pode selecionar o tile **Automated IP Warming** na seção **Pick up where you left off** do seu dashboard inicial, e esse tile permanece lá por 60 dias.

A Braze envia primeiro para seus assinantes mais engajados, o que permite que o volume diário cresça em um ritmo alinhado às melhores práticas. Em seguida, a Braze rastreia sinais de engajamento e entregabilidade. Se a Braze detectar algum problema, o sistema ajusta automaticamente sua programação.

{% alert note %}
Você pode realizar apenas um aquecimento de IP.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para realizar o aquecimento de IP automatizado, você deve ter o seguinte:

- Subdomínio verificado e endereços IP ativos
- Permissões para visualizar e iniciar um aquecimento de IP
    - "View Usage Data" para visualizar a seção de aquecimento de IP
    - "View Email Templates" para visualizar e selecionar os modelos de e-mail para o aquecimento de IP
    - "Manage Email Settings" para iniciar o aquecimento de IP
- "Access Campaigns"
- "Approve and Deny Campaigns" se o fluxo de aprovação para Campaigns estiver ativado
    - A Braze aprova automaticamente as campanhas criadas a partir do aquecimento de IP automatizado em seu nome.

## Configurar um plano de aquecimento de IP automatizado {#set-up-an-automated-ip-warming-plan}

### Etapa 1: Definir uma programação {#step-1-set-a-schedule}

1. Na seção **Sending information**, selecione o **From address** para aquecer os endereços IP.
2. Insira o volume de envio diário atual e o volume de envio desejado.
3. Selecione a data de início do aquecimento de IP automatizado. Essa data deve ser pelo menos um dia após o lançamento do plano.
4. Insira o horário de envio. As mensagens são enviadas no fuso horário da empresa.
5. Selecione **Next: Segments** para continuar a configuração.

![Exemplo de detalhes da programação.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Etapa 2: Selecionar e classificar segmentos {#step-2-select-and-rank-segments}

1. Em seguida, selecione os segmentos a serem direcionados. Durante o aquecimento de IP, a Braze começa enviando para seus usuários com maior engajamento e aumenta gradualmente o volume de envio ao longo do tempo, adicionando lentamente segmentos com menor engajamento.
2. Depois, arraste e solte os segmentos para classificá-los de alto a baixo engajamento. Alto engajamento inclui destinatários que abrem e clicam consistentemente nos seus e-mails. Baixo engajamento inclui destinatários que são inconsistentes no engajamento com seus e-mails ou que não interagem com seus e-mails há muito tempo.
3. Selecione **Next: Messages** para continuar a configuração.

![Dois segmentos selecionados como alvo para o aquecimento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Etapa 3: Selecionar as mensagens a enviar {#step-3-select-the-messages-to-send}

1. Selecione **Select email templates**.
2. Escolha os modelos de e-mail para as mensagens a serem enviadas. O conteúdo que você envia durante o aquecimento de IP deve incentivar aberturas e cliques. Recomendamos escolher conteúdo que teve boa recepção no passado. Por exemplo, você pode usar ofertas promocionais para incentivar engajamento imediato e compras.
3. Selecione **Select templates**. A Braze calcula o número de modelos necessários antes que você possa iniciar. Recomendamos fornecer mais modelos do que o mínimo necessário para permitir que o sistema se ajuste a problemas de entregabilidade sem parar.
4. Após adicionar o número necessário de modelos, selecione **Next: Summary**.

{% alert important %}
Alterações feitas nas campanhas criadas a partir da ferramenta de aquecimento de IP (como alterar a data programada, segmento ou volume) não são refletidas na página **Summary** do aquecimento de IP.
{% endalert %}

### Etapa 4: Selecionar eventos de conversão {#step-4-select-conversion-events}

Você pode definir até quatro dos seguintes eventos de conversão para rastrear. Esses eventos de conversão não podem ser atualizados após o lançamento do plano de aquecimento de IP automatizado.

- Inicia sessão
- Realiza pedido
- Realiza evento personalizado
- Faz upgrade do app
- Abre e-mail
- Clica no e-mail

Em seguida, selecione o prazo de conversão, que é o tempo máximo que pode passar entre um usuário entrar em uma campanha e o evento de conversão.

![Configurações de conversão mostrando a seleção de evento de conversão e o prazo de conversão.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Etapa 5: Revisar e lançar {#step-5-review-and-launch}

Revise os detalhes do seu plano de aquecimento de IP. Em seguida, selecione **Launch**.

## Durante o aquecimento de IP ativo {#during-active-ip-warming}

As campanhas de aquecimento de IP são criadas com 1 a 2 dias de antecedência, a menos que você esteja iniciando um aquecimento de IP para o dia seguinte. Essas campanhas são nomeadas automaticamente com o seguinte formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Quando a meta de envio diário é atingida, o sistema para de enviar naquele dia para proteger sua reputação.

O sistema monitora a integridade com base nos seguintes benchmarks do setor:

- Taxa de entrega cai para 90% ou menos
- Taxa de abertura menor que 10%
- Bounces maiores que 5%
- Taxas de relatório de spam maiores que 0,04%

Se as estatísticas estiverem abaixo dos nossos benchmarks, o sistema mantém o volume no dia seguinte em vez de aumentá-lo, para mitigar riscos à reputação do remetente.

## Parar um plano de aquecimento de IP {#stop-an-ip-warmup-plan}

A Braze permite que você pare o aquecimento de IP e a criação de campanhas futuras. Porém, se uma campanha já estiver ativa ou programada para as próximas 24 a 48 horas, pode ser necessário parar a campanha específica manualmente. Parar um plano de aquecimento de IP também para todas as campanhas associadas.

No entanto, quando parado, o aquecimento de IP não pode ser retomado. Em vez disso, você precisa configurar um novo plano para continuar de onde parou:

- Baixe os dados existentes do seu plano parado para manter em seus registros, pois ao iniciar um novo aquecimento de IP, o rastreador anterior será removido
- Atualize o **Current daily send volume** para o volume mais recente
- Adicione um filtro a um segmento se você planeja usar o mesmo segmento do último aquecimento de IP, excluindo usuários que já receberam campanhas anteriores

## Quando um aquecimento de IP é concluído {#when-an-ip-warmup-completes}

O aquecimento de IP é marcado como concluído quando o último dia de aquecimento de IP termina à meia-noite no fuso horário da sua empresa. Por exemplo, se a última campanha enviada no plano de aquecimento de IP é enviada às 20h, o plano é marcado como concluído após quatro horas.

O rastreador permanece na página inicial por 90 dias após o término do plano. Após 90 dias, o rastreador é removido. O download dos dados inclui estas métricas padrão de e-mail:

- _Enviados_
- _Entregues_
- _Bounces_
- _Relatórios de spam_
- _Total de aberturas_
- _Aberturas únicas_
- _Cliques_
- _Cancelamentos de inscrição_

Se um dia incluir múltiplas campanhas usadas para atingir os requisitos de volume, elas são agregadas na visualização diária.

![Rastreador de aquecimento de IP com volume de envio para a semana de 16 de janeiro.]({% image_buster /assets/img/automated_ip_warming_example.png %})