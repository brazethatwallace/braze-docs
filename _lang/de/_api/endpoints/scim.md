---
nav_title: SCIM
article_title: SCIM-Endpunkte
search_tag: Endpoint
page_order: 5
layout: dev_guide
alias: /scim/

description: "Auf dieser Landing-Page werden die SCIM-Endpunkte von Braze aufgelistet."
page_type: landing

guide_top_header: "SCIM-Endpunkte"
guide_top_text: "Die <a href=\"http://www.simplecloud.info/\">System for Cross-domain Identity Management (SCIM)</a>-Spezifikation soll die Verwaltung von Nutzer:innen-Identitäten in cloudbasierten Anwendungen und Diensten erleichtern, indem sie ein definiertes Schema zur Darstellung von Nutzer:innen und Gruppen bereitstellt. Verwenden Sie die SCIM-Endpunkte von Braze, um die automatisierte Nutzerbereitstellung zu verwalten."

guide_featured_title: ""
guide_featured_list:
  - name: "POST: Neues Dashboard-Nutzerkonto erstellen"
    link: /docs/post_create_user_account
    image: /assets/img/braze_icons/plus-circle.svg
  - name: "GET: Ein bestehendes Dashboard-Nutzerkonto anhand der Ressourcen-ID suchen"
    link: /docs/get_see_user_account_information
    image: /assets/img/braze_icons/eye.svg
  - name: "GET: Bestehendes Dashboard-Nutzerkonto per E-Mail durchsuchen"
    link: /docs/api/endpoints/scim/get_search_existing_dashboard_user
    image: /assets/img/braze_icons/eye.svg
  - name: "PUT: Dashboard-Nutzerkonto aktualisieren"
    link: /docs/post_update_existing_user_account
    image: /assets/img/braze_icons/pencil-01.svg
  - name: "DELETE: Dashboard-Nutzerkonto entfernen"
    link: /docs/delete_existing_dashboard_user
    image: /assets/img/braze_icons/trash-01.svg
---


{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' subject='endpoints' %}

## So exportieren Sie eine Liste von Nutzer:innen mit Dashboard-Zugriff {#how-to-export-a-list-of-users-with-dashboard-access}

Verwenden Sie diesen Workflow, um Nutzer:innen zu überprüfen, die Zugriff auf Ihr Braze-Dashboard haben.

1. Laden Sie den Sicherheitsereignisbericht unter **Konfiguration** > **Administratoreinstellungen** > **Sicherheitseinstellungen** > **Sicherheitsereignis-Download** herunter.
2. Extrahieren Sie die E-Mail-Adressen der Nutzer:innen aus dem Bericht.
3. Verwenden Sie für jede E-Mail-Adresse [GET: Bestehendes Dashboard-Nutzerkonto per E-Mail durchsuchen]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user), um die Nutzerdetails abzurufen.
4. Verwenden Sie bei Bedarf die zurückgegebene Ressourcen-`id` mit [GET: Ein bestehendes Dashboard-Nutzerkonto anhand der Ressourcen-ID suchen]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information), um weitere Nutzerdetails zu erhalten.

Die vollständige Liste der SCIM-Endpunkte finden Sie unter [SCIM-Endpunkte]({{site.baseurl}}/api/endpoints/scim). Weitere Informationen zur Berichtsquelle finden Sie unter [Einen Sicherheitsereignisbericht herunterladen]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report).