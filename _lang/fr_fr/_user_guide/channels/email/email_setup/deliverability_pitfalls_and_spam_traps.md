---
nav_title: Pièges de livrabilité et spam traps
article_title: Pièges de livrabilité et spam traps
page_order: 7
page_type: reference
description: "Cet article de référence aborde les pièges potentiels liés à la livrabilité des e-mails, les spam traps et comment les éviter."
channel: email

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}Pièges de livrabilité et spam traps

La livrabilité de vos e-mails peut être affectée par l'un des spam traps suivants :

| Type de piège | Description |
|---|---|
| Pristine Traps | Adresses e-mail et domaines qui n'ont jamais été utilisés. |
| Recycled Traps | Adresses e-mail qui appartenaient à de vrais utilisateurs, mais qui sont désormais inactives. |
| Typo Traps | Adresses e-mail contenant des fautes de frappe courantes. |
| Plaintes pour spam | Lorsque votre e-mail est signalé comme spam par un client. |
| Taux de rebond élevé | Lorsque votre e-mail échoue systématiquement à être livré parce que l'adresse du destinataire est invalide. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Comment éviter les spam traps

Ces pièges peuvent être évités en mettant en place un processus d'abonnement confirmé. En envoyant un premier e-mail d'abonnement et en demandant aux clients de vérifier qu'ils souhaitent recevoir vos messages, vous vous assurez que vos destinataires veulent avoir de vos nouvelles et que vous envoyez vos e-mails à des adresses réelles et valides. Voici d'autres moyens d'éviter les spam traps :

1. Envoyez un e-mail de double abonnement. Il s'agit d'un e-mail qui demande aux utilisateurs de confirmer leurs choix d'abonnement en cliquant sur un lien.
2. En tant que bonne pratique, mettez en place une [politique de temporisation]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **N'achetez jamais de listes d'adresses e-mail.**

{% alert tip %}
Les équipes de satisfaction client et de livrabilité de Braze peuvent vous aider à suivre les bonnes pratiques pour maximiser la livrabilité à travers le monde.
{% endalert %}

## Supprimer une adresse e-mail de votre liste de rebonds ou de spam

Vous pouvez supprimer les e-mails ayant rebondi et les e-mails figurant sur votre liste de spam Braze à l'aide des endpoints suivants :
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## Améliorer la livrabilité des e-mails

Pour découvrir les bonnes pratiques permettant d'améliorer la livrabilité de vos e-mails, consultez [Améliorer la livrabilité des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).