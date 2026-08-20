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

Si le message « You do not have any remaining Currents integrations » s'affiche lorsque vous ajoutez une nouvelle intégration, ou si le bouton permettant d'ajouter un nouveau connecteur Currents est grisé, les causes courantes sont les suivantes :

- Aucun droit d'accès à Currents n'a été acheté pour cet espace de travail.
- Le droit d'accès à Currents est disponible dans un autre espace de travail de votre entreprise.

Pour résoudre ce problème, vérifiez les autres espaces de travail au sein de votre entreprise. Un autre espace de travail peut disposer d'un droit d'accès à Currents. Si vous devez demander un droit d'accès ou ajuster votre configuration, contactez votre gestionnaire de compte Braze.

## Conditions requises {#requirements}

L'utilisation de Currents avec l'un de nos partenaires nécessite les mêmes paramètres de base et la même méthodologie de connexion.

Chaque partenaire exige que Braze ait l'autorisation d'écrire et d'envoyer des fichiers de données. Braze demande l'emplacement où ces fichiers doivent être écrits, en particulier les noms de compartiments ou les clés.

Les conditions suivantes sont les exigences de base minimales pour s'intégrer avec la plupart de nos partenaires. Certains partenaires nécessitent des paramètres supplémentaires, qui sont répertoriés dans leur [documentation partenaire]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) respective, ainsi que toutes les nuances associées à ces exigences de base.

| Condition requise | Origine | Accès | Description
|---|---|---|---|
| Compte chez le partenaire | Créez un compte auprès de ce partenaire ou contactez votre gestionnaire de compte Braze pour des suggestions. | Consultez le site du partenaire ou contactez-le pour vous inscrire. | Braze n'enverra pas de données à un partenaire si vous n'avez pas accès à ces données via le compte de votre entreprise.
| Clé API ou jeton du partenaire | Généralement dans le tableau de bord du partenaire. | Copiez-collez dans le champ Braze désigné. | Braze dispose d'un champ dédié à cet effet sur la page d'intégration de ce partenaire. Nous en avons besoin pour déterminer où envoyer vos données. **Maintenez vos clés ou jetons partenaires à jour ; des identifiants invalides peuvent désactiver votre connecteur et entraîner la perte d'événements.**
| Code/clé d'authentification, clé secrète, fichier de certification | Contactez un conseiller pour votre compte auprès de ce partenaire. Peut également se trouver dans le tableau de bord du partenaire. | Copiez-collez les clés dans le champ Braze désigné. Générez et téléchargez les fichiers `.json` ou autres fichiers de certification à l'emplacement approprié dans Braze. | Braze dispose d'un champ dédié à cet effet sur la page d'intégration de ce partenaire. Cela fournit à Braze les identifiants et nous autorise à écrire des fichiers sur votre compte partenaire. **Il est important de maintenir vos informations d'authentification à jour ; des identifiants invalides peuvent entraîner la désactivation de votre connecteur et la perte d'événements.**
| Compartiment, chemin de dossier | Certains partenaires organisent et trient les données par compartiments. Cela devrait se trouver dans le tableau de bord du partenaire. | Si cela est requis, copiez le nom du compartiment ou le chemin de fichier exactement dans l'espace désigné dans Braze. | Bien que cela ne soit requis que pour certains partenaires, il est important de le renseigner correctement lorsque c'est nécessaire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Conditions requises" }

{% alert important %}
Il est important de maintenir vos clés partenaires, jetons partenaires et informations d'authentification à jour ; si les identifiants de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

## Configuration de Currents {#setting-up-currents}

### Étape 1 : Choisir votre partenaire {#step-1-choose-your-partner}

Braze Currents vous permet de vous intégrer via le stockage de données à l'aide de fichiers plats ou à nos partenaires d'analyse comportementale et de données clients en utilisant des payloads JSON par lots vers un endpoint désigné.

Avant de commencer votre intégration, il est préférable de déterminer quelle intégration convient le mieux à vos besoins. Par exemple, si vous utilisez déjà mParticle et Segment et souhaitez que les données Braze y soient diffusées, il serait préférable d'utiliser un payload JSON par lots. Si vous préférez manipuler les données vous-même ou si vous disposez d'un système d'analyse de données plus complexe, il peut être préférable d'utiliser le stockage de données ([Braze utilise cette méthode]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents) !)

