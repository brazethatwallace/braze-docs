---
nav_title: Utiliser les codes
article_title: Utiliser les codes de promotion
page_order: 0.2
description: "Découvrez comment utiliser les codes de promotion et consulter leur utilisation pour vos Campaigns et Canvas."
---

# Utiliser les codes de promotion {#use-promotion-codes}

> Découvrez comment utiliser les codes de promotion et consulter leur utilisation pour vos Campaigns et Canvas.

## Conditions préalables {#prerequisites}

Avant de pouvoir utiliser des codes de promotion, vous devez [créer une liste de codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create).

## Utiliser les codes de promotion {#using-promotion-codes}

Pour envoyer un code de promotion dans un message, sélectionnez **Copier l'extrait de code** à côté de la liste de codes de promotion [que vous avez précédemment créée]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create).

![Option permettant de copier l'extrait de code à coller dans votre message.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Collez les extraits de code dans l'un de vos messages dans Braze, puis utilisez [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) pour insérer l'un des codes de promotion uniques de votre liste. Ce code est marqué comme envoyé, ce qui garantit qu'aucun autre message n'envoie le même code.

![Un exemple de message « Faites-vous plaisir ce printemps avec notre offre exclusive » suivi de l'extrait de code.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Entre les étapes du Canvas {#across-canvas-steps}

Lorsqu'un extrait de code est utilisé dans une Campaign ou un Canvas avec des messages multicanaux, chaque utilisateur reçoit un code unique. Dans un Canvas comportant plusieurs étapes qui font référence à des codes de promotion, un utilisateur obtient un nouveau code pour chaque étape dans laquelle il entre.

Pour attribuer un code de promotion dans un Canvas et le réutiliser entre les étapes :

1. Attribuez le code de promotion en tant qu'attribut personnalisé dans la première étape (Mise à jour utilisateur).
2. Utilisez Liquid dans les étapes suivantes pour faire référence à cet attribut personnalisé au lieu de générer un nouveau code.

Lorsqu'un utilisateur est éligible à un code sur plusieurs canaux, il reçoit le même code sur chaque canal. Par exemple, s'il reçoit des messages par e-mail et par notification push, le même code est envoyé aux deux. Le reporting reflète également un code unique.

{% alert note %}
Si aucun code de promotion n'est disponible, les messages de test ou en production qui dépendent de codes ne sont pas envoyés.
{% endalert %}

### Campaigns de messages in-app {#promotion-codes-iam-campaigns}

Après avoir créé une [Campaign de messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages), vous pouvez insérer un [extrait de code de liste de codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes) dans le corps de votre message in-app. Les codes de promotion dans les messages in-app sont déduits et utilisés uniquement lorsqu'un utilisateur déclenche l'affichage du message in-app.

### Messages de test {#test-messages}

Les envois de test et les envois d'e-mails au groupe initiateur consomment des codes de promotion, sauf demande contraire. Contactez votre gestionnaire de compte Braze pour modifier ce comportement afin que les codes de promotion ne soient pas utilisés lors des envois de test et des envois d'e-mails au groupe initiateur.

### Avec les extras de message pour Currents {#with-message-extras-for-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Enregistrer les codes de promotion dans les profils utilisateur {#save-to-profile}

Pour faire référence au même code de promotion dans les messages suivants, le code doit être enregistré dans le profil utilisateur en tant qu'attribut personnalisé. Cela peut être fait via une [étape de mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) qui attribue le code de réduction à un attribut personnalisé, comme « Code promo », directement avant une étape de message.

Tout d'abord, sélectionnez les éléments suivants pour chaque champ de l'étape de mise à jour utilisateur :

- **Nom de l'attribut :** Code promo
- **Action :** Mettre à jour
- **Valeur de la clé :** L'extrait de code Liquid du code de promotion, tel que {% raw %}`{% promotion('spring25') %}`{% endraw %}

Ensuite, ajoutez l'attribut personnalisé (dans cet exemple, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) à un message. Le code de réduction est alors intégré au modèle.

## Consulter l'utilisation des codes de promotion {#viewing-promotion-code-usage}

Vous pouvez trouver le nombre de codes restants dans la colonne **Restants** de la liste des codes de promotion sur la page **Codes de promotion**.

![Un exemple de code de promotion avec des codes non utilisés.]({% image_buster /assets/img/promocodes/promocode11.png %})

Ce nombre de codes peut également être consulté en revisitant une page de liste de codes de promotion existante. Vous pouvez aussi exporter les codes non utilisés sous forme de fichier CSV.

![Un code de promotion nommé « Black Friday Sale » avec 992 codes restants.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envois multicanaux et monocanaux {#multichannel-and-single-channel-sends}

Pour les Campaigns et Canvas multicanaux et à envoi unique, tous les codes de promotion référencés dans le Liquid d'un message sont déduits pour être utilisés **avant** l'envoi du message afin de garantir les points suivants :

- Les mêmes codes de promotion sont utilisés sur tous les canaux dans un message multicanal.
- Les codes de promotion supplémentaires ne sont pas utilisés si un message échoue ou est abandonné.

Si un utilisateur a deux listes de codes de promotion référencées dans un message divisé par une balise de logique conditionnelle Liquid, tous les codes de promotion sont tout de même déduits, quel que soit le flux conditionnel suivi par l'utilisateur.

Si un utilisateur entre dans une nouvelle étape du Canvas ou entre à nouveau dans un Canvas, et que l'extrait de code Liquid du code de promotion est appliqué à nouveau pour un message destiné à cet utilisateur, un nouveau code de promotion est utilisé.

### Exemple {#example}

Dans l'exemple suivant, les deux listes de codes de promotion `vip-deal` et `regular-deal` sont déduites. Voici le Liquid :

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}

Braze recommande de télécharger plus de codes de promotion que ce que vous estimez utiliser. Si une liste de codes de promotion expire ou est épuisée, les messages suivants sont abandonnés.

{% alert tip %}
**Voici une analogie pour comprendre comment les codes de promotion sont consommés dans Braze.** <br><br>Imaginez que l'envoi de votre message est comme l'envoi d'une lettre à la poste. Vous remettez la lettre à un employé, et celui-ci constate que votre lettre doit inclure un coupon. L'employé prend le premier coupon de la pile et l'ajoute à l'enveloppe. L'employé envoie la lettre, mais pour une raison quelconque, la lettre se perd dans le courrier (et le coupon est désormais perdu également). <br><br>Dans ce scénario, Braze est l'employé de la poste, et votre code de promotion est le coupon. Nous ne pouvons pas le récupérer une fois qu'il a été retiré de la pile de codes de promotion, quel que soit le résultat du webhook.
{% endalert %}