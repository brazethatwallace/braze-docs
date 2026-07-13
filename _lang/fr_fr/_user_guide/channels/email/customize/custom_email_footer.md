---
nav_title: Pied de page personnalisé
article_title: Pied de page personnalisé pour les e-mails
page_order: 6.5
description: "Cet article explique comment configurer un pied de page d'e-mail personnalisé à l'échelle de l'espace de travail."
channel:
  - email

---

# Pied de page personnalisé pour les e-mails {#custom-email-footer}

> Vous pouvez définir un pied de page d'e-mail personnalisé pour l'ensemble de l'espace de travail, que vous pouvez intégrer dans chaque e-mail à l'aide de l'attribut Liquid {% raw %}`{{${email_footer}}}`{% endraw %}.

En utilisant des pieds de page d'e-mail personnalisés, vous n'avez plus besoin de créer un nouveau pied de page pour chaque modèle d'e-mail ou chaque Campaign que vous utilisez. Toutes les Campaigns existantes et nouvelles reflètent les modifications apportées à votre pied de page personnalisé. N'oubliez pas que le respect de la [loi CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) vous oblige à inclure une adresse physique pour votre entreprise et un lien de désabonnement dans vos e-mails.

{% alert warning %}
Il est de votre responsabilité de vous assurer que votre pied de page personnalisé répond aux exigences susmentionnées.
{% endalert %}

## Créer votre pied de page personnalisé {#create-your-custom-footer}

Pour créer ou modifier votre pied de page personnalisé, procédez comme suit :

1. Allez dans **Paramètres** > **Préférences des e-mails** > **Pages et pieds de page de désabonnement**.
2. Allez dans la section **Pied de page personnalisé** et activez les pieds de page personnalisés.
3. Sélectionnez **Modifier**, puis modifiez votre pied de page dans la section **Rédiger**.
4. Sélectionnez **Prévisualisation** pour voir à quoi ressemblera votre pied de page dans la boîte de réception d'un client. Vous pouvez également sélectionner **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable montrant le rendu de l'e-mail pour un utilisateur aléatoire. Ce lien est valide pendant sept jours, après quoi il doit être régénéré.
5. Envoyez un message de test.

![Un exemple de pied de page personnalisé.]({% image_buster /assets/img_archive/custom_footer.png %})

Le pied de page par défaut utilise l'attribut {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} et notre adresse postale physique. Si vous utilisez ce pied de page par défaut, veillez à sélectionner **&#60;other&#62;** pour le **Protocol**.

{% alert important %}
Pour respecter la réglementation CAN-SPAM, votre pied de page personnalisé doit inclure un lien de désabonnement. Vous pouvez utiliser l'attribut Liquid {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} ou votre propre URL de désabonnement personnalisée. Vous ne pourrez pas enregistrer un pied de page personnalisé sans lien de désabonnement.
{% endalert %}

![Valeurs de protocole et d'URL nécessaires pour le pied de page personnalisé.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Pieds de page sans lien de désabonnement {#footers-without-unsubscribe-links}

Soyez très prudent lorsque vous utilisez un modèle avec le pied de page personnalisé {% raw %}`{{${email_footer}}}` mais sans la balise de lien de désabonnement `{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Un avertissement s'affichera, mais c'est à vous de décider d'envoyer un e-mail avec ou sans lien de désabonnement.

Voici un avertissement dans le compositeur d'e-mails :

![Exemple d'e-mail composé sans pied de page.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Voici un avertissement dans le compositeur de Campaign :

![Composition de Campaign sans pied de page.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Ajouter un lien de désabonnement personnalisé {#adding-a-custom-unsubscribe-link}

Pour ajouter un lien de désabonnement personnalisé, vous pouvez remplacer le lien de désabonnement dans le pied de page personnalisé {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} par un lien vers votre propre site web avec un paramètre de requête incluant l'ID utilisateur. Par exemple :
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Ensuite, appelez l'[endpoint `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) pour mettre à jour le statut d'abonnement de l'utilisateur. Pour plus de détails, consultez notre documentation sur la [modification des abonnements e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

Puis enregistrez ce nouveau lien. La balise de désabonnement par défaut de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} doit figurer dans le pied de page. Cela signifie que vous devez inclure le lien par défaut en le « masquant », soit en plaçant la balise dans un commentaire, soit dans une balise `<div>` masquée.

## Bonnes pratiques {#best-practices}

Voici quelques bonnes pratiques à suivre lors de la création et de l'utilisation de pieds de page personnalisés.

### Personnaliser avec des attributs {#personalizing-with-attributes}

Lors de la création d'un pied de page personnalisé, Braze vous recommande d'utiliser des [attributs pour la personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags). L'ensemble complet des attributs par défaut et personnalisés est disponible, mais voici quelques-uns qui pourraient vous être utiles :

| Attribut | Balise |
| --------- | --- |
| Adresse e-mail de l'utilisateur | {% raw %}`{{${email_address}}}`{% endraw %} |
| URL de désabonnement personnalisée de l'utilisateur | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Cette balise remplace l'ancienne balise {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Nous vous recommandons d'utiliser la nouvelle balise {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} à la place. |
| URL d'abonnement personnalisée de l'utilisateur | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| URL d'inscription personnalisée de l'utilisateur | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| URL du centre de préférences Braze personnalisé de l'utilisateur | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personnaliser avec des attributs" }

### Inclure un lien de désabonnement et un lien d'abonnement {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
Braze recommande d'inclure à la fois un lien de désabonnement (tel que ``{{${set_user_to_unsubscribed_url}}}``) et un lien d'abonnement (tel que ``{{${set_user_to_opted_in_url}}}``) dans votre pied de page personnalisé. Ainsi, les utilisateurs pourront se désabonner ou s'abonner, et vous pourrez collecter passivement des données d'abonnement pour une partie de vos utilisateurs.
{% endraw %}

### Définir des pieds de page personnalisés pour les e-mails en texte brut {#setting-custom-footers-for-plaintext-emails}

Vous pouvez également définir un pied de page personnalisé pour les e-mails en texte brut depuis l'onglet **Pages et pieds de page de désabonnement** de la page **Préférences des e-mails**. Les mêmes règles que pour le pied de page personnalisé des e-mails HTML s'appliquent.

Si vous n'incluez pas de pied de page en texte brut, Braze en créera automatiquement un à partir du pied de page HTML. Lorsque vos pieds de page personnalisés vous conviennent, sélectionnez **Enregistrer**.

![E-mail avec l'option de pied de page personnalisé en texte brut sélectionnée.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## Considérations {#considerations}

Si vous utilisez [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio), notez que {% raw %}`{{${email_footer}}}`{% endraw %} n'est pas une balise Liquid standard. Elle est pré-traitée avant l'exécution de Liquid, donc utiliser {% raw %}`{{${email_footer}}}`{% endraw %} comme valeur de variable de contexte et appeler le drapeau `:rerender` échouera silencieusement. Utilisez plutôt un [bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers) pour un pied de page d'e-mail.