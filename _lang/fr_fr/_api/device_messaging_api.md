---
nav_title: API Device Messaging
article_title: API Device Messaging
search_tag: Endpoint
page_order: 2.2
layout: dev_guide
description: "Cette page de destination présente l'API Device Messaging de Braze."
page_type: landing
hidden: true
guide_top_header: "API Device Messaging"
guide_top_text: "Utilisez l'API Device Messaging de Braze pour récupérer les propriétés des Banners et signaler les événements d'impression et de clic des Banners sans intégrer de SDK Braze. L'API Device Messaging prend en charge les intégrations côté client et côté serveur, et utilise des clés REST API côté client limitées à un seul espace de travail."
guide_top_alert: "Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Device Messaging sont susceptibles d'évoluer. Contactez votre gestionnaire de compte Braze pour demander l'accès."
guide_top_text2: "Remarque : cette API ne récupère que les propriétés d'une bannière donnée, et non le HTML de la bannière."
guide_featured_title: "Premiers pas"
guide_featured_list:
  - name: "Aperçu de l'API Device Messaging"
    link: /docs/api/device_messaging_api/overview
    image: /assets/img/braze_icons/annotation-info.svg
  - name: "Authentification et sécurité"
    link: /docs/api/device_messaging_api/authentication
    image: /assets/img/braze_icons/key-01.svg
  - name: "Gestion des erreurs et nouvelles tentatives"
    link: /docs/api/device_messaging_api/error_handling
    image: /assets/img/braze_icons/alert-circle.svg
  - name: "Limites de débit"
    link: /docs/api/device_messaging_api/rate_limits
    image: /assets/img/braze_icons/speedometer-01.svg
guide_menu_title: "Endpoints Banner"
guide_menu_list:
  - name: "POST : Récupérer les Banners pour un utilisateur"
    link: /docs/api/device_messaging_api/endpoints/banners/post_sync_banners
    image: /assets/img/braze_icons/download-01.svg
  - name: "POST : Suivre les événements d'analyse des Banners"
    link: /docs/api/device_messaging_api/endpoints/banners/post_track_banner_events
    image: /assets/img/braze_icons/line-chart-up-02.svg
---