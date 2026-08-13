---
nav_title: Comprendre les enregistrements DNS
article_title: Comprendre les enregistrements DNS
page_order: 2
page_type: reference
description: "Cet article de référence explique le fonctionnement des enregistrements DNS pour les différents fournisseurs de services d'e-mailing de Braze, notamment SPF, DKIM, DMARC et les structures d'enregistrements spécifiques à chaque fournisseur."
channel: email
---

# Comprendre les enregistrements DNS {#understanding-dns-records}

> Cet article de référence explique le fonctionnement des enregistrements DNS au sein de Braze pour les trois principaux fournisseurs de services d'e-mailing (ESP) : SparkPost, SendGrid et Amazon Simple Email Service (SES). Une configuration DNS correcte est essentielle pour l'authentification des e-mails (SPF, DKIM, DMARC) et la cohérence de marque, et elle a un impact direct sur la livrabilité.

Pour en savoir plus, consultez [Authentification des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).

## Principes fondamentaux de l'authentification des e-mails {#core-email-authentication-fundamentals}

Avant d'examiner les structures propres à chaque fournisseur, il est important de comprendre le rôle de ces enregistrements et la manière dont Braze les utilise pour assurer un alignement correct.

### Sender Policy Framework (SPF) {#spf}

SPF est un enregistrement DNS sur un domaine qui spécifie quelles adresses IP sont autorisées à envoyer des e-mails au nom de ce domaine.

Braze ne vous demande pas de modifier ou d'ajouter des enregistrements SPF sur votre domaine racine d'entreprise (comme `example.com`). Au lieu de cela, Braze isole la distribution en utilisant un domaine Return-Path dédié et personnalisé (également appelé domaine de rebond, domaine MAIL FROM ou domaine d'enveloppe From), tel que `bounce.mail.example.com`.

Étant donné que les fournisseurs de boîtes de réception valident le SPF par rapport à ce domaine Return-Path plutôt que par rapport au domaine visible dans l'en-tête `From:`, la configuration SPF se situe entièrement au niveau du sous-domaine. Selon l'ESP sous-jacent, Braze gère cette validation de deux manières :

- Délégation CNAME (SendGrid et SparkPost) : créez un `CNAME` pointant votre sous-domaine vers l'ESP. L'ESP héberge et met à jour les politiques SPF sur son infrastructure, validant automatiquement la vérification SPF.
- Enregistrement TXT explicite (Amazon SES) : publiez un enregistrement `TXT` codé en dur directement sur le sous-domaine de rebond contenant une chaîne d'autorisation explicite (par exemple, `v=spf1 include:amazonses.com ~all`), donnant à AWS la permission d'envoyer des e-mails depuis cette zone.

### Domain Keys Identified Mail (DKIM) {#dkim}

DKIM ajoute une signature numérique cryptographique à l'en-tête de l'e-mail. Le serveur de réception utilise la clé publique de l'expéditeur (publiée dans le DNS) pour vérifier que l'e-mail provient bien du propriétaire du domaine et n'a pas été altéré en transit.

Braze exige que les clés publiques DKIM soient publiées via des enregistrements `TXT` ou `CNAME` afin que les fournisseurs de services Internet puissent valider les signatures cryptographiques générées par votre ESP.

### Alignement DMARC {#dmarc}

Pour qu'un e-mail passe la vérification DMARC, le domaine dans l'en-tête `From:` visible par l'utilisateur doit correspondre (s'aligner) avec le domaine validé par SPF (le Return-Path) ou DKIM. Comme les configurations Braze assurent l'alignement à la fois par SPF et DKIM, vos politiques DMARC sont correctement satisfaites.

Braze gère l'authentification SPF et DKIM de base par défaut, mais vous devez tout de même ajouter un enregistrement DMARC à votre domaine d'envoi. DMARC est un outil d'authentification essentiel exigé par la quasi-totalité des principaux fournisseurs de boîtes de réception. Il prouve la légitimité de vos e-mails, renforce la réputation de votre domaine et maintient une bonne livrabilité dans le temps.

