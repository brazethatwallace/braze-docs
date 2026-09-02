---
nav_title: IP-Warming
article_title: IP-Warming
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das Thema IP-Warming und Best Practices."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming'
---

# IP-Warming {#ip-warming}

> IP-Warming bedeutet, dass die Anbieter von E-Mail-Postfächern daran gewöhnt werden, Nachrichten von Ihren dedizierten IP-Adressen zu empfangen. Es ist ein äußerst wichtiger Bestandteil des E-Mail-Versands bei jedem E-Mail-Anbieter (E-Mail-Anbieter) und bei Braze Standardpraxis, um sicherzustellen, dass Ihre Nachrichten den Posteingang mit einer gleichbleibend hohen Rate erreichen. Wenn Sie [automatisiertes IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming) nutzen, lesen Sie die [FAQ zum automatisierten IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

IP-Warming soll Ihnen helfen, einen positiven Ruf bei Internet-Providern (ISPs) aufzubauen. Jedes Mal, wenn eine neue IP-Adresse zum Versenden einer E-Mail verwendet wird, überwachen ISPs diese E-Mails programmatisch, um sicherzustellen, dass sie nicht zum Versenden von Spam an Nutzer:innen verwendet wird. Stellen Sie sich Ihre IP- und Domain-Reputation wie einen Kredit-Score vor – ISPs nutzen diese Reputation, um zu entscheiden, ob Ihre E-Mail im Posteingang oder im Spam-Ordner landet. Ähnlich wie bei einem Kredit-Score braucht es Zeit, eine positive Reputation aufzubauen, und noch länger, eine schlechte wiederherzustellen.

## E-Mail-Zustellung und Zustellbarkeit {#email-delivery-and-deliverability}

**Zustellung** ist der Anteil der E-Mails, die akzeptiert wurden und keinen Hard Bounce verursacht haben. **Zustellbarkeit** beschreibt, ob E-Mails im Posteingang statt im Spam-Ordner landen – Posteingangsanbieter stellen das nicht als einzelne Metrik bereit.

Eine gesunde Zustellrate liegt häufig bei etwa 99 % zugestellt, mit einer Bounce-Rate von nicht mehr als etwa 1 %. Die Raten können auf dem Papier gut aussehen und dennoch Probleme verbergen (zum Beispiel viele Bounces von einer einzelnen Domain oder E-Mails, die zwar zugestellt, aber in den Spam-Ordner gefiltert werden). Beobachten Sie Öffnungen und Klicks, nicht nur die Zustellung. Selbst eine geringe gemeldete Spam-Rate kann eine genauere Überprüfung rechtfertigen.

### Empfehlungen vor dem IP-Warming {#recommendations-before-ip-warming}

Bevor Sie mit dem IP-Warming beginnen:

1. Legen Sie unter **Einstellungen** > **E-Mail-Einstellungen** Ihre Standard-Sendedomain fest, fügen Sie einen gültigen Abmeldelink in Ihrer [benutzerdefinierten Fußzeile]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer) hinzu, aktivieren Sie den [List-Unsubscribe-Header]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) und ziehen Sie bei Bedarf benutzerdefinierte Abmelde-/Opt-in-Seiten in Betracht.
2. Konfigurieren Sie [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) für E-Mails.
3. Erstellen Sie Ihre erforderlichen Templates, indem Sie zu **Inhalt** > **E-Mail** navigieren.

## Was passiert, wenn ich keine Zeit habe, IPs aufzuwärmen? {#what-if-i-dont-have-time-to-warm-ips}

**IP-Warming ist erforderlich.** Wenn Sie Ihre IPs nicht ordnungsgemäß aufwärmen und das Muster Ihrer E-Mails Verdacht erregt, kann die Zustellgeschwindigkeit Ihrer E-Mails erheblich gedrosselt oder verlangsamt werden. Ihre Domain oder IP kann auch von ISPs blockiert werden, was dazu führen kann, dass Ihre E-Mails direkt im Spam-Ordner des Posteingangs Ihrer Nutzer:innen landen. Daher ist es wichtig, Ihre IPs ordnungsgemäß aufzuwärmen.

ISPs drosseln die E-Mail-Zustellung, wenn ein Spam-Verdacht besteht, um ihre Nutzer:innen zu schützen. Wenn Sie beispielsweise an 100.000 Nutzer:innen senden, könnte der ISP die E-Mail in der ersten Stunde nur an 5.000 dieser Nutzer:innen zustellen. Anschließend überwacht der ISP Engagement-Metriken wie Öffnungsraten, Klickraten, Abmeldungen und Spam-Berichte. Wenn eine erhebliche Anzahl von Spam-Berichten eingeht, kann er sich dafür entscheiden, den Rest dieser Sendung in den Spam-Ordner zu verschieben, anstatt sie in den Posteingang der Nutzer:innen zuzustellen.

Wenn das Engagement moderat ist, kann der ISP Ihre E-Mails weiterhin drosseln, um mehr Engagement-Daten zu sammeln und mit größerer Sicherheit festzustellen, ob es sich bei der E-Mail um Spam handelt oder nicht. Wenn die E-Mail sehr hohe Engagement-Metriken aufweist, kann der ISP die Drosselung dieser E-Mail vollständig einstellen. Diese Daten werden verwendet, um eine E-Mail-Reputation aufzubauen, die bestimmt, ob Ihre E-Mails automatisch als Spam gefiltert werden.

Wenn Ihre Domain oder IP von einem ISP blockiert wird, enthalten die Nachrichtenprotokolle im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) Informationen darüber, welche Websites Sie besuchen können, um bei diesen ISPs Einspruch einzulegen und von diesen Listen entfernt zu werden.

## IP-Warming-Zeitpläne {#ip-warming-schedules}

Wir empfehlen dringend, sich strikt an einen IP-Warming-Zeitplan zu halten, um die Zustellbarkeit zu unterstützen. Es ist außerdem wichtig, keine Tage auszulassen, da eine konsistente Skalierung die Zustellmetriken verbessert. Wählen Sie einen Zeitplan basierend auf Ihrem bestehenden E-Mail-Versandverlauf und Ihren Zustellbarkeitsmetriken.

{% alert tip %}
Wenn Sie an einer dedizierten Zustellbarkeitsressource als Teil Ihres Account-Teams interessiert sind, wenden Sie sich an Ihren Braze Account Manager:in für weitere Informationen.
{% endalert %}

{% tabs local %}
{% tab Konservativ %}

Der konservative Zeitplan ist ein langsamerer, vorsichtigerer Ansatz, der dabei hilft, eine starke Absender-Reputation von Grund auf aufzubauen. Dies wird empfohlen, wenn Sie neu im E-Mail-Versand sind, von einer geteilten IP migrieren oder Zustellbarkeitsprobleme wie Drosselung oder Blocklisting durch einen Posteingangsanbieter erlebt haben.

Tag | Anzahl der zu sendenden E-Mails
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1.000
11 | 1.000
12 | 1.000
13 | 2.000
14 | 2.000
15 | 2.000
16 | 4.000
17 | 4.000
18 | 4.000
19 | 8.000
20 | 8.000
21 | 8.000
22+ | Alle 3 Tage verdoppeln, bis das gewünschte Volumen erreicht ist

{% endtab %}
{% tab Moderat %}

Der moderate Zeitplan ist ein ausgewogener Ansatz, der das Sendevolumen in einem gleichmäßigen Tempo steigert. Dies wird für die meisten Absender empfohlen, einschließlich derjenigen mit etwas E-Mail-Versandverlauf, die auf eine neue IP wechseln.

Tag | Anzahl der zu sendenden E-Mails
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.000
6 | 4.000
7 | 8.000
8 | 16.000
9 | 25.000
10 | 35.000
11 | 50.000
12 | 75.000
13 | 100.000
14 | 150.000
15 | 200.000
16 | 275.000
17 | 375.000
18 | 500.000
19 | 650.000
20 | 825.000
21 | 1.000.000
22+ | Alle 2 Tage verdoppeln, bis das gewünschte Volumen erreicht ist

{% endtab %}
{% tab Aggressiv %}

{% alert important %}
Der aggressive Zeitplan ist der schnellste Ansatz und wird nur für Absender mit einem etablierten, positiven Versandverlauf und Zustellbarkeitsmetriken empfohlen, die den Best Practices entsprechen, einschließlich hoher Öffnungsraten, hoher Klickraten und niedriger Bounce-Raten. Die Verwendung dieses Zeitplans ohne eine nachgewiesene Erfolgsbilanz kann Ihrer Absender-Reputation schaden.
{% endalert %}

Tag | Anzahl der zu sendenden E-Mails
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.500
6 | 5.000
7 | 9.000
8 | 16.000
9 | 29.000
10 | 52.000
11 | 98.000
12 | 160.000
13 | 225.000
14 | 315.000
15 | 450.000
16 | 615.000
17 | 875.000
18 | 1.200.000
19 | 1.750.000
20 | 2.750.000
21+ | Täglich verdoppeln, bis das gewünschte Volumen erreicht ist

{% endtab %}
{% endtabs %}

In den meisten Fällen sollten Sie auf Ihr durchschnittliches tägliches Sendevolumen aufwärmen, nicht auf Ihr Spitzenvolumen. ISPs betrachten hauptsächlich das Sendeverhalten der letzten Wochen, um Ihre Reputation zu bewerten. Wenn Sie also nur alle paar Monate Spitzenvolumen erreichen (zum Beispiel 7 Millionen während einer saisonalen Phase), können Sie näher am Sendedatum auf dieses Spitzenvolumen hochfahren. Wenn Sie jedoch alle ein bis zwei Wochen Spitzenvolumen erreichen, sollten Sie von Anfang an auf dieses Spitzenvolumen aufwärmen.

Nachdem das IP-Warming abgeschlossen ist und Sie Ihr gewünschtes tägliches Volumen erreicht haben, sollten Sie darauf abzielen, dieses Volumen täglich beizubehalten. Gewisse Schwankungen sind zu erwarten, aber das gewünschte Volumen zu erreichen und dann nur einmal pro Woche einen Massenversand durchzuführen, kann sich negativ auf Ihre Zustellmetriken und Absender-Reputation auswirken.

{% alert important %}
Die meisten ISPs speichern Reputationsdaten nur für 30 Tage. Wenn Sie einen Monat lang keine Nachrichten senden, müssen Sie den IP-Warming-Prozess wiederholen.
{% endalert %}

### IP-Adressen {#ip-addresses}

Nach drei Monaten ohne Nutzung kann Braze IP-Adressen recyceln und neu zuweisen. Unabhängig vom bisherigen Verlauf einer IP-Adresse wird für alle neu zugewiesenen IPs ein vollständiges IP-Warming empfohlen, da die meisten ISPs Reputationsdaten nur für 30 Tage speichern. Für die meisten ISPs bedeutet dies, dass eine dreimonatige Abkühlphase die Reputation effektiv zurücksetzt. Wenn Sie weitere Fragen zum Verlauf einer bestimmten IP-Adresse haben, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## So begrenzen Sie Sendungen während des Warmings {#how-to-limit-sends-during-warming}

Unser integriertes Feature zur Nutzer:innenbegrenzung ist ein nützliches Werkzeug, das Sie beim Warming Ihrer IP-Adresse unterstützt. Nachdem Sie während der Campaign-Erstellung Ihre gewünschten Messaging-Segmente ausgewählt haben, wählen Sie im Schritt [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas) das Dropdown **Advanced Options** aus, um Ihre Nutzer:innen zu begrenzen. Während Ihr Warming-Zeitplan fortschreitet, können Sie dieses Limit schrittweise erhöhen, um das Volumen der von Ihnen gesendeten E-Mails zu steigern.

