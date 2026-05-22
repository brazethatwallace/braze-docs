---
nav_title: Envoyer des Canvas de test
article_title: Envoyer des Canvas de test
page_order: 1
description: "Cet article de référence explique comment tester un Canvas avant son lancement et présente les bonnes pratiques."
page_type: reference
tool: Canvas
---

# Envoyer des Canvas de test

> Après avoir [créé votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/), vous souhaiterez peut-être effectuer plusieurs vérifications avant le lancement, en fonction de détails tels que la taille de votre audience ou le nombre de filtres de segmentation.

Dans la mesure du possible, Braze recommande de tester un Canvas avant de le lancer. Ce test se déroulera généralement dans votre environnement Braze. Tester votre Canvas peut impliquer de le dupliquer, de faire passer des utilisateurs test à travers le parcours utilisateur et de vérifier que le comportement des utilisateurs correspond à ce que vous avez défini dans votre Canvas.

## Étape 1 : Créer votre plan de test

Créer un plan de test est essentiel avant de commencer à tester votre Canvas. Un plan de test vous aide à identifier et suivre des zones spécifiques du parcours de votre Canvas.

Lors de l'élaboration de votre plan de test, posez-vous les questions suivantes :
- Au moins un utilisateur a-t-il été créé pour chaque branche et chemin du Canvas ?
- Des segments sont-ils utilisés dans votre Canvas ?
	- Si des segments sont utilisés, il peut y avoir des conditions préalables pour qu'un utilisateur entre dans le Canvas avant d'être éligible à un parcours utilisateur.
- Les messages du Canvas de test contiennent-ils du Liquid dans les titres des messages qui récupèrent l'ID utilisateur ou l'adresse e-mail afin de faciliter l'identification du message et de l'utilisateur à des fins de test ?

## Étape 2 : Identifier les utilisateurs test

Ensuite, identifiez un ensemble d'utilisateurs test qui passeront par les étapes du Canvas sans envoyer réellement de messages à vos utilisateurs cibles. Les utilisateurs test peuvent être des adresses e-mail existantes qui ne sont pas utilisées pour des services réels sur votre tableau de bord de Braze, ou de nouvelles adresses e-mail utilisées exclusivement à des fins de test.

## Étape 3 : Configurer votre Canvas

Il est maintenant temps de tester votre Canvas ! Pour garder les informations de votre Canvas original et de votre Canvas de test bien organisées, créez un duplicata de votre Canvas à des fins de test.

Il existe deux façons de tester votre Canvas.

- **Méthode 1 :** Dans le Canvas dupliqué, modifiez la section **Audience d'entrée** du générateur de Canvas afin que seuls les utilisateurs test soient éligibles au Canvas. Vous pouvez également saisir votre propre adresse e-mail en tant qu'utilisateur test en ajoutant le filtre de test **Adresse e-mail**. Dans l'exemple ci-dessous, nous avons limité le Canvas à deux utilisateurs test qui ont utilisé l'application pour la première fois il y a moins de trois jours.

![Un Canvas avec une audience d'entrée « A utilisé ces applications pour la première fois il y a moins de 3 jours » et les adresses e-mail de deux utilisateurs test.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Méthode 2 :** [Prévisualisez les parcours utilisateur]({{site.baseurl}}/preview_user_paths/) en sélectionnant le bouton **Test Canvas** dans le pied de page du générateur de Canvas.

## Étape 4 : Lancer votre test

Lancez votre Canvas de test pour permettre aux utilisateurs de commencer à y entrer. Effectuez les comportements utilisateur sur votre application qui enverraient les utilisateurs à travers le parcours Canvas correspondant.

Vérifiez que vos utilisateurs test reçoivent les messages prévus à chaque étape du Canvas. Notez que vos utilisateurs test peuvent ne pas recevoir de message pour des raisons telles que :

- Non-éligibilité au Groupe de contrôle global
- Limitations de la limite de fréquence
- Appartenance à un segment non concordante
- Messages abandonnés
- Jetons de notification push associés à d'autres utilisateurs

Continuez à itérer sur les tests du Canvas pour vous assurer qu'il fonctionne comme prévu.

## Conseils généraux

### Identifier les étapes de votre Canvas

Dans certains cas, un utilisateur peut potentiellement recevoir plusieurs messages en parcourant un Canvas. Si le délai entre les étapes a été considérablement réduit pour les tests, il n'est pas toujours évident de savoir quel message est déclenché pendant le test. S'assurer que les messages de test incluent le nom de l'étape ou l'ID utilisateur (en utilisant Liquid) facilitera l'identification et la confirmation que le bon message a été envoyé aux bons utilisateurs.

### Créer un groupe interne

Au lieu de créer des utilisateurs test individuels, vous pouvez créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/), qui est un groupe interne dont l'objectif est de vérifier le contenu de vos messages. Il s'agit d'un groupe d'utilisateurs qui recevra des messages de test provenant de campagnes et de Canvas. Vous pouvez ensuite ajouter ce groupe de test dans le champ **Ajouter des groupes de test de contenu** sous **Destinataires du test**.

### Réduire les délais

Pour exécuter les tests plus efficacement, nous vous suggérons de réduire les délais à quelques minutes ou secondes à des fins de test afin de pouvoir consulter les messages en temps voulu. Par exemple, prévoyez au moins 2 à 3 minutes entre les tests pour pouvoir isoler des actions spécifiques dans des parcours Canvas spécifiques.

### Exploiter les blocs de contenu

Si du contenu est amené à être répété dans votre cadre de test (par exemple, du Liquid complexe pour filtrer les utilisateurs dans différentes étapes du Canvas), essayez d'enregistrer ce contenu répété en tant que [bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). Vous pourrez ainsi inclure le bloc de contenu dans les différentes étapes du Canvas.

### Utiliser Postman et l'endpoint de suivi des utilisateurs

Vous pouvez exécuter des tests avec Postman et la [collection Postman de Braze]({{site.baseurl}}/api/postman_collection/). Utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour enregistrer et suivre les événements personnalisés et les achats de vos différents utilisateurs test.

Notez que l'envoi de données à l'API de suivi des utilisateurs ne peut se faire qu'avec un ID externe. Les utilisateurs test devront donc peut-être être ajoutés en tant qu'utilisateurs test au sein d'un groupe interne dans le tableau de bord de Braze afin que des erreurs spécifiques puissent être examinées plus en détail.

#### Tester avec plusieurs branches

Lorsque vous testez un Canvas comportant plusieurs branches qui ciblent les utilisateurs en fonction de différents attributs et événements, suivez ce plan de test :

1. Pour chaque branche, identifiez les attributs et événements que l'utilisateur doit posséder pour être inclus dans le parcours Canvas.
2. Intégrez-les dans un PAYLOAD JSON à envoyer via l'endpoint `/users/track`.