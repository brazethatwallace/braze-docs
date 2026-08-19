---
nav_title: FAQ
article_title: FAQ sobre aquecimento automatizado de IP
channel: email
page_order: 3
description: "Respostas para perguntas frequentes sobre o aquecimento automatizado de IP na Braze."
---

# FAQ sobre aquecimento automatizado de IP {#automated-ip-warming-faq}

> Respostas para perguntas frequentes sobre o [aquecimento automatizado de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming). Para conceitos de aquecimento de IP e cronogramas manuais, consulte [Aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).

## Quando devo usar o aquecimento automatizado de IP? {#when-should-i-use-automated-ip-warming}

Use o aquecimento automatizado de IP quando você precisar:

- Aquecer novos endereços IP pela primeira vez
- Aquecer novas unidades de negócio ou marcas com novos subdomínios
- Reaquecer IPs existentes para melhorar a entregabilidade
- Reaquecer para provedores de caixa de entrada específicos para melhorar a entregabilidade

Para etapas de configuração e pré-requisitos, consulte [Aquecimento automatizado de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming).

## Com que antecedência a data de início deve ser definida? {#how-far-in-advance-must-the-start-date-be}

A data de início deve ser amanhã ou posterior no fuso horário do seu espaço de trabalho (ou fuso horário da empresa, caso o espaço de trabalho não tenha uma substituição).

A Braze cria Campaigns à meia-noite nesse fuso horário para o dia atual e o dia seguinte (0 a 1 dias antes do envio). Lançar um plano também cria as próximas Campaigns imediatamente.

## Quantos modelos são necessários? {#how-many-templates-are-required}

A Braze calcula o mínimo a partir dos volumes de envio planejados e dos usuários com e-mail habilitado nos Segments selecionados (não o tamanho total do Segment). Forneça mais modelos do que o mínimo para que o sistema possa se ajustar a problemas de entregabilidade sem interromper o processo. Para mais detalhes, consulte [Etapa 3: Selecionar as mensagens para envio]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Posso usar o mesmo Segment para várias tentativas de aquecimento? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

Dentro de um único plano ativo, a Braze exclui automaticamente os usuários que já receberam envios anteriores de aquecimento de IP para o mesmo modelo. Se você parar um plano e iniciar um novo que reutilize os mesmos Segments, adicione um filtro para excluir os usuários que receberam Campaigns do plano anterior.

## Posso iniciar o aquecimento de IP no meio do cronograma? {#can-i-start-ip-warming-mid-schedule}

O aquecimento de IP automatizado sempre constrói o cronograma a partir do início da rampa. Para aproximar um início no meio do cronograma, defina **Volume de envio diário atual** com um valor maior que 0 para corresponder ao seu volume atual. Quando o volume atual é maior que 0, a Braze não aplica o escalonamento por contagem de IP ao dia 1.

## Qual fuso horário é usado para envio? {#what-time-zone-is-used-for-sending}

Os envios usam o fuso horário do espaço de trabalho quando um está definido; caso contrário, usam o fuso horário da empresa. As Campaigns não são criadas no fuso local de cada usuário. Para enviar no fuso local, atualize manualmente as Campaigns criadas pelo plano.

## Quantos planos de aquecimento de IP podem ser executados ao mesmo tempo? {#how-many-ip-warming-plans-can-run-at-the-same-time}

Mais de um plano pode ser executado simultaneamente. Para mais detalhes, consulte [Aquecimento de IP múltiplo]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming).

## Como o volume escala para pools de IP com múltiplos IPs? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

Quando o **Volume de envio diário atual** é 0, o dia 1 começa no menor valor entre 50 envios por IP ou 500 no total. O volume então cresce cerca de 1,75 vezes por dia de envio, sujeito a limites de rampa. Por exemplo, com 10 IPs: 500 → 875 → 1.532 → 2.681.

Se você definir um volume atual personalizado maior que 0, o escalonamento por contagem de IPs não é aplicado ao dia 1. Para mais informações sobre planos com múltiplos IPs, consulte [Aquecer múltiplos IPs em um pool]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool).

## O aquecimento automatizado de IP suporta limite de frequência por Campaign? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

Não. Cada Campaign envia no horário configurado sem um limite de frequência por Campaign.

## Quando a Braze retém o volume durante o aquecimento de IP? {#when-does-braze-hold-volume-during-ip-warming}

A Braze avalia a entregabilidade de Campaigns enviadas entre 12 e 20 horas atrás. Se as taxas de entrega, abertura, bounce ou relatório de SPAM ultrapassarem os benchmarks em [Durante o aquecimento de IP ativo]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming), a Braze retém o volume para o próximo dia de envio em vez de aumentá-lo.

## O que acontece quando o volume é mantido? {#what-happens-when-volume-is-held}

A manutenção de volume é o ajuste automático que a Braze aplica quando esses limites são ultrapassados. O próximo envio agendado mantém o mesmo volume em vez de avançar. A Braze replaneja as entradas futuras do cronograma, arquiva as Campaigns futuras existentes do plano e cria novas Campaigns para o cronograma atualizado imediatamente. O plano pode levar mais tempo para atingir o volume alvo.

## Por que as edições de Campaign não aparecem no rastreador de aquecimento de IP? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

As alterações feitas em Campaigns criadas pelo aquecimento de IP automatizado (como cronograma, Segment ou volume) não são sincronizadas de volta com o rastreador de aquecimento de IP. Para notas de configuração relacionadas, consulte [Etapa 3: Selecionar as mensagens para envio]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Posso interromper um plano de aquecimento de IP? {#can-i-stop-an-ip-warming-plan}

Sim. Interromper encerra permanentemente o plano: a Braze desativa as Campaigns vinculadas e não cria novas. Não é possível retomar um plano interrompido — crie um novo plano para continuar. Para saber como prosseguir após uma interrupção, consulte [Interromper um plano de aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan).

## Quando um plano de aquecimento de IP é marcado como concluído? {#when-is-an-ip-warming-plan-marked-as-complete}

O plano é marcado como concluído após o término do último dia de envio agendado, à meia-noite no fuso horário efetivo (espaço de trabalho ou empresa). Por exemplo, se a última Campaign é enviada às 20h, o plano é marcado como concluído à meia-noite, quatro horas depois.

## Quais dados posso baixar? {#what-data-can-i-download}

A exportação CSV inclui linhas por Campaign com métricas diárias: *Enviados*, *Entregues*, *Bounces*, *Relatórios de SPAM*, *Total de aberturas*, *Aberturas únicas*, *Cliques* e *Cancelamentos de inscrição*. A tabela de rastreamento agrega várias Campaigns do mesmo dia em uma visualização diária. Para saber mais, consulte [Quando um aquecimento de IP é concluído]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes).