---
nav_title: Armadilhas de entregabilidade e spam traps
article_title: Armadilhas de entregabilidade e spam traps
page_order: 7
page_type: reference
description: "Este artigo de referência aborda possíveis armadilhas de entregabilidade de e-mail, spam traps e como evitá-las."
channel: email

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}Armadilhas de entregabilidade e spam traps

A entregabilidade do seu e-mail pode ser afetada por qualquer uma das seguintes spam traps:

| Tipo de armadilha | Descrição |
|---|---|
| Pristine Traps | Endereços de e-mail e domínios que nunca foram usados. |
| Recycled Traps | Endereços de e-mail que originalmente pertenciam a usuários reais, mas agora estão inativos. |
| Typo Traps | Endereços de e-mail que contêm erros de digitação comuns. |
| Reclamações de spam | Quando seu e-mail é marcado como spam por um cliente. |
| Alta taxa de bounce | Quando seu e-mail falha consistentemente na entrega porque o endereço do destinatário é inválido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como evitar spam traps

Essas armadilhas podem ser evitadas se você configurar um processo de opt-in confirmado. Ao enviar um e-mail inicial de opt-in e pedir que os clientes verifiquem que desejam receber suas mensagens, você garante que seus destinatários querem ouvir de você e que está enviando para endereços reais e válidos. Veja outras formas de evitar spam traps:

1. Envie um e-mail de opt-in duplo. Esse é um e-mail que exigirá que os usuários confirmem suas escolhas de inscrição clicando em um link.
2. Como prática recomendada, implemente uma [política de sunset]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **Nunca compre listas de e-mail.**

{% alert tip %}
As equipes de Sucesso do Cliente e Entregabilidade da Braze podem ajudar a garantir que você esteja seguindo as práticas recomendadas para maximizar a entregabilidade em todo o mundo.
{% endalert %}

## Remover um endereço de e-mail da sua lista de bounce ou spam

Você pode remover e-mails com bounce e e-mails da sua lista de spam da Braze com os seguintes endpoints:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## Melhorar a entregabilidade de e-mail

Para práticas recomendadas para melhorar a entregabilidade do seu e-mail, consulte [Melhorar a entregabilidade de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).