---
nav_title: Armadilhas da entregabilidade e armadilhas de spam
article_title: Armadilhas da entregabilidade e armadilhas de spam
page_order: 7
page_type: reference
description: "Este artigo de referência aborda as possíveis armadilhas de entregabilidade de e-mail, as armadilhas de spam e como evitá-las."
channel: email

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} Armadilhas da entregabilidade e armadilhas de spam {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomemail-onboarding-for-pro-and-enterprise-achieving-high-deliverability-stylefloatrightwidth120pxborder0-classnoimgborderdeliverability-pitfalls-and-spam-traps}

> Este artigo aborda as armadilhas comuns de entregabilidade de e-mail, as armadilhas de spam e como evitá-las.

A entregabilidade do seu e-mail pode ser afetada por qualquer uma das seguintes armadilhas de spam:

| Tipo de armadilha | Descrição |
|---|---|
| Armadilhas imaculadas | Endereços de e-mail e domínios que nunca foram usados. |
| Armadilhas recicladas | Endereços de e-mail que originalmente eram de usuários reais, mas que agora estão inativos. |
| Armadilhas de erro de digitação | Endereços de e-mail que contêm erros de digitação comuns. |
| Reclamações de spam | Quando seu e-mail é marcado como spam por um cliente. |
| Alta taxa de bounce | Quando seu e-mail falha constantemente na entrega porque o endereço do destinatário é inválido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como evitar armadilhas de spam {#how-to-avoid-spam-traps}

Essas armadilhas podem ser evitadas se você configurar um processo de opt-in confirmado. Ao enviar um e-mail inicial de opt-in e pedir aos clientes que verifiquem se desejam receber suas mensagens, você garante que os destinatários queiram ouvir de você e que você esteja enviando para endereços reais e válidos. Aqui estão outras maneiras de evitar armadilhas de spam:

1. Envie um e-mail de opt-in duplo. Esse é um e-mail que exigirá que os usuários confirmem suas escolhas de inscrição clicando em um link.
2. Como prática recomendada, implemente uma [política de sunset]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **Nunca compre listas de e-mail.**

{% alert tip %}
As equipes de sucesso do cliente e entregabilidade da Braze podem ajudar a garantir que você esteja seguindo as práticas recomendadas para maximizar a entregabilidade em todo o mundo.
{% endalert %}

## Remover um endereço de e-mail da sua lista de bounce ou spam {#remove-an-email-address-from-your-bounce-or-spam-list}

Você pode remover e-mails com bounce e e-mails da sua lista de spam da Braze com os seguintes endpoints:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)

## Melhorar a entregabilidade de e-mail {#improve-email-deliverability}

Para práticas recomendadas sobre como melhorar a entregabilidade do seu e-mail, consulte [Melhorar a entregabilidade de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).