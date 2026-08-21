---
nav_title: "Configuration"
article_title: Configuration des e-mails
layout: dev_guide
page_order: 0
guide_top_header: "Configuration des e-mails"
guide_top_text: "Braze peut vous aider à envoyer des campagnes par e-mail. Suivez nos guides ou consultez notre cours d'apprentissage Braze Learning <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Email Onboarding</a>."
page_type: landing
description: "Cette page de destination comprend des ressources pour bien démarrer avec les campagnes par e-mail, notamment la configuration de vos adresses IP et domaines, l'IP warming, la validation des e-mails, et plus encore."
channel: email

guide_featured_title: "Articles de la section"
guide_featured_list:
- name: "Configuration des adresses IP et des domaines"
  link: /docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains
  image: /assets/img/braze_icons/target-05.svg
- name: "IP warming"
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
- name: "Statut d'abonnement"
  link: /docs/user_guide/audience/subscription_preferences/subscription_status
  image: /assets/img/braze_icons/check-verified-02.svg
---

## Prérequis {#requirements}

Avant de commencer à envoyer des e-mails, il y a quelques éléments à mettre en place. Consultez le tableau suivant pour en savoir plus sur ces prérequis.

| Prérequis | Description | Source |
|---|---|---|
| Une IP dédiée (Internet Protocol) | Une IP dédiée est une adresse internet unique attribuée exclusivement à un seul compte d'hébergement. | Braze vous fournit des IP dédiées pour garantir le contrôle de votre réputation d'expéditeur d'e-mails. L'équipe d'onboarding de Braze se chargera de la configuration pour vous. |
| Domaines en marque blanche | Ils se composent d'un domaine et d'un sous-domaine. En utilisant la marque blanche, vous pouvez réussir les vérifications d'authentification des e-mails pour DKIM et SPF. | L'équipe d'onboarding de Braze génère ces domaines pour vous, mais vous devez choisir leurs noms. |
| Sous-domaines | Il s'agit d'une subdivision d'un domaine (par exemple « @news.company.com ») au sein de votre adresse e-mail. Disposer d'un sous-domaine permet d'éviter toute erreur susceptible de nuire à la réputation officielle de votre entreprise en matière d'e-mails. | L'équipe d'onboarding le génère pour vous, mais vous devez décider du nom du sous-domaine. Vous ne pouvez pas utiliser de sous-domaines déjà utilisés en dehors de Braze. |
| Pools d'IP | Il s'agit d'une configuration optionnelle utilisée pour séparer la réputation de différents types d'e-mails (tels que « promotionnel » et « transactionnel ») afin d'éviter que la réputation de l'un n'affecte l'autre et de favoriser une meilleure livrabilité. | L'équipe d'onboarding configure les pools pour vous. Ensuite, lors de la composition de votre e-mail, vous pouvez consulter le pool d'IP de votre e-mail à l'étape **Target Audiences**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## IP warming {#ip-warming}

{% alert important %}
L'IP warming est l'**étape la plus importante** du processus de configuration des e-mails. Bien que ce ne soit pas votre première étape (c'est en fait la dernière), nous la mentionnons ici pour vous informer que vous devez impérativement réchauffer votre adresse IP, sinon les e-mails que vous envoyez risquent d'être envoyés dans les spams ou de rencontrer d'autres obstacles à l'envoi.
{% endalert %}

L'[IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) consiste à envoyer un nombre relativement restreint d'e-mails lors de votre premier envoi, puis à augmenter progressivement le volume au fil des envois suivants jusqu'à atteindre votre volume quotidien habituel. Cette opération est réalisée à la toute fin de votre processus de configuration des e-mails.

En commençant par de plus petits volumes d'e-mails, vous établissez un niveau de confiance avec votre fournisseur de messagerie, en lui montrant que vous n'envoyez des e-mails qu'à des utilisateurs pertinents. Envoyer votre premier lot d'e-mails à vos utilisateurs les plus engagés peut vous aider à gagner plus rapidement la confiance de votre fournisseur.

Une fois l'IP warming terminé, vous pouvez [commencer à créer et envoyer des e-mails]({{site.baseurl}}/user_guide/channels/email/html_editor) !

## E-mails transactionnels légalement requis {#legally-required-transactional-emails}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>