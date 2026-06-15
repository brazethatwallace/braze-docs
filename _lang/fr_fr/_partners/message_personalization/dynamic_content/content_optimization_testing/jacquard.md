---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et Jacquard Dynamic Optimisation qui utilise Braze Currents et le Contenu connecté pour collecter les informations de suivi des clics de vos abonnés par le biais de webhooks. Jacquard relie ensuite ces événements à vos variantes linguistiques pour une optimisation linguistique en temps réel."
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> [Jacquard](https://www.jacquard.com/) réunit l'intelligence artificielle, la linguistique informatique et un esprit centré sur le client pour aider à déployer le langage de marque à grande échelle, sur des canaux personnalisés aux couleurs de votre marque.

Dynamic Optimisation, alimenté par Jacquard X, utilise Braze Currents et le Contenu connecté pour collecter les informations de suivi des clics de vos abonnés par le biais de webhooks. Jacquard relie ensuite ces événements à vos variantes linguistiques pour une optimisation linguistique en temps réel.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Jacquard | Un [compte Jacquard](https://www.jacquard.com/) est nécessaire pour bénéficier de ce partenariat. |
| Jeton du serveur de connexion Jacquard | Une longue chaîne de caractères qui servira de mot de passe à votre Campaign Braze pour accéder à votre langage Jacquard.<br><br>Vous pouvez en faire la demande auprès de votre gestionnaire de la satisfaction client Jacquard si vous ne l'avez pas encore reçu. |
| Currents | Pour pouvoir exporter des données vers Currents, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Demander les identifiants Amazon S3 de Jacquard {#step-1-request-jacquard-amazon-s3-credentials}

Vous aurez besoin que Jacquard configure un compartiment Amazon S3 dédié afin de recevoir vos événements de suivi des clics depuis Braze. Contactez votre gestionnaire de la satisfaction client Jacquard pour démarrer ce processus. Lorsque le compartiment sera créé, vous recevrez des identifiants uniques pour créer votre flux Currents.

### Étape 2 : Créer un flux Currents {#step-2-create-current}

1. Dans Braze, sélectionnez **Currents > Create New Current > Amazon S3 Data Export**.
2. Nommez ensuite votre flux Currents et saisissez un e-mail de contact.
3. Ajoutez votre ID de clé d'accès Jacquard AWS et votre clé d'accès secrète dans la section des identifiants. Ensuite, ajoutez « phrasee-braze-currents-exports » comme nom de compartiment AWS S3.
4. Enfin, ajoutez le dossier du compartiment AWS S3 que vous avez reçu de votre gestionnaire de la satisfaction client Jacquard. Il s'agira probablement du nom de votre société.
5. Sous **General Settings**, cochez la case « Include events from anonymous users », et sous **Manage Engagement Events**, cochez « Email Click ».
6. Lorsque vous avez terminé, sélectionnez **Launch Current**.

### Étape 3 : Demander la suppression des informations personnellement identifiables (IPI) {#step-3-request-to-remove-personally-identifiable-information-pii}

Ensuite, contactez votre équipe de compte Braze pour vous assurer qu'aucune information personnellement identifiable n'est transmise à Jacquard.

Par défaut, le flux Currents inclura certains attributs contenant des IPI, comme l'e-mail et l'adresse. Jacquard ne peut pas recevoir et ne recevra pas d'IPI ; il est donc essentiel que vous demandiez à l'équipe de votre compte Braze de désactiver cette fonctionnalité pour toutes les données d'événements transmises à Jacquard.

### Étape 4 : Extraits de code Jacquard X {#step-4-jacquard-x-code-snippets}

Contactez l'équipe de votre compte Jacquard pour obtenir les extraits de code nécessaires.

Ces extraits utilisent le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) et, une fois placés dans vos e-mails, ils intègrent dynamiquement le langage et un pixel de suivi afin que Jacquard puisse optimiser votre langage en temps réel à l'aide de Jacquard X.