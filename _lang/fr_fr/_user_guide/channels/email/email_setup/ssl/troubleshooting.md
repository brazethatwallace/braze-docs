---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de suivi des clics SSL
page_order: 5
page_type: reference
description: "Diagnostiquez les problèmes de suivi des clics SSL et de configuration CDN à l'aide d'un index des symptômes et d'un parcours d'investigation standard."
channel: email
---

# Résolution des problèmes de suivi des clics SSL {#troubleshoot-ssl-click-tracking}

> Utilisez cette page pour identifier les problèmes courants de suivi des clics SSL. Les recommandations ci-dessous sont génériques, car chaque CDN est unique. Pour les problèmes de configuration, de certificats ou de proxy de votre CDN, contactez l'équipe d'assistance de votre fournisseur, car ces configurations sont effectuées en dehors de Braze.

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

| Symptôme | Aller à |
| --- | --- |
| Les taux d'ouverture des e-mails ont chuté soudainement | [Faibles taux d'ouverture des e-mails](#low-email-open-rates) |
| Les liens suivis renvoient HTTP 403 | [HTTP 403 sur les liens de redirection](#http-403-on-redirect-links) |
| Le DNS ou le CNAME pointe vers le fournisseur de services d'e-mailing au lieu du CDN | [Problèmes de registre de domaine](#domain-registry-issues) |
| « La connexion n'est pas privée » ou les liens ne fonctionnent pas pendant la configuration | [Problèmes de CDN](#cdn-issues) |
| La configuration SSL est terminée mais les liens affichent toujours HTTP | [Statut d'activation SSL](#ssl-enablement-status) |
| L'URL suivie échoue mais l'URL non suivie fonctionne | [Problèmes de suivi des clics](#click-tracking-issues) |
| Erreurs d'activation SSL spécifiques à Amazon SES | [Amazon SES](#amazon-ses) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme SSL" }

## Parcours d'investigation standard {#standard-investigation-path}

1. Confirmez que votre sous-domaine de suivi des clics pointe vers votre [réseau de diffusion de contenu (CDN)]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it), et non directement vers votre fournisseur de services d'e-mailing (SendGrid, SparkPost ou Amazon SES). Demandez à votre équipe informatique ou web de vérifier que les paramètres de votre domaine correspondent à votre configuration Braze. Pour les exigences Braze, consultez [Obtenir un certificat SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).
2. Confirmez que votre certificat SSL est actif pour le domaine de suivi. Demandez à votre équipe informatique ou web de confirmer que le certificat est à jour et couvre votre sous-domaine de suivi des clics. Pour les étapes de configuration et les guides spécifiques au CDN, consultez [Obtenir un certificat SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) et [Ressources supplémentaires]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#additional-resources).
3. Envoyez un e-mail de test à l'aide du [modèle de résolution des problèmes de suivi des clics](#click-tracking-issues). Comparez les URL suivies et non suivies.
4. Si les liens suivis échouent avec une erreur 403, vérifiez les règles du CDN et du WAF (agents utilisateurs, chaînes de requête, schémas de redirection).
5. Si la configuration est terminée mais que les liens restent en HTTP, contactez votre gestionnaire du succès des clients Braze pour confirmer que Braze a activé le SSL.
6. En cas de problèmes persistants, coordonnez-vous avec votre CDN ou votre équipe informatique et contactez l'[Assistance Braze]({{site.baseurl}}/braze_support) en fournissant les codes d'erreur et tout détail provenant de votre CDN ou de votre fournisseur de domaine.

## Concepts clés {#key-concepts}

- **Domaine de suivi des clics (CTD) :** Le sous-domaine personnalisé que Braze utilise pour encapsuler les liens à des fins de suivi des clics (par exemple, `clicks.mail.yourbrand.com`).
- **URL suivie :** Encapsule le lien HTTPS d'origine dans votre domaine de suivi. Lorsqu'un utilisateur clique dessus, le domaine de suivi résout la requête et redirige vers la destination finale. Un CDN vous permet de suivre les URL sécurisées (HTTPS). Sans CDN, les utilisateurs peuvent rencontrer une erreur de confidentialité « la connexion n'est pas sécurisée ».
- **URL non suivie :** Conserve l'URL d'origine intacte, en contournant le CDN pour servir d'environnement de contrôle.
- **Routage Phase 1 et Phase 2 :** La Phase 1 fait pointer le CNAME de votre domaine de suivi des clics directement vers votre fournisseur de services d'e-mailing (ESP) pour la vérification HTTP initiale. La Phase 2 fait pointer le CNAME vers votre CDN ou pare-feu d'application web (WAF), qui termine le SSL et transmet les requêtes par proxy à l'ESP avec les en-têtes requis. Pour les destinations CNAME spécifiques à chaque ESP, consultez [Routage ESP Phase 1 et Phase 2](#esp-phase-1-and-phase-2-routing).

## Domaines de suivi des clics et phases DNS {#click-tracking-domains-and-dns-phases}

Le suivi des clics SSL nécessite une configuration DNS en deux phases, car Braze ne provisionne ni ne renouvelle les certificats de sécurité externes en votre nom.

1. **Phase 1 (configuration initiale) :** Le CNAME de votre domaine de suivi des clics pointe directement vers l'endpoint de votre fournisseur de services d'e-mailing pour la vérification HTTP non chiffrée.
2. **Phase 2 (déploiement SSL) :** Vous mettez à jour le CNAME pour qu'il pointe vers votre CDN ou votre WAF edge, qui détient votre certificat SSL personnalisé et transmet les requêtes au fournisseur de services d'e-mailing avec les en-têtes requis. Le fournisseur de services d'e-mailing enregistre le clic et redirige le destinataire vers la destination finale.

{% alert important %}
Braze n'active le suivi des clics SSL qu'une fois la vérification de la Phase 1 terminée. Si le SSL est activé mais que votre DNS pointe toujours vers le fournisseur de services d'e-mailing (Phase 1), les destinataires peuvent voir des [erreurs de non-concordance de nom SSL](#ssl-name-mismatch-errors).
{% endalert %}

## Routage ESP Phase 1 et Phase 2 {#esp-phase-1-and-phase-2-routing}

Lors de la résolution des problèmes d'erreurs de suivi des liens, vérifiez si votre enregistrement DNS pointe vers le réseau ESP non chiffré (Phase 1) ou vers votre CDN (Phase 2).

| ESP | Destination CNAME Phase 1 (directe vers l'ESP) | Destination CNAME Phase 2 | Configuration CDN requise |
| --- | --- | --- | --- |
| Amazon SES | `r.us-east-1.awstrack.me` (US)<br>`r.eu-central-1.awstrack.me` (EU) | Votre endpoint CDN (par exemple, `d123.cloudfront.net`, `ssl.fastly.net` ou Cloudflare) | Activez l'en-tête `X-Forwarded-Host` avec le nom de domaine de suivi des clics |
| SendGrid | `sendgrid.net` | Votre endpoint CDN | Transférez les en-têtes `Host` d'origine (ou les identifiants de suivi personnalisés) vers l'origine sans supprimer les paramètres |
| SparkPost | `spgo.io` | Votre endpoint CDN | Activez `X-Forwarded-Host` et transférez l'en-tête `User-Agent` d'origine intact |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Routage ESP Phase 1 et Phase 2" }

Pour les étapes de configuration du CDN et la documentation des partenaires, consultez [SSL chez Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl).

## Erreurs de non-concordance de nom SSL {#ssl-name-mismatch-errors}

Une non-concordance de nom SSL est un échec d'authentification d'identité lors de la négociation TLS. Elle se produit lorsqu'un navigateur établit une connexion chiffrée mais que le domaine dans la barre d'adresse ne correspond à aucune entrée dans les champs Nom commun (CN) ou Noms alternatifs du sujet (SAN) du certificat.

### Le DNS pointe toujours vers le fournisseur de services d'e-mailing (Phase 1) {#dns-still-points-to-the-esp-phase-1}

Si vous demandez à Braze d'activer le suivi des clics SSL mais que vous laissez votre CNAME DNS pointer directement vers le fournisseur de services d'e-mailing (par exemple, `sendgrid.net` de SendGrid), le navigateur du destinataire ouvre votre domaine de suivi des clics et atteint l'infrastructure du fournisseur. Le fournisseur n'a aucune trace de votre certificat personnalisé et sert son propre certificat de secours (par exemple, `*.sendgrid.net`). La non-concordance de nom fait échouer la connexion et renvoie un avertissement de connexion privée.

### Le certificat ne couvre pas le sous-domaine de suivi (Phase 2) {#certificate-does-not-cover-the-tracking-subdomain-phase-2}

Si votre DNS pointe vers votre CDN (Cloudflare, CloudFront, etc.) mais que votre équipe de sécurité a appliqué un certificat qui ne couvre que les ressources web principales (par exemple, `yourbrand.com` et `www.yourbrand.com`), le sous-domaine spécifique de suivi des clics (par exemple, `clicks.mail.yourbrand.com`) n'est pas inclus. Le CDN sert un certificat qui ne correspond pas au domaine de suivi, et les navigateurs affichent une erreur de confidentialité.

## Flux de travail de triage {#triage-workflow}

### Étape 1 : Effectuer une recherche CNAME faisant autorité {#step-1-run-an-authoritative-cname-lookup}

Ouvrez votre terminal et vérifiez le routage DNS brut pour votre domaine de suivi des clics :

```bash
dig CNAME clicks.mail.yourbrand.com
```

Dans la section `ANSWER SECTION`, examinez vers où le CNAME résout :

| Résultat | Signification | Étape suivante |
| --- | --- | --- |
| Résout vers un endpoint ESP (`sendgrid.net`, `spgo.io` ou `awstrack.me`) | Le DNS est encore en Phase 1 | Mettez à jour votre registre de domaine pour acheminer le trafic via votre CDN. Consultez [Routage ESP Phase 1 et Phase 2](#esp-phase-1-and-phase-2-routing). |
| Résout vers un endpoint de distribution CDN | Le routage DNS Phase 2 est correct | Passez à l'étape 2 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Résultats de la recherche CNAME" }

### Étape 2 : Valider le certificat TLS {#step-2-validate-the-tls-certificate}

Forcez une validation TLS en direct sur votre domaine de suivi des clics pour voir exactement quel certificat les navigateurs reçoivent. Saisissez votre domaine de suivi des clics dans un vérificateur SSL externe, tel que [SSL Checker de SSL Shopper](https://www.sslshopper.com/ssl-checker.html#hostname=clicks.mail.yourbrand.com) (remplacez `clicks.mail.yourbrand.com` par votre domaine).

Confirmez les points suivants :

- Le certificat est valide et n'est pas expiré
- Votre domaine de suivi des clics apparaît dans le Common Name ou les Subject Alternative Names
- La chaîne de certificats est complète, sans avertissement de certificat intermédiaire non approuvé

{% alert tip %}
Pour un rapport TLS plus détaillé, vous pouvez également utiliser le [test de serveur SSL de Qualys SSL Labs](https://www.ssllabs.com/ssltest/).
{% endalert %}

### Étape 3 : Vérifier les problèmes de configuration du CDN {#step-3-review-cdn-configuration-issues}

Si les liens dans les e-mails en direct ne fonctionnent pas pendant la configuration, vérifiez que le DNS n'a pas été pointé vers votre CDN avant que la configuration ne soit terminée. Cela peut se manifester par un lien incorrect ou une erreur de connexion. Contactez votre fournisseur de CDN et consultez sa documentation pour résoudre les problèmes de proxy et de paramètres d'origine. Coordonnez-vous avec l'équipe qui gère votre configuration SSL et CDN pour obtenir une assistance supplémentaire.

## Faibles taux d'ouverture des e-mails {#low-email-open-rates}

**Symptôme :** Les taux d'ouverture des e-mails ont chuté soudainement après des modifications SSL ou CDN.

Si vous constatez soudainement de faibles taux d'ouverture des e-mails, vérifiez que le certificat SSL est à jour. S'il a expiré, vous devez renouveler ce certificat SSL auprès de votre CDN ou de votre fournisseur de certificats.

## HTTP 403 sur les liens de redirection {#http-403-on-redirect-links}

**Symptôme :** Les liens e-mail suivis renvoient « 403 Forbidden ».

Si les liens de redirection suivis renvoient `403 Forbidden`, l'échec se produit souvent au niveau de votre réseau de diffusion de contenu (CDN) ou de votre pare-feu d'application web (WAF) — par exemple, des règles sur AWS WAF ou Amazon CloudFront qui bloquent certains agents utilisateurs, chaînes de requête ou schémas de redirection. Examinez les journaux et les indicateurs des requêtes bloquées avec votre fournisseur de CDN ou de cloud. Pour AWS, consultez [Résolution des problèmes avec CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

Pour déterminer si le problème est spécifique au suivi des clics, désactivez le suivi des clics pour un lien de test (voir [Désactiver le suivi des clics lien par lien]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)). Si l'URL de destination se charge lorsque le suivi des clics est désactivé mais renvoie `403` lorsqu'il est activé, concentrez-vous sur la configuration de votre domaine de suivi des clics, de votre CDN et de votre WAF. Si votre CNAME pointe toujours vers le fournisseur de services d'e-mailing alors que le SSL est activé, vous pouvez rencontrer une [erreur de non-concordance de nom SSL](#ssl-name-mismatch-errors) à la place — commencez par le [flux de triage](#triage-workflow).

## Problèmes de registre de domaine {#domain-registry-issues}

**Symptôme :** Le DNS ou le CNAME de votre sous-domaine de suivi pointe vers votre fournisseur de services d'e-mailing au lieu de votre CDN.

Exécutez une commande dig pour confirmer que le suivi des liens pointe vers le CDN. Dans votre terminal, exécutez `dig CNAME link_tracking_subdomain`. Sous `ANSWER SECTION`, la réponse indique vers où pointe votre CNAME. S'il pointe vers le fournisseur de services d'e-mailing (SendGrid, SparkPost ou Amazon SES) et non vers votre CDN, reconfigurez votre registre de domaine pour pointer vers votre CDN.

## Problèmes de CDN {#cdn-issues}

**Symptôme :** Les utilisateurs voient des erreurs « la connexion n'est pas privée », ou les liens cessent de fonctionner pendant la configuration du CDN.

Si les liens d'e-mails en production cessent de fonctionner pendant la configuration, vous avez probablement dirigé le DNS vers votre CDN avant que la configuration ne soit correctement effectuée. Cela peut se manifester par une erreur de « mauvais lien ». Contactez votre fournisseur de CDN et consultez sa documentation pour résoudre le problème de configuration.

Si vous voyez un message d'erreur indiquant que votre connexion n'est pas privée, cela peut indiquer que votre SSL ou votre CDN n'est pas correctement configuré. Exécutez une commande `dig` dans votre terminal (par exemple, `dig CNAME your_link_tracking_subdomain`). Dans la section `ANSWER SECTION`, si le résultat pointe vers votre fournisseur de services d'e-mailing au lieu de votre CDN, le problème est une mauvaise configuration. Pour que le suivi des clics SSL de Braze fonctionne, le CNAME doit pointer vers votre CDN. Coordonnez-vous avec l'équipe qui gère votre configuration SSL et CDN pour obtenir de l'aide.

## Statut d'activation SSL {#ssl-enablement-status}

**Symptôme :** La configuration SSL est terminée, mais les liens suivis apparaissent toujours en HTTP.

Si vous avez terminé la configuration SSL et que les liens apparaissent toujours en HTTP, contactez votre gestionnaire du succès des clients Braze pour confirmer que Braze a activé le SSL. Braze n'active le SSL qu'une fois toutes les étapes de configuration terminées.

### Amazon SES {#amazon-ses}

Si vous utilisez Amazon SES comme fournisseur de services d'e-mailing, les problèmes de configuration suivants peuvent empêcher Braze d'activer le SSL ou provoquer des erreurs pendant la configuration :

- **Incompatibilité de région :** Vérifiez que l'origine de votre CDN pointe vers le domaine de suivi AWS correspondant à votre cluster Braze. Les clusters US utilisent `r.us-east-1.awstrack.me`. Les clusters EU utilisent `r.eu-central-1.awstrack.me`. L'utilisation de la mauvaise région peut bloquer l'activation du SSL.
- **En-tête host :** Amazon SES exige que votre CDN transmette le bon en-tête host. Activez l'en-tête `X-Forwarded-Host` sur votre domaine de suivi des clics. Pour les exigences de routage Phase 1 et Phase 2, consultez la section [Routage ESP Phase 1 et Phase 2](#esp-phase-1-and-phase-2-routing).
- **Configuration du proxy :** Une configuration de proxy ou de CDN qui remplace ou entre en conflit avec l'en-tête host peut entraîner l'échec de l'activation du SSL. Vérifiez les paramètres du proxy avec votre fournisseur de CDN pour confirmer qu'ils n'interfèrent pas avec la transmission de l'en-tête host.
- **Enregistrement alias Route 53 :** Si vous utilisez Route 53 pour gérer le DNS de votre domaine, créez un [enregistrement alias dans Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) qui pointe vers votre distribution CDN (par exemple, `d111111abcdef8.cloudfront.net`). L'utilisation d'un CNAME standard au lieu d'un enregistrement alias peut renvoyer des erreurs HTTP 400.
- **Transmission d'en-têtes désactivée :** Si l'activation du SSL échoue toujours après avoir configuré `X-Forwarded-Host`, essayez de désactiver la transmission d'en-têtes sur votre CDN ou votre proxy. Certaines configurations résolvent le problème lorsque la transmission est entièrement désactivée. Travaillez avec votre équipe informatique ou votre fournisseur de CDN pour tester cette configuration.

## Problèmes de suivi des clics {#click-tracking-issues}

**Symptôme :** Les liens d'e-mail suivis échouent alors que les liens non suivis fonctionnent, ou les utilisateurs voient des erreurs de certificat ou de DNS après avoir cliqué.

Les problèmes courants de redirection résultent généralement d'une mauvaise configuration entre le CDN hébergeant le domaine de suivi et ses certificats SSL associés ou ses enregistrements DNS CNAME. Ces mauvaises configurations entraînent souvent une erreur de confidentialité « la connexion n'est pas sécurisée » ou un échec `404` après avoir cliqué sur un lien d'e-mail suivi.

### Exigences de formatage des liens HTML {#html-link-formatting-requirements}

Pour que le suivi des clics fonctionne, votre fournisseur de services d'e-mailing (SendGrid, SparkPost ou Amazon SES) doit trouver et remplacer les liens dans votre HTML. Quel que soit le fournisseur, les liens doivent respecter ces exigences de formatage :

- Les liens doivent se trouver dans une balise HTML `<a>` avec un attribut `href`.
- L'URL doit commencer par `http://` ou `https://`.

Règles supplémentaires spécifiques aux fournisseurs :

- **SendGrid :** Entourez l'URL de guillemets simples ou doubles, et n'incluez pas d'espaces autour du `=` dans l'attribut `href`.
- **Amazon SES :** Les URL doivent être conformes à la [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). Les espaces non encodés dans une URL empêchent Amazon SES de suivre le lien.

Pour en savoir plus sur les schémas d'URL pris en charge par le suivi des clics Braze, consultez [Exigences relatives aux liens de suivi des clics]({{site.baseurl}}/user_guide/channels/email/email_setup/open_pixel_and_click_tracking#click-tracking-link-requirements). Pour les détails HTML spécifiques aux fournisseurs, consultez [Bonnes pratiques HTML pour le suivi des clics SendGrid](https://www.twilio.com/docs/sendgrid/ui/analytics-and-reporting/click-tracking-html-best-practices), [Langage de modèle SparkPost](https://developers.sparkpost.com/api/template-language/) et [FAQ sur les indicateurs d'envoi d'e-mails Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/faqs-metrics.html).

Exemples valides :

```html
<a href="http://www.example.com">Link</a>
<a href='https://example.com'>Link</a>
<a target="_blank" href="https://example.com">Link</a>
```

Les exemples suivants omettent `http://` ou `https://` et ne sont pas suivis :

```html
<a href="example.com">Link</a>
<a href="www.example.com">Link</a>
```

Si vous utilisez SendGrid, les exemples suivants ne sont pas non plus suivis :

```html
<a href= http://www.example.com>Link</a>
<a href = "https://example.com">Link</a>
```

{% alert note %}
Bien qu'un sous-domaine `www` soit facultatif, `http://` ou `https://` est requis pour que le suivi des clics fonctionne correctement.
{% endalert %}

### Tester le suivi des clics {#testing-click-tracking}

Après avoir complété le [parcours de triage](#triage-workflow), utilisez le modèle suivant pour tester la configuration du CDN de votre domaine de suivi, qui est le mécanisme prenant en charge l'analyse des liens dans vos e-mails.

1. Copiez et collez le modèle suivant dans une Campaign d'e-mail HTML Braze.

{% details Modèle de résolution des problèmes de suivi des clics %}
{% raw %}
```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Click Tracking Test</title>
    <style>
        /* Base Dark Mode (Default) */
        body {
            margin: 0;
            padding: 0;
            background-color: #2b0562;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            color: #ffd1e9;
        }

        .email-container {
            width: 100%;
            max-width: 600px;
            margin: 40px auto;
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid #F3697F;
            border-radius: 16px;
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #E83F21 0%, #F3697F 100%);
            padding: 40px 20px 50px 20px;
            text-align: center;
        }

        .logo {
            display: block;
            margin: 0 auto 25px auto;
            border: 0;
            outline: none;
            text-decoration: none;
        }

        .header h1 {
            color: #ffffff;
            margin: 0;
            font-size: 26px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        .content {
            padding: 40px 40px 20px 40px;
            line-height: 1.8;
            font-size: 15px;
        }

        .troubleshoot {
            margin: 0 40px 40px 40px;
            padding: 25px;
            background-color: rgba(253, 167, 216, 0.1);
            border-radius: 12px;
            font-size: 14px;
            border: 1px dashed #F3697F;
        }

        .troubleshoot h2 {
            margin-top: 0;
            font-size: 18px;
            color: #ffffff;
        }

        .btn-section {
            padding: 0 40px 40px 40px;
            text-align: center;
        }

        .btn {
            display: inline-block;
            padding: 16px 32px;
            border-radius: 12px;
            font-weight: 700;
            text-decoration: none;
            margin: 10px;
            font-size: 14px;
        }

        .btn-tracked {
            background-color: #F3697F;
            color: #ffffff;
        }

        .btn-untracked {
            border: 2px solid #FDA7D8;
            color: #FDA7D8;
            background-color: transparent;
        }

        .footer {
            text-align: center;
            font-size: 12px;
            color: #FDA7D8;
            padding-bottom: 40px;
            opacity: 0.6;
        }

        /* Light Mode Overrides */
        @media (prefers-color-scheme: light) {
            body { background-color: #F7FCFF !important; color: #2b0562 !important; }
            .email-container { background-color: #ffffff !important; border: 1px solid #FDA7D8 !important; box-shadow: 0 4px 20px rgba(43, 5, 98, 0.1); }
            .content { color: #2b0562 !important; }
            .troubleshoot { background-color: #F7FCFF !important; border-color: #F3697F !important; color: #2b0562 !important; }
            .troubleshoot h2 { color: #E83F21 !important; }
            .btn-untracked { color: #F3697F !important; border-color: #F3697F !important; }
            .footer { color: #2b0562 !important; }
            strong { color: #E83F21 !important; }
        }

        /* Mobile Optimization */
        @media only screen and (max-width: 480px) {
            .btn { display: block !important; margin: 10px 0 !important; width: auto !important; }
            .content, .troubleshoot { padding: 25px !important; }
        }
    </style>
</head>
{%- capture url -%}https://example.com{%- endcapture -%}
<body>
    <center>
        <table class="email-container" role="presentation" width="600" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td class="header">
                    <img src="https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137"
                         width="150"
                         alt="Logo"
                         class="logo">
                    <h1>Testing Click Tracking Functionality</h1>
                </td>
            </tr>
            <tr>
                <td class="content">
                    <p>
                        Use this template to test the <strong>CDN configuration</strong> of your tracking domain—the mechanism supporting analytics for links within your emails.
                    </p>
                    <p>
                        A <strong>Tracked URL</strong> wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs; without it, users may encounter a "connection is not secure" privacy error. An <strong>Untracked URL</strong> maintains the original URL intact, bypassing the CDN to serve as a control environment.
                    </p>
                    <p>
                        Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and the <strong>associated SSL certificate or DNS CNAME records.</strong>
                    </p>
                    <p>
                        <i style="font-size: 13px;">This template uses "example.com" as the destination URL. To test your own domain, replace the URL in the <strong>capture</strong> tag located on line 125.</i>
                    </p>
                </td>
            </tr>
            <tr>
                <td class="btn-section">
                    <a href="{{url}}" class="btn btn-tracked">Tracked URL</a>

                    <a href="{{url}}"
                       class="btn btn-untracked"
                       clicktracking="off"
                       data-msys-clicktrack="0"
                       ses:no-track="true">
                       Untracked URL
                    </a>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="troubleshoot">
                        <h2>Troubleshooting the Test</h2>
                        <ul>
                            <li><strong>Tracked URL Fails / Untracked Works:</strong> This indicates a CDN or SSL certificate issue. Verify that your SSL certificate is valid and correctly bound to your tracking domain.</li>
                            <li><strong>Privacy Error (HTTPS):</strong> Ensure your CDN is configured to handle port 443 traffic and that the certificate matches your tracking CNAME.</li>
                            <li><strong>Both URLs Fail:</strong> Check the destination URL or your internal network firewall settings.</li>
                            <li>For more information, visit: <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/channels/email/email_setup/ssl">SSL at Braze</a></li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table>
        <div class="footer">
            Braze :: 63 Madison Avenue, 13th Floor :: New York, NY 10016
        </div>
    </center>
</body>
</html>
```
{% endraw %}
{% enddetails %}

{: start="2"}
2. Configurez votre URL. Remplacez l'URL dans la balise `capture` en haut du corps du modèle (là où `https://example.com` est défini). Par exemple, remplacez `https://example.com` par `https://braze.com/docs`.
3. Envoyez-vous un e-mail de test et sélectionnez les deux boutons.
4. Vérifiez que le comportement attendu et les critères de réussite correspondent à ce qui est décrit dans le modèle.

Si votre URL non suivie fonctionne mais que votre URL suivie échoue, il se peut qu'il y ait un problème de configuration. Consultez la documentation de votre fournisseur de services d'e-mailing et de votre CDN. Pour connaître les exigences détaillées en matière de provisionnement de certificats, consultez [SSL chez Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl).

Utilisez le tableau suivant pour diagnostiquer les erreurs courantes lors du test du suivi des clics.

| Code d'erreur | Résolution des problèmes |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Complétez le [parcours de triage](#triage-workflow) et consultez [Erreurs de non-concordance de nom SSL](#ssl-name-mismatch-errors). Vérifiez que votre domaine de suivi des clics figure dans le Common Name ou les Subject Alternative Names du certificat. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Vérifiez vos paramètres DNS. Assurez-vous que votre sous-domaine de suivi est configuré conformément aux recommandations de votre CDN et de votre fournisseur de services d'e-mailing. |
| `525 / 526 SSL Error` | Vérifiez que le paramètre SSL de votre CDN (comme Cloudflare) correspond aux capacités de votre origine. |
| `404 Not Found` | Vérifiez que votre CDN est configuré pour transmettre l'intégralité du chemin de l'URL au fournisseur de services d'e-mailing, plutôt que de pointer vers un répertoire racine vide. |
| `400 Bad Request: Request Header or Cookie Too Large` | Cette erreur se produit généralement lorsque le domaine de suivi des clics hérite d'un trop grand nombre de cookies volumineux provenant du domaine de votre site web. Braze ne définit ni ne bloque aucun cookie sur le domaine de suivi. Configurez votre CDN pour ne pas envoyer ces cookies au fournisseur de services d'e-mailing lors du reverse-proxy de la requête de suivi des clics. Vous devrez peut-être également augmenter le paramètre `large_client_header_buffers` dans votre configuration nginx (par exemple, `large_client_header_buffers 4 32k;` pour autoriser des en-têtes jusqu'à 32&nbsp;Ko). Pour plus d'informations, consultez votre fournisseur de CDN ou votre équipe d'ingénierie web. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Codes d'erreur et résolution des problèmes" }