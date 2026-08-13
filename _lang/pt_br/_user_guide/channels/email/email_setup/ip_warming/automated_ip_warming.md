---
nav_title: Aquecimento de IP automatizado
article_title: Aquecimento de IP automatizado
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o aquecimento de IP automatizado e como monitorar seu aquecimento de IP."
channel: email
---

# Aquecimento de IP automatizado {#automated-ip-warming}

> Use o aquecimento de IP automatizado para aumentar gradualmente o volume de e-mails de novos IPs dedicados e construir a reputação do remetente com os provedores de caixa de entrada.

## Como funciona {#how-it-works}

Você pode usar o aquecimento de IP automatizado para aumentar gradualmente seu volume de envio diário, permitindo que os provedores de caixa de entrada aprendam e confiem nos seus padrões de envio. Ao adicionar um domínio ao seu espaço de trabalho, você pode selecionar o bloco **Automated IP Warming** na seção **Pick up where you left off** do seu dashboard inicial. Esse bloco permanece por 60 dias enquanto seu espaço de trabalho estiver na janela de integração de novo remetente.

Cada plano de aquecimento de IP automatizado está vinculado a um endereço de remetente. Esse endereço de remetente é mapeado para um subdomínio de envio e um pool de IP. Se o pool contiver vários IPs dedicados, a Braze os aquece juntos em um único plano.

A Braze envia primeiro para seus inscritos com maior engajamento, o que permite que o volume diário cresça em um ritmo alinhado às melhores práticas. Em seguida, a Braze monitora sinais de engajamento e entregabilidade. Se a Braze detectar algum problema, o sistema ajusta seu cronograma automaticamente.

Após concluir pelo menos um plano, você pode visualizar os planos concluídos em **Settings** > **Email Preferences** > **Automated IP warming**.

{% alert note %}
Se você vir apenas uma experiência de plano único no seu dashboard, seu espaço de trabalho pode ainda não ter acesso a múltiplos planos de aquecimento de IP. Entre em contato com a equipe da sua conta Braze para verificar a disponibilidade.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para realizar o aquecimento de IP automatizado, você precisa ter o seguinte:

- Subdomínio verificado e endereços IP ativos
- Permissões para visualizar e iniciar um aquecimento de IP
    - "View Usage Data" para visualizar a seção de aquecimento de IP
    - "View Email Templates" para visualizar e selecionar os modelos de e-mail para aquecimento de IP
    - "Manage Email Settings" para iniciar o aquecimento de IP
- "Access Campaigns"
- "Approve and Deny Campaigns" se o fluxo de aprovação para Campaigns estiver ativado
    - A Braze aprova automaticamente as Campaigns criadas a partir do aquecimento de IP automatizado em seu nome.

{% alert important %}
Este recurso pode não ser compatível dependendo da sua infraestrutura de e-mail.
{% endalert %}

## Configure um plano automatizado de aquecimento de IP {#set-up-an-automated-ip-warming-plan}

### Etapa 1: Defina um cronograma {#step-1-set-a-schedule}

1. Se o seu espaço de trabalho suporta múltiplos planos de aquecimento de IP, insira um **Nome do plano** exclusivo. Os nomes de plano podem conter apenas letras, números, hifens e underscores, e devem ser exclusivos no seu espaço de trabalho. Um nome de plano é obrigatório antes de você poder lançar.
2. Na seção **Informações de envio**, selecione o **Endereço de remetente** para aquecer os endereços IP. A Braze exibe o **Pool de IP** associado e o número de **Endereços IP no pool** para esse endereço de remetente.
3. Insira o **Volume de envio diário atual** e o **Volume de envio desejado**. A Braze sugere um volume de envio desejado de até 2 milhões de envios por IP no pool selecionado. Se o seu volume de envio diário atual for 0, o primeiro dia do seu cronograma começa com até 50 envios por IP, limitado a 500 no total.
4. Selecione a data de início para o aquecimento de IP automatizado. Essa data deve ser pelo menos um dia após o lançamento do plano.
5. Insira o horário de envio. As mensagens são enviadas no fuso horário da empresa.
6. Selecione **Próximo: Segments** para continuar a configuração.

![Exemplo de detalhes do cronograma.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Etapa 2: Selecione e classifique os segments {#step-2-select-and-rank-segments}

1. Em seguida, selecione os segments a serem segmentados. Durante o aquecimento de IP, a Braze começa enviando para os usuários com maior engajamento e aumenta gradualmente o volume de envio ao longo do tempo, adicionando lentamente segments com menor engajamento.
2. Depois, arraste e solte os segments para classificá-los de alto a baixo engajamento. Alto engajamento inclui destinatários que abrem e clicam consistentemente nos seus e-mails. Baixo engajamento inclui destinatários que são inconsistentes no engajamento com seus e-mails ou que não interagem com seus e-mails há muito tempo.
3. Selecione **Próximo: Mensagens** para continuar a configuração.

![Dois segments selecionados para segmentação no aquecimento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Etapa 3: Selecione as mensagens a enviar {#step-3-select-the-messages-to-send}

1. Selecione **Selecionar modelos de e-mail**.
2. Escolha os modelos de e-mail para as mensagens a enviar. O conteúdo que você envia durante o aquecimento de IP deve incentivar aberturas e cliques. Recomendamos escolher conteúdo que teve boa recepção no passado. Por exemplo, você pode usar ofertas promocionais para incentivar engajamento e compras imediatas.
3. Selecione **Selecionar modelos**. A Braze calcula o número de modelos necessários antes de você poder lançar. Recomendamos fornecer mais modelos do que o mínimo necessário para permitir que o sistema se ajuste a problemas de entregabilidade sem parar.
4. Após adicionar o número necessário de modelos, selecione **Próximo: Resumo**.

{% alert important %}
Alterações feitas nas Campaigns criadas a partir da ferramenta de aquecimento de IP (como alterar a data agendada, segment, volume) não são refletidas na página de **Resumo** do aquecimento de IP.
{% endalert %}

### Etapa 4: Selecione eventos de conversão {#step-4-select-conversion-events}

Você pode definir até quatro dos seguintes eventos de conversão para rastrear. Esses eventos de conversão não podem ser atualizados após o lançamento do plano automatizado de aquecimento de IP.

- Inicia sessão
- Realiza pedido
- Realiza evento personalizado
- Faz upgrade do app
- Abre e-mail
- Clica no e-mail

Em seguida, selecione o prazo de conversão, que é o tempo máximo que pode passar entre um usuário entrar em uma Campaign e o evento de conversão.

![Configurações de conversão mostrando a seleção de evento de conversão e o prazo de conversão.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Etapa 5: Revise e lance {#step-5-review-and-launch}

Revise os detalhes do seu plano de aquecimento de IP. Em seguida, selecione **Lançar**.

## Aquecimento de múltiplos IPs {#multiple-ip-warming}

Use vários planos de aquecimento de IP automatizado quando precisar aquecer mais de um endereço de remetente ou pool de IP.

| Cenário | Recomendação |
| --- | --- |
| Múltiplos IPs dedicados em um pool de IP | Crie um plano e selecione o endereço de remetente para esse pool |
| Múltiplos pools de IP ou endereços de remetente | Crie um plano separado para cada endereço de remetente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cenários de aquecimento de múltiplos IPs" }

### Aquecer múltiplos IPs em um pool {#warm-multiple-ips-in-one-pool}

Quando você seleciona um endereço de remetente na [Etapa 1: Definir um cronograma](#step-1-set-a-schedule), a Braze mostra o pool de IP associado e os endereços IP no pool. A Braze usa a contagem de IPs ao compilar seu cronograma de ramp-up e sugere o volume de envio desejado.

Se o seu **Volume de envio diário atual** for 0, o primeiro dia agendado começa com até 50 envios por IP no pool, limitado a 500 no total. A Braze sugere um **Volume de envio desejado** de até 2 milhões de envios por IP no pool.

### Aquecer múltiplos pools de IP {#warm-multiple-ip-pools}

Para aquecer mais de um endereço de remetente ou pool de IP:

1. Acesse **Configurações** > **Preferências de e-mail** > **Aquecimento de IP automatizado**.
2. Selecione **Novo plano de aquecimento de IP**.
3. Insira um **Nome do plano** exclusivo.
4. Conclua a configuração para esse endereço de remetente.
5. Repita para cada endereço de remetente ou pool de IP adicional que você precisar aquecer.

Acompanhe cada plano na tabela **Aquecimento de IP automatizado**. Cada plano tem seu próprio cronograma, Segments, modelos, Campaigns e rastreador. Os planos podem estar com status **Rascunho**, **Em andamento**, **Concluído** ou **Parado**.

{% alert important %}
Evite enviar Campaigns grandes que não sejam de aquecimento a partir do mesmo endereço de remetente ou pool de IP enquanto um plano de aquecimento de IP automatizado estiver ativo. Envios adicionais durante o aquecimento podem afetar os sinais de entregabilidade e dificultar o isolamento de problemas.
{% endalert %}

## Durante o aquecimento de IP ativo {#during-active-ip-warming}

As campanhas de aquecimento de IP são criadas com 1 a 2 dias de antecedência, a menos que você esteja iniciando um aquecimento de IP no dia seguinte. Essas campanhas são nomeadas automaticamente com o seguinte formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Quando a meta diária de envio é atingida, o sistema para de enviar naquele dia para proteger sua reputação.

O sistema monitora sua integridade com base nos seguintes benchmarks do setor:

- Taxa de entrega cai para menos de ou igual a 90%
- Taxa de abertura inferior a 10%
- Bounces superiores a 5%
- Taxas de relatório de SPAM superiores a 0,04%

Se as estatísticas estiverem abaixo dos nossos benchmarks, o sistema mantém o volume no dia seguinte em vez de aumentá-lo, para reduzir o risco à sua reputação do remetente.

## Interromper um plano de aquecimento de IP {#stop-an-ip-warmup-plan}

A Braze permite interromper o aquecimento de IP e a criação de futuras Campaigns, mas se uma Campaign já estiver ativa ou agendada para as próximas 24 a 48 horas, pode ser necessário interromper a Campaign específica manualmente. Interromper um plano de aquecimento de IP também interrompe todas as Campaigns associadas.

No entanto, uma vez interrompido, o aquecimento de IP não pode ser retomado. Em vez disso, você deve configurar um novo plano para continuar de onde parou:

- Baixando os dados existentes do plano interrompido para manter em seus registros
- Atualizando o **Volume de envio diário atual** para o volume mais recente
- Adicionando um filtro a um Segment se você planeja usar o mesmo Segment do último aquecimento de IP, excluindo os usuários que já receberam Campaigns anteriores

## Quando um aquecimento de IP é concluído {#when-an-ip-warmup-completes}

O aquecimento de IP é marcado como concluído quando o último dia do aquecimento de IP termina à meia-noite no fuso horário da sua empresa. Por exemplo, se a última Campaign enviada no plano de aquecimento de IP é enviada às 20h, o plano é marcado como concluído após quatro horas.

Os planos concluídos permanecem disponíveis em **Configurações** > **Preferências de e-mail** > **Aquecimento de IP automatizado**. Se o seu espaço de trabalho usa a experiência de plano único, o rastreador também permanece no dashboard principal por 90 dias após o término do plano. Após 90 dias, o rastreador do dashboard principal é removido.

O download dos dados inclui estas métricas de e-mail padrão:

- _Enviados_
- _Entregues_
- _Bounces_
- _Relatórios de SPAM_
- _Total de aberturas_
- _Aberturas únicas_
- _Clicados_
- _Cancelamentos de inscrição_

Se um dia inclui múltiplas Campaigns usadas para atender aos requisitos de volume, elas são agregadas na visualização diária.

![Rastreador de aquecimento de IP com volume de envio para a semana de 16 de janeiro.]({% image_buster /assets/img/automated_ip_warming_example.png %})