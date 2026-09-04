---
nav_title: Configurer Currents
article_title: Configurer Currents
page_order: 1
page_type: tutorial
description: "Cet article pratique vous guide dans le processus d'intégration et de configuration de Braze Currents."
tool: Currents
search_rank: 8
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Configurer Currents {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> Cette page décrit le processus générique d'intégration et de configuration de Braze Currents.

{% alert important %}
Currents est inclus dans certaines offres Braze. Contactez votre conseiller Braze si vous avez des questions ou souhaitez y accéder.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

### Impossible d'ajouter une nouvelle intégration Currents {#cannot-add-a-new-currents-integration}

Si vous voyez le message « You do not have any remaining Currents integrations » lors de l'ajout d'une nouvelle intégration, ou si le bouton pour ajouter un nouveau connecteur Currents est grisé, les causes les plus courantes sont :

- Aucun droit d'accès Currents n'a été acheté pour cet espace de travail.
- Le droit d'accès Currents est disponible dans un autre espace de travail de votre entreprise.

Pour résoudre ce problème, vérifiez les autres espaces de travail de votre entreprise. Un autre espace de travail peut afficher un droit d'accès Currents disponible. Si vous devez demander un droit d'accès ou ajuster votre configuration, contactez votre gestionnaire de compte Braze.

### Impossible d'activer le suivi d'événements supplémentaires {#cannot-enable-additional-event-tracking}

Si vous pouvez créer ou modifier un connecteur mais que vous ne parvenez pas à activer l'un des commutateurs de suivi facultatifs, votre espace de travail a peut-être atteint la limite de droits d'accès pour cette catégorie d'événements.

- **Track Customer Behavior and User Events** nécessite des droits d'accès **Customer Behavior Events** disponibles.
- **Track user profiles and attributes** nécessite des droits d'accès **User Profiles and Attributes** disponibles.

Si vous avez besoin de droits d'accès supplémentaires ou d'aide pour ajuster votre configuration, contactez votre gestionnaire de compte Braze.

## Conditions requises {#requirements}

L'utilisation de Currents avec l'un de nos partenaires nécessite les mêmes paramètres de base et la même méthodologie de connexion.

Chaque partenaire exige que Braze ait l'autorisation d'écrire et d'envoyer des fichiers de données vers leur service, et Braze demande l'emplacement vers lequel ces fichiers doivent être écrits, en particulier les noms de compartiments ou les clés.

Les conditions suivantes sont les exigences de base minimales pour s'intégrer à la plupart de nos partenaires. Certains partenaires nécessiteront des paramètres supplémentaires, qui sont répertoriés dans leur [documentation partenaire]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) respective, accompagnés de toutes les nuances associées à ces exigences de base.

| Condition requise | Origine | Accès | Description
|---|---|---|---|
| Compte chez le partenaire | Ouvrez un compte auprès de ce partenaire ou contactez votre gestionnaire de compte Braze pour des suggestions. | Consultez le site du partenaire ou contactez-le pour vous inscrire. | Braze n'enverra pas de données à un partenaire si vous n'avez pas accès à ces données via le compte de votre entreprise.
| Clé API ou jeton du partenaire | Généralement dans le tableau de bord du partenaire. | Copiez et collez-le dans le champ Braze prévu à cet effet. | Braze dispose d'un champ dédié à cet effet sur la page d'intégration de ce partenaire. Nous en avons besoin pour déterminer où envoyer vos données. **Maintenez vos clés ou jetons de partenaire à jour ; des identifiants non valides peuvent désactiver votre connecteur et entraîner la perte d'événements.**
| Code d'authentification/clé, clé secrète, fichier de certification | Contactez un conseiller pour votre compte chez ce partenaire. Peut également se trouver dans le tableau de bord du partenaire. | Copiez et collez les clés dans le champ Braze prévu à cet effet. Générez et chargez les fichiers `.json` ou autres fichiers de certification à l'emplacement approprié dans Braze. | Braze dispose d'un champ dédié à cet effet sur la page d'intégration de ce partenaire. Cela fournit à Braze les identifiants et nous autorise à écrire des fichiers sur votre compte partenaire. **Il est important de maintenir vos informations d'authentification à jour ; des identifiants non valides peuvent entraîner la désactivation de votre connecteur et la perte d'événements.**
| Compartiment, chemin de dossier | Certains partenaires organisent et trient les données par compartiments. Cela devrait se trouver dans le tableau de bord du partenaire. | Si cela est requis, copiez exactement le nom du compartiment ou le chemin du fichier dans l'espace prévu à cet effet dans Braze. | Bien que cela ne soit requis que pour certains partenaires, il est important de le configurer correctement lorsque vous en avez besoin. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Conditions requises" }

{% alert important %}
Il est important de maintenir à jour vos clés de partenaire, vos jetons de partenaire et vos informations d'authentification ; si les identifiants de votre connecteur expirent, celui-ci cessera d'envoyer des événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

## Configuration de Currents {#setting-up-currents}

### Étape 1 : Choisir votre partenaire {#step-1-choose-your-partner}

Braze Currents vous permet de vous intégrer via le stockage de données en utilisant des fichiers plats, ou vers nos partenaires d'analyse comportementale et de données client en utilisant des payloads JSON par lots vers un endpoint désigné.

Avant de commencer votre intégration, il est préférable de déterminer quelle intégration convient le mieux à vos besoins. Par exemple, si vous utilisez déjà mParticle et Segment et souhaitez y diffuser vos données Braze, il serait préférable d'utiliser un payload JSON par lots. Si vous préférez manipuler les données vous-même ou si vous disposez d'un système d'analyse de données plus complexe, il serait peut-être préférable d'utiliser le stockage de données ([Braze utilise cette méthode]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents) !)

