---
nav_title: EmailShepherd
article_title: EmailShepherd
alias: /partners/emailshepherd/
description: "Cet article de référence décrit le partenariat entre Braze et EmailShepherd, une plateforme agentique de création d'e-mails basée sur votre Email Design System qui publie les e-mails approuvés dans votre espace de travail Braze."
page_type: partner
search_tag: Partner
---

# EmailShepherd

> [EmailShepherd](https://emailshepherd.com/) est une plateforme agentique de création d'e-mails basée sur votre Email Design System qui permet à l'ensemble de votre équipe marketing — ainsi qu'aux agents IA — de produire des e-mails conformes à votre marque et prêts pour la production, sans goulots d'étranglement. L'intégration Braze publie les e-mails approuvés directement dans votre espace de travail Braze, afin que les marketeurs puissent augmenter la production d'e-mails dans Braze sans sacrifier la cohérence de marque.

_Cette intégration est maintenue par EmailShepherd._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et EmailShepherd vous permet de créer des e-mails à partir de votre Email Design System dans EmailShepherd et de les exporter vers Braze en tant que modèles d'e-mail. Votre équipe crée et approuve les e-mails dans EmailShepherd, puis publie des modèles prêts pour la production dans Braze sans transfert manuel de HTML.

## Conditions préalables {#prerequisites}

Les éléments suivants sont requis pour utiliser cette intégration :

| Condition | Description |
| ----------- | ----------- |
| Compte EmailShepherd | Un compte EmailShepherd est requis pour utiliser cette intégration. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations complètes « Templates ». <br><br>Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Instance Braze | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze correspond à votre tableau de bord Braze et à votre endpoint REST. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

EmailShepherd est conçu pour les équipes qui souhaitent augmenter la production d'e-mails tout en gardant chaque envoi conforme à la marque. C'est une solution adaptée si vous souhaitez :

- **Garantir la cohérence de marque à grande échelle :** votre Email Design System définit les composants, couleurs et mises en page approuvés. Chaque e-mail publié dans Braze est conforme à la marque par construction.
- **Ouvrir la production d'e-mails à toute votre équipe :** un générateur par glisser-déposer alimenté par votre Email Design System permet à quiconque de créer des e-mails prêts pour la production.
- **Utiliser la création agentique de campagnes :** les agents IA créent dans le cadre des garde-fous de votre Email Design System, de sorte que les campagnes qu'ils produisent sont conformes à la marque et prêtes à être envoyées.

## Intégration {#integration}

### Étape 1 : Créer votre connecteur EmailShepherd {#step-1-create-your-emailshepherd-connector}

{% alert note %}
Il s'agit d'une configuration unique. Une fois le connecteur créé, EmailShepherd utilise ces identifiants pour tous les futurs exports vers Braze.
{% endalert %}

1. Dans EmailShepherd, accédez à **Connectors** > **Add connector**.
2. Sélectionnez **Braze** et saisissez un nom de connecteur.
3. Saisissez votre clé API et sélectionnez votre instance Braze.
4. Sélectionnez **Create Connector** pour enregistrer la connexion.

![Formulaire de connecteur EmailShepherd avec les champs d'instance Braze et de clé API]({% image_buster /assets/img_archive/emailshepherd_step1.png %}){: style="max-width:60%;"}

### Étape 2 : Exporter un e-mail depuis EmailShepherd {#step-2-export-an-email-from-emailshepherd}

Dans EmailShepherd, localisez un e-mail que vous souhaitez exporter vers Braze. Assurez-vous qu'il est publié, puis sélectionnez **Export**.

![Éditeur d'e-mail EmailShepherd avec l'action Export]({% image_buster /assets/img_archive/emailshepherd_step2.png %}){: style="max-width:60%;"}

### Étape 3 : Configurer et publier dans Braze {#step-3-configure-and-publish-to-braze}

1. Sur la page d'export, sélectionnez votre connecteur Braze sous **Connectors** (par exemple, **Braze Prod**).
2. Choisissez une option d'**hébergement d'images** pour les images de votre bibliothèque d'images EmailShepherd. Les images saisies par URL ne sont pas modifiées lors de l'export.
3. Confirmez la **Locale** et saisissez un **nom de modèle** pour l'e-mail dans Braze.
4. Sélectionnez **Start export**.

![Page d'export EmailShepherd avec les champs de connecteur Braze, d'hébergement d'images et de nom de modèle]({% image_buster /assets/img_archive/emailshepherd_step3.png %}){: style="max-width:60%;"}

## Utiliser l'intégration {#use-the-integration}

Dans Braze, retrouvez vos e-mails exportés sous **Contenu** > **E-mail**. Vous pouvez utiliser ces modèles dans des Campaigns et des Canvas Braze.

## Assistance {#support}

Pour plus d'informations sur les intégrations EmailShepherd, consultez la [documentation EmailShepherd](https://emailshepherd.com/docs/).