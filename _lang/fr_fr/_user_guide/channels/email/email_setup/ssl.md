---
nav_title: SSL chez Braze
article_title: Aperçu SSL
page_order: 5
page_type: reference
description: "Le présent article de référence couvre le SSL, son utilité et la manière dont il est utilisé chez Braze."
channel: email

---

# SSL chez Braze {#ssl-at-braze}

> Le protocole SSL (Secure Socket Layer) chiffre une URL avec HTTPS au lieu de HTTP. HTTPS indique qu'un certificat SSL ou TLS valide et fiable existe et que le site web peut être consulté en toute sécurité.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## Pourquoi le SSL est-il important ? {#why-is-ssl-important}

La plupart des domaines ne nécessitent pas de SSL, mais Braze recommande fortement de l'utiliser pour les raisons suivantes.

La sécurisation de votre site Internet et de vos liens avec SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement des informations sensibles sur leurs clients. Les utilisateurs font davantage confiance aux liens sécurisés avec SSL, et la couche d'authentification supplémentaire permet de protéger vos données.

### Nécessaire pour le suivi des clics et des ouvertures {#necessary-for-click-and-open-tracking}

Braze transforme vos liens en utilisant votre sous-domaine de suivi de liens personnalisé afin de suivre les clics et les ouvertures. Par défaut, ces liens commencent par HTTP. Les utilisateurs disposant de navigateurs ou d'extensions qui restreignent le trafic non sécurisé peuvent rencontrer des difficultés pour passer par la redirection avant l'URL de destination, même si l'URL est sécurisée. Cela peut entraîner des images endommagées et un suivi inexact. Appliquez le protocole SSL au sous-domaine de suivi de liens pour garantir des redirections sécurisées.

## Exigences {#requirements}

### Navigateurs {#browser}

Les principaux navigateurs tels que Google Chrome restreignent le trafic via des URL non sécurisées pour protéger les utilisateurs. L'utilisation du SSL permet de confirmer que le contenu est fiable et minimise les problèmes tels que les liens et images cassés dans les e-mails.

### Domaines HSTS {#hsts-domains}

Si vous disposez d'un domaine HTTP Strict Transport Security (HSTS), configurez le SSL et paramétrez un réseau de diffusion de contenu pour envoyer les certificats de sécurité requis. Sans SSL, les liens vers les images et les pages web ne fonctionneront pas.

## Obtenir un certificat SSL {#acquire-an-ssl-certificate}

Obtenez un certificat SSL auprès d'un tiers, généralement un réseau de diffusion de contenu (CDN). Un CDN héberge le certificat et le présente au navigateur lorsqu'un utilisateur clique sur un lien, en redirigeant le trafic via le CDN pour appliquer les certificats avant de l'envoyer à SendGrid ou SparkPost.

Pour démarrer la configuration SSL, contactez votre gestionnaire de la satisfaction client Braze afin de lancer une configuration complète de l'e-mail Braze.

Une fois que Braze a lancé la configuration, suivez ces étapes :

1. Braze fournira des enregistrements DNS à ajouter à votre registre de domaine.
2. Braze vérifiera si les enregistrements ont été correctement ajoutés à votre registre.
3. Ensuite, sélectionnez un CDN et obtenez des certificats SSL auprès d'un fournisseur tiers.
4. À ce stade, vous configurez votre CDN. Notez que Braze ne peut pas vous aider à résoudre les problèmes de configuration du CDN. Contactez votre fournisseur de CDN pour toute assistance supplémentaire.
5. Contactez votre gestionnaire de la satisfaction client pour activer le SSL.

## Qu'est-ce qu'un CDN et pourquoi en ai-je besoin ? {#what-is-a-cdn-and-why-do-i-need-it}

Un réseau de diffusion de contenu (CDN) est une plateforme de serveurs qui contribue à garantir des temps de chargement rapides du contenu sur différents supports tout en gérant les certificats de sécurité.

{% alert important %}
La configuration du CDN intervient toujours après la validation de vos enregistrements DNS par Braze. Si vous n'avez pas encore lancé cette étape, contactez votre gestionnaire de la satisfaction client pour en savoir plus sur la marche à suivre.
{% endalert %}

Pour le suivi des clics et des ouvertures, les partenaires de distribution transforment les liens à l'aide d'un sous-domaine personnalisé et le CDN applique le certificat SSL à ces liens transformés. Les partenaires doivent souvent présenter des certificats valides au navigateur du destinataire pour que les liens et les images s'affichent correctement. Comme Braze ne demande ni ne gère les certificats, vous devez effectuer cette configuration via un CDN.

{% alert note %}
Si vous ne pouvez pas ou ne souhaitez pas utiliser les CDN répertoriés pour le suivi SSL des clics et des ouvertures, vous pouvez mettre en place une configuration SSL personnalisée. Les CDN alternatifs ou les proxys personnalisés peuvent entraîner une configuration plus complexe. Consultez la documentation de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et de [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Ressources supplémentaires {#additional-resources}

{% alert important %}
Pour la résolution des problèmes de configuration de votre CDN, contactez votre fournisseur de CDN ou consultez la section [Résolution des problèmes]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting) pour des conseils généraux.
{% endalert %}

Consultez les ressources suivantes fournies par les partenaires ESP sur la configuration de certains CDN. Même si votre CDN spécifique n'est pas répertorié, vous devez vous assurer qu'il est capable d'appliquer des certificats SSL.

Lorsque vous configurez le domaine de suivi des clics de votre CDN, activez l'en-tête `X-Forwarded-Host` pour prévenir d'éventuels problèmes de sécurité tels que les attaques par en-tête d'hôte. Consultez la documentation de votre CDN ou votre équipe d'assistance pour connaître les étapes à suivre.

| Partenaire | CDN | Documentation |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Utiliser HTTPS avec CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Premiers pas avec SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Configurer TLS avec des certificats gérés par Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [Comment configurer un SSL personnalisé](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Certificats SSL gérés par Google](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [Comment configurer SSL pour le suivi des clics avec CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Utiliser CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Utiliser Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Utiliser KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Guide étape par étape avec AWS CloudFront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Guide étape par étape avec Cloudflare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Guide étape par étape avec Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Guide étape par étape avec Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Guide étape par étape avec Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ressources supplémentaires" }

### Amazon SES

Si vous utilisez Amazon SES comme ESP, consultez **Option 2: Configuring an HTTPS domain** dans la [documentation d'Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) et spécifiez le domaine de suivi AWS par région en fonction de votre cluster Braze :

- **Clusters Braze US :** `r.us-east-1.awstrack.me`
- **Clusters Braze EU :** `r.eu-central-1.awstrack.me`

{% alert important %}
Lorsque vous configurez le domaine de suivi des clics de votre CDN, activez l'en-tête `X-Forwarded-Host` pour prévenir d'éventuels problèmes de sécurité tels que les attaques par en-tête d'hôte. Consultez votre fournisseur de CDN pour connaître les étapes à suivre.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

Bien que la configuration du CDN, les certificats et les problèmes de proxy doivent être gérés avec votre fournisseur de CDN, utilisez ces conseils pour identifier les problèmes courants liés au suivi SSL des clics. Pour des conseils de résolution des problèmes, consultez la section [Résolution des problèmes]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting).