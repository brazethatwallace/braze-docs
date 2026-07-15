---
nav_title: Políticas de sunset
article_title: Políticas de sunset para e-mail
page_order: 8
page_type: reference
description: "Este artigo aborda as melhores práticas relacionadas a políticas de sunset e a compreensão de situações em que é melhor descontinuar mensagens para usuários desengajados."
channel: email

---

# Políticas de sunset {#sunset-policies}

> Embora você possa ser tentado a enviar campanhas para o maior número de usuários possível, há situações em que é realmente vantajoso parar de enviar mensagens para usuários desengajados.

Para e-mails, seu IP de envio tem uma pontuação de reputação que leva em consideração o engajamento, o relatório de spam, a lista de bloqueio e mais. Você pode usar ferramentas como [Sender Score](https://www.senderscore.org/) ou [Serviço de Dados da Rede Inteligente do Outlook](https://postmaster.live.com/snds/) para monitorar sua pontuação de reputação. Se sua pontuação de reputação estiver consistentemente baixa, provedores de acesso à internet e filtros de caixa de correio podem automaticamente classificar seus e-mails em uma pasta de spam ou de baixa prioridade para todos os destinatários, até mesmo os engajados. Criar uma política de sunset ajuda a entregar seus e-mails apenas para destinatários ativos.

Os filtros de segmentação ajudam a evitar que seu envio de mensagens pareça spam, permitindo que você implemente facilmente políticas de sunset para e-mails, push e notificações no app. Aqui estão algumas coisas a considerar ao criar uma política de sunset:

- O que conta como um usuário "desengajado"?
- O engajamento é definido por cliques, compras, uso de app ou uma combinação desses comportamentos?
- Quanto tempo precisa durar o lapso no engajamento para que você pare de enviar mensagens?
- Você vai enviar alguma Campaign especial para os usuários antes de excluí-los dos seus Segments?
- A quais canais de envio de mensagens sua política de sunset se aplicará?

Por exemplo, se você tem usuários que optaram pela [proteção de privacidade de e-mail (MPP) da Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp), considere como isso pode afetar suas Campaigns de e-mail e métricas de entregabilidade e determine a melhor forma de estruturar sua política de sunset.

Para incorporar políticas de sunset às suas Campaigns, crie um [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#creating-a-segment) que exclua automaticamente os usuários que marcaram seus e-mails como spam ou que não interagiram com suas mensagens por um determinado período de tempo.

Para configurar esses Segments, escolha os filtros `Has Marked You As Spam` e `Last Engaged With Message` localizados na seção **Redirecionamento** no menu suspenso de filtros.

Ao aplicar o filtro `Last Engaged With Message`, especifique o tipo de mensagem (push, e-mail ou notificação no app) com a qual o usuário interagiu ou não, bem como o número de dias desde a última interação. Depois de criar um Segment, escolha direcionar esse Segment com qualquer [canal de envio de mensagens]({{site.baseurl}}/user_guide/channels).

![Página de informações do Segment com o filtro "Last Engaged with Message" selecionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Embora a Braze pare automaticamente de enviar e-mails para usuários que marcaram você como spam, o filtro `Has Marked You As Spam` permite que você também envie mensagens push direcionadas e notificações no app para esses usuários. Esse filtro é útil para [campanhas de redirecionamento]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#retarget-campaigns). Por exemplo, você pode enviar mensagens para usuários desengajados lembrando-os dos recursos e ofertas que estão perdendo ao não abrir seus e-mails.

As políticas de sunset podem ser especialmente úteis em Campaigns de e-mail direcionadas a usuários inativos. Embora essas Campaigns foquem em Segments que não interagiram com seu app por um período de tempo, elas podem colocar em risco a entregabilidade dos seus e-mails se incluírem repetidamente destinatários desengajados. As políticas de sunset permitem que você direcione usuários inativos sem cair na pasta de spam.