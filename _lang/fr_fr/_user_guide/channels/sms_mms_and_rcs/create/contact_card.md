---
nav_title: Cartes de contact
article_title: Cartes de contact
page_order: 3
description: "Cet article de référence explique comment créer une carte de contact à inclure dans vos messages MMS et SMS."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS

---

# Cartes de contact {#contact-cards}

> Les cartes de contact (parfois appelées vCard ou fichiers de contact virtuels (VCF)) sont un format de fichier standardisé permettant d'envoyer des informations professionnelles et de contact que vous pouvez facilement importer dans des carnets d'adresses ou des répertoires de contacts.

{% alert note %}
L'envoi d'une carte de contact est facturé comme un MMS. Vérifiez le volume de MMS prévu et l'utilisation des crédits de messages ou d'actions lorsque vous créez des cartes de contact, et confirmez les coûts sur votre [page de facturation]({{site.baseurl}}/user_guide/administer/global/billing) Braze.
{% endalert %}

Les cartes de contact peuvent être créées [par programmation](https://www.twilio.com/blog/send-vcard-twilio-sms) et importées dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#media-library) de Braze, ou créées via notre générateur de cartes de contact intégré. Ces cartes peuvent se voir attribuer des propriétés courantes telles que le nom de votre entreprise, le numéro de téléphone, l'adresse, l'e-mail et une petite photo. Pour commencer à créer des cartes de contact, assurez-vous d'abord que vous êtes configuré pour utiliser les MMS dans Braze.

## Générateur de cartes de contact {#contact-card-generator}

### Étape 1 : Affecter un nom {#step-1-assign-name}

Les cartes de contact peuvent être créées depuis le compositeur SMS et MMS. Sélectionnez l'onglet **Contact Card Generator** pour commencer.

Ensuite, vous serez invité à saisir le nom ou le surnom de votre entreprise. C'est le nom que vos utilisateurs verront lorsqu'ils enregistreront la carte. Une limite de 20 caractères est appliquée pour garantir que l'utilisateur puisse voir l'intégralité du nom ou de l'alias de votre entreprise dans ses contacts et son application de messagerie.

![L'onglet Contact Card Generator.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Étape 2 : Affecter un numéro de téléphone {#step-2-assign-phone-number}

Sélectionnez le groupe d'abonnement et le numéro de téléphone souhaité parmi les options déroulantes disponibles. Ce numéro sera indiqué sur votre carte de contact et disponible sur le téléphone de l'utilisateur pour envoyer des messages une fois la carte enregistrée.

Notez que les codes alphanumériques ne sont pas compatibles avec la messagerie bidirectionnelle et ne sont pas pris en charge pour les cartes de contact.

### Étape 3 : Champs facultatifs {#step-3-optional-fields}

![Champs facultatifs pour le générateur de cartes de contact.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Importer une photo de contact {#upload-contact-card-contact-photo}

Vous pouvez importer une photo de contact facultative pour votre carte de contact. Nous recommandons une image JPEG ou PNG de 240 x 240&nbsp;px. Toute image haute résolution importée sera redimensionnée à 240 x 240&nbsp;px pour garantir la livrabilité du message, car les messages MMS de plus de 5&nbsp;Mo peuvent échouer.

{% alert note %}
L'image importée apparaît sur la carte de contact lorsque le destinataire l'ouvre ; le champ [**Full Name**](#add-more-information) détermine ce qui s'affiche dans la miniature de la conversation.
{% endalert %}

#### Ajouter des informations supplémentaires {#add-more-information}

D'autres champs vous permettent d'insérer votre nom, sous-titre, adresse et d'autres coordonnées que votre utilisateur pourrait souhaiter avoir à disposition.

Le champ **Full Name** détermine les initiales qui apparaissent dans la miniature de la conversation. Lorsque ce champ est marqué comme facultatif et laissé vide, les destinataires voient un cercle blanc au lieu des initiales.

### Étape 4 : Enregistrer votre carte de contact {#step-4-saving-your-contact-card}

Une fois que vous avez rempli tous les champs nécessaires, sélectionnez **Generate Contact Card** pour que la carte soit automatiquement jointe à votre campagne ou Canvas. À partir de là, vous pouvez ajouter un message, tester votre carte de contact et lancer votre campagne ou Canvas.

La carte de contact sera également enregistrée dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#media-library) pour être facilement réutilisée dans de futures campagnes et Canvas.

## Ajouter une carte de contact existante {#adding-an-existing-contact-card}

Pour ajouter une carte de contact existante, créez une campagne ou un Canvas et sélectionnez le groupe d'abonnement souhaité. Ensuite, une option **Add Media** apparaîtra dans la fenêtre du compositeur de messages. Vous pouvez y importer un fichier de carte de contact existant ou en trouver un via la bibliothèque multimédia.