![Das integrierte Feature zur Nutzer:innenbegrenzung unterstützt Sie beim Warming Ihrer IP-Adresse. Nachdem Sie während der Campaign-Erstellung Ihre gewünschten Messaging-Segmente ausgewählt haben, wählen Sie im Schritt „Zielgruppe zusammenstellen“ das Dropdown „Advanced Options“ aus, um Ihre Nutzer:innen zu begrenzen. Während Ihr Warming-Zeitplan fortschreitet, können Sie dieses Limit schrittweise erhöhen, um das Volumen der gesendeten E-Mails zu steigern.]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Subdomain-Segmentierung {#subdomain-segmentation}

Viele ISPs und E-Mail-Zugangsanbieter filtern nicht mehr nur nach der Reputation der IP-Adresse. Diese Filtertechnologien berücksichtigen inzwischen auch die domainbasierte Reputation. Das bedeutet, dass Filter alle Daten betrachten, die mit der Domain des Absenders verknüpft sind, und nicht nur die IP-Adresse isoliert bewerten. Aus diesem Grund empfehlen wir zusätzlich zum Warming Ihrer E-Mail-IP, separate Domains oder Subdomains für Marketing-, Transaktions- und Unternehmens-E-Mails zu verwenden.

{% alert important %}
Die Subdomain-Segmentierung ist besonders wichtig für Absender mit hohem Volumen. Diese Absender sollten bei der Einrichtung ihres Kontos mit einer Braze-Vertretung zusammenarbeiten, um sicherzustellen, dass sie diese Praxis einhalten.
{% endalert %}

Wir empfehlen, Ihre Domains so zu segmentieren, dass Unternehmens-E-Mails über Ihre Top-Level-Domain gesendet werden und Marketing- sowie Transaktions-E-Mails über verschiedene Domains oder Subdomains versendet werden.

## Best Practices {#best-practices}

Sie können alle Konsequenzen eines fehlenden IP-Warmings vermeiden, indem Sie diese Best Practices befolgen:

### Beginnen Sie mit kleinen E-Mail-Sendevolumen {#start-with-small-sending-volumes-of-email}

Erhöhen Sie die Menge, die Sie täglich senden, so schrittweise wie möglich. Abrupte E-Mail-Campaigns mit hohem Volumen werden von ISPs am kritischsten betrachtet. Beginnen Sie daher mit dem Versand kleiner E-Mail-Mengen und steigern Sie das Volumen schrittweise bis zu der Menge, die Sie letztendlich senden möchten. Bedenken Sie, dass Sie Ihre IP bei jedem ISP einzeln aufwärmen – ISPs teilen keine Reputationsdaten untereinander. Achten Sie beim Aufbau Ihrer Warming-Volumen darauf, dass Sie das Volumen bei keinem einzelnen ISP zu schnell erhöhen. Unabhängig vom Volumen empfehlen wir, Ihre IP sicherheitshalber aufzuwärmen. Siehe [IP-Warming-Zeitpläne](#ip-warming-schedules).

### Erstellen Sie ansprechende Einführungsinhalte {#have-engaging-introductory-content}

Stellen Sie sicher, dass Ihre ersten Inhalte besonders ansprechend sind und die Wahrscheinlichkeit maximieren, dass Nutzer:innen Ihre E-Mails anklicken, öffnen und mit ihnen interagieren. Bevorzugen Sie beim IP-Warming immer gut zielgerichtete E-Mails gegenüber wahllosem Massenversand.

### Legen Sie eine konsistente Sendefrequenz fest {#set-a-consistent-sending-cadence}

Sobald das IP-Warming abgeschlossen ist, erstellen Sie eine Sendefrequenz und verteilen Sie Ihre E-Mails über einen Tag oder mehrere Tage. Indem Sie einen möglichst konsistenten Zeitplan erstellen, können Sie ein IP-Cooldown verhindern, das auftreten kann, wenn das Sendevolumen für mehr als ein paar Tage stoppt oder deutlich abnimmt.

Orientieren Sie sich an unserem [IP-Warming-Zeitplan](#ip-warming-schedules), um Ihren Versand über einen längeren Zeitraum zu verteilen, anstatt einen Massenversand zu einem einzelnen Zeitpunkt durchzuführen.

### Bereinigen Sie Ihre E-Mail-Listen {#clean-your-email-lists}

Stellen Sie sicher, dass Ihre E-Mail-Liste sauber ist und keine alten oder unverifizierten E-Mail-Adressen enthält. Es ist ideal, wenn Sie sowohl [CASL- als auch CAN-SPAM-konform]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations) sind.

### Überwachen Sie Ihre Absender-Reputation {#monitor-your-sender-reputation}

Achten Sie während des IP-Warming-Prozesses darauf, Ihre Absender-Reputation sorgfältig zu überwachen. Diese spezifischen Metriken sind wichtig zu beobachten:
- **Bounce-Raten:** Wenn eine Campaign eine Bounce-Rate von mehr als 3–5 % aufweist, sollten Sie die Sauberkeit Ihrer Liste überprüfen, indem Sie die Richtlinien in unserem Artikel [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/) befolgen. Darüber hinaus sollten Sie die Implementierung einer [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) in Betracht ziehen, um den Versand an nicht engagierte oder inaktive E-Mail-Adressen einzustellen.
- **Spam-Berichte:** Wenn eine Campaign mit einer Rate von mehr als 0,08 % als Spam gemeldet wird, sollten Sie den Inhalt, den Sie senden, neu bewerten, prüfen, ob er an eine interessierte Zielgruppe gerichtet ist, und sicherstellen, dass Ihre E-Mails so formuliert sind, dass sie das Interesse wecken.
- **Öffnungsraten:** Öffnungsraten sind ein nützlicher Indikator für die Posteingangsplatzierung. Wenn Ihre eindeutigen Öffnungsraten über 25 % liegen, erleben Sie wahrscheinlich eine hohe Posteingangsplatzierung, was auf eine positive Absender-Reputation hinweist.

{% alert tip %}
Braze empfiehlt, [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) nicht zum Aufwärmen Ihrer IPs zu verwenden. Da IP-Warming-Campaigns zu den ersten Campaigns gehören, die Sie senden, verfügt Braze nicht über genügend Informationen über Ihre Nutzer:innen, um einen optimalen Sendezeitpunkt zu berechnen. In diesem Fall würden alle Nachrichten mit intelligentem Timing auf die Fallback-Zeit zurückfallen und ohnehin zur gleichen Zeit gesendet werden.
{% endalert %}

{% alert tip %}
Es ist normal, dass E-Mails während des IP-Warmings im Spam-Ordner landen, da Ihre Domain und IP noch keine positive Reputation aufgebaut haben. Wenn E-Mails in Ihrem Spam-Ordner landen, muss Ihr E-Mail-Administrator möglicherweise Ihre Braze-Sendedomain und IP zur Zulassungsliste Ihres Unternehmens hinzufügen.
{% endalert %}