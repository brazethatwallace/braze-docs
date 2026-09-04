---
nav_title: FAQ
article_title: FAQ sobre aquecimento automatizado de IP
channel: email
page_order: 3
description: "Respostas para perguntas frequentes sobre o aquecimento automatizado de IP na Braze."
---

# FAQ sobre aquecimento automatizado de IP {#automated-ip-warming-faq}

> Respostas para perguntas frequentes sobre o [aquecimento automatizado de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming). Para conceitos de aquecimento de IP e cronogramas manuais, consulte [Aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).

## Quando devo usar o aquecimento de IP automatizado? {#when-should-i-use-automated-ip-warming}

Use o aquecimento de IP automatizado quando precisar:

- Aquecer novos endereços IP pela primeira vez
- Aquecer novas unidades de negócio ou marcas com novos subdomínios
- Reaquecer IPs existentes para melhorar a entregabilidade
- Reaquecer para provedores de caixa de e-mail específicos para melhorar a entregabilidade

Para etapas de configuração e pré-requisitos, consulte [Aquecimento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming).

## Com que antecedência a data de início deve ser definida? {#how-far-in-advance-must-the-start-date-be}

A data de início deve ser amanhã ou posterior no fuso horário do seu espaço de trabalho (ou no fuso horário da empresa, se o espaço de trabalho não tiver uma configuração personalizada).

A Braze cria Campaigns à meia-noite nesse fuso horário para o dia atual e o dia seguinte (0 a 1 dias antes do envio). Ao lançar um plano, as próximas Campaigns também são criadas imediatamente.

## Quantos modelos são necessários? {#how-many-templates-are-required}

A Braze calcula o mínimo a partir dos seus volumes de envio planejados e dos usuários com e-mail habilitado nos Segments selecionados (não o tamanho total do Segment). Forneça mais modelos do que o mínimo para que o sistema possa se ajustar a problemas de entregabilidade sem parar. Para saber mais, consulte [Etapa 3: Selecionar as mensagens para envio]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Posso usar o mesmo Segment para várias tentativas de aquecimento? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

Dentro de um único plano ativo, a Braze exclui automaticamente os usuários que já receberam envios anteriores de aquecimento de IP para o mesmo modelo. Se você parar um plano e iniciar um novo que reutilize os mesmos Segments, adicione um filtro para excluir os usuários que receberam Campaigns do plano anterior.

## Um usuário pode receber mais de um modelo de e-mail no mesmo dia? {#can-a-user-receive-more-than-one-email-template-on-the-same-day}

Sim. A Braze exclui usuários que já receberam um determinado modelo dentro do plano, mas usuários que receberam um modelo diferente continuam elegíveis. Quando o público disponível para o cronograma de um dia se esgota, o plano reinicia o ciclo pelos seus modelos e alguns usuários recebem um segundo modelo naquele dia.

Isso acontece quando o número total de usuários com e-mail disponível nos Segments selecionados é menor que o **Volume de envio desejado**, geralmente no último dia ou nos últimos dias do plano. Por exemplo, com 400.000 usuários com e-mail disponível e um volume de envio desejado de 600.000, cerca de 200.000 usuários recebem dois modelos no último dia. Para evitar isso, mantenha o número total de usuários com e-mail disponível maior ou igual ao volume de envio desejado. Para saber mais, consulte [Tamanho do público e múltiplos envios por usuário]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#audience-size-and-multiple-sends-per-user).

## Posso começar o aquecimento de IP no meio do cronograma? {#can-i-start-ip-warming-mid-schedule}

O aquecimento automatizado de IP sempre cria o cronograma a partir do início da rampa. Para aproximar um início no meio do cronograma, defina **Volume de envio diário atual** com um valor maior que 0, correspondente ao seu volume atual. Quando o volume atual é maior que 0, a Braze não aplica a escala de contagem de IP ao dia 1.

## Qual fuso horário é usado para o envio? {#what-time-zone-is-used-for-sending}

