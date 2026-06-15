---
nav_title: "Fonctionnalité d'icône d'application personnalisée (iOS 10.3)"
article_title: "Fonctionnalité d'icône d'application personnalisée (iOS 10.3)"
page_order: 3
page_type: reference
description: "Cet article de référence couvre la mise à jour iOS 10.3 sur l'icône d'application personnalisable."
platform: iOS
channel:
  - push

---

# Fonctionnalité d'icône d'application personnalisée (iOS 10.3) {#custom-app-icon-feature-ios-103}

> Avec iOS 10.3, Apple a introduit la possibilité de changer l'icône d'une application sur l'écran d'accueil sans avoir à mettre à jour l'application depuis l'Apple App Store. Le développeur peut désormais permettre à l'utilisateur de modifier l'icône de l'écran d'accueil directement dans son application. Apple exige que toutes les images d'icônes d'application que le développeur souhaite mettre à disposition de l'utilisateur soient incluses dans le binaire soumis à Apple pour examen lors de la publication de l'application sur l'Apple App Store.

Pour informer vos utilisateurs de cette fonctionnalité, il est possible d'envoyer un message in-app ou une notification push via Braze à l'utilisateur pour lui expliquer cette fonctionnalité ou lui demander s'il souhaite changer son icône. Le développeur n'aurait qu'à créer un lien profond vers l'application où l'invite native iOS peut être affichée pour effectuer le changement d'icône. Cette approche est similaire aux recommandations que nous fournissons aujourd'hui pour la mise en place d'une amorce de notification push pour les APNs.

De plus, cet envoi de messages peut tirer pleinement parti de la segmentation pour rendre le contenu du message hautement contextuel pour chaque utilisateur. Vous pouvez également exploiter le test A/B des messages pour déterminer quel message a le plus d'impact sur le résultat souhaité.