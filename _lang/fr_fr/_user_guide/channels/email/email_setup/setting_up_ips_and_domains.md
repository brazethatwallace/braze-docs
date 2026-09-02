---
nav_title: Configurer les adresses IP et les domaines
article_title: Configurer les adresses IP et les domaines
page_order: 0
page_type: tutorial
channel: email
description: "Cet article pratique vous explique comment configurer les adresses IP, les pools d'IP, les domaines et les sous-domaines pour envoyer des e-mails avec Braze."
---

# Configurer les adresses IP et les domaines {#set-up-ips-and-domains}

> Cet article vous guide à travers les exigences et les étapes nécessaires pour configurer vos adresses IP et vos pools, ainsi que les domaines et sous-domaines requis avant de pouvoir commencer à envoyer des e-mails avec Braze.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
À partir de 2026, Braze utilise Amazon Simple Email Service (SES) comme fournisseur de services d'e-mail marketing or e-mailing (fournisseur de services d'e-mailing) par défaut pour les nouvelles configurations d'e-mail. Pour plus de détails, consultez [Configuration d'Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).
{% endalert %}

## Méthode 1 : Configuration en libre-service des e-mails {#method-1-self-service-email-setup}

Cette méthode configure vos domaines d'envoi et de suivi pour une entreprise. Vous devrez d'abord consulter l'équipe d'onboarding Braze et envoyer les informations suivantes à votre conseiller Braze pour que vos pools d'IP et adresses IP soient ajoutés :

- Vos domaines et sous-domaines choisis
- Le nombre approximatif d'e-mails que vous envoyez chaque mois, ce qui permet de déterminer le nombre d'IP dont vous avez besoin
- La manière dont vous souhaitez associer vos domaines d'envoi à vos pools d'IP alloués

### Conditions préalables {#prerequisites}

Pour utiliser la configuration en libre-service des e-mails, vérifiez que vous remplissez les conditions préalables suivantes :

- Vous êtes un nouveau client en phase d'onboarding.
- Vous disposez de la permission au niveau de l'entreprise « Edit Domain Settings ».

### Étape 1 : Commencer la configuration {#step-1-begin-setup}

1. Accédez à **Paramètres** > **Email Self Serve** sous **Paramètres de l'entreprise**.
2. Sélectionnez **Start setup**.

### Étape 2 : Ajouter et vérifier un domaine d'envoi {#step-2-add-and-verify-a-sending-domain}

Un domaine d'envoi est utilisé dans l'adresse « from » lors de l'envoi d'un e-mail.

1. Saisissez un domaine d'envoi et sélectionnez **Submit**.
2. Ajoutez les enregistrements TXT et CNAME situés en bas de la page à votre fournisseur DNS.

![Section des enregistrements DNS affichant les enregistrements TXT et CNAME à copier dans votre système de gestion de domaine.]({% image_buster /assets/img/email_setup/dns_records.png %})

{: start="3"}
3. Retournez dans le tableau de bord de Braze et sélectionnez **Verify**.

Demandez à vos ingénieurs et développeurs d'ajouter ces enregistrements DNS là où c'est nécessaire. Pour des explications détaillées sur le fonctionnement des enregistrements DNS au sein des fournisseurs de services d'e-mail marketing or e-mailing de Braze, notamment SPF, DKIM, DMARC et les structures d'enregistrements spécifiques à chaque fournisseur, consultez [Comprendre les enregistrements DNS]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records).

{% multi_lang_include channels/email/dns_records.md %}

Si la vérification échoue et que vous pensez que vos enregistrements DNS sont corrects, contactez l'assistance Braze pour obtenir de l'aide.

{% alert important %}
Le domaine d'envoi doit être subordonné à un domaine que vous possédez. Par exemple, si vous possédez « example.com », un sous-domaine pourrait être « mail.example.com », ce qui vous permet d'utiliser l'adresse d'envoi « @mail.example.com ».
{% endalert %}

### Étape 3 : Ajouter et vérifier un domaine de suivi {#step-3-add-and-verify-a-tracking-domain}

Un domaine de suivi est utilisé pour encapsuler les liens dans vos e-mails à des fins de suivi des clics et de branding. Il est visible par vos destinataires lorsqu'ils survolent ou cliquent sur les liens de vos e-mails. Braze recommande de le faire correspondre à votre domaine d'envoi.

1. Saisissez un domaine de suivi et sélectionnez **Submit**.
2. Ajoutez les enregistrements CNAME situés en bas de la page à votre fournisseur DNS.
3. Retournez dans le tableau de bord de Braze et sélectionnez **Verify**.

### Étape 4 : Ajouter une adresse IP {#step-4-add-an-ip-address}

Braze génère un enregistrement A pour associer votre adresse IP à votre sous-domaine d'envoi dans une configuration appelée DNS inversé (rDNS). Ajoutez l'enregistrement A dans votre fournisseur DNS, puis sélectionnez **Set up rDNS** pour favoriser la livrabilité.

Pour ajouter ou modifier vos adresses IP pour un pool d'IP, contactez l'assistance Braze.

#### Pools d'IP avec plus d'une IP dédiée {#ip-pools-with-more-than-one-dedicated-ip}

Lorsqu'un pool d'IP contient plusieurs adresses IP dédiées, Braze et votre fournisseur de services d'e-mail marketing or e-mailing répartissent les envois volumineux entre ces IP pour optimiser la capacité et la livrabilité. La répartition est approximative : chaque message d'une Campaign n'utilise pas nécessairement toutes les IP, et les envois plus petits peuvent sembler inégalement répartis entre les adresses. SendGrid traite souvent les e-mails par lots (de l'ordre d'environ 1 500 messages par lot), de sorte que le volume ne se divise pas toujours selon un ratio strict un pour un entre les IP. Si vous envoyez régulièrement un volume quotidien très élevé, discutez du dimensionnement du pool avec votre contact d'onboarding ou de satisfaction client chez Braze.

### Étapes suivantes {#next-steps}

Une fois la vérification de votre expéditeur terminée, Braze recommande l'IP warming afin que vos messages atteignent les boîtes de réception de destination à un taux élevé et constant. Utilisez l'[IP warming automatisé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming) pour vous aider à configurer et surveiller votre calendrier de montée en charge.

Après avoir terminé cette configuration, consultez l'équipe d'onboarding Braze pour confirmer que vos domaines et votre [IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) fonctionnent correctement.

## Méthode 2 : Domaines vérifiés {#method-2-verified-domains}

Les domaines vérifiés vous permettent d'accorder à Braze le contrôle d'un sous-domaine spécifique afin que Braze puisse automatiser la configuration des e-mails et le suivi des clics HTTPS. Grâce à la délégation de domaine DNS, Braze gère les enregistrements DNS nécessaires à l'envoi d'e-mails et au suivi des clics. Par exemple, si votre sous-domaine est « mail.example.com », vous pouvez le déléguer à Braze pour configurer vos domaines d'envoi et de suivi.

{% alert important %}
Les domaines vérifiés ne prennent actuellement en charge qu'Amazon SES. Si vous utilisez SendGrid ou SparkPost, cette fonctionnalité n'est pas disponible.<br><br>Les domaines vérifiés sont pris en charge uniquement pour les e-mails. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

### Configuration {#setup}

#### Étape 1 : Coordonner avec Braze {#step-1-coordinate-with-braze}

Envoyez les informations suivantes à votre conseiller Braze :

- Vos domaines et sous-domaines choisis
- La manière dont vous souhaitez associer vos domaines à vos pools d'IP
- Le nombre approximatif d'e-mails que vous prévoyez d'envoyer chaque mois sur chaque sous-domaine, ce qui permet de déterminer le nombre d'IP nécessaires pour vos pools d'IP
- Tout problème de livrabilité antérieur devant être signalé

#### Étape 2 : Braze configure les informations {#step-2-braze-configures-information}

Après réception de votre e-mail, Braze ajoute le nombre prévu d'IP et de pools d'IP. Une fois les pools d'IP et les adresses IP ajoutés, suivez les étapes décrites dans [Domaines vérifiés]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains).