---
nav_title: SSL chez Braze
article_title: SSL chez Braze
page_order: 5
page_type: reference
description: "Cet article de référence couvre le SSL, son utilité et la manière dont il est utilisé chez Braze."
channel: email
---

# SSL chez Braze {#ssl-at-braze}

> Le protocole SSL (Secure Socket Layer) chiffre une URL avec HTTPS au lieu de HTTP. HTTPS indique qu'un certificat SSL ou TLS valide et fiable existe et que le site web peut être consulté en toute sécurité.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## Pourquoi le SSL est-il important ? {#why-is-ssl-important}

La plupart des domaines ne nécessitent pas le SSL, mais Braze recommande fortement son utilisation pour les raisons suivantes.

Sécuriser votre site web et vos liens avec le SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement d'informations sensibles sur leurs clients. Les utilisateurs font davantage confiance aux liens sécurisés par SSL, et la couche d'authentification supplémentaire contribue à protéger vos données.

### Nécessaire pour le suivi des clics et des ouvertures {#necessary-for-click-and-open-tracking}

Braze transforme vos liens en utilisant votre sous-domaine de suivi de liens de marque pour suivre les clics et les ouvertures. Par défaut, ces liens commencent par HTTP. Les utilisateurs disposant de navigateurs ou d'extensions qui restreignent le trafic non sécurisé peuvent avoir des difficultés à passer par la redirection avant l'URL de destination, même si cette URL est sécurisée. Cela peut entraîner des images cassées et un suivi imprécis. Appliquez le SSL au sous-domaine de suivi des liens pour garantir des redirections sécurisées.

## Prérequis {#requirements}

### Navigateur {#browser}

Les principaux navigateurs tels que Google Chrome restreignent le trafic via des URL non sécurisées afin de protéger les utilisateurs. L'utilisation du SSL permet de confirmer que le contenu est fiable et de minimiser les problèmes tels que les liens et images cassés dans les e-mails.

### Domaines HSTS {#hsts-domains}

Si vous disposez d'un domaine HTTP Strict Transport Security (HSTS), configurez le SSL et paramétrez un CDN pour envoyer les certificats de sécurité requis. Sans SSL, les liens vers les images et les pages web ne fonctionneront pas.

## Obtenir un certificat SSL {#acquire-an-ssl-certificate}

Obtenez un certificat SSL auprès d'un tiers, généralement un réseau de diffusion de contenu (CDN). Un CDN héberge le certificat et le fournit au navigateur lorsqu'un utilisateur clique sur un lien, en redirigeant le trafic à travers le CDN pour appliquer les certificats avant de l'envoyer à Sendgrid ou SparkPost.

Pour démarrer la configuration SSL, contactez votre gestionnaire du succès des clients Braze afin de lancer une configuration complète de l'e-mail Braze.

Une fois que Braze a initié la configuration, suivez les étapes suivantes :

1. Braze fournira des enregistrements DNS à ajouter à votre registre de domaine.
2. Braze vérifiera si les enregistrements ont été correctement ajoutés à votre registre.
3. Ensuite, sélectionnez un CDN et obtenez des certificats SSL auprès d'un fournisseur tiers.
4. À ce stade, configurez votre CDN. Notez que Braze ne peut pas aider à la résolution des problèmes de configuration du CDN. Contactez votre fournisseur de CDN pour toute assistance supplémentaire.
5. Contactez votre gestionnaire du succès des clients pour activer le SSL.

## Qu'est-ce qu'un CDN et pourquoi en ai-je besoin ? {#what-is-a-cdn-and-why-do-i-need-it}

Un réseau de diffusion de contenu (CDN) est une plateforme de serveurs qui contribue à garantir des temps de chargement rapides sur différents supports, tout en gérant les certificats de sécurité.

{% alert important %}
La configuration du CDN intervient toujours après la validation de vos enregistrements DNS par Braze. Si vous n'avez pas encore initié cette étape, contactez votre gestionnaire du succès des clients pour en savoir plus sur la marche à suivre.
{% endalert %}

Pour le suivi des clics et des ouvertures, les partenaires de distribution transforment les liens à l'aide d'un sous-domaine de marque, et le CDN applique le certificat SSL à ces liens transformés. Les partenaires doivent souvent présenter des certificats valides au navigateur du destinataire pour que les liens et les images s'affichent correctement. Étant donné que Braze ne demande ni ne gère de certificats, vous devez configurer cela via un CDN.

