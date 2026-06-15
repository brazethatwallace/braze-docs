---
nav_title: Utiliser le compteur de badges
article_title: Utiliser le compteur de badges
page_order: 8

page_type: reference
description: "Cet article explique comment utiliser le compteur de badges iOS pour réengager les utilisateurs qui n'ont pas remarqué une notification push, ou qui ont désactivé les notifications push au premier plan."
platform: iOS
channel:
- push
- in-app messages

---

# Utiliser le compteur de badges {#utilizing-badge-count}

> Le compteur de badges iOS affiche le nombre de notifications non lues au sein de votre application, sous la forme d'un cercle rouge dans le coin supérieur droit de l'icône de l'application. Ces dernières années, le badge est devenu un moyen efficace de réengagement des utilisateurs d'applications.

Le compteur de badges peut être utilisé pour réengager vos utilisateurs qui n'ont pas remarqué une notification push, ou qui ont désactivé les notifications push au premier plan. De même, il peut être utilisé pour informer vos utilisateurs de messages non consultés, tels que des mises à jour in-app.

## Compteur de badges avec Braze {#badge-count-with-braze}

Vous pouvez spécifier le nombre de badges souhaité lorsque vous rédigez une notification push via le tableau de bord de Braze. Ce nombre peut être défini comme un attribut utilisateur avec un envoi de messages personnalisé, permettant une logique de personnalisation infinie. Si vous souhaitez envoyer une notification push silencieuse qui met à jour le compteur de badges sans déranger l'utilisateur, ajoutez le flag « Content-Available » à votre notification push et laissez le contenu du message vide.

{% alert note %}
Vous vous demandez comment définir le compteur de badges pour Android ? Android gère automatiquement les badges d'application pour les notifications push, il n'y a donc pas de paramètres de personnalisation pour les badges dans Braze.
{% endalert %}

### Supprimer le compteur de badges {#removing-the-badge-count}

Définissez le compteur de badges à 0 ou "" pour supprimer le compteur de badges de l'icône de l'application. Braze effacera également automatiquement le badge lorsqu'une notification push est reçue alors que l'application est au premier plan.

## Bonnes pratiques {#best-practices}

Afin d'optimiser le pouvoir de réengagement des badges, il est essentiel de configurer vos paramètres de badges de manière à simplifier au maximum l'expérience utilisateur.

### Maintenir un compteur de badges bas {#keep-the-badge-count-low}
Les études montrent qu'au-delà de deux chiffres, les utilisateurs perdent généralement tout intérêt pour les mises à jour et cessent souvent d'utiliser l'application.

> Il peut y avoir des exceptions à cette règle selon la nature de votre application (par exemple, les applications d'e-mail et de messagerie de groupe).

### Limiter ce que le compteur de badges peut représenter {#limit-the-things-a-badge-count-can-represent}
Lorsque vous utilisez les badges, vous souhaitez rendre les notifications aussi claires et directes que possible. En limitant le nombre de choses qu'une notification de badge peut représenter, vous offrez à vos utilisateurs une familiarité avec les fonctionnalités et les mises à jour de votre application.