### Étape 2 : Ouvrir Currents {#step-2-open-currents}

Pour commencer, accédez à **Intégrations partenaires** > **Currents**. Vous serez dirigé vers la page de gestion des intégrations Currents.

![Page Currents dans le tableau de bord de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Étape 3 : Ajouter votre partenaire {#step-3-add-your-partner}

Ajoutez un partenaire, parfois appelé « connecteur Currents », en sélectionnant le menu déroulant en haut de l'écran.

Chaque partenaire nécessite un ensemble différent d'étapes de configuration. Pour activer chaque intégration, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) et suivez les instructions sur leurs pages respectives.

{% multi_lang_include currents/contact_email_notifications.md %}

### Étape 4 : Configurer vos événements {#step-4-configure-your-events}

Choisissez les événements que vous souhaitez transmettre à ce partenaire en cochant les options disponibles. Vous trouverez la liste de ces événements dans nos bibliothèques [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![Page de configuration Currents avec les événements partenaires sélectionnés pour l'exportation.]({% image_buster /assets/img/current4.png %})

Si nécessaire, vous pouvez en apprendre davantage sur nos événements dans notre article sur la [sémantique de livraison des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

### Étape 5 : Configurer les transformations de champs {#step-5-set-up-field-transformations}

Vous pouvez utiliser les transformations de champs Currents pour supprimer ou hacher un champ de type chaîne de caractères.

- **Supprimer :** Remplace le champ de type chaîne de caractères par `[REDACTED]`. Cela est utile si votre partenaire rejette les événements dont les champs sont manquants ou vides.
- **Hacher :** Applique un algorithme de hachage SHA-256 au champ de type chaîne de caractères.

Sélectionner un champ pour l'une de ces transformations appliquera cette transformation à tous les événements dans lesquels ce champ apparaît. Par exemple, sélectionner `email_address` pour le hachage hachera le champ `email_address` dans les événements d'envoi d'e-mail, d'ouverture d'e-mail, de rebond d'e-mail et de changement d'état du groupe d'abonnement.

![Ajout de transformations de champs]({% image_buster /assets/img/current3.png %})

### Étape 6 : Tester votre intégration {#step-6-test-your-integration}

{% alert important %}
Currents abandonnera les événements dont les payloads sont excessivement volumineux, supérieurs à 900&nbsp;Ko.
{% endalert %}

Avant de tester, envisagez de consulter nos [exemples de données Currents sur GitHub](https://github.com/Appboy/currents-examples). Lorsque vous êtes prêt à tester, choisissez une option dans la section suivante :

#### Envoi d'événements de test {#sending-test-events}

Pour tester votre intégration, vous pouvez sélectionner **Send Test Events** pour envoyer un événement de chaque type d'événement sélectionné vers ce Current. Pour des informations détaillées sur chaque type d'événement, consultez nos bibliothèques [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![La page « Test Currents » dans le tableau de bord de Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Test des connecteurs Currents {#testing-currents-connectors}

Les connecteurs Currents de test sont des versions gratuites de nos connecteurs existants qui peuvent être utilisées pour tester et essayer différentes destinations. Les Currents de test disposent de :

- Jusqu'à 10 connecteurs Currents de test par espace de travail.
- Un maximum agrégé de 1 500 événements par période fixe de 24 heures, réinitialisé à minuit UTC. Ce total d'événements est mis à jour toutes les heures sur le tableau de bord.

Lorsque vos connecteurs Currents de test atteignent la limite d'envoi, votre connecteur n'enverra plus d'événements jusqu'au jour suivant (à minuit UTC).

Pour mettre à niveau votre connecteur Currents de test, modifiez l'intégration dans le tableau de bord et sélectionnez **Upgrade Test Integration**.

## Mise à jour de Currents {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## Liste d'autorisation des IP {#ip-allowlisting}

Braze enverra les données Currents à partir des adresses IP répertoriées :

{% multi_lang_include administer/data_centers.md datacenters='ips' %}