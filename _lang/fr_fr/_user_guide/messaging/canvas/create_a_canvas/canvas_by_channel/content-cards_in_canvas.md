---
nav_title: Content Cards
article_title: Content Cards dans Canvas
page_order: 1
page_type: reference
description: "Cet article de référence décrit les fonctionnalités et les particularités liées à l'utilisation des Content Cards comme canal de communication dans Canvas."
tool: Canvas
channel: content cards

---

# Content Cards dans Canvas {#content-cards-in-canvas}

> Les Content Cards peuvent être envoyées à vos clients dans le cadre de leur parcours Canvas. Cet article décrit les fonctionnalités et les particularités liées à l'utilisation des Content Cards comme canal de communication dans Canvas.

Comme pour les autres canaux de communication de Canvas, les Content Cards sont envoyées sur l'appareil de l'utilisateur lorsqu'il remplit les critères d'audience et de ciblage définis pour l'étape concernée. Une fois la Content Card envoyée, elle sera disponible dans le flux de chaque utilisateur éligible lors de la prochaine actualisation de son flux de cartes.

![Content Cards sélectionnées comme canal de communication pour une étape Message.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Deux options modifient la façon dont l'étape Content Card interagit avec Canvas : son [expiration](#content-card-expiration) et sa [suppression](#removal).

## Expiration des Content Cards {#content-card-expiration}

Lors de la création d'une nouvelle Content Card, vous pouvez choisir quand elle doit expirer du flux de l'utilisateur en fonction de son heure d'envoi. Le compte à rebours de l'expiration d'une Content Card commence lorsque l'utilisateur atteint l'étape Message dans le Canvas où la carte est envoyée. La carte sera active dans le flux de l'utilisateur à partir de ce moment jusqu'à son expiration. Une carte peut rester dans le flux d'un utilisateur pendant 30 jours maximum.

![Paramètres d'expiration d'une Content Card pour une étape Message qui sera supprimée après trois heures dans le flux de l'utilisateur.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Types d'expiration {#types-of-expiration}

Vous disposez de deux méthodes pour définir quand une carte doit disparaître du flux d'un utilisateur : une date relative ou une date absolue.

#### Dates relatives {#relative-dates}

Lorsque vous choisissez une date relative, comme « Supprimer les cartes envoyées après 5 jours dans le flux de l'utilisateur », vous pouvez définir une date d'expiration allant jusqu'à 30 jours.

#### Dates absolues {#absolute-dates}

Lorsque vous choisissez une date absolue, comme « Supprimer les cartes envoyées le 1er décembre 2023 à 16 h », certaines subtilités sont à prendre en compte.

Bien que vous puissiez spécifier une durée d'expiration supérieure à 30 jours, la Content Card restera dans le flux de l'utilisateur pendant 30 jours maximum. Spécifier une durée supérieure à 30 jours vous permet de tenir compte d'éventuels retards avant le déclenchement de l'étape Message, mais cela ne prolonge pas la durée de vie maximale de la carte dans le flux de l'utilisateur.

Soyez prudent lorsque vous définissez une date d'expiration plus de 30 jours après le lancement du Canvas. Si un utilisateur atteint l'étape Message plus de 30 jours avant la date d'expiration spécifiée, la carte ne sera pas envoyée.

#### Expiration personnalisée avec Liquid {#personalized-expiry-with-liquid}

Lorsque vous utilisez la personnalisation Liquid pour définir la durée d'expiration (par exemple, en utilisant des attributs personnalisés ou des propriétés d'entrée Canvas), le comportement diffère de celui des dates absolues ou relatives :

- Si l'expiration personnalisée aboutit à une durée supérieure à 30 jours, Braze la plafonne automatiquement à la limite maximale de 30 jours.
- La Content Card est tout de même envoyée à l'utilisateur avec l'expiration plafonnée.
- L'utilisateur progresse vers l'étape suivante du Canvas.

Ce plafonnement garantit que les cartes avec une expiration personnalisée sont délivrées même lorsque la durée calculée dépasse la limite de la plateforme. Le résultat du registre de traitement affichera « Personalized expiration capped by max TTL » avec des détails indiquant `reason=capped_by_max_ttl` et `capped=true`.

### Comportement à l'expiration {#expiration-behavior}

La Content Card reste disponible dans le flux de l'utilisateur jusqu'à sa date d'expiration, même si l'utilisateur progresse vers les étapes suivantes du parcours Canvas. Si vous ne souhaitez pas que la Content Card soit active lorsque les étapes suivantes du Canvas sont délivrées, assurez-vous que l'expiration est plus courte que le délai des étapes suivantes.

Après l'expiration d'une Content Card, elle sera automatiquement supprimée du flux de l'utilisateur lors de la prochaine actualisation, même si l'utilisateur ne l'a pas encore consultée.

## Suppression des Content Cards {#removal}

Les Content Cards peuvent être supprimées lorsque les utilisateurs effectuent un achat ou réalisent un événement personnalisé. Vous pouvez sélectionner l'un des événements de suppression suivants : **Perform Custom Event** et **Place Order**. Sélectionnez ensuite **Add Trigger**.

![« Supprimer les cartes lorsque les utilisateurs effectuent un achat ou réalisent un événement personnalisé » sélectionné avec le déclencheur de suppression des cartes pour les utilisateurs qui effectuent un achat spécifique.]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Rapports et analyses {#reporting-and-analytics}

Après le lancement d'une étape Content Cards dans Canvas, vous pouvez commencer à analyser plusieurs indicateurs pour cette étape. Ces indicateurs incluent le nombre de messages envoyés, les impressions quotidiennes uniques, les taux de conversion, le chiffre d'affaires total, et bien plus encore.

![Analyses d'une étape Message avec les performances des messages Content Card.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Pour plus d'informations sur les indicateurs disponibles et leurs définitions, consultez notre [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

## Cas d'utilisation {#use-cases}

### Offres promotionnelles {#promotional-offers}

Ajoutez des cartes au flux d'un utilisateur lorsqu'il devient éligible à des promotions et publicités spécifiques. Par exemple, si un utilisateur devient éligible à une nouvelle offre après avoir effectué une action ou un achat, Canvas vous permet de lui envoyer une Content Card, en complément d'autres canaux de communication, afin que l'offre soit disponible lors de sa prochaine ouverture de l'application.

### Boîte de réception des notifications push {#push-notification-inbox}

Il arrive qu'un utilisateur ignore une notification push ou supprime un e-mail, mais vous souhaitez lui rappeler l'offre ou la promouvoir au cas où il changerait d'avis.

Avec Canvas, vous pouvez ajouter un composant qui envoie à la fois une Content Card et une notification push, offrant ainsi aux utilisateurs une « boîte de réception » persistante de cartes correspondant aux messages promotionnels envoyés par notification push.

### Flux multiples basés sur des catégories {#multiple-feeds-based-on-categories}

Vous pouvez séparer vos Content Cards en plusieurs flux basés sur des catégories, comme différents sujets que les utilisateurs peuvent parcourir, ou des flux transactionnels et marketing. Pour plus d'informations sur la création de flux multiples à l'aide de paires clé-valeur, consultez notre guide sur la [personnalisation des flux de Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds).