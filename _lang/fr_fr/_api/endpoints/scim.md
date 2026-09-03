---
nav_title: SCIM
article_title: Endpoints SCIM
search_tag: Endpoint
page_order: 5
layout: dev_guide
alias: /scim/

description: "Cette page répertorie les endpoints SCIM de Braze."
page_type: landing

guide_top_header: "Endpoints SCIM"
guide_top_text: "La spécification <a href=\"http://www.simplecloud.info/\">System for Cross-domain Identity Management (SCIM)</a> est conçue pour faciliter la gestion des identités des utilisateurs dans les applications et services basés sur le cloud en fournissant un schéma défini pour représenter les utilisateurs et les groupes. Utilisez les endpoints SCIM de Braze pour gérer le provisionnement automatisé des utilisateurs."

guide_featured_title: ""
guide_featured_list:
  - name: "POST : Créer un nouveau compte utilisateur de tableau de bord"
    link: /docs/post_create_user_account
    image: /assets/img/braze_icons/plus-circle.svg
  - name: "GET : Rechercher un compte utilisateur de tableau de bord existant par ID de ressource"
    link: /docs/get_see_user_account_information
    image: /assets/img/braze_icons/eye.svg
  - name: "GET : Rechercher un compte utilisateur de tableau de bord existant par e-mail"
    link: /docs/api/endpoints/scim/get_search_existing_dashboard_user
    image: /assets/img/braze_icons/eye.svg
  - name: "PUT : Mettre à jour un compte utilisateur du tableau de bord"
    link: /docs/post_update_existing_user_account
    image: /assets/img/braze_icons/pencil-01.svg
  - name: "DELETE : Supprimer un compte utilisateur de tableau de bord"
    link: /docs/delete_existing_dashboard_user
    image: /assets/img/braze_icons/trash-01.svg
---


{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' subject='endpoints' %}

## Comment exporter une liste d'utilisateurs ayant accès au tableau de bord {#how-to-export-a-list-of-users-with-dashboard-access}

Utilisez ce flux de travail pour auditer les utilisateurs qui ont accès à votre tableau de bord de Braze.

1. Téléchargez le rapport d'événements de sécurité depuis **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** > **Téléchargement des événements de sécurité**.
2. Extrayez les adresses e-mail des utilisateurs à partir du rapport.
3. Pour chaque adresse e-mail, utilisez [GET : Rechercher un compte utilisateur de tableau de bord existant par e-mail]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user) pour récupérer les détails de l'utilisateur.
4. Si nécessaire, utilisez l'`id` de ressource renvoyé avec [GET : Rechercher un compte utilisateur de tableau de bord existant par ID de ressource]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information) pour obtenir des détails supplémentaires sur l'utilisateur.

Pour la liste complète des endpoints SCIM, consultez la section [Endpoints SCIM]({{site.baseurl}}/api/endpoints/scim). Pour plus d'informations sur la source du rapport, consultez la section [Télécharger un rapport d'événements de sécurité]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report).