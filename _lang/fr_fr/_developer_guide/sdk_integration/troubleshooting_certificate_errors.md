---
page_order: 1.35
nav_title: Erreurs de confiance de certificat
article_title: Résolution des erreurs de confiance de certificat SDK
description: "Résolvez les erreurs de confiance de certificat HTTPS qui peuvent bloquer l'initialisation du SDK Braze sur Android, Swift et d'autres SDK."
---

# Résolution des erreurs de confiance de certificat SDK {#troubleshooting-sdk-certificate-trust-errors}

Si l'initialisation du SDK échoue avec des erreurs de confiance de certificat SSL ou TLS, cela signifie généralement que l'appareil, le simulateur, le navigateur ou le serveur ne parvient pas à valider la chaîne de certificats pour l'endpoint Braze.

Par exemple, sur Android ou d'autres environnements basés sur la JVM, vous pouvez voir :

```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found
```

Il s'agit généralement d'un problème de configuration réseau ou de confiance de certificat dans votre environnement, et non d'un bug d'intégration SDK.

## Causes courantes {#common-causes}

- Un proxy d'entreprise, un pare-feu ou un outil d'inspection du trafic intercepte le trafic HTTPS avec un certificat que votre environnement d'exécution ne reconnaît pas comme fiable.
- Un certificat racine ou intermédiaire requis est manquant dans le magasin de certificats de confiance de l'appareil, du simulateur, du navigateur ou du serveur.
- Les paramètres de sécurité locaux bloquent le trafic HTTPS sortant vers les endpoints Braze.
- Les paramètres de certificat ou de sécurité du transport au niveau de l'application bloquent la connexion.

## Étapes de résolution des problèmes {#troubleshooting-steps}

1. Confirmez votre endpoint SDK et l'accès réseau.
   - Vérifiez que vous utilisez le bon [endpoint SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) pour votre espace de travail.
   - Vérifiez que votre environnement peut atteindre cet endpoint via HTTPS.
2. Comparez le comportement sur différents réseaux.
   - Testez sur un réseau différent (par exemple, les données mobiles au lieu du Wi-Fi d'entreprise).
   - Si le problème ne survient que sur un seul réseau, la cause est probablement liée à la configuration du proxy ou du pare-feu.
3. Validez votre configuration de confiance.
   - Confirmez que les certificats racine et intermédiaires requis sont installés et approuvés dans l'environnement d'exécution où le SDK fonctionne.
   - Si votre environnement utilise des autorités de certification personnalisées, confirmez que ces certificats sont distribués correctement.
4. Vérifiez les paramètres de sécurité de la plateforme.
   - Si votre application ou votre environnement dispose de règles de transport ou de certificat explicites, confirmez que ces paramètres autorisent les requêtes HTTPS vers les endpoints Braze.
5. Collaborez avec votre équipe réseau ou sécurité.
   - Partagez l'erreur complète et l'horodatage afin qu'ils puissent vérifier les chaînes de certificats, les paramètres d'inspection TLS et les règles de liste d'autorisation.

{% alert note %}
Étant donné que le trafic du SDK Braze utilise HTTPS, les échecs de confiance des certificats peuvent affecter tout SDK Braze (y compris Android, Swift, Web, React Native, Flutter, Unity et Cordova) dans les environnements soumis à des politiques réseau restrictives.
{% endalert %}