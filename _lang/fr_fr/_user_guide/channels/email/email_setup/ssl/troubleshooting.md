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
| Les liens suivis renvoient une erreur HTTP 403 | [HTTP 403 sur les liens de redirection](#http-403-on-redirect-links) |
| Le DNS ou le CNAME pointe vers le fournisseur de services d'e-mailing au lieu du CDN | [Problèmes de registre de domaine](#domain-registry-issues) |
| « La connexion n'est pas privée » ou les liens ne fonctionnent pas pendant la configuration | [Problèmes de CDN](#cdn-issues) |
| La configuration SSL est terminée mais les liens affichent toujours HTTP | [Statut d'activation SSL](#ssl-enablement-status) |
| L'URL suivie échoue mais l'URL non suivie fonctionne | [Problèmes de suivi des clics](#click-tracking-issues) |
| Erreurs d'activation SSL spécifiques à Amazon SES | [Amazon SES](#amazon-ses) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme SSL" }

## Parcours d'investigation standard {#standard-investigation-path}

1. Confirmez que votre sous-domaine de suivi des clics pointe vers votre [réseau de diffusion de contenu (CDN)]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it), et non directement vers votre fournisseur de services d'e-mailing (SendGrid, SparkPost ou Amazon SES). Demandez à votre équipe informatique ou web de vérifier que les paramètres de votre domaine correspondent à votre configuration Braze. Pour les exigences Braze, consultez [Obtenir un certificat SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).
2. Confirmez que votre certificat SSL est actif pour le domaine de suivi. Demandez à votre équipe informatique ou web de confirmer que le certificat est à jour et couvre votre sous-domaine de suivi des clics. Pour les étapes de configuration et les guides spécifiques aux CDN, consultez [Obtenir un certificat SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) et [Ressources supplémentaires]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#additional-resources).
3. Envoyez un e-mail de test à l'aide du [modèle de résolution des problèmes de suivi des clics](#click-tracking-issues). Comparez les URL suivies et non suivies.
4. Si les liens suivis échouent avec une erreur 403, vérifiez les règles du CDN et du WAF (agents utilisateurs, chaînes de requête, schémas de redirection).
5. Si la configuration est terminée mais que les liens restent en HTTP, contactez votre gestionnaire du succès des clients Braze pour confirmer que Braze a activé le SSL.
6. Pour les problèmes persistants, coordonnez-vous avec votre CDN ou votre équipe informatique et contactez l'[Assistance Braze]({{site.baseurl}}/braze_support) en fournissant les codes d'erreur et tout détail provenant de votre CDN ou de votre fournisseur de domaine.

## Concepts clés {#key-concepts}

- **URL suivie :** Encapsule le lien HTTPS d'origine dans votre domaine de suivi. Lorsqu'un utilisateur clique dessus, le domaine de suivi résout la requête et redirige vers la destination finale. Un CDN vous permet de suivre les URL sécurisées (HTTPS). Sans celui-ci, les utilisateurs peuvent rencontrer une erreur de confidentialité « la connexion n'est pas sécurisée ».
- **URL non suivie :** Conserve l'URL d'origine intacte, en contournant le CDN pour servir d'environnement de contrôle.

## Faibles taux d'ouverture des e-mails {#low-email-open-rates}

**Symptôme :** Les taux d'ouverture des e-mails ont chuté soudainement après des modifications SSL ou CDN.

Si vous constatez soudainement de faibles taux d'ouverture des e-mails, vérifiez que le certificat SSL est à jour. S'il a expiré, vous devez renouveler ce certificat SSL auprès de votre CDN ou de votre fournisseur de certificats.

## HTTP 403 sur les liens de redirection {#http-403-on-redirect-links}

**Symptôme :** Les liens e-mail suivis renvoient « 403 Forbidden ».

Si les liens de redirection suivis renvoient « 403 Forbidden », l'échec se produit souvent au niveau de votre réseau de diffusion de contenu (CDN) ou de votre pare-feu d'application web (WAF) — par exemple, des règles sur AWS WAF ou Amazon CloudFront qui bloquent certains agents utilisateurs, chaînes de requête ou schémas de redirection. Examinez les journaux et les indicateurs des requêtes bloquées avec votre fournisseur de CDN ou de cloud. Pour AWS, consultez [Résolution des problèmes avec CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

Pour déterminer si le problème est spécifique au suivi des clics, désactivez le suivi des clics pour un lien de test (voir [Désactiver le suivi des clics lien par lien]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)). Si l'URL de destination se charge lorsque le suivi des clics est désactivé mais renvoie 403 lorsqu'il est activé, concentrez-vous sur la configuration de votre domaine de suivi des clics, de votre CDN et de votre WAF.

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
- **En-tête host :** Amazon SES exige que votre CDN transmette le bon en-tête host. Activez l'en-tête `X-Forwarded-Host` sur votre domaine de suivi des clics. Pour plus d'informations, consultez la section [Amazon SES](#amazon-ses).
- **Configuration du proxy :** Une configuration de proxy ou de CDN qui remplace ou entre en conflit avec l'en-tête host peut entraîner l'échec de l'activation du SSL. Vérifiez les paramètres du proxy avec votre fournisseur de CDN pour confirmer qu'ils n'interfèrent pas avec la transmission de l'en-tête host.
- **Enregistrement alias Route 53 :** Si vous utilisez Route 53 pour gérer le DNS de votre domaine, créez un [enregistrement alias dans Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) qui pointe vers votre distribution CDN (par exemple, `d111111abcdef8.cloudfront.net`). L'utilisation d'un CNAME standard au lieu d'un enregistrement alias peut renvoyer des erreurs HTTP 400.
- **Transmission d'en-têtes désactivée :** Si l'activation du SSL échoue toujours après avoir configuré `X-Forwarded-Host`, essayez de désactiver la transmission d'en-têtes sur votre CDN ou votre proxy. Certaines configurations résolvent le problème lorsque la transmission est entièrement désactivée. Travaillez avec votre équipe informatique ou votre fournisseur de CDN pour tester cette configuration.

## Problèmes de suivi des clics {#click-tracking-issues}

**Symptôme :** Les liens d'e-mail suivis échouent alors que les liens non suivis fonctionnent, ou les utilisateurs voient des erreurs de certificat ou de DNS après avoir cliqué.

Les problèmes courants de redirection résultent généralement d'une mauvaise configuration entre le CDN hébergeant le domaine de suivi et ses certificats SSL associés ou ses enregistrements DNS CNAME. Ces mauvaises configurations entraînent souvent une erreur de confidentialité « la connexion n'est pas sécurisée » ou un échec `404` après avoir cliqué sur un lien d'e-mail suivi.

Utilisez le modèle suivant pour tester la configuration du CDN de votre domaine de suivi, qui est le mécanisme prenant en charge l'analyse des liens dans vos e-mails.

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

Si votre URL non suivie fonctionne mais que votre URL suivie échoue, il se peut qu'il y ait un problème de configuration. Pour résoudre le problème, consultez la documentation de votre fournisseur de services d'e-mailing et de votre CDN. Vous pouvez également consulter [SSL chez Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl) pour connaître les exigences détaillées en matière de provisionnement de certificats.

Utilisez le tableau suivant pour diagnostiquer les erreurs courantes lors du test du suivi des clics.

| Code d'erreur | Résolution des problèmes |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Vérifiez que votre domaine de suivi dispose d'un certificat SSL valide. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Vérifiez vos paramètres DNS. Assurez-vous que votre sous-domaine de suivi est configuré conformément aux recommandations de votre CDN et de votre fournisseur de services d'e-mailing. |
| `525 / 526 SSL Error` | Vérifiez que le paramètre SSL de votre CDN (comme Cloudflare) correspond aux capacités de votre origine. |
| `404 Not Found` | Vérifiez que votre CDN est configuré pour transmettre l'intégralité du chemin de l'URL au fournisseur de services d'e-mailing, plutôt que de pointer vers un répertoire racine vide. |
| `400 Bad Request: Request Header or Cookie Too Large` | Cette erreur se produit généralement lorsque le domaine de suivi des clics hérite d'un trop grand nombre de cookies volumineux provenant du domaine de votre site web. Braze ne définit ni ne bloque aucun cookie sur le domaine de suivi. Configurez votre CDN pour ne pas envoyer ces cookies au fournisseur de services d'e-mailing lors du reverse-proxy de la requête de suivi des clics. Vous devrez peut-être également augmenter le paramètre `large_client_header_buffers` dans votre configuration nginx (par exemple, `large_client_header_buffers 4 32k;` pour autoriser des en-têtes jusqu'à 32&nbsp;Ko). Pour plus d'informations, consultez votre fournisseur de CDN ou votre équipe d'ingénierie web. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Codes d'erreur et résolution des problèmes" }