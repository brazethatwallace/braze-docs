---
nav_title: Créer des codes
article_title: Créer des codes de promotion
page_order: 0.1
description: "Découvrez comment créer des codes de promotion dans vos campagnes et Canvas."
---

# Créer des codes de promotion

> Découvrez comment créer des codes de promotion dans vos campagnes et Canvas.

## Création d'une liste de codes de promotion {#create}

### Étape 1 : Créer une nouvelle liste

Dans le tableau de bord, accédez à **Paramètres des données** > **Codes de promotion**, puis sélectionnez **Créer une liste de codes de promotion**.

![Bouton pour créer un code de promotion.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Étape 2 : Saisir les détails

1. Nommez votre liste de codes de promotion et ajoutez une description facultative.
2. Ensuite, créez un extrait de code pour le code de promotion.

Voici quelques points à prendre en compte lors de la création d'un extrait de code :

- Vous ne pouvez pas modifier un extrait de code après l'avoir enregistré.
- Les extraits de code sont sensibles à la casse. Par exemple, le système reconnaît « Birthday_promo » et « birthday_promo » comme deux extraits différents.
- Utilisez le nom de l'extrait de code dans Liquid pour référencer cet ensemble de codes de promotion.
- Assurez-vous que l'extrait de code n'est pas déjà utilisé dans une autre liste.

![Une liste de codes de promotion nommée « SpringSale2025 » avec l'extrait de code « spring25 ».]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Étape 3 : Choisir les options du code de promotion

Chaque liste de codes de promotion possède une date et une heure d'expiration correspondantes, définies lors de la création. La durée d'expiration maximale est de six mois à compter du jour où vous créez ou modifiez votre liste.

Pendant cette période, vous pouvez modifier et mettre à jour la date d'expiration autant de fois que nécessaire. Cette date d'expiration s'applique à tous les codes ajoutés à cette liste. À l'expiration, les codes sont supprimés du système Braze et tout message faisant appel à l'extrait de code de cette liste n'est pas envoyé.

![Paramètres d'expiration de la liste indiquant que tous les codes restants expireront le 30 avril 2025 à 0 h 00.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Vous avez également la possibilité de configurer des alertes de seuil facultatives et personnalisées. Si elles sont configurées, ces alertes envoient un e-mail au destinataire désigné lorsque la liste est à court de codes de promotion disponibles ou lorsque votre liste de codes de promotion approche de sa date d'expiration. Le destinataire est notifié une fois par jour.

![Un exemple d'alerte de seuil pour notifier « marketing@abc.com » lorsque la liste de codes de promotion expire dans 5 jours.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Étape 4 : Charger les codes de promotion

Braze ne gère ni la création ni l'utilisation des codes, ce qui signifie que vous devez générer vos codes de promotion dans un fichier CSV et les charger dans Braze.

Assurez-vous que votre fichier CSV respecte les consignes suivantes :

- Il inclut une colonne pour les codes de promotion.
- Il contient un code de promotion par ligne.

Vous pouvez utiliser notre intégration native avec [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) pour créer et exporter des codes de promotion.

{% alert important %}
La taille maximale du fichier est de 100&nbsp;Mo et la taille maximale de la liste est de 20 millions de codes non utilisés. Si vous constatez que le mauvais fichier a été chargé, chargez-en un nouveau pour remplacer le précédent.
{% endalert %}

1. Une fois le chargement terminé, sélectionnez **Enregistrer la liste** pour enregistrer tous les détails et codes que vous venez de saisir.

![Fichier CSV nommé « springsale » chargé avec succès.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2. Après avoir sélectionné enregistrer, une nouvelle ligne apparaît dans l'**Historique d'importation**.
3. Pour actualiser le tableau et vérifier si votre importation est terminée, sélectionnez <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Synchroniser** en haut du tableau.

![Codes de promotion en cours de chargement.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Les fichiers volumineux nécessitent plusieurs minutes pour être importés. Pendant ce temps, vous pouvez quitter la page et travailler sur autre chose. Lorsque l'importation est terminée, l'état passe à **Terminé** dans le tableau.
{% endalert %}

## Mise à jour d'une liste de codes de promotion

Pour mettre à jour une liste, sélectionnez l'une de vos listes existantes. Vous pouvez modifier le nom, la description, l'expiration de la liste et les alertes de seuil. Vous pouvez également ajouter d'autres codes à la liste en chargeant de nouveaux fichiers et en sélectionnant **Mettre à jour la liste**. Tous les codes de la liste ont la même date d'expiration, quelle que soit la date d'importation.

{% alert important %}
Les codes de promotion ne peuvent pas être supprimés.
{% endalert %}

### Correction d'une liste de codes de promotion incorrecte

Si vous avez chargé un fichier CSV contenant des codes de promotion incorrects et sélectionné **Enregistrer la liste**, vous pouvez résoudre ce problème de l'une des manières suivantes :

- Rendre la liste obsolète : cessez d'utiliser la liste de codes de promotion actuelle dans toutes les campagnes, Canvas ou modèles. Ensuite, chargez le fichier CSV contenant les codes corrects et utilisez-les dans vos messages.
- Utiliser les codes incorrects : créez une campagne qui envoie des codes de promotion de la liste incorrecte vers une marque substitutive jusqu'à ce que tous les codes incorrects soient utilisés. Ensuite, chargez les codes de promotion corrects dans la même liste.