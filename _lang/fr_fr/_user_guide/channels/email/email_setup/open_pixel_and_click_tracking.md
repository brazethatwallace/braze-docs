---
nav_title: Pixel d'ouverture et suivi des clics
article_title: Pixel d'ouverture et suivi des clics pour les e-mails
page_order: 9
page_type: reference
description: "Cet article de référence explique comment mettre en œuvre le pixel d'ouverture et le suivi des clics."

---

# Pixel d'ouverture et suivi des clics pour les e-mails {#email-open-pixel-and-click-tracking}

> Le [suivi par pixel d'ouverture]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#changing-location-of-tracking-pixel) et le suivi des clics peuvent être activés ou désactivés pour chaque profil utilisateur. Cette flexibilité vous permet de respecter les lois régionales sur la confidentialité, lorsqu'un profil utilisateur individuel indique qu'il ne souhaite plus être suivi.

## Activer le pixel d'ouverture ou le suivi des clics {#turning-on-open-pixel-or-click-tracking}

Lors de l'importation ou de la mise à jour d'un profil utilisateur via l'[API]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields), un [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv) ou l'[Ingestion de données cloud (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), deux champs sont disponibles pour modification :

- `email_open_tracking_disabled` : accepte `true` ou `false`. Définissez la valeur sur `false` pour ajouter le pixel de suivi d'ouverture à tous les futurs e-mails envoyés à cet utilisateur. Disponible pour SparkPost et SendGrid uniquement.
- `email_click_tracking_disabled` : accepte `true` ou `false`. Définissez la valeur sur `false` pour ajouter le suivi des clics à tous les liens contenus dans les futurs e-mails envoyés à cet utilisateur. Disponible pour SparkPost et SendGrid uniquement.

Pour référence, ces informations sont visibles sur le profil utilisateur dans les **Paramètres de contact** de l'e-mail, situés dans l'onglet **Engagement**.

![Champs du pixel de suivi d'ouverture et de suivi des clics dans l'onglet Engagement du profil d'un utilisateur]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

## Exigences relatives aux liens de suivi des clics {#click-tracking-link-requirements}

Le suivi des clics de Braze ne réécrit que les liens utilisant des URL `http://` ou `https://`. Les liens utilisant d'autres schémas, tels que `mailto:` ou `tel:`, ne font pas l'objet d'un suivi des clics.

Pour suivre les clics sur des numéros de téléphone ou des adresses e-mail, utilisez une URL de redirection `https://` qui redirige vers la destination `tel:` ou `mailto:`.