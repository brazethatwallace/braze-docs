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

Para e-mails, a reputação do seu IP de envio e do seu domínio leva em consideração o engajamento, o relatório de SPAM, a lista de bloqueio e mais. Se a reputação permanecer baixa, ISPs e filtros de caixa de correio podem classificar seus e-mails em pastas de SPAM ou de baixa prioridade para todos os destinatários, não apenas os inativos. As políticas de sunset limitam envios contínuos para usuários desengajados, o que ajuda a proteger a reputação; combine-as com monitoramento regular para identificar problemas cedo.

## Monitore a integridade do IP e do domínio {#monitor-ip-and-domain-health}

Use o [Centro de Entregabilidade]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) para acompanhar como os provedores de caixa de correio enxergam seus envios:

- **Google Postmaster Tools** (após conectar sua conta): reputação do IP, reputação do domínio, erros de entrega, autenticação (SPF, DKIM, DMARC) e métricas de criptografia para visibilidade relacionada ao Gmail.
- **Microsoft Smart Network Data Services (SNDS)** (quando configurado para seus IPs): integridade do IP para caixas de correio do Outlook e da Microsoft, incluindo resultados de filtros, taxas de reclamação e ocorrências de spam traps.

Para uma higiene de envio mais ampla, consulte [Melhorar a entregabilidade de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) e [Armadilhas de entregabilidade e spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

Você também pode usar ferramentas externas como [Sender Score](https://www.senderscore.org/) ou [Outlook Smart Network Data Services](https://postmaster.live.com/snds/) fora da Braze para sinais adicionais.

## Use listas de supressão {#use-suppression-lists}

[Listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists) são grupos de usuários definidos com filtros de Segment or segmento or segmento que não recebem Campaigns ou Canvas por padrão, mesmo quando aparecem no Segment or segmento or segmento de destino. Para destinatários inativos ou desengajados, uma lista de supressão funciona como uma proteção em nível de espaço de trabalho. Quando os usuários atendem aos seus critérios de inatividade, eles param de receber a maioria das mensagens sem que você precise editar cada Segment or segmento or segmento ou Campaign.

Para alinhar com uma política de sunset, crie a lista de supressão com filtros que capturem usuários que não devem mais receber e-mails promocionais contínuos (por exemplo, `Last Engaged With Message` ou outros filtros em **Redirecionamento**) usando a mesma janela de retrospectiva e as mesmas opções de canal que você usa para definir "desengajado" na sua política. A associação é dinâmica: os usuários entram quando atendem aos filtros e saem quando voltam a interagir.

Se você ainda quiser que determinados envios alcancem usuários inativos, como uma última tentativa de recuperação ou jornadas transacionais aprovadas, configure tags de exceção na lista de supressão para que Campaigns ou Canvas com essas tags ainda sejam entregues quando os usuários estiverem no público-alvo. As listas de supressão funcionam em conjunto com a segmentação, que pode definir quem você inclui em um envio. Para etapas de configuração, permissões e limites, consulte [Configurando listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists#setup).

## Use filtros de segmentação {#use-segmentation-filters}

Os filtros de segmentação ajudam a evitar que seu envio de mensagens pareça SPAM, permitindo que você implemente facilmente políticas de sunset para e-mails, push e notificações no app. Aqui estão algumas coisas a considerar ao criar uma política de sunset:

- O que conta como um usuário "desengajado"?
- O engajamento é definido por cliques, compras, uso de app ou uma combinação desses comportamentos?
- Quanto tempo precisa durar o lapso no engajamento para que você pare de enviar mensagens?
- Você vai enviar alguma Campaign especial para os usuários antes de excluí-los dos seus segmentos?
- A quais canais de envio de mensagens sua política de sunset se aplicará?

Por exemplo, se você tem usuários que optaram pela [MPP or proteção de privacidade de e-mail or proteção de privacidade de e-mail (MPP or proteção de privacidade de e-mail) da Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp), considere como isso pode afetar suas campanhas de e-mail e métricas de entregabilidade e determine a melhor forma de estruturar sua política de sunset.

Para incorporar políticas de sunset às suas campanhas, crie um [Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) que exclua automaticamente os usuários que marcaram seus e-mails como SPAM ou que não interagiram com suas mensagens por um determinado período de tempo.

Para configurar esses segmentos, escolha os filtros `Has Marked You As Spam` e `Last Engaged With Message` localizados na seção **Redirecionamento** no menu suspenso de filtros.

Ao aplicar o filtro `Last Engaged With Message`, especifique o tipo de mensagem (push, e-mail ou notificação no app) com a qual o usuário interagiu ou não, bem como o número de dias desde a última interação. Depois de criar um Segment or segmento or segmento, escolha direcionar esse Segment or segmento or segmento com qualquer [canal de envio de mensagens]({{site.baseurl}}/user_guide/channels).

![Página de detalhes do Segment or segmento or segmento com o filtro "Last Engaged with Message" selecionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Embora a Braze pare automaticamente de enviar e-mails para usuários que marcaram você como SPAM, o filtro `Has Marked You As Spam` permite que você também envie mensagens push direcionadas e notificações no app para esses usuários. Esse filtro é útil para [campanhas de redirecionamento]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns). Por exemplo, você pode enviar mensagens para usuários desengajados lembrando-os dos recursos e ofertas que estão perdendo ao não abrir seus e-mails.

As políticas de sunset podem ser especialmente úteis em campanhas de e-mail direcionadas a usuários inativos. Embora essas campanhas foquem em segmentos que não interagiram com seu app por um período de tempo, elas podem colocar em risco a entregabilidade dos seus e-mails se incluírem repetidamente destinatários desengajados. As políticas de sunset permitem que você direcione usuários inativos sem cair na pasta de SPAM.