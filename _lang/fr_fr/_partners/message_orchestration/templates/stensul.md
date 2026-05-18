---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Cet article de référence présente le partenariat entre Braze et Stensul, une plateforme d'e-mail d'entreprise permettant de créer des modèles d'e-mails adaptés aux mobiles sur l'ensemble des canaux."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) fournit aux marketeurs e-mail des outils pour créer des e-mails adaptés aux mobiles et conformes à l'identité de marque dans Stensul, avant de les envoyer en aval vers Braze en temps réel pour la création de campagnes.

_Cette intégration est maintenue par Stensul._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Stensul vous permet d'exporter vos e-mails Stensul au format HTML et de les importer en tant que modèles dans Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ------------| ----------- |
| Compte Stensul | Un compte Stensul est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec l'ensemble des autorisations **Templates**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze correspond à votre tableau de bord de Braze et à votre endpoint REST.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Fournissez votre clé API REST de Braze et votre instance de cluster à votre équipe Customer Success Stensul. L'équipe mettra ensuite en place l'intégration initiale pour vous.

{% alert important %}
Il s'agit d'une configuration unique ; toutes les exportations futures utiliseront automatiquement cette clé API.
{% endalert %}

### Étape 1 : Créer un e-mail Stensul {#step-1-create-stensul-email}

Créez un e-mail Stensul dans la plateforme Stensul et cliquez sur **Complete**.

![Options d'enregistrement de Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Étape 2 : Exporter le modèle vers Braze {#step-2-export-template-to-braze}
Dans la nouvelle boîte de dialogue qui s'affiche sur la page de finalisation, sélectionnez **Upload to ESP**.

![Options de téléchargement de Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Saisissez ensuite le **template name**, le **subject** et le **preheader** de votre e-mail, puis sélectionnez **Upload**. Vous recevrez alors une confirmation que l'envoi a réussi, ainsi qu'un historique des envois précédents du fichier, le cas échéant.

![Téléchargement réussi dans Stensul]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Utilisation {#usage}

Vous trouverez le modèle Stensul importé dans la section **Templates & Media > Email Templates** de votre compte Braze. Vous pouvez désormais utiliser ce modèle d'e-mail pour commencer à envoyer des messages attrayants à vos clients !