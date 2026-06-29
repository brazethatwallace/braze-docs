---
nav_title: Personnaliser l'URL
article_title: Personnaliser l'URL
description: "Découvrez comment personnaliser les URL de vos pages d'accueil avec la marque de votre entreprise en connectant votre domaine à votre espace de travail Braze."
page_order: 1
---

# Personnaliser les URL des pages d'accueil {#customize-landing-page-urls}

> Découvrez comment personnaliser les URL de vos pages d'accueil avec la marque de votre entreprise en connectant votre domaine à votre espace de travail Braze.

## Comment ça fonctionne {#how-it-works}

Lorsque vous [connectez votre domaine à Braze](#connect-your-domain-to-braze), il sera utilisé comme domaine par défaut pour toutes les pages d'accueil. Par exemple, si vous connectez le sous-domaine `forms.example.com`, les URL de vos pages d'accueil seront désormais `forms.example.com/holiday-sale`.

Le nombre de domaines personnalisés que vous pouvez connecter à votre compte Braze dépend de votre [niveau de forfait]({{site.baseurl}}/user_guide/messaging/landing_pages/#plan-tiers). Pour augmenter votre limite, contactez votre gestionnaire de compte Braze.

## Connecter votre domaine à Braze {#connect-your-domain-to-braze}

Pour connecter un domaine à votre compte Braze, demandez à un administrateur de suivre les étapes ci-dessous.

1. Accédez à **Settings** > **Landing Page Settings**.
2. Saisissez le domaine que vous souhaitez connecter et sélectionnez **Submit**. Par exemple, `forms.example.com`.
3. Copiez et collez les enregistrements **TXT** et **CNAME** dans les paramètres DNS de votre fournisseur de domaine.
4. Retournez au tableau de bord de Braze pour vérifier la connexion.

![Page des paramètres de la page d'accueil avec un enregistrement TXT et deux enregistrements CNAME répertoriés avec leurs noms et valeurs respectifs.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Selon votre fournisseur de domaine, la connexion peut prendre jusqu'à 48 heures. Lorsque le processus est terminé, nous commencerons à utiliser votre domaine personnalisé pour vos pages d'accueil dans le tableau de bord de Braze.
{% endalert %}

### Configuration du certificat SSL {#ssl-certificate-setup}

Braze utilise Cloudflare pour provisionner automatiquement des certificats SSL pour votre domaine personnalisé via un [challenge ACME DNS-01](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge). Cette méthode de validation continue est activée par l'un des enregistrements CNAME que vous avez fournis lors de la configuration, et permet à l'autorité de certification (LetsEncrypt) de vérifier la propriété de votre domaine via les enregistrements DNS sans que Braze ait besoin de posséder votre domaine.

## Supprimer votre domaine {#remove-your-domain}

Si vous êtes administrateur Braze, vous pouvez supprimer un domaine précédemment configuré en suivant les étapes suivantes :

1. Accédez à **Settings** > **Landing Page Settings**.
2. Sélectionnez **Remove Custom Domain**.
3. Confirmez la suppression du domaine.
4. Supprimez les enregistrements DNS répertoriés de vos paramètres de domaine.

{% alert important %}
Lorsque vous supprimez un domaine personnalisé, cette URL ne sera plus valide. Toutes les pages d'accueil qui utilisaient ce domaine reviendront automatiquement au domaine par défaut défini par Braze.
{% endalert %}

## Migrer votre domaine {#migrate-your-domain}

Pour migrer un domaine personnalisé vers un autre espace de travail :

1. Supprimez le domaine personnalisé.
2. Créez un nouveau domaine personnalisé dans l'espace de travail souhaité.
3. Reconfigurez le domaine personnalisé avec les nouveaux enregistrements DNS. Notez que votre sous-domaine sera indisponible pendant ce processus.

## Ressources DNS {#dns-resources}

{% multi_lang_include channels/email/dns_records.md %}

## Résolution des problèmes {#troubleshooting}

### La connexion de mon domaine a échoué {#my-domain-connection-failed}

Vérifiez que votre domaine a été saisi correctement et qu'il correspond à ce que vous avez soumis à Braze depuis votre compte de fournisseur de domaine. Si c'est correct et que cela correspond, vérifiez les enregistrements TXT et CNAME fournis par Braze. Ils doivent correspondre aux enregistrements que vous avez saisis dans votre compte de fournisseur de domaine.

## Questions fréquemment posées {#frequently-asked-questions}

### Puis-je utiliser des sous-domaines imbriqués pour mon domaine personnalisé ? {#can-i-use-nested-subdomains-for-my-custom-domain}

Oui, vous pouvez utiliser des sous-domaines imbriqués pour vos pages d'accueil. Par exemple, `forms.braze.com`, `pages.forms.braze.com` ou des niveaux plus profonds sont tous pris en charge. La seule exigence est que vous ne pouvez pas utiliser un domaine apex (tel que `braze.com`) car Braze utilise des enregistrements CNAME pour la connexion.

### Puis-je connecter plusieurs sous-domaines à mon espace de travail, ou connecter un sous-domaine à plusieurs espaces de travail ? {#can-i-connect-multiple-subdomains-to-my-workspace-or-connect-one-subdomain-to-multiple-workspaces}

Non, vous ne pouvez actuellement connecter qu'un seul sous-domaine à un espace de travail.

### Puis-je utiliser le même sous-domaine que celui que j'utilise actuellement pour mon site web principal ou mon domaine d'envoi ? {#can-i-use-the-same-subdomain-that-i-currently-use-for-my-main-website-or-my-sending-domain}

Non, vous ne pouvez pas utiliser des sous-domaines déjà utilisés. Bien que ces sous-domaines soient valides, ils ne peuvent pas être utilisés pour les pages d'accueil s'ils sont déjà affectés à d'autres usages ou s'ils ont des enregistrements DNS en conflit avec les enregistrements CNAME requis.

### Pourquoi mon domaine personnalisé reste-t-il bloqué sur « Connexion en cours » malgré des enregistrements DNS valides ? {#why-is-my-custom-domain-stuck-on-connecting-despite-valid-dns-records}

Si votre domaine personnalisé affiche tous les enregistrements DNS comme « Connecté » mais que l'état du domaine reste sur « Connexion en cours » pendant plus de quatre heures, votre organisation utilise peut-être des enregistrements CAA (Certificate Authority Authorization) ou des blocages de zone Cloudflare qui empêchent Braze de sécuriser votre page.

#### Enregistrements CAA {#caa-records}

Les enregistrements CAA limitent les autorités de certification autorisées à émettre des certificats SSL pour votre domaine. Si vos enregistrements CAA n'incluent pas LetsEncrypt, Braze (via Cloudflare) ne peut pas émettre le certificat SSL requis.

Pour résoudre ce problème, demandez à votre équipe informatique d'ajouter un enregistrement CAA à votre sous-domaine avec les valeurs suivantes :
- **Type d'enregistrement :** CAA
- **Valeur :** `0 issue "letsencrypt.org"`

Pour plus d'informations, consultez la [documentation CAA de LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### Blocages de zone Cloudflare {#cloudflare-zone-holds}

Si votre organisation utilise Cloudflare, une fonctionnalité de sécurité de blocage de zone peut empêcher Braze de créer votre domaine personnalisé.

Pour résoudre ce problème, demandez à votre équipe informatique de libérer temporairement le blocage de zone. Pour plus d'informations, consultez la [documentation sur les blocages de zone de Cloudflare](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Redémarrer le processus de validation {#restarting-the-validation-process}

Après avoir résolu l'un ou l'autre problème, supprimez et recréez votre domaine personnalisé dans le tableau de bord de Braze pour redémarrer le processus de validation.

### Puis-je utiliser un proxy inverse pour servir des pages d'accueil sous mon domaine principal ou un sous-répertoire ? {#can-i-use-a-reverse-proxy-to-serve-landing-pages-under-my-main-domain-or-a-subdirectory}

Non, les balises Liquid d'URL de page d'accueil ne fonctionneront pas correctement avec les proxys inverses.