Os envios utilizam o fuso horário do espaço de trabalho quando um está definido; caso contrário, utilizam o fuso horário da empresa. As Campaigns não são criadas no fuso local de cada usuário. Para enviar no fuso local, atualize manualmente as Campaigns criadas pelo plano.

## Quantos planos de aquecimento de IP podem ser executados ao mesmo tempo? {#how-many-ip-warming-plans-can-run-at-the-same-time}

Mais de um plano pode ser executado simultaneamente. Para saber mais, consulte [Aquecimento de IP múltiplo]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming).

## Como o volume escala para pools de IP com múltiplos IPs? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

Quando o **Volume de envio diário atual** é 0, o dia 1 começa pelo menor valor entre 50 envios por IP ou 500 no total. O volume então cresce aproximadamente 1,75 vezes por dia de envio, sujeito a limites de rampa. Por exemplo, com 10 IPs: 500 → 875 → 1.532 → 2.681.

Se você definir um volume atual personalizado maior que 0, o escalonamento por contagem de IPs não será aplicado ao dia 1. Para saber mais sobre planos com múltiplos IPs, consulte [Aquecer múltiplos IPs em um pool]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool).

## O aquecimento de IP automatizado suporta limite de frequência por Campaign? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

Não. Cada Campaign envia no horário configurado sem um limite de frequência por Campaign.

## Quando a Braze retém volume durante o aquecimento de IP? {#when-does-braze-hold-volume-during-ip-warming}

A Braze avalia a entregabilidade de Campaigns enviadas entre 12 e 20 horas atrás. Se as taxas de entrega, abertura, bounce ou reclamações de SPAM ultrapassarem os benchmarks em [Durante o aquecimento de IP ativo]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming), a Braze retém o volume para o próximo dia de envio em vez de aumentá-lo.

## O que acontece quando o volume é retido? {#what-happens-when-volume-is-held}

O volume retido é o ajuste automático que a Braze aplica quando esses limites são ultrapassados. O próximo envio agendado mantém o mesmo volume em vez de avançar. A Braze replaneja as entradas futuras do cronograma, arquiva as Campaigns futuras existentes do plano e cria novas Campaigns para o cronograma atualizado imediatamente. O plano pode levar mais tempo para atingir o volume alvo.

## Por que as edições de Campaign não aparecem no rastreador de aquecimento de IP? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

As alterações que você faz em Campaigns criadas pelo aquecimento de IP automatizado (como cronograma, Segment ou volume) não são sincronizadas de volta com o rastreador de aquecimento de IP. Para notas de configuração relacionadas, consulte [Etapa 3: Selecionar as mensagens para envio]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Posso interromper um plano de aquecimento de IP? {#can-i-stop-an-ip-warming-plan}

Sim. Interromper encerra permanentemente o plano: a Braze desativa as Campaigns vinculadas e não cria novas. Não é possível retomar um plano interrompido — crie um novo plano para continuar. Para saber as etapas de como prosseguir após uma interrupção, consulte [Interromper um plano de aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan).

## Quando um plano de aquecimento de IP é marcado como concluído? {#when-is-an-ip-warming-plan-marked-as-complete}

O plano é marcado como concluído após o término do último dia de envio agendado, à meia-noite no fuso horário efetivo (do espaço de trabalho ou da empresa). Por exemplo, se a última Campaign é enviada às 20h, o plano é marcado como concluído à meia-noite, quatro horas depois.

## Quais dados posso baixar? {#what-data-can-i-download}

A exportação CSV inclui linhas por Campaign com métricas diárias: *Sent*, *Delivered*, *Bounces*, *Spam Reports*, *Total opens*, *Unique opens*, *Clicked* e *Unsubscribed*. A tabela de rastreamento agrega várias Campaigns do mesmo dia em uma visualização diária. Para saber mais, consulte [Quando um aquecimento de IP é concluído]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes).