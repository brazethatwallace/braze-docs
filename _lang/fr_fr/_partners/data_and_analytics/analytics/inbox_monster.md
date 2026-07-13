---
nav_title: Inbox Monster
article_title: Inbox Monster
alias: /partners/inbox_monster/
description: "Cet article de référence présente le partenariat entre Braze et Inbox Monster, un outil d'e-mail marketing en ligne qui permet aux clients de Braze d'obtenir de puissantes informations sur la livrabilité et des analyses créatives pour améliorer les performances de leur boîte de réception."
page_type: partner
search_tag: Partner

---

# Inbox Monster

> [Inbox Monster](https://inboxmonster.com/) est une plateforme de signaux de boîte de réception qui aide les marques d'entreprise à faire atterrir chaque envoi. Il s'agit d'une suite intégrée de solutions pour la livrabilité, le rendu créatif et le suivi des SMS, qui permet aux équipes modernes de gestion de la relation client (CRM) d'être plus performantes et de mettre fin aux angoisses liées à l'envoi.

L'intégration de Braze et Inbox Monster vous permet d'éliminer les tests manuels de seedlist, d'automatiser la création de signaux de placement en boîte de réception puissants et exploitables, de simplifier le processus d'examen et d'approbation des ressources créatives des e-mails et d'obtenir des informations précieuses sur la livrabilité. Vous pouvez également importer de façon fluide des modèles d'e-mails pour des diagnostics créatifs et des prévisualisations sur différents appareils.

## Conditions préalables {#prerequisites}

| Condition | Description |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compte sur la plateforme Inbox Monster | Un compte sur la plateforme Inbox Monster est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST Braze | Une clé API REST de Braze avec les autorisations suivantes :  <br> - `messages.send` <br>  - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> Et avec les adresses IP suivantes sur liste blanche : <br> - `3.136.16.19` <br>  - `3.140.233.31`<br> - `18.220.127.138` <br><br> Cette clé peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API** dans l'onglet **Clés API** |
| Identifiant de l'application Braze | Un identifiant de l'application Braze. <br><br>Vous trouverez cette information dans le tableau de bord de Braze, sous **Paramètres** > **Clés API**, dans l'onglet **Identifiants de l'application**. |
| Endpoint Braze | [Votre endpoint Braze]({{site.baseurl}}/api/basics/#endpoints) correspond à l'URL de votre tableau de bord de Braze.<br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

Pour intégrer Inbox Monster, suivez les étapes décrites dans la section [Intégration avec Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3).

## Utilisation {#usage}

Pour savoir comment envoyer des tests de placement en boîte de réception planifiés via Inbox Monster, reportez-vous à la section [Tests de placement en boîte de réception planifiés](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e).