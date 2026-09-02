---
nav_title: Configuration d'Amazon SES
article_title: Configuration d'Amazon SES
page_order: 1
page_type: reference
description: "Cet article de référence explique comment configurer Amazon SES en tant que fournisseur de services d'e-mail marketing."
channel: email
---

# Configuration d'Amazon SES {#amazon-ses-setup}

> Braze utilise Amazon Simple Email Service (SES) comme fournisseur de services d'e-mail marketing par défaut lors de la configuration initiale des e-mails. Si la configuration requise ne correspond pas aux fonctionnalités d'Amazon SES, contactez l'assistance Braze pour avoir la possibilité de finaliser la configuration dans SparkPost ou SendGrid.

## Conditions préalables {#prerequisites}

Avant de commencer la configuration d'Amazon SES, vérifiez que vous disposez des éléments suivants :

- Noms de domaines d'envoi
- Noms de pools d'IP (tels que marketing, transaction, staging)
- Le nombre d'adresses IP pour chaque pool d'IP
- Le suffixe souhaité pour les domaines de suivi des clics (tel que « clicks » ou « click », « links » ou « link »)

## Exemple de configuration {#setup-example}

Une configuration Amazon SES typique se présente comme suit :

- **Nom du sous-compte :** braze
- **Cluster :** eu-02

| Pool d'IP | Nombre d'IP | Jeu de configuration | Domaine d'envoi | Domaine de suivi des clics |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Exemple de configuration" }

{% alert note %}
Le cluster et le nom du sous-compte sont automatiquement ajoutés aux pools d'IP et aux jeux de configuration.
{% endalert %}

## Exemples de configuration de domaines de suivi des clics {#click-tracking-domain-configuration-examples}

Les tableaux suivants présentent des exemples de configurations possibles de domaines de suivi des clics en fonction de vos préférences de branding.

### Un domaine de suivi des clics pour chaque domaine d'envoi {#one-click-tracking-domain-for-each-sending-domain}

| Pool d'IP marketing | Jeu de configuration | Sous-domaines d'envoi | Domaines de suivi des clics |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Un domaine de suivi des clics pour chaque domaine d'envoi" }

### Un domaine de suivi des clics pour tous les domaines d'envoi {#one-click-tracking-domain-for-all-sending-domains}

Ceci repose sur la règle selon laquelle le domaine de suivi des clics doit correspondre à au moins un domaine d'envoi du jeu de configuration.

| Pool d'IP marketing | Jeu de configuration | Sous-domaines d'envoi | Domaines de suivi des clics |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Un domaine de suivi des clics pour tous les domaines d'envoi" }

## Remarques importantes {#considerations}

- Les pools d'IP sur Amazon SES hébergent uniquement l'adresse IP elle-même, tandis que les jeux de configuration hébergent les domaines d'envoi et le domaine de suivi des clics.
- Chaque jeu de configuration ne peut avoir qu'un seul pool d'IP affecté à la fois, mais il est possible de créer plusieurs jeux de configuration utilisant le même pool d'IP avec des domaines d'envoi différents.
- Amazon SES gère les enregistrements rDNS et A en interne, car ils entretiennent des relations étroites avec les fournisseurs de boîtes de réception afin de faciliter la reconnaissance des adresses IP.
- Chaque domaine d'envoi possède un identifiant MAIL FROM qui lui est associé pour faciliter les validations SPF.
    - La valeur pour chaque domaine d'envoi est « e ».
    - La valeur MAIL FROM ne modifie pas l'adresse d'expéditeur que vos clients voient.
- Les périodes de début et de fin des messages trap ne sont pas disponibles si vous utilisez Amazon SES comme fournisseur de services d'e-mail marketing.

## Étapes suivantes {#next-steps}

- [Configurer le SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/)