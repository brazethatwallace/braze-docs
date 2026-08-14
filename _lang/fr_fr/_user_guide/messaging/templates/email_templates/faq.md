---
nav_title: FAQ
article_title: FAQ sur les modèles d'e-mail et de lien
page_order: 10

page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur les modèles d'e-mail et les modèles de lien."
tool:
  - Templates
channel: email

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page fournit des réponses à certaines questions fréquemment posées sur les modèles d'e-mail et les modèles de lien.

## Modèles d'e-mail {#email-templates}

### Puis-je ajouter un lien « voir cet e-mail dans un navigateur » à mes e-mails ? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Non, Braze ne propose pas cette fonctionnalité. En effet, une majorité croissante d'e-mails sont ouverts sur des appareils mobiles et des clients de messagerie modernes, qui affichent les images et le contenu sans aucun problème.

**Solution de contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de destination externe (comme votre site web), vers laquelle vous pouvez ensuite créer un lien depuis la Campaign que vous êtes en train de créer, en utilisant l'outil **Lien** lors de la modification du corps de l'e-mail.

### Comment créer un lien de désabonnement personnalisé pour mes modèles d'e-mail ? {#how-do-i-create-a-custom-unsubscribe-link-for-my-email-templates}

Il existe une option de redirection pour la page de désabonnement.

Vous pouvez remplacer le lien de désabonnement dans le pied de page personnalisé de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} par un lien vers votre propre site web avec un paramètre de requête incluant l'identifiant utilisateur. Par exemple :
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Ensuite, vous pouvez appeler l'[endpoint `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) pour mettre à jour le statut d'abonnement de l'utilisateur. Pour plus de détails, consultez notre documentation sur le [changement du statut d'abonnement aux e-mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

Pour enregistrer ce nouveau lien, la balise de désabonnement par défaut de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} doit figurer dans le pied de page. Cela signifie que vous devrez inclure le lien par défaut en le « masquant », soit en plaçant la balise dans un commentaire, soit dans une balise `<div>` masquée.

- **Exemple de balise dans un commentaire :** `<!-- ${set_user_to_unsubscribed_url} -->`
- **Exemple de commentaire dans une balise `<div>` masquée :** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### Que se passe-t-il si je modifie un modèle d'e-mail actuellement utilisé dans une Campaign ou un Canvas ? {#what-happens-if-i-edit-an-email-template-that-is-currently-being-used-in-a-campaign-or-canvas}

Les modèles d'e-mail servent de point de départ lors de la création d'un e-mail dans une Campaign ou un Canvas. Lorsque vous sélectionnez un modèle, vous pouvez le modifier au sein de la Campaign ou du Canvas, et ces modifications sont indépendantes du modèle d'origine.

Les modifications apportées à un modèle existant ne seront pas répercutées dans les Campaigns ou les Canvas créés à partir de versions précédentes de ce modèle. De même, les modifications apportées à l'e-mail au sein d'une Campaign ou d'un Canvas ne seront pas synchronisées avec le modèle d'origine. Pour les Campaigns API qui incluent un `email_template_id` dans le corps de la requête, Braze utilise la dernière version du modèle au moment de l'envoi.

## Modèles de lien {#link-templates}

### Puis-je ajouter plusieurs modèles de lien à mon e-mail ? {#can-i-upload-multiple-link-templates-to-my-email}

Oui, vous pouvez insérer autant de modèles que vous le souhaitez dans vos e-mails. En tant que bonne pratique, vous devriez tester vos e-mails pour vous assurer que les liens ne dépassent pas 2 000 caractères, car la plupart des navigateurs raccourcissent ou coupent les liens.

### Comment puis-je prévisualiser mes liens avec toutes les balises appliquées ? {#how-do-i-preview-my-links-with-all-of-the-tags-applied}

Il existe plusieurs façons de prévisualiser vos liens. Après avoir appliqué le [modèle de lien]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template), vous pouvez vous envoyer un [e-mail de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) pour visualiser tous les liens.

