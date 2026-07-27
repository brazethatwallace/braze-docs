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

Para e-mails, a reputação do seu IP de envio e do seu domínio leva em consideração o engajamento, o relatório de SPAM, a lista de bloqueio e mais. Se a reputação permanecer baixa, ISPs e filtros de caixa de correio podem classificar seus e-mails em uma pasta de SPAM ou de baixa prioridade para todos os destinatários, não apenas os inativos. As políticas de sunset limitam o envio contínuo para usuários desengajados, o que ajuda a proteger a reputação. Combine essas políticas com monitoramento regular para identificar problemas com antecedência.

## Monitore a integridade de IP e domínio {#monitor-ip-and-domain-health}

Use o [Deliverability Center]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) para acompanhar como os provedores de caixa de entrada enxergam seus envios:

- **Google Postmaster Tools** (após conectar sua conta): reputação de IP, reputação de domínio, erros de entrega, autenticação (SPF, DKIM, DMARC) e métricas de criptografia para visibilidade relacionada ao Gmail.
- **Microsoft Smart Network Data Services (SNDS)** (quando configurado para seus IPs): integridade de IP para caixas de entrada do Outlook e da Microsoft, incluindo resultados de filtros, taxas de reclamação e ocorrências de SPAM traps.

Para uma higiene de envio mais ampla, consulte [Melhorar a entregabilidade de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) e [Armadilhas de entregabilidade e SPAM traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

Você também pode alavancar ferramentas externas como [Sender Score](https://www.senderscore.org/) ou [Outlook Smart Network Data Services](https://postmaster.live.com/snds/) fora da Braze para sinais adicionais.

## Use listas de supressão {#use-suppression-lists}

[Listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists) são grupos de usuários definidos com filtros de Segment que não recebem Campaigns ou Canvas por padrão, mesmo quando aparecem no Segment de destino. Para destinatários inativos ou desengajados, uma lista de supressão funciona como uma proteção em todo o espaço de trabalho. Quando os usuários atendem aos seus critérios de inatividade, eles param de receber a maioria das mensagens sem que você precise editar cada Segment ou Campaign.

Para alinhar com uma política de sunset, crie a lista de supressão com filtros que capturem usuários que não devem mais receber e-mails promocionais contínuos (por exemplo, `Last Engaged With Message` ou outros filtros em **Redirecionamento**) usando a mesma janela de retrospectiva e as mesmas opções de canal que você usa para "desengajados" na sua política. A associação é dinâmica: os usuários entram quando atendem aos filtros e saem quando voltam a interagir.

Se você ainda quiser que determinados envios alcancem usuários inativos, como uma tentativa final de recuperação ou jornadas transacionais aprovadas, configure tags de exceção na lista de supressão para que Campaigns ou Canvas com essas tags ainda sejam entregues quando os usuários estiverem no público-alvo. As listas de supressão funcionam em conjunto com a segmentação, que pode definir quem você inclui em um envio. Para etapas de configuração, permissões e limites, consulte [Configurando listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists#setup).

## Use filtros de segmentação {#use-segmentation-filters}

Os filtros de segmentação ajudam a evitar que suas mensagens pareçam SPAM, permitindo que você implemente facilmente políticas de sunset para e-mails, push e notificações in-app. Aqui estão alguns pontos a considerar ao criar uma política de sunset:

- O que conta como um usuário "não engajado"?
- O engajamento é definido por cliques, compras, uso do app ou uma combinação desses comportamentos?
- Quanto tempo de inatividade é necessário para que você pare de enviar mensagens?
- Você vai entregar alguma Campaign especial aos usuários antes de excluí-los dos seus Segments?
- A quais canais de envio de mensagens sua política de sunset se aplicará?

Por exemplo, se você tem usuários que optaram pela [proteção de privacidade de e-mail (MPP) da Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp), considere como isso pode impactar suas campanhas de e-mail e métricas de entregabilidade, e determine a melhor forma de estruturar sua política de sunset.

Para incorporar políticas de sunset às suas campanhas, crie um [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) que exclua automaticamente usuários que marcaram seus e-mails como SPAM ou que não interagiram com suas mensagens por um determinado período de tempo.

Para configurar esses Segments, escolha os filtros `Has Marked You As Spam` e `Last Engaged With Message` localizados na seção **Redirecionamento** no menu suspenso de filtros.

Ao aplicar o filtro `Last Engaged With Message`, especifique o tipo de envio de mensagens (push, e-mail ou notificação in-app) com o qual o usuário interagiu ou não, bem como o número de dias desde a última interação do usuário. Depois de criar um Segment, escolha direcionar esse Segment com qualquer [canal de envio de mensagens]({{site.baseurl}}/user_guide/channels).

![Página de detalhes do Segment com o filtro "Last Engaged with Message" selecionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Embora a Braze pare automaticamente de enviar e-mails para usuários que marcaram você como SPAM, o filtro `Has Marked You As Spam` permite que você também envie mensagens push direcionadas e notificações in-app para esses usuários. Esse filtro é útil para [campanhas de redirecionamento]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns). Por exemplo, você pode enviar mensagens para usuários não engajados lembrando-os dos recursos e ofertas que estão perdendo ao não abrir seus e-mails.

As políticas de sunset podem ser especialmente úteis em campanhas de e-mail direcionadas a usuários inativos. Embora essas campanhas foquem em Segments que não interagiram com seu app por um período de tempo, elas podem colocar em risco a entregabilidade dos seus e-mails se incluírem repetidamente destinatários não engajados. As políticas de sunset permitem que você direcione usuários inativos sem cair na pasta de SPAM.