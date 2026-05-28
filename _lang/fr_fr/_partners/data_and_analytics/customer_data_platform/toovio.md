---
nav_title: Toovio
article_title: Toovio
description: "Cet article de référence présente le partenariat entre Braze et Toovio, une société de données en tant que service, qui vous aide à découvrir vos données exploitables et à utiliser les éléments les plus importants pour obtenir des résultats incrémentaux en fonction d'objectifs prédéfinis."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) est une société de données en tant que service alimentée par l'intelligence artificielle qui vous aide à découvrir vos données exploitables et à utiliser les éléments les plus critiques pour obtenir des résultats incrémentaux en fonction d'objectifs prédéfinis.

_Cette intégration est maintenue par Toovio._

## À propos de l'intégration {#about-the-integration}

Le partenariat entre Braze et Toovio permet le déclenchement de messages en temps quasi réel, fournit des outils pour améliorer les performances incrémentales et donne accès aux outils de mesure de campagne avancés de Toovio.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Toovio | Un compte Toovio est nécessaire pour bénéficier de ce partenariat. |
| Clé REST API de Braze | Une clé REST API de Braze avec les autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Braze Currents | Braze Currents permet aux clients de Braze de transmettre des données d'événements ou de comportement en continu à un partenaire de données de Braze (AWS S3, Google Cloud Storage ou Microsoft Azure Blob Storage) pour un traitement externe à la plateforme Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

L'intégration suivante permet à Toovio de générer des déclencheurs ciblant des clients spécifiques et de communiquer en temps quasi réel. Les déclencheurs déterminés par Toovio seront transmis à Braze via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze.

### Étape 1 : Définir le partenaire de données {#step-1-define-data-partner}

Un emplacement de dépôt pour le flux Currents doit être partagé avec Toovio ; cela permet à Toovio d'accéder aux données d'événements et de comportement des utilisateurs et de les traiter.

### Étape 2 : Configurer une campagne déclenchée {#step-2-set-up-a-triggered-campaign}

Créez une [campagne déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) de Braze en fonction des événements clients que Toovio ciblera. De plus, les attributs et les valeurs utilisateur qui déclencheront la campagne doivent être définis.

### Étape 3 : Configurer votre compte Toovio {#step-3-set-up-your-toovio-account}

Contactez Toovio à l'adresse [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) avec l'objet « New Customer Request » pour créer un compte. Toovio travaillera avec les clients pour mettre en place les déclencheurs et les modèles sous-jacents.