---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "L'intégration de Braze et Movable Ink Da Vinci permet aux marques de diffuser des messages hautement personnalisés en s'appuyant sur le moteur de décision de contenu piloté par l'intelligence artificielle de Da Vinci. Da Vinci sélectionne le contenu le plus pertinent pour chaque utilisateur et déploie les messages de façon fluide via Braze."
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> L'intégration de Braze et Movable Ink [Da Vinci](https://movableink.com/da-vinci) permet aux marques de diffuser des messages hautement personnalisés en s'appuyant sur le moteur de décision de contenu piloté par l'intelligence artificielle de Da Vinci. Da Vinci sélectionne le contenu le plus pertinent pour chaque utilisateur et déploie les messages de façon fluide via Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
|------------|-------------|
| Movable Ink Da Vinci | Un compte Movable Ink Da Vinci est nécessaire pour bénéficier de ce partenariat. |
| Braze Currents – Événements d'engagement liés aux messages | Une exportation Braze Custom Currents est nécessaire pour envoyer les données d'événements d'engagement liés aux messages à Movable Ink. |
| Clé REST API Braze | Une clé REST API Braze avec les autorisations `messages.send`, `sends.id.create` et `campaigns.details` est requise. Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. <br><br>Votre équipe de compte Movable Ink vous fournira directement des instructions de configuration supplémentaires. Reportez-vous à la section [Intégration](#integration). |
| Instance de l'application Da Vinci dans Braze | Créez une instance dédiée à l'application Da Vinci dans Braze. Une nouvelle application peut être créée dans le tableau de bord de Braze en accédant à **Paramètres** > **Paramètres des applications** > **+ Ajouter une app**. Nommez l'application « **Movable Ink - Da Vinci** » et sélectionnez n'importe quelle plateforme (la sélection d'une plateforme est requise, mais le type n'a pas d'impact sur la fonctionnalité). En savoir plus sur [l'ajout d'une nouvelle application]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour démarrer l'intégration, contactez votre équipe de compte Movable Ink pour obtenir de l'aide. Movable Ink vous fournira les accès et les instructions de configuration nécessaires. Vous devrez fournir à Movable Ink un ensemble d'identifiants API Braze pour permettre à Da Vinci d'envoyer des déploiements d'e-mails via l'API d'envoi de messages de Braze.

Une fois connecté, Movable Ink va :

- Collaborer avec le client et Braze pour configurer le compte Da Vinci de la marque afin de réussir le déploiement avec Braze.
- Capturer les configurations spécifiques à la marque pour les aligner sur vos cas d'utilisation d'envoi de messages.
- Mener des tests complets et une assurance qualité pour valider que les e-mails sont livrés comme prévu et qu'ils répondent à toutes les normes de performance et d'exploitation.