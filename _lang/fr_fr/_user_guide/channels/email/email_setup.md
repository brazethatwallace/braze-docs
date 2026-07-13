---
nav_title: "Configuration"
article_title: Configuration des e-mails
layout: dev_guide
page_order: 0
guide_top_header: "Configuration des e-mails"
guide_top_text: "Braze peut vous aider à envoyer des campagnes par e-mail. Suivez nos guides ou consultez notre cours d'apprentissage Braze Learning <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Email Onboarding</a>."
page_type: landing
description: "Cette page de destination comprend des ressources pour bien démarrer avec les campagnes par e-mail, notamment la configuration de vos adresses IP et domaines, le réchauffement d'adresses IP, la validation des e-mails, et plus encore."
channel: email

guide_featured_title: "Articles de la section"
guide_featured_list:
- name: "Configuration des adresses IP et des domaines"
  link: /docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains
  image: /assets/img/braze_icons/target-05.svg
- name: "Réchauffement d'adresses IP"
  link: /docs/user_guide/channels/email/email_setup/ip_warming
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Validation des e-mails"
  link: /docs/user_guide/channels/email/email_setup/email_validation
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Authentification par e-mail"
  link: /docs/user_guide/channels/email/email_setup/authentication
  image: /assets/img/braze_icons/user-square.svg
- name: "Importez votre liste d'e-mails"
  link: /docs/user_guide/channels/email/email_setup/import_your_email_list
  image: /assets/img/braze_icons/list.svg
- name: "Aperçu SSL"
  link: /docs/user_guide/channels/email/email_setup/ssl
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentement et collecte d'adresses"
  link: /docs/user_guide/channels/email/email_setup/consent_and_address_collection
  image: /assets/img/braze_icons/book-closed.svg
- name: "Écueils de livrabilité et pièges à spam"
  link: /docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps
  image: /assets/img/braze_icons/alert-triangle.svg
- name: "Pixel d'ouverture et suivi des clics"
  link: /docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
  image: /assets/img/braze_icons/cursor-click-02.svg
---

## Prérequis {#requirements}

Avant de commencer à envoyer des e-mails, vous devez remplir certaines conditions. Consultez le tableau suivant pour en savoir plus sur ces exigences.

| Condition | Description | Source |
|---|---|---|
| Une IP dédiée (protocole Internet) | Une adresse IP dédiée est une adresse internet unique fournie exclusivement à un seul compte d'hébergement. | Braze vous fournit des adresses IP dédiées afin de garantir le contrôle de la réputation de votre expéditeur d'e-mails. L'onboarding de Braze se chargera de cette configuration pour vous. |
| Domaines en marque blanche | Ils se composent d'un domaine et d'un sous-domaine. La marque blanche vous permet de passer les vérifications d'authentification des e-mails pour DKIM et SPF. | L'équipe d'onboarding de Braze génèrera ces domaines pour vous, mais vous devez choisir leurs noms. |
| Sous-domaines | Il s'agit d'une subdivision d'un domaine (par exemple « @news.company.com ») au sein de votre adresse e-mail. Disposer d'un sous-domaine permet d'éviter toute erreur susceptible de nuire à la réputation officielle de l'e-mail de votre entreprise. | L'équipe d'onboarding génèrera ce sous-domaine pour vous, mais vous devez en choisir le nom. Vous ne pouvez pas utiliser de sous-domaines déjà utilisés en dehors de Braze. |
| Pools d'adresses IP | Il s'agit d'une configuration facultative permettant de séparer la réputation de différents types d'e-mails (par exemple « promotionnels » et « transactionnels ») afin d'éviter que la réputation de l'un n'affecte l'autre et de favoriser une meilleure livrabilité. | L'équipe d'onboarding configure les pools pour vous. Ensuite, lors de la rédaction de votre e-mail, vous pouvez consulter le pool d'adresses IP de votre e-mail à l'étape **Audiences cibles**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## Réchauffement d'adresses IP {#ip-warming}

{% alert important %}
Le réchauffement d'adresses IP est l'étape **la plus importante** du processus de configuration des e-mails. Bien que ce ne soit pas votre première étape (c'est en fait la dernière), nous la mentionnons ici pour vous informer que vous devez réchauffer votre adresse IP, sans quoi les e-mails que vous enverrez risquent d'atterrir dans les spams ou de rencontrer d'autres obstacles à l'envoi.
{% endalert %}

Le [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) consiste à envoyer un nombre relativement faible d'e-mails lors de votre premier envoi, puis à augmenter progressivement le volume au fil des envois suivants jusqu'à atteindre votre volume quotidien habituel. Cette opération est réalisée à la toute fin du processus de configuration des e-mails.

En commençant par de petits volumes d'e-mails, vous établissez un niveau de confiance avec votre fournisseur de messagerie, en lui montrant que vous n'envoyez des e-mails qu'à des utilisateurs pertinents. Envoyer votre premier lot d'e-mails à vos utilisateurs les plus engagés peut vous aider à gagner plus rapidement la confiance de votre fournisseur.

Une fois le réchauffement de votre adresse IP terminé, vous pouvez [commencer à créer et envoyer des e-mails]({{site.baseurl}}/user_guide/channels/email/html_editor) !

## E-mails transactionnels légalement requis {#legally-required-transactional-emails}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>