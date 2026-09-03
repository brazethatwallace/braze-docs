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

En utilisant des pieds de page d'e-mail personnalisés, vous n'avez plus besoin de créer un nouveau pied de page pour chaque modèle d'e-mail ou chaque campagne que vous utilisez. Toutes les campagnes existantes et nouvelles reflètent les modifications apportées à votre pied de page personnalisé. N'oubliez pas que le respect de la [loi CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) vous oblige à inclure une adresse physique pour votre entreprise et un lien de désabonnement dans vos e-mails.

{% alert warning %}
Il est de votre responsabilité de vous assurer que votre pied de page personnalisé répond aux exigences susmentionnées.
{% endalert %}

## Créer votre pied de page personnalisé {#create-your-custom-footer}

Pour créer ou modifier votre pied de page personnalisé, procédez comme suit :

1. Allez dans **Paramètres** > **Préférences e-mail** > **Pages d'abonnement et pieds de page**.
2. Accédez à la section **Pied de page personnalisé** et activez les pieds de page personnalisés.
3. Sélectionnez **Modifier** puis modifiez votre pied de page dans la section **Composer**.
4. Sélectionnez **Aperçu** pour prévisualiser l'apparence de votre pied de page d'e-mail dans la boîte de réception d'un client. Vous pouvez éventuellement sélectionner **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Pour plus d'informations, consultez [Aperçu partageable]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).
5. Envoyez un message de test.

![Un exemple de pied de page personnalisé.]({% image_buster /assets/img_archive/custom_footer.png %})

Le pied de page par défaut utilise l'attribut {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} et notre adresse postale physique. Si vous utilisez ce pied de page par défaut, veillez à sélectionner **&#60;other&#62;** pour le **Protocole**.

{% alert important %}
Pour respecter la réglementation CAN-SPAM, votre pied de page personnalisé doit inclure un lien de désabonnement. Vous pouvez utiliser l'attribut Liquid {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} ou votre propre URL de désabonnement personnalisée. Vous ne pourrez pas enregistrer un pied de page personnalisé sans lien de désabonnement.
{% endalert %}

![Valeurs de protocole et d'URL nécessaires pour le pied de page personnalisé.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Pieds de page sans lien de désabonnement {#footers-without-unsubscribe-links}

Soyez très prudent lorsque vous utilisez un modèle avec le pied de page personnalisé {% raw %}`{{${email_footer}}}` mais sans l'étiquette de lien de désabonnement `{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Un avertissement s'affiche, mais c'est à vous de décider d'envoyer un e-mail avec ou sans lien de désabonnement.

Voici un avertissement dans le compositeur d'e-mail :

![Exemple d'e-mail composé sans pied de page.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Voici un avertissement dans le compositeur de Campaign :

![Composition de Campaign sans pied de page.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Ajouter un lien de désabonnement personnalisé {#adding-a-custom-unsubscribe-link}

Pour ajouter un lien de désabonnement personnalisé, vous pouvez remplacer le lien de désabonnement dans le pied de page personnalisé {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} par un lien vers votre propre site web avec un paramètre de requête incluant l'ID utilisateur. Par exemple :
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Ensuite, appelez l'[endpoint `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) pour mettre à jour le statut d'abonnement de l'utilisateur. Pour plus de détails, consultez notre documentation sur le [changement du statut d'abonnement e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

Enregistrez ensuite ce nouveau lien. L'étiquette de désabonnement par défaut de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} doit figurer dans le pied de page. Cela signifie que vous devez inclure le lien par défaut en le « masquant », soit en plaçant l'étiquette dans un commentaire, soit dans une balise `<div>` masquée.

## Bonnes pratiques {#best-practices}

Nous vous suggérons les bonnes pratiques suivantes lors de la création et de l'utilisation de pieds de page personnalisés.

### Personnaliser avec des attributs {#personalizing-with-attributes}

Lors de la création d'un pied de page personnalisé, Braze vous suggère d'utiliser des [attributs pour la personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags). L'ensemble complet des attributs par défaut et personnalisés est disponible, mais voici quelques-uns que vous pourriez trouver utiles :

| Attribut | Étiquette |
| --------- | --- |
| Adresse e-mail de l'utilisateur | {% raw %}`{{${email_address}}}`{% endraw %} |
| URL de désabonnement personnalisée de l'utilisateur | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Cette étiquette remplace l'ancienne étiquette {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Nous vous recommandons d'utiliser la nouvelle étiquette {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} à la place. |
| URL d'abonnement personnalisée de l'utilisateur | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| URL d'inscription personnalisée de l'utilisateur | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| URL du centre de préférences Braze personnalisé de l'utilisateur | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personnaliser avec des attributs" }

### Inclure un lien de désabonnement et un lien d'abonnement {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
En tant que bonne pratique, Braze recommande d'inclure à la fois un lien de désabonnement (tel que ``{{${set_user_to_unsubscribed_url}}}``) et un lien d'abonnement (tel que ``{{${set_user_to_opted_in_url}}}``) dans votre pied de page personnalisé. De cette façon, les utilisateurs peuvent se désabonner ou s'abonner, et vous pouvez collecter passivement des données d'abonnement pour une partie de vos utilisateurs.
{% endraw %}

### Définir des pieds de page personnalisés pour les e-mails en texte brut {#setting-custom-footers-for-plaintext-emails}

Vous pouvez également choisir de définir un pied de page personnalisé pour les e-mails en texte brut depuis l'onglet **Subscription Pages and Footers** de la page **Email Preferences**, qui suit les mêmes règles que le pied de page personnalisé pour les e-mails HTML.

Si vous n'incluez pas de pied de page en texte brut, Braze en crée automatiquement un à partir du pied de page HTML. Lorsque vos pieds de page personnalisés vous conviennent, sélectionnez **Save**.

![E-mail avec l'option « Set Custom Plaintext Footer » sélectionnée.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## Considérations {#considerations}


### BrazeAI Decisioning Studio™

Si vous utilisez [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio), notez que {% raw %}`{{${email_footer}}}`{% endraw %} n'est pas une étiquette Liquid standard. Elle est pré-traitée avant l'exécution de Liquid, donc utiliser {% raw %}`{{${email_footer}}}`{% endraw %} comme valeur de variable de contexte et appeler le drapeau `:rerender` échoue silencieusement. Utilisez plutôt un [bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers) pour un pied de page d'e-mail.

### Modèles de liens et paramètres UTM {#link-templates-and-utm-parameters}

Les modèles de liens ne sont pas automatiquement ajoutés aux liens dans les pieds de page d'e-mail personnalisés lorsque vous utilisez {% raw %}`{{${email_footer}}}`{% endraw %}. Si vous avez besoin de modèles de liens comme des paramètres UTM dans les liens de votre pied de page, utilisez plutôt un [bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers), ou ajoutez manuellement les paramètres UTM aux liens spécifiques de votre pied de page personnalisé.