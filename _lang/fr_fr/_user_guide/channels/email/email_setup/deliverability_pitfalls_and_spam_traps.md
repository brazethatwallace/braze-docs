---
nav_title: Pièges de la livrabilité et pièges à spam
article_title: Écueils de livrabilité et pièges à spam
page_order: 7
page_type: reference
description: "Le présent article de référence couvre les écueils de livrabilité des e-mails potentiels, les pièges à spam et la manière de les éviter."
channel: email

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}Écueils de livrabilité et pièges à spam {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomemail-onboarding-for-pro-and-enterprise-achieving-high-deliverability-stylefloatrightwidth120pxborder0-classnoimgborderdeliverability-pitfalls-and-spam-traps}

> Cet article couvre les écueils courants de livrabilité des e-mails, les pièges à spam et la manière de les éviter.

Votre livrabilité par e-mail peut être affectée par l'un des pièges à spam suivants :

| Type de piège | Description |
|---|---|
| Pièges vierges | Adresses e-mail et domaines qui n'ont jamais été utilisés. |
| Pièges recyclés | Adresses e-mail qui appartenaient à des utilisateurs réels, mais qui sont désormais dormantes. |
| Pièges typographiques | Adresses e-mail contenant des fautes de frappe courantes. |
| Plaintes pour spam | Lorsque votre e-mail est signalé comme spam par un client. |
| Taux de rebond élevé | Lorsque votre e-mail ne parvient pas systématiquement au destinataire parce que son adresse n'est pas valide. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Comment éviter les pièges à spam {#how-to-avoid-spam-traps}

Ces pièges peuvent être évités si vous mettez en place un processus d'abonnement confirmé. En envoyant un e-mail d'abonnement initial et en demandant aux clients de vérifier qu'ils souhaitent recevoir vos messages, vous vous assurez que vos destinataires souhaitent avoir de vos nouvelles et que vous envoyez à des adresses réelles et valides. Voici d'autres moyens d'éviter les pièges à spam :

1. Envoyez un e-mail de double abonnement. Il s'agit d'un e-mail qui demande aux utilisateurs de confirmer leurs choix d'abonnement en cliquant sur un lien.
2. En tant que bonne pratique, mettez en place une [politique de temporisation]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **N'achetez jamais de listes d'adresses e-mail.**

{% alert tip %}
Les équipes de satisfaction client et de livrabilité de Braze peuvent vous aider à suivre les bonnes pratiques pour maximiser la livrabilité à travers le monde.
{% endalert %}

## Supprimer une adresse e-mail de votre liste de rebonds ou de spam {#remove-an-email-address-from-your-bounce-or-spam-list}

Vous pouvez supprimer les e-mails ayant rebondi et les e-mails figurant sur votre liste de spam Braze à l'aide des endpoints suivants :
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)

## Améliorer la livrabilité des e-mails {#improve-email-deliverability}

Pour découvrir les bonnes pratiques permettant d'améliorer la livrabilité de vos e-mails, consultez [Améliorer la livrabilité des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).