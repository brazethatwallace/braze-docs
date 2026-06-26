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
| Plaintes pour spam | Lorsque votre e-mail est signalé comme spam par un consommateur. |
| Taux de rebond élevé | Lorsque votre e-mail ne parvient pas systématiquement au destinataire parce que son adresse n'est pas valide. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Écueils de livrabilité et pièges à spam" }

## Comment éviter les pièges à spam {#how-to-avoid-spam-traps}

Ces pièges peuvent être évités si vous mettez en place un processus d'abonnement confirmé. En envoyant un e-mail d'abonnement initial et en demandant aux utilisateurs abonnés de vérifier qu'ils souhaitent recevoir vos messages, vous vous assurez que vos destinataires souhaitent avoir de vos nouvelles et que vous envoyez à des adresses réelles et valides. Voici d'autres moyens d'éviter les pièges à spam :

1. Envoyez un e-mail de double abonnement. Il s'agit d'un e-mail qui demande aux utilisateurs de confirmer leurs choix d'abonnement en cliquant sur un lien.
2. En tant que bonne pratique, mettez en place une [politique de temporisation]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **N'achetez jamais de listes d'adresses e-mail.**

{% alert tip %}
Les équipes de satisfaction client et de livrabilité de Braze peuvent vous aider à suivre les bonnes pratiques pour maximiser la livrabilité à travers le monde.
{% endalert %}

## Comment résoudre un blocage de domaine e-mail gratuit par Microsoft {#how-to-resolve-a-free-email-domain-block-for-microsoft}

Microsoft débloque rarement les expéditeurs qui rencontrent des difficultés de livraison vers les domaines e-mail gratuits (Hotmail, Live, MSN et Outlook). Réduisez plutôt votre volume vers ces domaines de manière agressive et n'envoyez qu'aux contacts récemment engagés. Si vous ne parvenez pas à identifier un groupe principal de destinataires engagés, cessez complètement d'envoyer vers ces domaines.

Voici un exemple de message de blocage de domaine e-mail gratuit :

`550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your Internet service provider since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

Vous pouvez augmenter progressivement le volume de manière similaire au [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/), en surveillant attentivement les indicateurs. Il existe souvent une cause profonde des problèmes de livrabilité à identifier et à résoudre. En général, il s'agit d'un manque d'autorisations appropriées, d'un manque d'hygiène continue des listes, ou d'une combinaison de ces facteurs.

## Supprimer une adresse e-mail de votre liste de rebonds ou de spam {#remove-an-email-address-from-your-bounce-or-spam-list}

Vous pouvez supprimer les e-mails ayant rebondi et les e-mails figurant sur votre liste de spam Braze à l'aide des endpoints suivants :

- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)

## Améliorer la livrabilité des e-mails {#improve-email-deliverability}

Pour en savoir plus, consultez [Améliorer la livrabilité des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).