---
nav_title: Einstellung von TLS 1.0 und 1.1
page_order: 2

page_type: update
description: "Dieser Artikel beschreibt die Einstellung von TLS 1.0 und TLS 1.1 durch Braze, die im Mai 2018 abgeschlossen wurde."
---
# Einstellung von TLS 1.0 und 1.1 {#tls-10-11-deprecation}

{% alert Update or aktualisieren %}
Braze hat die Unterstützung für Transport Layer Security (TLS)-Chiffren sowohl in TLS 1.0 als auch in 1.1 entfernt, in Übereinstimmung mit den Empfehlungen des PCI Security Standards Council. Wir haben diese Einstellung der Unterstützung in zwei Phasen durchgeführt, die im Mai 2018 abgeschlossen wurden.
{% endalert %}

## Hintergrund {#background}

Braze stellt bekannte schwache Transport Layer Security (TLS)-Chiffren sowohl in TLS 1.0 als auch in 1.1 ein, gemäß den Empfehlungen des PCI Security Standards Council in zwei Phasen, die im Mai 2018 abgeschlossen wurden.

Diese Änderung erfolgt nicht als Reaktion auf einen Sicherheitsvorfall oder ein Problem im Zusammenhang mit der Plattform von Braze, sondern als Vorsichtsmaßnahme, um unsere erstklassigen Sicherheits- und Datenstandards aufrechtzuerhalten und unsere Kund:innen und deren Verbraucher:innen proaktiv zu schützen.

In den letzten Jahren gab es eine Reihe von systematischen Sicherheitsproblemen im Zusammenhang mit TLS und seinem Vorgänger Secure Sockets Layer (SSL), darunter [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)) und andere, die den verschlüsselten Internetverkehr bedrohten und Teile des Internets Sicherheitslücken aussetzten. Zusammen mit anderen Technologieunternehmen hat Braze bereits früher Maßnahmen ergriffen, um schwache Verschlüsselungsprotokolle und Chiffren zu deaktivieren, sobald Angriffe entdeckt werden – so wurde beispielsweise die Unterstützung für SSLv3 im Jahr 2014 eingestellt.

Vor kurzem hat der PCI Security Standards Council im April 2015 einen Leitfaden zur Verschlüsselung für den [Payment Card Industry Data Security Standard](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS) veröffentlicht. Der Leitfaden schließt SSL 3.0, TLS 1.0 und einige der von TLS 1.1 unterstützten Chiffre or verschlüsseln-Suiten von der Protokollliste starker kryptographischer Chiffren aus und ermutigt Unternehmen, die Unterstützung für diese Protokolle oder Chiffren einzustellen, um die Sicherheit der Nutzer:innen im Internet zu gewährleisten.

Eine Chiffre or verschlüsseln-Suite ist eine Kombination von Algorithmen, die bei der Aushandlung einer sicheren SSL- oder TLS-Verbindung für Verschlüsselung, Authentifizierung und Kommunikationsintegrität sorgen. Wenn entdeckt wird, dass eine bestimmte Chiffre or verschlüsseln geknackt werden kann – unabhängig davon, ob es bereits bekannte Angriffe gibt oder nicht –, gilt die Chiffre or verschlüsseln als „Schwachstelle“, die zukünftige Angriffe ermöglichen könnte. Durch den Ausschluss dieser TLS-Chiffren von den PCI-DSS-Compliance-Anforderungen verlangt der PCI DSS Council von Dienstleistern, dass sie nur erstklassige Verschlüsselungsstandards unterstützen. Der PCI DSS Council hat eine Frist bis zum 30. Juni 2018 für die Einhaltung der Verschlüsselungsanforderung gesetzt, die Unterstützung für TLS 1.0 und TLS 1.1 einzustellen.

## Einstellungsplan von Braze {#brazes-deprecation-plan}
Um die Empfehlungen des PCI DSS Council zu erfüllen, wird Braze die Mindestversionen von TLS, die wir in unseren Diensten unterstützen, anheben. Um Ihnen eine bessere Vorstellung von unserem Compliance-Plan und seinen potenziellen Auswirkungen auf Ihre Marke und Ihre Nutzer:innen zu geben, sollten Sie sich über die zwei Hauptphasen unseres Plans im Klaren sein:

### Phase 1: 1. Oktober 2017 {#phase-1-october-1-2017}

Braze wird die Möglichkeit entfernen, die folgenden Chiffren im Braze-Dashboard und den Representational State Transfer APIs zu verwenden:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Diese Änderung sollte keine Auswirkungen auf Kund:innen haben, die auf das Braze-Dashboard zugreifen, da alle modernen Webbrowser sicherere Chiffren unterstützen. Sollte jedoch nach dem 1. Oktober beim Zugriff auf das Dashboard ein SSL-Verschlüsselungsfehler auftreten, können Sie das Problem beheben, indem Sie einfach auf die neueste Version Ihres Webbrowsers Update or aktualisieren or aktualisieren.

