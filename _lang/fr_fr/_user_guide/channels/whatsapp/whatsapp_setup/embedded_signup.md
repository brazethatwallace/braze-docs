---
nav_title: Inscription intégrée
article_title: Inscription intégrée WhatsApp
page_order: 1
description: "Cet article de référence fournit un guide étape par étape du processus d'inscription intégrée WhatsApp dans Braze."
page_type: reference
channel:
  - WhatsApp
---

# Inscription intégrée WhatsApp {#whatsapp-embedded-signup}

> Cet article de référence fournit un guide étape par étape du processus d'inscription intégrée WhatsApp dans Braze.

Le processus d'inscription intégrée WhatsApp est accessible lorsque vous [intégrez WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) pour la première fois dans votre espace de travail Braze, et lorsque vous [ajoutez un compte WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) à une intégration WhatsApp existante.

{% alert note %}
Vous pouvez ajouter [plusieurs comptes WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) à un espace de travail Braze. Cependant, chaque compte WhatsApp Business spécifique ne peut être ajouté qu'à un seul espace de travail Braze.
{% endalert %}

## Accéder au processus {#accessing-the-workflow}

Accédez à **Intégrations partenaires** > **Partenaires technologiques**, puis recherchez et sélectionnez **WhatsApp**. Votre prochaine sélection dépend de votre cas d'utilisation :

- Si vous intégrez WhatsApp dans votre espace de travail, sélectionnez **Begin Integration**. <br><br>![Page partenaire WhatsApp avec un bouton pour commencer l'intégration.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- Si vous ajoutez un compte WhatsApp Business à une intégration WhatsApp existante, sélectionnez **Add WhatsApp Business Account**. <br><br>![« WhatsApp Messaging Integration » avec des options pour ajouter un compte WhatsApp Business ou un groupe d'abonnement et un numéro.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

Le processus à partir de ce point est le même pour les deux cas d'utilisation.

## Processus d'inscription intégrée WhatsApp {#whatsapp-embedded-signup-workflow}

1. Dans la fenêtre de connexion Meta (Facebook), sélectionnez **Login as** ou **Continue**. <br><br>![Fenêtre de connexion Meta.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Lisez les autorisations que vous partagerez avec Braze, puis sélectionnez **Get Started**. <br><br>![Liste des autorisations que vous partagerez avec Braze pour l'intégration.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. Sur cet écran, configurez les éléments suivants, puis sélectionnez **Next** :
- Dans le menu déroulant **Business portfolio**, sélectionnez votre portefeuille d'entreprise. Celui-ci est lié à votre compte WhatsApp Business. Si vous ne voyez pas le portefeuille d'entreprise attendu, vérifiez vos autorisations.
- Dans le champ **WhatsApp business account**, sélectionnez **Create a new WhatsApp Business Account**, y compris lorsque vous ajoutez un autre compte WhatsApp Business à votre espace de travail ou lorsque ce compte existe déjà dans Meta. Choisissez cette option au lieu de sélectionner un compte WhatsApp Business existant dans le menu déroulant. <br><br>![Une fenêtre avec des champs pour saisir les informations de votre entreprise, y compris le nom de votre portefeuille d'entreprise.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. Sélectionnez les options suivantes dans les menus déroulants, puis sélectionnez **Next**.
- **Choose a WhatsApp Business account** : Create a WhatsApp business account
- **Create or select a WhatsApp Business profile** : Create a new WhatsApp business profile <br><br>![Champs pour spécifier si vous choisissez ou créez un compte et un profil WhatsApp Business.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. Fournissez les informations suivantes, puis sélectionnez **Next**.
- Nom du compte WhatsApp Business
- Nom d'affichage WhatsApp Business
- Catégorie <br><br>![Champs pour fournir les détails du nouveau compte WhatsApp Business.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. Saisissez votre numéro de téléphone et choisissez **Text message** ou **Phone call**. Pour un nouveau numéro, celui-ci doit respecter les exigences de WhatsApp en matière de numéro de téléphone, y compris ne pas être enregistré sur un autre compte WhatsApp. Si vous migrez un numéro existant (voir l'étape 3) et que Meta indique que le numéro est déjà utilisé, ignorez l'avertissement pour terminer la migration. <br><br>![Champs pour ajouter un numéro de téléphone.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. Saisissez votre code d'authentification à deux facteurs, puis sélectionnez **Next**. <br><br>![Un champ de saisie pour un code d'authentification à deux facteurs.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. Vérifiez les autorisations que votre compte WhatsApp Business recevra, puis sélectionnez **Continue**. <br><br>![Liste des autorisations demandées par le compte WhatsApp Business.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. C'est terminé ! <br><br>![Fenêtre indiquant que vous êtes prêt à commencer à envoyer des messages.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}