---
nav_title: API de mensajería de dispositivos
article_title: API de mensajería de dispositivos
search_tag: Endpoint
page_order: 2.2
layout: dev_guide
description: "Esta página de destino presenta la API de mensajería de dispositivos de Braze."
page_type: landing
hidden: true
guide_top_header: "API de mensajería de dispositivos"
guide_top_text: "Usa la API de mensajería de dispositivos de Braze para recuperar propiedades de Banner e informar eventos de impresión y clic de Banner sin integrar un SDK or kit de desarrollo de software de Braze. La API de mensajería de dispositivos admite integraciones del lado del cliente y del lado del servidor, y utiliza claves de API REST or transferencia de estado representacional del lado del cliente con alcance a un único espacio de trabajo."
guide_top_alert: "Esta página está en fase beta. Las características y la documentación de la API de mensajería de dispositivos están sujetas a cambios. Ponte en contacto con tu director de cuentas de Braze para solicitar acceso."
guide_top_text2: "Nota: esta API solo recupera propiedades para un banner determinado, no el HTML del banner."
guide_featured_title: "Primeros pasos"
guide_featured_list:
  - name: "Resumen de la API de mensajería de dispositivos"
    link: /docs/api/device_messaging_api/overview
    image: /assets/img/braze_icons/annotation-info.svg
  - name: "Autenticación y seguridad"
    link: /docs/api/device_messaging_api/authentication
    image: /assets/img/braze_icons/key-01.svg
  - name: "Manejo de errores y reintentos"
    link: /docs/api/device_messaging_api/error_handling
    image: /assets/img/braze_icons/alert-circle.svg
  - name: "Límites de velocidad"
    link: /docs/api/device_messaging_api/rate_limits
    image: /assets/img/braze_icons/speedometer-01.svg
guide_menu_title: "Endpoints de Banner"
guide_menu_list:
  - name: "POST: Recuperar Banners para un usuario"
    link: /docs/api/device_messaging_api/endpoints/banners/post_sync_banners
    image: /assets/img/braze_icons/download-01.svg
  - name: "POST: Registrar eventos de análisis de Banner"
    link: /docs/api/device_messaging_api/endpoints/banners/post_track_banner_events
    image: /assets/img/braze_icons/line-chart-up-02.svg
---