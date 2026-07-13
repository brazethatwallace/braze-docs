---
nav_title: Campagnes pour utilisateurs actifs
article_title: Campagnes pour utilisateurs actifs
page_order: 0.5
page_type: tutorial
description: "Cet article pratique décrit les avantages des campagnes pour utilisateurs actifs dans le tableau de bord de Braze, ainsi que les étapes pour en créer et en configurer une."
tool:
  - Campaigns

---

# Campagnes pour utilisateurs actifs {#active-user-campaigns}

> Identifiez vos utilisateurs actifs pour créer des campagnes sur mesure et récompenser ceux qui utilisent régulièrement votre plateforme.

Contacter les utilisateurs déjà actifs de votre application peut être un levier puissant pour constituer une communauté fidèle d'utilisateurs réguliers. Un peu de reconnaissance personnalisée envers vos utilisateurs les plus engagés peut les transformer en véritables ambassadeurs de votre application.

Vous pouvez également consulter notre [cours d'apprentissage Braze](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sur la stratégie marketing par e-mail et les campagnes basées sur le cycle de vie client recommandées !

## Comprendre les utilisateurs actifs {#understanding-active-users}

Braze définit un « utilisateur actif » sur une période donnée comme tout utilisateur ayant eu une session au cours de cette période.

Si un utilisateur perd sa connexion, les données de session sont mises en cache localement et envoyées lorsque l'utilisateur retrouve une connexion réseau. Ces sessions sont également prises en compte dans le nombre d'utilisateurs actifs. De plus, si votre application comporte un processus d'inscription, Braze comptabilise tous les utilisateurs comme actifs, qu'ils soient inscrits ou non.

Si vous définissez des ID utilisateur pour identifier les utilisateurs lorsqu'un nouvel utilisateur se connecte, celui-ci sera comptabilisé comme un utilisateur actif distinct. Les utilisateurs mis à jour via l'API seront également comptabilisés comme utilisateurs actifs pendant la période au cours de laquelle ils sont mis à jour.

## Étape 1 : Identifier vos meilleurs utilisateurs {#step-1-identifying-your-top-users}

En utilisant notre sélection de filtres, créez un segment d'utilisateurs qui représente selon vous votre base d'utilisateurs les plus fidèles et réguliers. L'exemple de segment suivant définit les meilleurs utilisateurs.

![Exemple de filtres de segment Braze définissant une audience de meilleurs utilisateurs.]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

De plus, vous n'aurez pas besoin de mettre à jour ce segment en continu : les utilisateurs qui entrent ou sortent des critères de la Campaign seront automatiquement ciblés ou exclus.

{% alert note %}
L'exemple précédent segmente les utilisateurs en fonction de l'utilisation générale de l'application. Dans la plupart des cas, l'ensemble des filtres nécessaires pour définir votre segment de meilleurs utilisateurs dépendra largement des spécificités de votre application.
{% endalert %}

## Étape 2 : Contactez vos meilleurs utilisateurs {#step-2-contact-your-top-users}

### Montrez à vos utilisateurs qu'ils comptent {#make-your-users-feel-appreciated}

Montrez à vos utilisateurs que vous appréciez leur fidélité et leur engagement envers votre application. Donnez-leur encore plus de raisons de revenir pour encourager une activité continue. Cela peut prendre la forme d'offres spéciales ou de bonus réservés exclusivement à vos meilleurs utilisateurs.

Les récompenses inattendues peuvent être plus efficaces pour encourager les actions continues des utilisateurs que si vous les aviez promises dès le départ !

![Une Campaign à l'étape Rédiger avec une notification enrichie iOS qui indique : « Merci encore pour vos achats chez nous ! Pour vous montrer notre reconnaissance, nous vous offrons la livraison gratuite sur votre prochaine commande ».]({% image_buster /assets/img/congratulations_push.jpg %})

### Suivez vos résultats {#keep-track-of-your-results}

Suivez les ouvertures pour vous assurer que vous ciblez le bon ensemble d'utilisateurs avec le type de message optimal. De plus, surveillez les désinscriptions aux notifications push et restez vigilant face à la perte de ces utilisateurs essentiels.