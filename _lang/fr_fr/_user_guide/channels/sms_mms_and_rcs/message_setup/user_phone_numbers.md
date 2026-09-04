---
nav_title: "Numéros de téléphone des utilisateurs"
article_title: Numéros de téléphone des utilisateurs SMS
page_order: 3
description: "Cet article de référence traite du formatage des numéros de téléphone SMS, de l'importation des numéros de téléphone, ainsi que de l'ajout d'utilisateurs aux groupes d'abonnement SMS."
page_type: reference
alias: /user_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

# Numéros de téléphone des utilisateurs {#user-phone-numbers}

> Cet article aborde différents sujets relatifs aux numéros de téléphone de vos utilisateurs ou clients. Si vous recherchez des informations sur vos propres numéros, consultez notre article sur les [numéros de téléphone d'envoi]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Format recommandé {#recommended-format}

Nous vous recommandons d'importer les numéros de téléphone au format [`E.164`](https://en.wikipedia.org/wiki/e.164) pour garantir l'exactitude dans le cas où vous envoyez vers plusieurs régions avec des indicatifs de pays ou de zones différents&#8212;même pour les numéros de téléphone basés aux États-Unis.

- **Numéros américains :** Tous les numéros américains doivent être des numéros de téléphone valides à 10 chiffres avec un indicatif régional valide. Si un numéro à 10 chiffres ne comporte pas de `+` et d'indicatif de pays, Braze l'interprète comme un numéro américain. Les numéros de téléphone portoricains nécessitent tout de même un `+` et un indicatif de pays, même s'ils utilisent un format à 10 chiffres avec des indicatifs régionaux de type américain.
- **Numéros internationaux :** Tous les numéros internationaux doivent commencer par un `+`, suivi de leur indicatif de pays puis du numéro de téléphone. Par exemple, `+442071838750`.

![Exemple d'un numéro de téléphone international valide au format E.164.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Voici quelques exemples illustrant les différences entre le format local et le format `E.164` :

| Pays | Local | Indicatif de pays | `E.164` |
|---|---|---|---|
| États-Unis | `4155552671` | 1 | `+14155552671` |
| Royaume-Uni | `2071838750` | 44 | `+442071838750` |
| Brésil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Format recommandé" }

## Importation des numéros de téléphone {#import-phone-numbers}

Lors de l'importation des numéros de téléphone, il est important de suivre le [format recommandé](#recommended-format). Pour importer des numéros de téléphone, utilisez l'une des méthodes suivantes :

- [Charger un fichier CSV dans Braze]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [Utiliser l'endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Les numéros de téléphone des utilisateurs apparaissent dans Braze sous forme de chaîne de chiffres. Si vous importez un numéro contenant des caractères non numériques (tels que `,`, `-` ou `(`) autres que le {% raw %}`+`{% endraw %} initial, ces caractères sont supprimés lors de l'affichage dans Braze. Par exemple, l'importation de `+1 (724) 123-4567` apparaîtra sous la forme `+17241234567`.
{% endalert %}

## Validation des numéros de téléphone {#phone-number-validation}

Braze utilise la bibliothèque [libphonenumber](https://github.com/google/libphonenumber) de Google pour valider les numéros de téléphone. Lorsque de nouveaux préfixes de numéros mobiles sont introduits, leur prise en charge est ajoutée au fur et à mesure de la mise à jour de la bibliothèque en amont. Braze ne gère pas de liste distincte de préfixes valides.

### Gestion des numéros de téléphone invalides {#handling-invalid-phone-numbers}

Lorsqu'un numéro de téléphone est considéré comme invalide, Braze marque le numéro de téléphone de l'utilisateur comme invalide et ne tente pas d'envoyer d'autres communications à ce numéro. Un numéro de téléphone invalide est signalé dans l'**onglet Engagement** du profil utilisateur.

![Exemple de message d'erreur pour les numéros de téléphone invalides dans Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Un numéro de téléphone est considéré comme invalide pour les raisons suivantes :

- **Erreur du fournisseur** : une erreur permanente a été reçue de la part du fournisseur SMS et RCS. Cela indique que le numéro de téléphone fourni est mal formaté ou qu'il est définitivement incapable de recevoir des messages SMS ou RCS.
- **Désactivé** : le numéro de téléphone a été désactivé parce qu'un abonné mobile a résilié son service et libéré son numéro auprès de son opérateur (le numéro peut éventuellement être recyclé et attribué à un nouvel utilisateur). Un numéro de téléphone désactivé peut être marqué comme invalide même si vous n'avez envoyé aucun message SMS ou RCS à ce numéro.

Ces numéros de téléphone invalides peuvent être gérés à l'aide des [endpoints SMS et RCS]({{site.baseurl}}/api/endpoints/sms).

{% alert note %}
Si plusieurs profils utilisateur partagent le même numéro de téléphone et que ce numéro est marqué comme invalide, tous les profils utilisateur existants associés à ce numéro s'afficheront comme invalides. Les profils utilisateur nouvellement créés ne sont jamais marqués comme invalides lors de leur création.
{% endalert %}

Vous pouvez également inclure ou exclure les utilisateurs dont les numéros de téléphone sont invalides lors de la [création d'un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment).

## Exclure les envois SMS rejetés de la segmentation {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
Les rejets de SMS peuvent être comptabilisés dans votre allocation SMS en fonction de votre contrat Braze et de votre fournisseur SMS. Pour les implications en matière de facturation, consultez [Reporting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).
{% endalert %}

Pour exclure de vos Segments les utilisateurs dont les envois SMS ont été rejetés, utilisez les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) en procédant comme suit :

1. Accédez à **Audience** > **Segment Extensions**.
2. Sélectionnez **Create New Extension** > **Full refresh** ou **Incremental refresh**.
3. Rédigez une requête SQL qui identifie les utilisateurs ayant des rejets SMS. Par exemple, vous pouvez interroger l'événement `USERS_MESSAGES_SMS_REJECTION_SHARED` pour trouver les utilisateurs qui ont reçu des rejets SMS.
4. Enregistrez votre extension de Segment.
5. Lors de la création de votre Segment SMS, ajoutez un filtre pour exclure les utilisateurs présents dans cette extension de Segment.

## Ajouter des utilisateurs aux groupes d'abonnement SMS et RCS {#add-users-to-sms-and-rcs-subscription-groups}

Pour qu'un utilisateur puisse recevoir un message SMS ou RCS, il doit disposer d'un numéro de téléphone valide et avoir accepté de recevoir les communications d'un groupe d'abonnement. Les groupes d'abonnement sont liés au programme SMS ou RCS que vous utilisez (assurez-vous de respecter les [exigences légales relatives aux SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) et d'avoir recueilli le consentement de chaque client). Pour en savoir plus, consultez la section [Groupes d'abonnement SMS et RCS]({{site.baseurl}}/sms_rcs_subscription_groups).

## Sourçage et vérification par des tiers {#third-party-sourcing-and-verification}

Braze s'appuie sur des outils tiers pour identifier les numéros invalides. Braze n'est pas responsable des pannes ou des informations erronées provenant de ces services. Par conséquent, cet outil ne doit pas être utilisé comme votre seule méthode de conformité pour la vérification des numéros invalides.

## Capture de numéros de téléphone {#phone-number-capture}

Pour capturer des numéros de téléphone via des messages in-app, consultez le [formulaire d'inscription SMS, RCS et WhatsApp]({{site.baseurl}}/phone_number_capture).