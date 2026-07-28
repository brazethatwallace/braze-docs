---
page_order: 1.35
nav_title: Zertifikatsvertrauensfehler
article_title: Fehlerbehebung bei SDK-Zertifikatsvertrauensfehlern
description: "Beheben Sie HTTPS-Zertifikatsvertrauensfehler, die die Braze-SDK-Initialisierung unter Android, Swift und anderen SDKs blockieren können."
---

# Fehlerbehebung bei SDK-Zertifikatsvertrauensfehlern {#troubleshooting-sdk-certificate-trust-errors}

Wenn die SDK-Initialisierung mit SSL- oder TLS-Zertifikatsvertrauensfehlern fehlschlägt, bedeutet dies in der Regel, dass das Gerät, der Simulator, der Browser oder der Server die Zertifikatskette für den Braze-Endpunkt nicht validieren kann.

Auf Android oder in anderen JVM-basierten Umgebungen kann beispielsweise folgender Fehler auftreten:

```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found
```

Dies ist in der Regel ein Problem mit der Netzwerk- oder Zertifikatsvertrauenskonfiguration in Ihrer Umgebung und kein Fehler in der SDK-Integration.

## Häufige Ursachen {#common-causes}

- Ein Unternehmens-Proxy, eine Firewall oder ein Tool zur Datenverkehrsinspektion fängt HTTPS-Datenverkehr mit einem Zertifikat ab, dem Ihre Laufzeitumgebung nicht vertraut.
- Ein erforderliches Stamm- oder Zwischenzertifikat fehlt im Vertrauensspeicher des Geräts, Simulators, Browsers oder Servers.
- Lokale Sicherheitseinstellungen blockieren ausgehende HTTPS-Verbindungen zu Braze-Endpunkten.
- Zertifikats- oder Transportsicherheitseinstellungen auf App-Ebene blockieren die Verbindung.

## Schritte zur Fehlerbehebung {#troubleshooting-steps}

1. Bestätigen Sie Ihren SDK-Endpunkt und den Netzwerkzugang.
   - Überprüfen Sie, ob Sie den korrekten [SDK-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) für Ihren Workspace verwenden.
   - Überprüfen Sie, ob Ihre Umgebung diesen Endpunkt über HTTPS erreichen kann.
2. Vergleichen Sie das Verhalten über verschiedene Netzwerke hinweg.
   - Testen Sie in einem anderen Netzwerk (zum Beispiel mobile Daten statt Unternehmens-WLAN).
   - Wenn das Problem nur in einem Netzwerk auftritt, liegt die Ursache wahrscheinlich in der Proxy- oder Firewall-Konfiguration.
3. Validieren Sie Ihre Vertrauenskonfiguration.
   - Bestätigen Sie, dass die erforderlichen Stamm- und Zwischenzertifikate in der Laufzeitumgebung, in der das SDK ausgeführt wird, installiert und als vertrauenswürdig eingestuft sind.
   - Wenn Ihre Umgebung angepasste Zertifizierungsstellen verwendet, bestätigen Sie, dass diese Zertifikate korrekt verteilt sind.
4. Überprüfen Sie die Sicherheitseinstellungen der Plattform.
   - Wenn Ihre App oder Umgebung explizite Transport- oder Zertifikatsregeln hat, bestätigen Sie, dass diese Einstellungen HTTPS-Anfragen an Braze-Endpunkte zulassen.
5. Arbeiten Sie mit Ihrem Netzwerk- oder Sicherheitsteam zusammen.
   - Teilen Sie den vollständigen Fehler und den Zeitstempel mit, damit das Team Zertifikatsketten, TLS-Inspektionseinstellungen und Allowlist-Regeln überprüfen kann.

{% alert note %}
Da der Braze-SDK-Datenverkehr HTTPS verwendet, können Zertifikatsvertrauensfehler jedes Braze SDK betreffen (einschließlich Android, Swift, Web, React Native, Flutter, Unity und Cordova) – insbesondere in Umgebungen mit restriktiven Netzwerkrichtlinien.
{% endalert %}