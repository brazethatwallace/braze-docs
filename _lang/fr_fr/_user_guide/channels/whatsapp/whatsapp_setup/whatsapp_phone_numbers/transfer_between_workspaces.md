---
nav_title: Transfert entre espaces de travail
article_title: Transférer des numéros de téléphone et des groupes d'abonnement entre espaces de travail
page_order: 3
description: "Cet article de référence explique comment transférer votre numéro de téléphone WhatsApp et vos groupes d'abonnement entre espaces de travail."
page_type: reference
channel:
  - WhatsApp
---

# Transférer des numéros de téléphone WhatsApp et des groupes d'abonnement entre espaces de travail {#transfer-whatsapp-phone-numbers-and-subscription-groups-between-workspaces}

> Cette page explique comment déplacer un numéro de téléphone de compte WhatsApp Business (WABA) et son groupe d'abonnement associé d'un espace de travail à un autre dans Braze. Ce processus simplifie votre utilisation de WhatsApp avec Braze et réduit le besoin d'assistance technique.

## Conditions préalables {#prerequisites}

- Vérifiez que vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) « Manage Subscription Groups » dans l'espace de travail d'origine et dans le nouvel espace de travail.
- Le WABA ne peut pas être utilisé sur plusieurs [clusters Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Cela est peu probable si vous travaillez au sein d'une même entreprise.

## Transférer un numéro de téléphone et un groupe d'abonnement {#transferring-a-phone-number-and-subscription-group}

### Étape 1 : Archiver le groupe d'abonnement {#step-1-archive-the-subscription-group}

Pour archiver un groupe d'abonnement WhatsApp, suivez ces étapes :

1. Accédez à l'espace de travail dans lequel le groupe d'abonnement existe actuellement.
2. Accédez à **Audience** > **Gestion des groupes d'abonnement** et trouvez le groupe d'abonnement associé au numéro de téléphone WhatsApp que vous souhaitez déplacer.
3. Survolez l'état du groupe d'abonnement et sélectionnez <i class="fa-solid fa-box-archive"></i> **Archiver**, ce qui marquera le groupe d'abonnement comme inactif sans le supprimer.

![Le bouton « Archiver » apparaît au survol de l'état « Actif » d'un groupe d'abonnement.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Étape 2 : Intégrer le numéro de téléphone WhatsApp dans le nouvel espace de travail {#step-2-integrate-the-whatsapp-phone-number-into-the-new-workspace}

1. Accédez à l'espace de travail dans lequel vous souhaitez déplacer le numéro de téléphone WhatsApp.
2. Accédez à **Intégrations partenaires** > **Partenaires technologiques** > **WhatsApp**, puis faites défiler jusqu'à la section **WhatsApp Messaging Integration**.
3. Sélectionnez l'option **Create new subscription group and phone number**.
4. Lancez le processus d'intégration, au cours duquel vous pourrez sélectionner le numéro de téléphone du groupe d'abonnement archivé.

### Étape 3 : Vérifier l'intégration {#step-3-verify-the-integration}

1. Une fois l'intégration terminée, confirmez que le numéro de téléphone WhatsApp est désormais associé au groupe d'abonnement dans le nouvel espace de travail.
2. Effectuez un test pour vérifier que les messages peuvent être envoyés et reçus via ce numéro de téléphone WhatsApp.

## Remarques {#considerations}

- Si vous devez retransférer le numéro de téléphone WhatsApp vers l'espace de travail d'origine, répétez les étapes. Archivez le groupe d'abonnement dans l'espace de travail de destination, puis intégrez-le dans l'espace de travail d'origine.
- Vous n'avez pas besoin de supprimer le numéro de téléphone WhatsApp de votre Meta Business Manager pendant le transfert.