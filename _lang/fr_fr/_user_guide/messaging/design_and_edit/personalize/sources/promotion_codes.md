---
nav_title: Codes de promotion
article_title: Codes de promotion
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Découvrez les listes de codes de promotion pour les ajouter à vos campagnes et Canvas."
---

# Codes de promotion

> Découvrez les listes de codes de promotion pour les ajouter à vos campagnes et Canvas.

## À propos des codes de promotion

Les codes de promotion vous permettent d'insérer des valeurs uniques et limitées dans le temps dans vos messages pour stimuler les conversions. Chaque liste peut contenir jusqu'à 20 millions de codes, et chaque code peut durer jusqu'à six mois avant d'expirer.

Lorsque Braze envoie un message contenant un code de promotion, le code est déduit avant l'envoi du message. Pour garantir que les codes sont cohérents, uniques et jamais réutilisés :

- Un message échoué consomme tout de même le code.
- Lors d'envois multicanaux, le même code est appliqué sur tous les canaux.
- Avec le Liquid conditionnel, toutes les listes référencées voient leurs codes déduits, même si une seule branche est affichée.
- L'entrée ou la réentrée dans une étape du Canvas consomme un nouveau code.

Si vous placez plusieurs extraits de code provenant de la même liste dans un seul message, Braze appliquera le même code à tous les extraits. Pour éviter de manquer de codes, nous vous recommandons d'en importer plus que ce que vous prévoyez d'utiliser.

{% tabs local %}
{% tab Exemple %}
Pensez aux codes de promotion comme à des coupons dans un bureau de poste. Une fois que l'employé a retiré un coupon de la pile pour votre lettre, il est parti — même si la lettre n'arrive jamais.

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
Les codes de promotion ne peuvent pas être envoyés dans les messages in-app dans Canvas.
{% endalert %}

## Étapes suivantes

Vous cherchez les prochaines étapes ? Commencez ici :

- [Créer une liste de codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/)
- [Utiliser des codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#using-promotion-codes)
- [Consulter l'utilisation des codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#viewing-promotion-code-usage)

## Questions fréquentes

### Quels canaux de communication puis-je utiliser avec les codes de promotion ?

Les codes de promotion sont actuellement pris en charge pour les e-mails, les notifications push mobiles, les notifications push Web, les cartes de contenu, les webhooks, les SMS et WhatsApp. Les campagnes d'e-mails transactionnels Braze et les messages in-app ne prennent pas en charge les codes de promotion actuellement.

### Les envois de test et les envois au groupe initiateur comptent-ils dans l'utilisation ?

Par défaut, les envois de test et les envois d'e-mails au groupe initiateur utilisent des codes de promotion par utilisateur et par envoi de test. Cependant, vous pouvez contacter votre gestionnaire de compte Braze pour modifier ce comportement afin de ne pas utiliser de codes de promotion pendant les tests.

### Que se passe-t-il lorsque plusieurs canaux de communication utilisent le même extrait de code de promotion ?

Si un utilisateur donné est éligible pour recevoir un code via plusieurs canaux, il recevra le même code sur chaque canal. Un seul code de promotion sera utilisé, quel que soit le nombre de canaux concernés.

### Puis-je utiliser plusieurs extraits Liquid pour référencer la même liste de codes de promotion dans un seul message ?

Oui. Braze appliquera le même code de promotion à toutes les instances de cet extrait dans le message, garantissant que l'utilisateur ne reçoive qu'un seul code unique.

### Que se passe-t-il lorsqu'une liste de codes de promotion est expirée ou vide ?

Les codes expirés sont supprimés après six mois.

Si le message devait contenir un code de promotion provenant d'une liste vide ou expirée, le message sera annulé.

Si le message contient une logique Liquid qui insère conditionnellement un code de promotion, le message ne sera annulé que s'il devait contenir un code de promotion. Si le message ne devait pas contenir de code de promotion, il sera envoyé normalement.

### Si j'ai importé les mauvais codes de promotion, puis-je les mettre à jour ?

Oui. Vous pouvez résoudre ce problème en rendant obsolète la liste entière ou en utilisant une marque substitutive pour supprimer la liste. Pour en savoir plus, consultez [Mettre à jour une liste de codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/#updating-a-promotion-code-list).

### Puis-je enregistrer un code de promotion dans le profil d'un utilisateur pour de futurs messages ?

Oui. Vous pouvez enregistrer des codes de promotion dans le profil d'un utilisateur via une étape de mise à jour utilisateur. Pour en savoir plus, consultez [Enregistrer des codes de promotion dans les profils utilisateur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#save-to-profile).