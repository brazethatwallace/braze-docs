---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Cet article de référence présente le partenariat entre Braze et Stripo, un générateur de modèles d'e-mails par glisser-déposer permettant de créer des e-mails sophistiqués avec des éléments interactifs."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) est un générateur de modèles d'e-mails par glisser-déposer pour concevoir des e-mails réactifs avec des éléments interactifs. Les utilisateurs de Stripo peuvent également modifier en HTML et décider des éléments à afficher ou à masquer sur différents appareils grâce à l'éditeur de Stripo.

_Cette intégration est maintenue par Stripo._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Stripo vous permet d'exporter vos e-mails Stripo personnalisés et de les télécharger en tant que modèles dans Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ------------| ----------- |
| Compte Stripo | Un compte Stripo est nécessaire pour bénéficier de ce partenariat. |
| Clé REST API de Braze | Une clé REST API de Braze avec l'ensemble des autorisations sur les **modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze correspond à votre tableau de bord de Braze et à votre endpoint REST. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer un e-mail Stripo {#step-1-create-stripo-email}

Créez un e-mail Stripo dans la plateforme Stripo et cliquez sur **Export**.

![Exportation de Stripo]({% image_buster /assets/img_archive/stripo_export.png %})

### Étape 2 : Exporter le modèle vers Braze {#step-2-export-template-to-braze}

Dans la boîte de dialogue qui s'affiche, sélectionnez **Braze** comme méthode d'exportation.

Ensuite, entrez votre **nom de compte** (tel que le nom de l'espace de travail), votre **clé API** et votre **instance de cluster**.

![Formulaire Stripo]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Il s'agit d'une configuration unique, et toutes les prochaines exportations utiliseront automatiquement cette clé API.
{% endalert %}

## Utilisation {#usage}

Vous trouverez le modèle Stripo que vous avez téléchargé dans la section **Modèles et médias > Modèles d'e-mail** de votre compte Braze. Vous pouvez désormais utiliser ce modèle d'e-mail pour commencer à envoyer des e-mails attrayants à vos clients !