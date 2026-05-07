---
nav_title: Ouvertures influencées
article_title: Ouvertures influencées
page_order: 2
page_type: reference
description: "Cet article de référence explique les ouvertures influencées et comment les suivre pour obtenir un niveau de détail plus riche sur vos campagnes push."
channel: push

---

# Ouvertures influencées {#influenced-opens}

> Lorsqu'un utilisateur sélectionne une notification push et est redirigé vers votre application, Braze l'enregistre comme une ouverture directe. Lorsque les utilisateurs ne sélectionnent pas la notification mais peuvent tout de même être influencés par celle-ci, Braze l'enregistre comme une ouverture influencée. Cela permet d'obtenir un niveau de détail plus riche sur l'effet de vos Campaigns push.

## Fonctionnement {#how-it-works}

Les ouvertures influencées mesurent essentiellement le nombre d'utilisateurs qui ouvrent l'application après avoir reçu une notification sans avoir sélectionné celle-ci. Comme il n'y a pas d'action directe reliant la notification à l'ouverture de l'application, une ouverture influencée est enregistrée si l'utilisateur ouvre l'application moins de trente minutes après avoir reçu la notification push, ou dans un délai inférieur à la moitié du temps moyen écoulé depuis la dernière session de cet utilisateur.

Par exemple, imaginons que vous envoyez une notification push à vos utilisateurs. Si un utilisateur qui ouvre normalement l'application 30 fois par jour l'ouvre six heures après avoir reçu la notification push, celle-ci reçoit peu ou pas de crédit pour avoir influencé l'ouverture. En revanche, si un utilisateur qui utilise normalement l'application une fois par mois l'ouvre six heures après avoir reçu la notification push, l'ouverture a beaucoup plus de chances d'être comptée comme une ouverture influencée.

Ce n'est pas la même chose que de définir les ouvertures d'application en tant qu'événement de conversion pour une Campaign push. Pour les conversions, toutes les ouvertures survenant dans la fenêtre de conversion sont attribuées à la Campaign. Les ouvertures influencées définissent une fenêtre temporelle et un crédit d'attribution en fonction du comportement de chaque utilisateur.

## Affichage des ouvertures influencées d'une Campaign {#viewing-a-campaigns-influenced-opens}

Les ouvertures influencées sont ajoutées aux ouvertures directes d'une Campaign pour donner un nombre total d'ouvertures. Ce total est affiché sur la page **Campaign Analytics** d'une Campaign push. Le nombre total d'ouvertures et les ouvertures directes apparaissent dans les sections de performance du message et **Historical Performance**. Les ouvertures influencées correspondent à la différence entre ces deux mesures.

![Statistiques sur les ouvertures influencées sur la page des détails d'une Campaign]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Pour plus d'informations sur le suivi des ouvertures, consultez la section correspondante de nos [bonnes pratiques pour les notifications push]({{site.baseurl}}/user_guide/channels/push/best_practices/).