---
nav_title: Envoyer des e-mails à Apple Private Relay
article_title: Envoyer des e-mails à Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Cet article décrit le processus d'envoi d'e-mails au relais privé d'Apple."
channel:
  - email
toc_headers: h2
---

# Envoyer des e-mails à Apple Private Relay {#send-emails-to-apple-private-relay}

> La fonctionnalité d'authentification unique (SSO) d'Apple permet aux utilisateurs de partager leur adresse e-mail (`example@icloud.com`) ou de la masquer en fournissant aux marques une adresse anonymisée (`tq1234snin@privaterelay.appleid.com`) au lieu de leur adresse e-mail personnelle. Apple transfère ensuite les messages envoyés aux adresses relais vers l'adresse e-mail réelle de l'utilisateur.

Pour envoyer des e-mails au relais d'e-mail privé d'Apple, enregistrez vos domaines d'envoi auprès d'Apple. Si vous ne configurez pas vos domaines avec Apple, les e-mails envoyés à des adresses relais entraîneront des rebonds.

Si un utilisateur décide de désactiver le transfert d'e-mails vers l'adresse relais de votre application, Braze recevra les informations de rebond comme d'habitude. Ces utilisateurs peuvent gérer les applications qui utilisent la connexion avec Apple depuis leur page de paramètres Apple ID (voir la [documentation d'Apple](https://support.apple.com/en-us/HT210426)).

## Configurer votre fournisseur d'e-mail {#configure-your-email-provider}

{% tabs %}
{% tab SendGrid %}

Si vous utilisez SendGrid comme fournisseur d'e-mail, vous pouvez envoyer des e-mails à Apple sans effectuer de modifications DNS.

1. Connectez-vous au [portail des développeurs Apple](https://developer.apple.com/).
2. Accédez à la page **Certificates, Identifiers & Profiles**.
3. Sélectionnez **Services** > **Sign in with Apple for Email Communication**.
4. Dans la section **Email Sources**, ajoutez les domaines et sous-domaines.
- L'adresse doit être formatée comme suit : `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (par exemple : `bounces+1234567@braze.online.docs.com`).

Si l'adresse « From » souhaitée est une adresse `abmail`, incluez-la dans votre sous-domaine. Par exemple, utilisez `abmail.docs.braze.com` au lieu de `docs.braze.com`.

{% endtab %}
{% tab SparkPost %}

Pour configurer Apple Private Relay avec SparkPost, suivez ces étapes :

1. Connectez-vous avec Apple.
2. Suivez la [documentation d'Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) pour enregistrer les domaines d'e-mail.
3. Apple vérifiera automatiquement les domaines, affichera ceux qui sont vérifiés et proposera l'option de revérifier ou de supprimer les domaines.

### Lorsque le domaine d'envoi est aussi le domaine de rebond {#when-the-sending-domain-is-also-the-bounce-domain}

Si un domaine d'envoi est également utilisé comme domaine de rebond, vous ne pourrez pas stocker d'enregistrements et devrez suivre ces étapes supplémentaires :

1. Si le domaine a déjà été vérifié sur SparkPost, vous **devez** créer des enregistrements MX et TXT :

| Instance | Enregistrement MX | Enregistrement TXT |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Lorsque le domaine d'envoi est aussi le domaine de rebond" }

{% alert important %}
Pour éviter les échecs SPF, vous devez créer les enregistrements MX et TXT et les propager dans le DNS **avant** de supprimer l'enregistrement CNAME.
{% endalert %}

{:start="2"}
2. Supprimez l'enregistrement CNAME.
3. Remplacez-le par les enregistrements MX et TXT pour un routage correct.
4. Créez votre enregistrement A pour pointer vers votre réseau de diffusion de contenu ou votre hébergement de fichiers.

{% endtab %}
{% tab Amazon SES %}

Pour configurer Apple Private Relay, il est recommandé d'avoir au préalable un domaine MAIL FROM personnalisé.

1. Connectez-vous avec Apple.
2. Suivez la [documentation d'Apple](https://developer.apple.com/help/account/capabilities/configure-private-email-relay-service) pour enregistrer les domaines d'e-mail.

{% alert important %}
Confirmez que vos enregistrements DKIM/SPF correspondent à ce que vous avez enregistré conformément aux instructions indiquées.
{% endalert %}

{:start="3"}
3. Apple vérifiera automatiquement les domaines, affichera ceux qui sont vérifiés et proposera l'option de revérifier ou de supprimer les domaines.

{% endtab %}
{% endtabs %}

Si vous avez d'autres questions, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).