{% alert note %}
Si vous ne pouvez pas ou ne souhaitez pas utiliser les CDN répertoriés pour le suivi des clics et des ouvertures via SSL, vous pouvez mettre en place une configuration SSL personnalisée. Les CDN alternatifs ou les proxys personnalisés peuvent engendrer une configuration plus complexe. Consultez la documentation de [Sendgrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et de [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Ressources supplémentaires {#additional-resources}

{% alert important %}
Pour la résolution des problèmes liés à la configuration de votre CDN, contactez votre fournisseur CDN ou consultez la section [Résolution des problèmes]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting) pour des conseils généraux.
{% endalert %}

Consultez les ressources suivantes des partenaires fournisseurs de services d'e-mail marketing or e-mailing sur la configuration de certains CDN. Même si votre CDN spécifique n'est pas listé, vous devez vous assurer qu'il a la capacité d'appliquer des certificats SSL.

Lorsque vous configurez le domaine de suivi des clics de votre CDN, activez l'en-tête `X-Forwarded-Host` pour prévenir d'éventuels problèmes de sécurité tels que les attaques par en-tête d'hôte. Consultez la documentation de votre CDN ou votre équipe de support pour connaître la procédure.

| Partenaire | CDN | Documentation |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Utiliser HTTPS avec CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Premiers pas avec SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Configurer TLS avec des certificats gérés par Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [Comment configurer un SSL personnalisé](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Certificats SSL gérés par Google](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| Sendgrid | AWS CloudFront | [Comment configurer SSL pour le suivi des clics avec CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| Sendgrid | CloudFlare | [Utiliser CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| Sendgrid | Fastly | [Utiliser Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| Sendgrid | KeyCDN | [Utiliser KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Guide étape par étape avec AWS CloudFront](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Guide étape par étape avec Cloudflare](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Guide étape par étape avec Fastly](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Guide étape par étape avec Google Cloud Platform](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Guide étape par étape avec Microsoft Azure](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ressources supplémentaires" }

### Amazon SES

Si vous utilisez Amazon SES comme fournisseur de services d'e-mail marketing or e-mailing, consultez l'**Option 2 : Configurer un domaine HTTPS** dans la [documentation d'Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) et spécifiez le domaine de suivi AWS par région en fonction de votre cluster Braze :

- **Clusters Braze US :** `r.us-east-1.awstrack.me`
- **Clusters Braze EU :** `r.eu-central-1.awstrack.me`

{% alert important %}
Lorsque vous configurez le domaine de suivi des clics de votre CDN, activez l'en-tête `X-Forwarded-Host` pour prévenir d'éventuels problèmes de sécurité tels que les attaques par en-tête d'hôte. Consultez votre fournisseur CDN pour connaître la procédure.
{% endalert %}

## Modèles d'URL de suivi des clics et des ouvertures {#click-and-open-tracking-url-patterns}

Votre fournisseur de services d'e-mail marketing or e-mailing (fournisseur de services d'e-mailing) réécrit chaque lien suivi pour le faire pointer vers votre domaine de suivi des clics, puis ajoute un préfixe de chemin qui identifie la requête comme un clic ou une ouverture suivie. Braze ne construit pas ces chemins. C'est votre fournisseur de services d'e-mailing qui les ajoute lorsqu'il réécrit le lien. Pour les règles CDN ou proxy, les listes d'autorisations de sécurité ou la gestion des liens dans les applications mobiles, consultez la documentation de votre fournisseur de services d'e-mailing comme source de référence.

| fournisseur de services d'e-mailing | Modèles de chemins | Documentation de l'fournisseur de services d'e-mailing |
| --- | --- | --- |
| SendGrid | `/wf/click?upn=...` pour les clics suivis, et `/uni/wf/click?upn=...` pour les liens que vous marquez comme liens universels. Selon votre configuration, les liens personnalisés peuvent aussi utiliser `/ls/click` (signature longue) ou `/ss/` (raccourci). | [Liens universels](https://www.twilio.com/docs/sendgrid/ui/sending-email/universal-links) et [liens raccourcis](https://support.sendgrid.com/hc/en-us/articles/44375837088795-How-to-Know-if-my-Links-Are-Shortened-by-SendGrid) |
| SparkPost | `/f/` pour les clics suivis et `/q/` pour les ouvertures suivies. Les liens qui définissent un chemin personnalisé `data-msys-sublink` suivent le modèle `/f/{custom_path}/`. | [Deep links](https://docs.sparkpost.com/docs/tech-resources/deep-links-self-serve) |
| Amazon SES | `/CL0/{encodedUrl}/{index}/{messageId}/{hmac}` pour les clics suivis. Les liens qui définissent l'attribut `ses:custom-path` suivent le modèle `/CL1/{customPath}/{encodedUrl}/...`. | [Domaines personnalisés pour les ouvertures et les clics](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modèles d'URL de suivi des clics et des ouvertures par fournisseur de services d'e-mailing" }

Par exemple, si votre domaine de suivi des clics est `clicks.example.com` et que votre fournisseur de services d'e-mailing est SparkPost, un clic suivi se résout en une URL commençant par `https://clicks.example.com/f/`.

{% alert important %}
Votre fournisseur de services d'e-mailing est propriétaire de ces préfixes de chemins et peut les modifier ou en ajouter de nouveaux. Braze ne peut donc pas garantir une liste permanente ou exhaustive. Lorsque vos outils de sécurité le permettent, ajoutez l'intégralité de votre domaine de suivi des clics à la liste d'autorisations plutôt que des chemins individuels, et confirmez les modèles actuels dans la documentation de votre fournisseur de services d'e-mailing.
{% endalert %}

Pour gérer ces chemins dans votre application mobile, consultez la section [Liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Résolution des problèmes {#troubleshooting}

Bien que vous deviez gérer la configuration du CDN, les certificats et les problèmes de proxy avec votre CDN, utilisez ces conseils pour identifier les problèmes courants de suivi des clics SSL. Pour obtenir des conseils de résolution des problèmes, consultez [Résolution des problèmes]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting).