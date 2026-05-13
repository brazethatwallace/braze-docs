---
nav_title: "Numéros de téléphone des utilisateurs"
article_title: Numéros de téléphone des utilisateurs WhatsApp
page_order: 3
description: "Cet article de référence traite du formatage des numéros de téléphone WhatsApp, de l'importation des numéros de téléphone, ainsi que de l'ajout d'utilisateurs aux groupes d'abonnement WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Numéros de téléphone des utilisateurs {#user-phone-numbers}

> Cet article aborde différents sujets relatifs aux numéros de téléphone de vos utilisateurs ou clients.

Les numéros de téléphone sont affichés dans le profil utilisateur au format local, mais ne seront pas dans le format que vous utilisez pour importer le numéro (`(724) 123 4567`).

## Importation des numéros de téléphone {#importing-phone-numbers}

Vous pouvez importer des numéros de téléphone en [chargeant un fichier CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv) ou [via l'API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour créer un utilisateur.

### Formatage {#formatting}

Il est important d'importer les numéros non américains au format [`E.164`](https://en.wikipedia.org/wiki/e.164), en incluant le « + » et l'indicatif du pays. Tout numéro de téléphone non fourni dans ce format sera interprété comme un numéro américain.

Si un numéro de téléphone est converti au format E.164 mais ne passe pas la validation, Braze ne pourra pas envoyer de messages WhatsApp à ce numéro. Tout utilisateur dont le numéro de téléphone ne peut pas être formaté sortira automatiquement d'une étape du Canvas incluant WhatsApp.

Tous les numéros américains doivent être des numéros de téléphone valides à 10 chiffres avec un indicatif régional valide. Ils peuvent être saisis sans le `+` et l'indicatif du pays, car Braze supposera et associera tous les numéros valides à 10 chiffres comme des numéros américains.

Tous les numéros internationaux doivent commencer par un `+`, suivi de l'indicatif du pays puis du numéro de téléphone (par exemple `+442071838750`).

![Exemple d'un numéro de téléphone international valide au format E.164.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Cependant, pour garantir la précision lorsque vous envoyez vers plusieurs régions avec des indicatifs de pays ou régionaux différents, il est recommandé d'utiliser le format `E.164`, même pour les numéros de téléphone basés aux États-Unis.

Vous pouvez voir les différences entre le formatage local des numéros et le formatage universel `E.164` dans le tableau suivant :

| Pays | Local | Indicatif du pays | `E.164` |
|---|---|---|---|
| États-Unis | `4155552671` | 1 | `+14155552671` |
| Royaume-Uni | `02071838750` | 44 | `+442071838750` |
| Brésil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Formatage" }

### Ajout d'utilisateurs à un groupe d'abonnement WhatsApp {#adding-users-to-whatsapp-a-subscription-group}

Pour qu'un client puisse recevoir un message WhatsApp, il doit disposer d'un numéro de téléphone valide et avoir donné son consentement à un groupe d'abonnement. Pour en savoir plus, consultez la section [Groupes d'abonnement WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/).


### Plusieurs utilisateurs avec le même numéro de téléphone {#multiple-users-with-the-same-phone-number}

Si plusieurs utilisateurs partagent le même numéro de téléphone au sein d'un segment d'une seule campagne ou d'une seule étape du Canvas, Braze dédupliquera l'envoi et n'enverra qu'un seul message à ce numéro de téléphone.