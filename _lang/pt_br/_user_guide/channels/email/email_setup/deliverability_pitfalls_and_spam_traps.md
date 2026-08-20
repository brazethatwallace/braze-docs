---
nav_title: Armadilhas de entregabilidade e spam traps
article_title: Armadilhas de entregabilidade e spam traps
page_order: 7
page_type: reference
description: "Este artigo de referência aborda as possíveis armadilhas de entregabilidade de e-mail, spam traps e como evitá-las."
channel: email

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} Armadilhas de entregabilidade e spam traps {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomemail-onboarding-for-pro-and-enterprise-achieving-high-deliverability-stylefloatrightwidth120pxborder0-classnoimgborderdeliverability-pitfalls-and-spam-traps}

> Este artigo aborda as armadilhas comuns de entregabilidade de e-mail, spam traps e como evitá-las.

A entregabilidade do seu e-mail pode ser afetada por qualquer uma das seguintes spam traps:

| Tipo de armadilha | Descrição |
|---|---|
| Armadilhas imaculadas | Endereços de e-mail e domínios que nunca foram usados. |
| Armadilhas recicladas | Endereços de e-mail que originalmente eram de usuários reais, mas que agora estão inativos. |
| Armadilhas de erro de digitação | Endereços de e-mail que contêm erros de digitação comuns. |
| Reclamações de spam | Quando seu e-mail é marcado como spam por um consumidor. |
| Alta taxa de bounce | Quando seu e-mail falha constantemente na entrega porque o endereço do destinatário é inválido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Armadilhas de entregabilidade e spam traps" }

## Como evitar spam traps {#how-to-avoid-spam-traps}

Essas armadilhas podem ser evitadas se você configurar um processo de aceitação confirmada. Ao enviar um e-mail inicial de aceitação e pedir aos inscritos que verifiquem se desejam receber suas mensagens, você garante que seus destinatários querem ouvir de você e que está enviando para endereços reais e válidos. Veja outras formas de evitar spam traps:

1. Envie um e-mail de aceitação dupla. Esse é um e-mail que exige que os usuários confirmem suas escolhas de inscrição clicando em um link.
2. Como prática recomendada, implemente uma [política de sunset]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies).
3. **Nunca compre listas de e-mails.**

{% alert tip %}
As equipes de sucesso do cliente e entregabilidade da Braze podem ajudar a garantir que você esteja seguindo as práticas recomendadas para maximizar a entregabilidade em todo o mundo.
{% endalert %}

## Como resolver um bloqueio de domínio de e-mail gratuito da Microsoft {#how-to-resolve-a-free-email-domain-block-for-microsoft}

A Microsoft raramente desbloqueia remetentes que têm dificuldade para entregar mensagens a domínios de e-mail gratuitos (Hotmail, Live, MSN e Outlook). Em vez disso, reduza agressivamente o volume de envios para esses domínios e envie apenas para contatos que interagiram recentemente. Se você não conseguir identificar um grupo principal de destinatários engajados, pare de enviar para esses domínios completamente.

Um exemplo de mensagem de bloqueio de domínio de e-mail gratuito é:

`550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your Internet service provider since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

Você pode aumentar o volume gradualmente, de forma semelhante ao [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming), prestando muita atenção às métricas. Geralmente existe uma causa raiz dos problemas de entregabilidade que precisa ser identificada e resolvida. Em geral, isso se deve à falta de permissão adequada, à falta de higienização contínua da lista de e-mails, ou a uma combinação desses fatores.

## Remover um endereço de e-mail da sua lista de bounce ou SPAM {#remove-an-email-address-from-your-bounce-or-spam-list}

Você pode remover e-mails com bounce e e-mails da sua lista de SPAM da Braze com os seguintes endpoints:

- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## Melhore a entregabilidade de e-mail {#improve-email-deliverability}

Para saber mais, consulte [Melhore a entregabilidade de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability).

## BIMI

Para BIMI (Brand Indicators for Message Identification), consulte [Autenticação de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).