### Étape 2 : Ouvrir Currents {#step-2-open-currents}

Pour commencer, accédez à **Intégrations partenaires** > **Currents**. Vous serez redirigé vers la page de gestion des intégrations Currents.

![Page Currents dans le tableau de bord de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Étape 3 : Ajouter votre partenaire {#step-3-add-your-partner}

Ajoutez un partenaire, parfois appelé « connecteur Currents », en sélectionnant le menu déroulant en haut de l'écran.

Chaque partenaire nécessite un ensemble différent d'étapes de configuration. Pour activer chaque intégration, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) et suivez les instructions sur leurs pages respectives.

{% multi_lang_include currents/contact_email_notifications.md %}

### Étape 4 : Configurer vos événements {#step-4-configure-your-events}

Choisissez les événements que vous souhaitez transmettre à ce partenaire en cochant les options disponibles. Vous pouvez trouver la liste de ces événements dans nos bibliothèques d'[événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et d'[événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![Page de configuration Currents avec les événements partenaires sélectionnés pour l'exportation.]({% image_buster /assets/img/current4.png %})

Si nécessaire, vous pouvez en savoir plus sur nos événements dans notre article sur la [sémantique de livraison des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

### Étape 5 : Configurer les transformations de champs {#step-5-set-up-field-transformations}

Vous pouvez utiliser les transformations de champs Currents pour supprimer ou hacher un champ de type chaîne de caractères.

- **Supprimer :** Remplace le champ de type chaîne de caractères par `[REDACTED]`. Cela est utile si votre partenaire rejette les événements comportant des champs manquants ou vides.
- **Hacher :** Applique un algorithme de hachage SHA-256 au champ de type chaîne de caractères.

Sélectionner un champ pour l'une de ces transformations appliquera cette transformation à tous les événements dans lesquels ce champ apparaît. Par exemple, sélectionner `email_address` pour le hachage hachera le champ `email_address` dans les événements Email Send, Email Open, Email Bounce et Subscription Group State Change.

![Ajout de transformations de champs]({% image_buster /assets/img/current3.png %})

### Étape 6 : Tester votre intégration {#step-6-test-your-integration}

{% alert important %}
Currents abandonnera les événements dont les payloads sont excessivement volumineux, dépassant 900&nbsp;Ko.
{% endalert %}

Avant de tester, pensez à consulter nos [exemples de données Currents sur GitHub](https://github.com/Appboy/currents-examples). Lorsque vous êtes prêt à tester, choisissez une option dans la section suivante :

#### Envoi d'événements de test {#sending-test-events}

Pour tester votre intégration, vous pouvez sélectionner **Send Test Events** pour envoyer un événement de chaque type d'événement sélectionné vers ce Current. Pour des informations détaillées sur chaque type d'événement, consultez nos bibliothèques d'[événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et d'[événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![La page « Currents Test » dans le tableau de bord de Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Test des connecteurs Currents {#testing-currents-connectors}

Les connecteurs Currents de test sont des versions gratuites de nos connecteurs existants qui peuvent être utilisées pour tester et essayer différentes destinations. Les Currents de test disposent de :

- Jusqu'à 10 connecteurs Currents de test par espace de travail.
- Un maximum agrégé de 1 500 événements par période fixe de 24 heures, réinitialisé à minuit UTC. Ce total d'événements est mis à jour toutes les heures sur le tableau de bord.

Une fois que vos connecteurs Currents de test atteignent la limite d'envoi, votre connecteur n'enverra plus d'événements jusqu'au jour suivant (à minuit UTC).

Pour mettre à niveau votre connecteur Currents de test, modifiez l'intégration dans le tableau de bord et sélectionnez **Upgrade Test Integration**.

## Mise à jour de Currents {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## Liste d'autorisation des IP {#ip-allowlisting}

Braze enverra les données Currents à partir des IP répertoriées :

{% multi_lang_include administer/data_centers.md datacenters='ips' %}