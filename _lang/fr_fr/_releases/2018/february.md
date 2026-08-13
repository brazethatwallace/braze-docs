---
nav_title: février
page_order: 11
noindex: true
page_type: update
description: "Cet article contient les notes de version de février 2018."
---
# Février 2018 {#february-2018}

## Compteur de badges push iOS {#ios-push-badge-count}

Vous pouvez désormais [mettre à jour le nombre de badges]({{site.baseurl}}/help/best_practices/utilizing_badge_count#utilizing-badge-count) dans le compositeur de notifications push depuis Braze.
Pour chaque message push, vous pouvez spécifier le nombre de badges déclenché par cette notification.

## Exportation des utilisateurs via API avec les adresses e-mail {#exporting-users-via-api-using-email-addresses}

Vous pouvez désormais [exporter les données du profil utilisateur via l'API]({{site.baseurl}}/developer_guide/rest_api/export#user-export) en spécifiant les adresses e-mail.
Cette exportation inclut tous les profils associés à l'adresse e-mail en question.

## API de modèles d'e-mail {#email-template-apis}

Vous pouvez désormais créer et mettre à jour des [modèles d'e-mail via l'API]({{site.baseurl}}/developer_guide/rest_api/email_templates#email-templates). Chaque modèle dispose d'un **email_template_id** qui peut être référencé dans d'autres appels API.

## Autorisations des clés API REST {#rest-api-keys-permissions}

Vous pouvez désormais créer [plusieurs clés API REST]({{site.baseurl}}/developer_guide/rest_api/basics#creating-rest-api-keys) et configurer les autorisations d'accès pour chacune d'entre elles. Chaque clé peut être configurée pour accorder l'accès à certains endpoints.

Vous pouvez également spécifier une [liste blanche d'adresses IP]({{site.baseurl}}/developer_guide/rest_api/basics#api-ip-whitelisting) et de sous-réseaux autorisés à effectuer des requêtes API REST pour une clé API REST donnée.