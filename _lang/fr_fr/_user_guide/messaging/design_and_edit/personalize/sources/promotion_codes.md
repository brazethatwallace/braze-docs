---
nav_title: Codes de promotion
article_title: Codes de promotion
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Découvrez les listes de codes de promotion pour les ajouter à vos campagnes et Canvas."
---

# Codes de promotion {#promotion-codes}

> Découvrez les listes de codes de promotion pour les ajouter à vos campagnes et Canvas.

## À propos des codes de promotion {#about-promotion-codes}

Les codes de promotion vous permettent d'insérer des valeurs uniques et limitées dans le temps dans vos messages pour stimuler les conversions. Chaque liste peut contenir jusqu'à 20 millions de codes, et chaque code peut durer jusqu'à six mois avant d'expirer.

Lorsque Braze envoie un message avec un code de promotion, le code est déduit avant l'envoi du message. Pour garantir que les codes sont cohérents, uniques et jamais réutilisés :

- Un message en échec consomme tout de même le code.
- Lors d'envois multicanaux, le même code est appliqué sur tous les canaux.
- Avec le Liquid conditionnel, toutes les listes référencées voient leurs codes déduits, même si une seule branche est affichée.
- L'entrée ou la réentrée dans une étape du Canvas consomme un nouveau code.

Si vous placez plusieurs extraits de code provenant de la même liste dans un seul message, Braze applique le même code à tous les extraits. Pour éviter de manquer de codes, importez plus de codes que ce que vous prévoyez d'utiliser.

{% tabs local %}
{% tab Exemple %}
Pensez aux codes de promotion comme des coupons dans un bureau de poste. Une fois que l'employé a retiré un coupon de la pile pour votre lettre, il est parti, même si la lettre n'arrive jamais.

Par exemple, dans le Liquid conditionnel suivant, les codes des deux listes (`vip-deal` et `regular-deal`) sont déduits, même si chaque utilisateur ne voit qu'une seule branche :

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Les codes de promotion sont disponibles dans les Campaigns de messages in-app, mais ne peuvent pas être envoyés dans les messages in-app dans Canvas.
{% endalert %}

## Prochaines étapes {#next-steps}

Vous cherchez les prochaines étapes ? Commencez ici :

{% article_tiles %}
- name: Créer une liste de codes de promotion
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create
- name: Utiliser les codes de promotion
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes
- name: Consulter l'utilisation des codes de promotion
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#viewing-promotion-code-usage
{% endarticle_tiles %}

## Questions fréquentes {#frequently-asked-questions}

### Quels canaux de communication puis-je utiliser avec les codes de promotion ? {#which-messaging-channels-can-i-use-with-promotion-codes}

Les codes de promotion sont pris en charge pour les e-mails, les notifications push mobiles, les notifications push Web, les Content Cards, les webhooks, les SMS et WhatsApp. Les campagnes de messages in-app prennent en charge les codes de promotion en tant que fonctionnalité en accès anticipé. Les campagnes d'e-mails transactionnels Braze et les messages in-app dans Canvas ne prennent pas en charge les codes de promotion.

### Les envois de test et les envois au groupe initiateur sont-ils comptabilisés dans l'utilisation ? {#do-test-and-seed-sends-count-towards-usage}

Par défaut, les envois de test et les envois d'e-mails au groupe initiateur utilisent des codes de promotion par utilisateur et par envoi de test. Cependant, vous pouvez contacter votre gestionnaire de compte Braze pour modifier ce comportement afin de ne pas utiliser de codes de promotion lors des tests.

### Que se passe-t-il lorsque plusieurs canaux de communication utilisent le même extrait de code de promotion ? {#what-happens-when-multiple-messaging-channels-use-the-same-promotion-code-snippet}

Si un utilisateur donné est éligible pour recevoir un code via plusieurs canaux, il reçoit le même code via chaque canal. Un seul code de promotion est utilisé, quel que soit le nombre de canaux par lesquels il est reçu.

### Puis-je utiliser plusieurs extraits Liquid pour référencer la même liste de codes de promotion dans un seul message ? {#can-i-use-multiple-liquid-snippets-to-reference-the-same-promotion-code-list-in-one-message}

Oui. Braze applique le même code de promotion à toutes les instances de cet extrait dans le message, garantissant ainsi que l'utilisateur ne reçoive qu'un seul code unique.

### Que se passe-t-il lorsqu'une liste de codes de promotion a expiré ou est vide ? {#what-happens-when-a-promotion-code-list-is-expired-or-empty}

Les codes expirés sont supprimés après six mois.

Si le message devait contenir un code de promotion provenant d'une liste vide ou expirée, le message est annulé.

Si le message contient une logique Liquid qui insère conditionnellement un code de promotion, le message n'est annulé que s'il devait contenir un code de promotion. Si le message ne devait pas contenir de code de promotion, le message est envoyé normalement.

### Si j'ai importé les mauvais codes de promotion, puis-je les mettre à jour ? {#if-i-uploaded-the-wrong-promotion-codes-can-i-update-them}

Si vous avez importé des codes incorrects, vous avez deux options pour résoudre ce problème :

- **Déprécier la liste entière :** arrêtez d'utiliser la liste actuelle dans toutes les Campaigns, tous les Canvas ou tous les modèles. Importez ensuite les codes corrects dans une nouvelle liste et mettez à jour tous vos messages pour utiliser la nouvelle liste.
- **Épuiser les codes incorrects :** créez une Campaign qui envoie des codes de la liste incorrecte à un utilisateur fictif jusqu'à ce que tous les mauvais codes soient utilisés. Ensuite, réimportez les codes corrects dans la même liste, en excluant les codes incorrects.

Pour des conseils généraux sur la mise à jour d'une liste, consultez [Mise à jour d'une liste de codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#updating-a-promotion-code-list).

### Braze suit-il quels utilisateurs ont reçu ou utilisé quels codes de promotion ? {#does-braze-track-which-users-received-or-redeemed-which-promotion-codes}

Lorsqu'un message utilise un code de promotion, Braze marque ce code comme consommé afin qu'il ne puisse pas être envoyé à nouveau et met à jour le décompte restant de la liste. Braze ne tient pas de rapport des codes envoyés, ne suit pas quels utilisateurs spécifiques ont reçu chaque code, et ne suit pas si les codes ont été utilisés.

Si vous devez associer des codes à des utilisateurs ou suivre l'utilisation vous-même, vous pouvez :

- Enregistrer les codes de promotion dans les profils utilisateur via une étape de mise à jour utilisateur. Pour en savoir plus, consultez [Enregistrer les codes de promotion dans les profils utilisateur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile).
- Envoyer les valeurs des codes de promotion vers Currents à l'aide de l'étiquette Liquid `message_extras`. Pour en savoir plus, consultez [Envoyer des informations de codes de promotion vers Currents]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#sending-promotion-code-information-to-currents).

### Puis-je enregistrer un code de promotion dans le profil d'un utilisateur pour de futurs messages ? {#can-i-save-a-promotion-code-to-a-users-profile-for-future-messages}

Oui. Vous pouvez enregistrer des codes de promotion dans le profil d'un utilisateur via une étape de mise à jour utilisateur. Pour en savoir plus, consultez [Enregistrer les codes de promotion dans les profils utilisateur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile).