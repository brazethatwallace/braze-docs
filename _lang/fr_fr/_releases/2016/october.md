---
nav_title: octobre
page_order: 3
noindex: true
page_type: update
description: "Cet article contient les notes de version d'octobre 2016."
---

# Octobre 2016 {#october-2016}

## Nouveaux paramètres de sécurité {#new-security-settings}
Nous avons ajouté des fonctionnalités de sécurité améliorées à Braze, notamment des règles d'expiration des mots de passe, des règles de longueur des mots de passe, des règles de complexité des mots de passe, la liste d'autorisation d'adresses IP pour la connexion au tableau de bord et l'authentification à deux facteurs.

> Mise à jour : Les **Paramètres de sécurité** de Braze, accessibles depuis la page **Paramètres de l'entreprise**, comprennent également des règles de réutilisation et d'expiration des mots de passe.

## Téléchargement d'un CSV après importation {#csv-download-after-import}
Les utilisateurs de l'entreprise peuvent désormais télécharger un CSV des utilisateurs récemment importés. Cela vous donne plus de visibilité sur la synchronisation des données depuis vos systèmes. En savoir plus sur l'[importation de fichiers CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/).

## Filtre d'anniversaire {#anniversary-filter}
En plus du [filtre de date de naissance]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/), Braze prend désormais en charge un filtre d'anniversaire qui vous permet de cibler les utilisateurs en fonction d'une date du calendrier pour les jalons de fidélité, les rappels de renouvellement, et bien plus encore ! Accédez à cette fonctionnalité en sélectionnant le filtre « Date of Custom Attribute » sur la page Segments. En savoir plus sur les [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Mises à jour des limites de fréquence {#frequency-capping-updates}
Auparavant, une campagne ou un Canvas qui ignorait les limites de fréquence pouvait toujours être pris en compte dans le calcul des limites de fréquence. Nous avons modifié le comportement de sorte que, par défaut, les nouvelles campagnes et les nouveaux Canvas qui n'obéissent pas aux limites de fréquence ne comptent pas non plus pour ces dernières. Ce paramètre est configurable pour chaque campagne et chaque Canvas. En savoir plus sur la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## Profils de couleurs pour les messages in-app {#in-app-message-color-profiles}
Nous avons ajouté des [profils de couleurs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) pour les messages in-app, ce qui permet aux clients de réutiliser les palettes de couleurs de leur marque lorsqu'ils créent de nouveaux messages dans Braze.