Depuis le volet de prévisualisation dans un nouvel onglet, vous pouvez également ouvrir les liens pour les consulter. Vous pouvez aussi survoler les liens dans le volet de prévisualisation et les voir en bas de votre navigateur.

### Comment le modèle de lien fonctionne-t-il avec Liquid ? {#how-does-link-templating-work-with-liquid}

Les modèles de lien sont développés et ajoutés à chaque URL avant toute expansion Liquid. Si une partie de votre URL est générée à l'aide d'un extrait de code Liquid, nous recommandons que la base de l'URL et le point d'interrogation (?) soient codés en dur pour que les modèles de lien soient correctement développés.

Évitez d'ajouter le point d'interrogation (?) à votre Liquid, car cela amènerait les modèles de lien à d'abord ajouter un point d'interrogation (?), puis le processus d'expansion Liquid ajouterait un second point d'interrogation (?).

#### URL codées en dur versus attributs personnalisés {#hardcoded-urls-versus-custom-attributes}

Lorsque vous utilisez une URL codée en dur dans l'éditeur HTML (par exemple, `https://braze.com?12345`), Braze détecte qu'un `?` existe déjà et utilise automatiquement `&` pour ajouter les paramètres de votre modèle de lien. Cependant, lorsque vous utilisez un attribut personnalisé contenant une URL avec un `?` (par exemple, {% raw %}`{{custom_attribute.${my_url}}}`{% endraw %} où `my_url` est `https://braze.com?12345`), Braze ne vérifie pas si un `?` existe déjà dans la valeur de l'attribut personnalisé. Dans ce cas, le modèle de lien ajoute un autre `?` avant les paramètres, ce qui donne une URL comme `https://braze.com?12345?utm_source=...`.

Pour éviter ce problème lorsque vous utilisez des attributs personnalisés susceptibles de contenir des paramètres de requête, codez en dur le `?` ou le `&` après l'attribut personnalisé selon que la valeur de l'attribut personnalisé inclut ou non des paramètres de requête. Par exemple, si votre attribut personnalisé inclut toujours un `?`, utilisez {% raw %}`{{custom_attribute.${my_url}}}&`{% endraw %} pour vous assurer que le modèle de lien ajoute correctement les paramètres.

## Aliasing de lien {#link-aliasing}

### Comment l'activation de l'aliasing de lien impactera-t-elle mes Content Blocks et mes modèles de lien ? {#how-will-enabling-link-aliasing-impact-my-content-blocks-and-link-templates}

Pour tous les nouveaux Content Blocks créés, l'aliasing de lien est appliqué à l'ensemble des espaces de travail, car il s'agit d'une fonctionnalité au niveau de l'entreprise.

Les Content Blocks existants ne seront pas modifiés lorsque l'aliasing de lien est activé. Bien que les modèles de lien existants ne soient pas modifiés, la section de modèle de lien existante dans un message sera supprimée. Consultez [Aliasing de lien dans les Content Blocks]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-aliasing-in-content-blocks) pour plus d'informations.

### Puis-je utiliser une logique conditionnelle Liquid entièrement dans une balise d'ancrage HTML ? {#can-i-use-liquid-conditional-logic-entirely-within-an-html-anchor-tag}

Non, l'aliasing de lien de Braze ne reconnaîtra pas correctement le HTML.

Lorsqu'une telle logique est utilisée conjointement avec des fonctionnalités qui doivent analyser le HTML (comme une accroche ou un modèle de lien), la bibliothèque utilisée pour scanner le HTML peut modifier la balise d'ancrage d'une manière qui empêchera le `href` approprié d'être correctement modélisé. La bibliothèque déterminera alors que le HTML est invalide, car elle est agnostique par rapport au code Liquid.

Utilisez plutôt une logique Liquid contenant une balise d'ancrage complète à chaque étape. Cela n'interférera pas avec l'analyse du HTML, car la logique inclut plusieurs instances de HTML valide. Vous pouvez également simplifier votre logique en assignant puis en modélisant une variable dans la balise d'ancrage appropriée.