Comme cela nécessite un accès au registre de domaine de votre entreprise, vous ou votre administrateur réseau devez ajouter cet enregistrement au niveau de votre domaine racine. Si vous débutez, une politique de base comme `p=none` satisfait les exigences minimales des fournisseurs de boîtes de réception. Pour en savoir plus sur DMARC, consultez [DMARC.org](https://dmarc.org/). Pour des conseils spécifiques à Braze concernant DMARC, consultez [Authentification des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc).

## Architecture DNS spécifique à chaque ESP {#esp-specific-dns-architecture}

Les différentes architectures ESP gèrent la délégation DNS de manière différente. Lors du provisionnement de votre environnement, utilisez les enregistrements exacts correspondant à votre cluster ESP spécifique.

### Architecture SparkPost {#sparkpost-architecture}

SparkPost utilise une configuration hybride. Il utilise des enregistrements `CNAME` explicites pour pointer l'infrastructure de suivi et de Return-Path vers SparkPost, tout en utilisant un enregistrement `TXT` brut pour l'authentification DKIM.

- Configuration SPF et Return-Path : SparkPost demande un sous-domaine dédié aux rebonds (par exemple, `mail.example.com`). Un enregistrement `CNAME` pointe ce sous-domaine vers les processeurs de rebonds entrants de SparkPost. Cela achemine correctement le trafic de rebonds et valide automatiquement le SPF, car le serveur de destination de SparkPost gère le protocole.
- Configuration DKIM : SparkPost nécessite un enregistrement `TXT` contenant la chaîne de clé publique exacte associée à un sélecteur spécifique.
- Suivi des clics et des ouvertures : configurez un sous-domaine de suivi avec un `CNAME` pointant vers les endpoints de suivi SparkPost (ou un proxy CDN si le suivi SSL est demandé).

#### Exemple de table DNS SparkPost {#example-sparkpost-dns-table}

Le tableau suivant présente des exemples d'enregistrements DNS pour une configuration SparkPost.

| Type d'enregistrement | Hôte/Nom | Valeur/Cible | Objectif |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Return-Path / alignement SPF |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | Authentification cryptographique DKIM |
| CNAME | click.mail.example.com | spgo.io (ou endpoint CDN) | Suivi des clics et des ouvertures |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemple de table DNS SparkPost" }

### Architecture SendGrid {#sendgrid-architecture}

SendGrid s'appuie sur une infrastructure automatisée appelée Domain Authentication. Au lieu de fournir des clés `TXT` brutes, SendGrid fournit une série d'enregistrements `CNAME` qui pointent directement vers les serveurs gérés par SendGrid.

- Configuration SPF et Return-Path : SendGrid utilise un `CNAME` spécifique (souvent préfixé par `em`) qui associe votre sous-domaine d'envoi à `uXXXXXX.wl.sendgrid.net`. SendGrid héberge et met à jour dynamiquement l'enregistrement SPF sur cet endpoint.
- Configuration DKIM : SendGrid génère deux enregistrements `CNAME` distincts pour DKIM (utilisant souvent des sélecteurs comme `s1` et `s2`). Ceux-ci pointent vers les clés de SendGrid.
- SendGrid fournit deux enregistrements `CNAME` DKIM afin de pouvoir effectuer une rotation automatique des clés cryptographiques sans que vous ayez à mettre à jour manuellement votre DNS.

#### Exemple de table DNS SendGrid {#example-sendgrid-dns-table}

Le tableau suivant présente des exemples d'enregistrements DNS pour une configuration SendGrid.

| Type d'enregistrement | Hôte/Nom | Valeur/Cible | Objectif |
| --- | --- | --- | --- |
| CNAME | em.mail.example.com | u123456.wl.sendgrid.net | Return-Path / SPF dynamique |
| CNAME | s1._domainkey.mail.example.com | s1.domainkey.u123456.wl.sendgrid.net | Clé DKIM primaire (rotation) |
| CNAME | s2._domainkey.mail.example.com | s2.domainkey.u123456.wl.sendgrid.net | Clé DKIM secondaire (rotation) |
| CNAME | email.mail.example.com | sendgrid.net (ou endpoint CDN) | Suivi des clics et des ouvertures |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemple de table DNS SendGrid" }

### Architecture Amazon SES {#amazon-ses-architecture}

Amazon SES utilise Easy DKIM avec des enregistrements `CNAME` ainsi qu'un routage explicite par `MX` et `TXT` pour le suivi personnalisé des rebonds.

- Configuration DKIM : Amazon SES utilise Easy DKIM, fournissant trois enregistrements `CNAME`. Ceux-ci pointent vers des sous-domaines gérés par AWS contenant les clés publiques. SES effectue automatiquement la rotation de ces clés de manière transparente pour maintenir la conformité en matière de sécurité.
- Configuration SPF et MAIL FROM personnalisé : SendGrid et SparkPost gèrent le routage du domaine de rebond via un `CNAME`. Amazon SES nécessite un enregistrement `MX` explicite et un enregistrement `TXT` placés directement sur le sous-domaine MAIL FROM désigné. L'enregistrement `MX` garantit que les notifications de rebond sont renvoyées vers les serveurs d'Amazon, et l'enregistrement `TXT` contient la chaîne SPF autorisée codée en dur.

Pour en savoir plus, consultez [Configuration d'Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).

#### Exemple de table DNS Amazon SES {#example-amazon-ses-dns-table}

Le tableau suivant présente des exemples d'enregistrements DNS pour une configuration Amazon SES.

| Type d'enregistrement | Hôte/Nom | Valeur/Cible | Objectif |
| --- | --- | --- | --- |
| CNAME | sel1._domainkey.mail.example.com | sel1.dkim.amazonses.com | Clé Easy DKIM 1 (rotation) |
| CNAME | sel2._domainkey.mail.example.com | sel2.dkim.amazonses.com | Clé Easy DKIM 2 (rotation) |
| CNAME | sel3._domainkey.mail.example.com | sel3.dkim.amazonses.com | Clé Easy DKIM 3 (rotation) |
| MX | bounce.mail.example.com | 10 feedback-smtp.us-east-1.amazonses.com | Achemine le traitement des rebonds vers AWS |
| TXT | bounce.mail.example.com | v=spf1 include:amazonses.com ~all | Autorisation SPF explicite |
| CNAME | track.mail.example.com | r.us-east-1.awstrack.me (ou CDN) | Suivi des clics et des ouvertures |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemple de table DNS Amazon SES" }

## Considérations DNS avancées {#advanced-dns-considerations}

### Découpage des chaînes d'enregistrements TXT DKIM {#txt-dkim-record-string-splitting}

Lors du déploiement de SparkPost ou de configurations DKIM manuelles, vous pouvez rencontrer de longues clés cryptographiques (clés DKIM de 2048 bits).

La spécification DNS de base (RFC 1035) limite toute chaîne de caractères unique au sein d'un enregistrement `TXT` à un maximum de 255 caractères. Une clé publique de 2048 bits dépasse régulièrement 400 caractères, ce qui amène les registres de domaine à rejeter la chaîne unique ou à la tronquer, invalidant ainsi la signature.

Le découpage de chaîne résout ce problème. Divisez la chaîne de caractères en segments de moins de 255 caractères. Encadrez chaque segment de guillemets droits, séparés par un espace, au sein du même enregistrement `TXT`.

{% alert note %}
Lorsque vous utilisez des fournisseurs DNS comme Cloudflare ou AWS Route 53, ces interfaces gèrent automatiquement le découpage lorsque vous collez une longue chaîne. Les systèmes plus anciens (comme GoDaddy ou Network Solutions) nécessitent un formatage manuel du découpage en utilisant la technique des guillemets doubles.
{% endalert %}

### Utiliser des sous-domaines dédiés {#dedicated-subdomains}

Une erreur courante lors de l'onboarding consiste à demander l'utilisation d'un domaine organisationnel de premier niveau (comme `example.com`) directement dans Braze comme domaine d'envoi. Braze exige l'utilisation d'un sous-domaine dédié (par exemple, `mail.example.com` ou `engage.example.com`).

L'utilisation du domaine parent peut perturber l'infrastructure de l'entreprise de plusieurs manières :

#### Conflits d'enregistrements MX {#mx-record-conflicts}

Un domaine ne peut prendre en charge qu'un seul jeu d'enregistrements `MX` de routage principal. Si vous associez votre domaine parent (`example.com`) à l'infrastructure ESP de Braze, les enregistrements `MX` personnalisés requis pour les rebonds écrasent vos enregistrements d'e-mail d'entreprise. Cela peut perturber les plateformes de messagerie interne comme Google Workspace ou Microsoft 365.

#### Surcharge des includes SPF et limite de 10 résolutions {#spf-include-bloat-and-the-10-lookup-limit}

La spécification SPF (RFC 7208) limite les serveurs de réception à un maximum de 10 résolutions DNS lors de la validation d'un enregistrement SPF.

- Si un domaine parent ajoute les mécanismes ESP de Braze (`include:sparkpostmail.com` ou `include:amazonses.com`), cela pèse fortement sur cette limite.
- Si la limite est dépassée, cela déclenche une erreur SPF PermError permanente, entraînant l'échec de l'authentification de tous les e-mails de l'entreprise.

#### Isolation de la réputation des IP et du domaine {#ip-and-domain-reputation-isolation}

Si les campagnes marketing, les reçus transactionnels et les e-mails internes des employés partagent un espace de domaine racine identique, un pic soudain de plaintes pour spam liées au marketing peut endommager la réputation du domaine parent. Cela risque de diriger les communications critiques de l'entreprise vers les dossiers de spam. L'utilisation d'un sous-domaine distinct isole la réputation de vos envois marketing.

## Workflow de déploiement {#implementation-workflow}

Pour garantir un transfert et un déploiement fluides, suivez cette séquence :

1. Fournissez les enregistrements structurés à votre administrateur informatique ou réseau pour les ajouter à votre plateforme d'hébergement (Cloudflare, Route 53, etc.).
2. Définissez une valeur de durée de vie (TTL) basse (par exemple, 300 secondes ou cinq minutes) pour les tests initiaux. Cela permet une récupération rapide en cas de faute de frappe lors de la saisie.
3. Exécutez une résolution DNS (par exemple, `dig CNAME mail.example.com`) ou utilisez un outil de validation pour confirmer que les enregistrements se résolvent correctement avant de passer à la phase de préchauffage.

## Documentation des fournisseurs DNS {#dns-provider-documentation}

Chaque fournisseur DNS possède une interface unique. Partagez ces spécifications avec votre administrateur réseau ou consultez la documentation de votre fournisseur spécifique pour mapper correctement les entrées dans votre fichier de zone.

Le tableau suivant répertorie la documentation officielle des fournisseurs DNS les plus couramment utilisés.

| Fournisseur DNS | Ressources |
| --- | --- |
| Cloudflare | [Gérer les enregistrements DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [Créer des jeux d'enregistrements de ressources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [Gérer les enregistrements DNS](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [Configurer les enregistrements DNS pour un nom de domaine](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [Gérer les enregistrements DNS à l'aide du portail Azure](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Documentation des fournisseurs DNS" }

Pour des ressources supplémentaires sur les fournisseurs de domaines, consultez [Configurer les IP et les domaines]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-3-add-dns-records).