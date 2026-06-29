---
nav_title: Configurer les adresses IP et les domaines
article_title: Configurer les adresses IP et les domaines
page_order: 0
page_type: tutorial
channel: email
description: "Cet article pratique vous explique comment configurer vos adresses IP et vos domaines pour envoyer des e-mails via Braze."

---

# Configurer les adresses IP et les domaines {#set-up-ips-and-domains}

> Cet article vous guide à travers les exigences et les étapes nécessaires pour configurer vos adresses IP et vos pools, ainsi que les domaines et sous-domaines requis avant de pouvoir commencer à envoyer des e-mails avec Braze.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
Vous pouvez utiliser SendGrid, SparkPost ou Amazon Simple Email Service (SES) comme fournisseur de services d'e-mailing (ESP) partenaire. À partir de 2026, Braze utilise Amazon SES comme ESP par défaut pour les nouvelles configurations d'e-mail. Pour plus de détails, consultez [Configuration d'Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses/).
{% endalert %}

## Méthode 1 : Coordonner avec Braze (recommandé) {#method-1-coordinate-with-braze-recommended}

### Étape 1 : Rassembler les informations {#step-1-outline-information}

Envoyez les informations suivantes à votre conseiller Braze :

* Les domaines et sous-domaines de votre choix
* Le nombre approximatif d'e-mails que vous enverrez chaque mois, ce qui nous aidera à déterminer le nombre d'adresses IP dont vous aurez besoin
* La manière dont vous préférez mapper vos domaines d'envoi vers l'adresse IP qui vous a été attribuée

### Étape 2 : Braze configure les informations {#step-2-braze-configures-information}

Après avoir reçu votre e-mail, nous nous chargerons de configurer vos adresses IP, domaines et sous-domaines, ainsi que vos pools d'adresses IP.

### Étape 3 : Ajouter des enregistrements DNS {#step-3-add-dns-records}

Une fois vos adresses IP, domaines, sous-domaines et pools d'adresses IP configurés, nous vous enverrons une liste d'enregistrements DNS. Demandez à vos ingénieurs et développeurs d'ajouter ces enregistrements DNS là où c'est nécessaire, et une fois qu'ils ont été ajoutés, informez-en l'équipe d'onboarding de Braze.

{% multi_lang_include channels/email/dns_records.md %}

Dès que Braze vous fournit vos enregistrements DNS, ajoutez-les dès que votre équipe DNS ou informatique est en mesure de le faire. La vérification de domaine est limitée dans le temps : si les enregistrements sont ajoutés trop tard, la vérification peut échouer même si les enregistrements DNS se résolvent correctement par la suite. Si vos enregistrements DNS semblent corrects mais que la vérification échoue, contactez l'équipe d'onboarding ou d'assistance de Braze pour relancer la vérification.

### Étapes suivantes {#next-steps}

Nous vérifierons votre configuration et validerons toutes les informations dans nos systèmes internes. L'équipe d'onboarding de Braze vous informera lorsque tout sera prêt, ou s'il y a des problèmes avec vos enregistrements DNS que vous devez résoudre avec votre équipe d'ingénierie.

## Méthode 2 : Configuration e-mail en libre-service {#method-2-self-service-email-setup}

Cette méthode permet de configurer un domaine d'envoi, un domaine de suivi et une adresse IP au total pour une société. Si vous prévoyez d'en configurer davantage, veuillez consulter l'équipe d'onboarding de Braze (méthode 1).

{% multi_lang_include alerts/early_access_beta_alert.md feature='This self-service email setup feature' type='beta' %}
<br>Si vous utilisez la fonctionnalité de configuration e-mail en libre-service, assurez-vous de consulter également l'équipe d'onboarding de Braze.

### Conditions préalables {#prerequisites}

Pour utiliser la configuration e-mail en libre-service, vous devez remplir les conditions préalables suivantes :

1. Vous êtes un nouveau client en phase d'onboarding.
2. Vous disposez de l'autorisation au niveau de l'entreprise « Manage Company Settings ».

### Étape 1 : Commencer la configuration {#step-1-begin-setup}

1. Accédez à **Paramètres** > **Paramètres d'administration** sous **Paramètres de l'entreprise**.
2. Ensuite, sélectionnez l'onglet **Vérification de l'expéditeur**. Pour afficher cet onglet, vous devez disposer de l'autorisation au niveau de l'entreprise « Manage Company Settings ».
3. Sélectionnez **Start setup**.

### Étape 2 : Ajouter et vérifier un domaine d'envoi {#step-2-add-and-verify-a-sending-domain}

Un domaine d'envoi est utilisé dans l'adresse « de » lors de l'envoi d'un e-mail. Saisissez un domaine d'envoi et cliquez sur **Envoyer**.

Ensuite, ajoutez les enregistrements TXT et CNAME situés en bas de la page à votre fournisseur DNS. Puis, retournez sur le tableau de bord de Braze et cliquez sur **Verify**.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

Si la vérification échoue et que vous pensez que vos enregistrements DNS sont corrects, contactez l'assistance Braze pour obtenir de l'aide.

{% alert important %}
Le domaine d'envoi doit être un sous-domaine d'un domaine que vous possédez. Par exemple, si vous possédez « example.com », un sous-domaine pourrait être « mail.example.com », ce qui vous permettrait d'utiliser l'adresse d'envoi « @mail.example.com ».
{% endalert %}

### Étape 3 : Ajouter et vérifier un domaine de suivi {#step-3-add-and-verify-a-tracking-domain}

Un domaine de suivi est utilisé pour encapsuler les liens dans vos e-mails à des fins de suivi des clics et de branding. Il sera visible par les utilisateurs lorsqu'ils survolent ou cliquent sur les liens de vos e-mails. Nous recommandons de le faire correspondre à votre domaine d'envoi.

1. Saisissez un domaine de suivi et sélectionnez **Envoyer**.
2. Ensuite, ajoutez les enregistrements CNAME situés en bas de la page à votre fournisseur DNS.
3. Puis, retournez sur le tableau de bord de Braze et sélectionnez **Verify**.

### Étape 4 : Ajouter une adresse IP {#step-4-add-an-ip-address}

Braze génère un enregistrement A pour associer votre adresse IP à votre sous-domaine d'envoi dans une configuration appelée DNS inversé (rDNS). Ajoutez l'enregistrement A dans votre fournisseur DNS, puis cliquez sur **Set up rDNS** pour favoriser la livrabilité.

Notez que les domaines supplémentaires qui ont été ajoutés n'apparaissent pas dans la section **Vérification de l'expéditeur**. Pour ajouter d'autres domaines, contactez l'équipe d'assistance de Braze.

### Pools d'adresses IP avec plusieurs adresses IP dédiées {#ip-pools-with-more-than-one-dedicated-ip}

Lorsqu'un pool d'adresses IP contient plusieurs adresses IP dédiées, Braze et votre fournisseur de services d'e-mailing répartissent les envois volumineux sur ces adresses IP pour optimiser la capacité et la livrabilité. La répartition est approximative : tous les messages d'une campagne n'utilisent pas nécessairement chaque adresse IP, et les envois plus petits peuvent sembler inégalement répartis entre les adresses. SendGrid traite souvent les e-mails par lots (de l'ordre d'environ 1 500 messages par lot), de sorte que le volume ne se divise pas toujours selon un ratio strict un pour un entre les adresses IP. Si vous envoyez régulièrement un volume quotidien très élevé, discutez du dimensionnement de votre pool avec votre contact d'onboarding ou de satisfaction client chez Braze.

### Étapes suivantes

Une fois la vérification de votre expéditeur terminée, nous recommandons le réchauffement d'adresses IP afin que vos messages atteignent les boîtes de réception de destination à un taux élevé et constant. Après avoir terminé cette configuration, assurez-vous de consulter également l'équipe d'onboarding de Braze pour confirmer que vos domaines et votre [adresse IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/) fonctionnent correctement.