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

Si vous voyez le message « You do not have any remaining Currents integrations » lors de l'ajout d'une nouvelle intégration, les causes courantes sont les suivantes :

- Aucun droit d'accès à Currents n'a été acheté pour cet espace de travail.
- Le droit d'accès à Currents est disponible dans un autre espace de travail de votre société.

Contactez votre gestionnaire de compte Braze pour demander un droit d'accès ou ajuster votre configuration.

## Conditions requises {#requirements}

L'utilisation de Currents avec l'un de nos partenaires nécessite les mêmes paramètres de base et la même méthodologie de connexion.

Chaque partenaire exige que Braze ait l'autorisation de lui écrire et de lui envoyer des fichiers de données, et Braze demande l'emplacement où ces fichiers doivent être écrits, en particulier les noms de compartiments ou les clés.

Les conditions suivantes sont les exigences élémentaires et minimales pour s'intégrer avec la plupart de nos partenaires. Certains partenaires exigeront des paramètres supplémentaires, qui sont énumérés dans la [documentation du partenaire]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) concerné, ainsi que toutes les nuances associées à ces exigences de base.

| Condition | Origine | Accès | Description
|---|---|---|---|
| Compte chez le partenaire | Ouvrez un compte auprès de ce partenaire ou contactez votre gestionnaire de compte Braze pour obtenir des suggestions. | Consultez le site de ce partenaire ou contactez-le pour vous inscrire. | Braze n'enverra pas de données à un partenaire si vous n'avez pas accès à ces données via le compte de votre société.
| Clé API ou jeton du partenaire | Généralement le tableau de bord du partenaire. | Copiez et collez la valeur dans le champ Braze prévu à cet effet. | Braze dispose d'un champ dédié dans la page d'intégration pour ce partenaire. Nous en avons besoin pour déterminer où envoyer vos données. **Veillez à ce que vos clés ou jetons de partenaires soient à jour ; des identifiants non valides peuvent désactiver votre connecteur et entraîner la perte d'événements.**
| Code/clé d'authentification, clé secrète, fichier de certification | Contactez un conseiller de votre compte chez ce partenaire. Ces informations sont parfois disponibles dans le tableau de bord du partenaire. | Copiez et collez les clés dans le champ Braze prévu à cet effet. Générez et chargez les fichiers `.json` ou autres fichiers de certification à l'emplacement approprié dans Braze. | Braze dispose d'un champ dédié dans la page d'intégration pour ce partenaire. Cela fournit des identifiants à Braze et nous autorise à écrire des fichiers sur le compte du partenaire. **Il est important que vos informations d'authentification soient à jour ; des identifiants non valides peuvent entraîner la désactivation de votre connecteur et la perte d'événements.**
| Compartiment, chemin de dossier | Certains partenaires organisent et trient les données par compartiments. Cette information se trouve dans le tableau de bord du partenaire. | Si cela est nécessaire, copiez le nom du compartiment ou le chemin d'accès au fichier exactement dans l'espace prévu à cet effet dans Braze. | Bien que cela ne soit requis que par certains partenaires, il est important de ne pas se tromper lorsque c'est le cas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Conditions requises" }

{% alert important %}
Il est important de garder vos clés/jetons de partenaire et vos informations d'authentification à jour ; si les identifiants de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si ce problème persiste pendant plus de **5 jours**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

## Configuration de Currents {#setting-up-currents}

### Étape 1 : Choisissez votre partenaire {#step-1-choose-your-partner}

Braze Currents vous permet de vous intégrer via Data Storage à l'aide de fichiers plats, ou avec nos partenaires d'analyse comportementale et de données clients en utilisant des payloads JSON en batch vers un endpoint désigné.

Avant de commencer votre intégration, il est préférable de décider quelle option vous convient le mieux. Par exemple, si vous utilisez déjà mParticle et Segment et que vous souhaitez y diffuser les données de Braze, il vaut mieux utiliser un payload JSON en batch. Si vous préférez manipuler les données par vous-même ou si vous disposez d'un système d'analyse des données plus complexe, il est préférable d'utiliser Data Storage ([Braze utilise cette méthode]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents) !)

### Étape 2 : Ouvrez Currents {#step-2-open-currents}

Pour commencer, rendez-vous dans **Intégrations partenaires** > **Currents**. Vous serez dirigé vers la page de gestion des intégrations Currents.

![Page Currents dans le tableau de bord de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Étape 3 : Ajoutez votre partenaire {#step-3-add-your-partner}

Ajoutez un partenaire, parfois appelé « connecteur Currents », en sélectionnant le menu déroulant en haut de l'écran.

Les étapes de configuration varient selon les partenaires. Pour activer chaque intégration, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) et suivez les instructions sur leurs pages respectives.

### Étape 4 : Configurez vos événements {#step-4-configure-your-events}

Choisissez les événements que vous souhaitez transmettre à ce partenaire en cochant les options disponibles. Vous trouverez la liste de ces événements dans nos bibliothèques [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![Page de configuration Currents avec les événements du partenaire sélectionnés pour l'exportation.]({% image_buster /assets/img/current4.png %})

Si nécessaire, vous pouvez en savoir plus sur nos événements dans notre article sur la [sémantique de livraison des événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

### Étape 5 : Configurez les transformations de champs {#step-5-set-up-field-transformations}

Vous pouvez utiliser les transformations de champs Currents pour supprimer ou hacher un champ de type chaîne de caractères.

- **Supprimer :** remplace le champ de chaîne de caractères par `[REDACTED]`. Ceci est utile si votre partenaire rejette les événements dont les champs sont manquants ou vides.
- **Hacher :** applique un algorithme de hachage SHA-256 au champ de chaîne de caractères.

La sélection d'un champ pour l'une de ces transformations appliquera cette transformation à tous les événements dans lesquels ce champ apparaît. Par exemple, si vous sélectionnez `email_address` pour le hachage, le champ `email_address` sera haché dans les événements Envoi d'e-mail, Ouverture d'e-mail, Rebond d'e-mail et Changement d'état du groupe d'abonnement.

![Ajout de transformations de champs]({% image_buster /assets/img/current3.png %})

### Étape 6 : Testez votre intégration {#step-6-test-your-integration}

{% alert important %}
Currents abandonnera les événements dont le payload est excessivement volumineux (supérieur à 900&nbsp;Ko).
{% endalert %}

Avant de tester, pensez à consulter notre [échantillon de données Currents sur GitHub](https://github.com/Appboy/currents-examples). Lorsque vous êtes prêt à tester, choisissez l'une des options ci-dessous :

#### Envoi d'événements de test {#sending-test-events}

Pour tester votre intégration, vous pouvez sélectionner **Send Test Events** pour envoyer un événement de chacun des types d'événements sélectionnés à ce Current. Pour obtenir des informations détaillées sur chaque type d'événement, consultez nos bibliothèques [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) et [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![La page « Currents Test » dans le tableau de bord de Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Test des connecteurs Currents {#testing-currents-connectors}

Les connecteurs Test Currents sont des versions gratuites de nos connecteurs existants qui peuvent être utilisées pour tester et essayer différentes destinations. Les connecteurs Test Currents présentent les caractéristiques suivantes :

- Jusqu'à 10 connecteurs Test Currents par espace de travail.
- Un maximum cumulé de 1 500 événements par période fixe de 24 heures, réinitialisé à minuit UTC. Ce total d'événements est mis à jour toutes les heures sur le tableau de bord.

Une fois que vos connecteurs Test Currents ont atteint la limite d'envoi, votre connecteur n'enverra plus d'événements avant le lendemain (à minuit UTC).

Pour mettre à niveau votre connecteur Test Currents, modifiez l'intégration dans le tableau de bord et sélectionnez **Upgrade Test Integration**.

## Mise à jour de Currents {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## Liste d'adresses IP autorisées {#ip-allowlisting}

Braze enverra les données Currents à partir des adresses IP répertoriées :

{% multi_lang_include administer/data_centers.md datacenters='ips' %}