Ihr Entwicklerteam sollte sicherstellen, dass keine dieser Chiffren für die Server-zu-Server-Kommunikation mit den Representational State Transfer APIs von Braze verwendet werden. Falls doch, muss der Code vor dem 1. Oktober auf sicherere Verschlüsselungschiffren aktualisiert werden, um die APIs von Braze weiterhin nutzen zu können. Um jedoch die Unterstützung für alte und veraltete mobile Geräte aufrechtzuerhalten, die möglicherweise schwache Chiffren verwenden, wird Braze diese Chiffren auf den APIs, die Daten von unseren SDKs empfangen, weiterhin unterstützen.

### Phase 2: 31. Mai 2018 {#phase-2-may-31-2018}

Braze wird die Unterstützung für TLS 1.0 und TLS 1.1 in allen Braze-Diensten am 31. Mai 2018 einstellen – einschließlich des Braze-Dashboards, der Representational State Transfer APIs und der APIs, die mit unseren SDKs kommunizieren. Wir werden auch die Unterstützung für die im vorangegangenen Abschnitt aufgeführten Chiffren in Verbindung mit den APIs, die SDK or Software-Development-Kit-Daten empfangen, entfernen. Das bedeutet, dass ab diesem Datum jegliche TLS 1.0- und 1.1-Kommunikation von und zu Braze von unserem Netzwerk nicht mehr unterstützt wird.

Infolge dieser Änderung können einige alte oder veraltete mobile Geräte – wahrscheinlich solche, auf denen frühe Versionen von Android laufen – möglicherweise nicht mehr mit Braze kommunizieren, sodass sie keine Daten mehr an Braze senden oder In-App-Nachrichten von Braze empfangen können. Wir gehen jedoch davon aus, dass die Änderung nur eine kleine Anzahl von Geräten betreffen wird. Alle betroffenen Geräte verlieren einen Monat später, am 30. Juni 2018, auch die Möglichkeit, mit jeder PCI-konformen Website oder jedem PCI-konformen Dienst zu kommunizieren – dem vom PCI DSS Council festgelegten Datum für die Entfernung der Chiffren TLS 1.0 und TLS 1.1.

## Aktionsplan {#action-plan}
Wenn Ihre Marke die Representational State Transfer APIs von Braze nutzt, sprechen Sie mit Ihrem Entwicklerteam, um sicherzustellen, dass alle Server-zu-Server-Aufrufe an Braze bis zum genannten Datum TLS 1.2 verwenden, um eine Unterbrechung des Dienstes zu vermeiden. Beachten Sie, dass einige Programmiersprachen – wie z. B. Java 7 – standardmäßig ältere Versionen von TLS verwenden, sodass Ihr Entwicklerteam möglicherweise Codeänderungen vornehmen muss, um die aktualisierten Verschlüsselungsanforderungen zu unterstützen.

Apple-Geräte werden von der geplanten Einstellung durch Braze nicht betroffen sein, da Apple seit Ende 2016 TLS 1.2 voraussetzt. Dasselbe gilt für moderne Webbrowser, sodass wir nicht davon ausgehen, dass diese Änderungen Auswirkungen auf die Nutzung des Web SDK or Software-Development-Kit haben werden. Android-Geräte mit Android 4.4 (KitKat) oder niedriger verwenden jedoch möglicherweise nicht standardmäßig TLS 1.2. Update or aktualisieren or aktualisieren Sie daher alle Ihre Android-Integrationen bis zum 31. Mai 2018 mindestens auf die Version 2.0.3 des Braze SDK or Software-Development-Kit (das standardmäßig TLS 1.2 verwendet, sofern ein bestimmtes Gerät dies unterstützen kann).

Aufgrund der bekannten Schwachstellen in TLS 1.0 und der Chiffre or verschlüsseln-Suite TLS 1.1 ist es möglich, dass in Zukunft Angriffe auftreten, die es erforderlich machen, dass Braze seinen Einstellungsplan beschleunigt, um die Sicherheit aller unserer Kund:innen zu gewährleisten. Braze wird den Stand der Sicherheit und alle relevanten Angriffe im Zusammenhang mit den Protokollen TLS 1.0 und 1.1 überwachen und Sie auf dem Laufenden halten, wenn wir von Angriffen erfahren, die den in den vorangegangenen Abschnitten dargelegten Zeitplan verändern. Aufgrund dieser möglichen Auswirkungen empfehlen wir Ihnen jedoch dringend, mit Ihrem Entwicklerteam zusammenzuarbeiten, um sicherzustellen, dass Ihre API-Aufrufe an Braze mit TLS 1.2 gesichert sind, und dass Sie in den kommenden Monaten ein Upgrade or upgraden auf das neueste Android SDK or Software-Development-Kit planen.