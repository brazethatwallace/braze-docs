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

> IP-Warming bedeutet, dass die Anbieter von E-Mail-Postfächern daran gewöhnt werden, Nachrichten von Ihren dedizierten IP-Adressen zu empfangen. Es ist ein äußerst wichtiger Bestandteil des E-Mail-Versands bei jedem E-Mail-Anbieter (ESP) und bei Braze Standardpraxis, um sicherzustellen, dass Ihre Nachrichten den Posteingang mit einer gleichbleibend hohen Rate erreichen.

IP-Warming soll Ihnen helfen, einen positiven Ruf bei Internet-Providern (ISPs) aufzubauen. Jedes Mal, wenn eine neue IP-Adresse zum Versenden einer E-Mail verwendet wird, überwachen ISPs diese E-Mails programmatisch, um sicherzustellen, dass sie nicht zum Versenden von Spam an Nutzer:innen verwendet wird. Stellen Sie sich Ihre IP- und Domain-Reputation wie einen Kredit-Score vor – ISPs nutzen diese Reputation, um zu entscheiden, ob Ihre E-Mail im Posteingang oder im Spam-Ordner landet. Ähnlich wie bei einem Kredit-Score braucht es Zeit, eine positive Reputation aufzubauen, und noch länger, eine schlechte wiederherzustellen.

## E-Mail-Zustellung und Zustellbarkeit {#email-delivery-and-deliverability}

**Zustellung** ist der Anteil der E-Mails, die akzeptiert wurden und keinen Hard Bounce verursacht haben. **Zustellbarkeit** beschreibt, ob E-Mails im Posteingang statt im Spam-Ordner landen – Postfachanbieter stellen dies nicht als einzelne Metrik zur Verfügung.

Eine gesunde Zustellrate liegt oft bei etwa 99 % zugestellt mit einer Bounce-Rate von nicht mehr als etwa 1 %. Die Raten können auf dem Papier gut aussehen und dennoch Probleme verbergen (zum Beispiel viele Bounces von einer Domain oder E-Mails, die zugestellt, aber in den Spam-Ordner gefiltert werden). Beobachten Sie Öffnungen und Klicks, nicht nur die Zustellung. Selbst eine geringe gemeldete Spam-Rate kann eine tiefere Überprüfung rechtfertigen.

### Empfehlungen vor dem IP-Warming {#recommendations-before-ip-warming}

Bevor Sie mit dem IP-Warming beginnen:

1. Legen Sie unter **Settings** > **Email Preferences** Ihre Standard-Versanddomain fest, fügen Sie einen gültigen Abmeldelink in Ihrer [angepassten Fußzeile]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/) hinzu, aktivieren Sie den [List-Unsubscribe-Header]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#list-unsubscribe) und erwägen Sie bei Bedarf angepasste Abmelde-/Opt-in-Seiten.
2. Konfigurieren Sie [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) für E-Mail.
3. Erstellen Sie Ihre erforderlichen Templates unter **Content** > **Email**.

## Was passiert, wenn ich keine Zeit habe, IPs aufzuwärmen? {#what-if-i-dont-have-time-to-warm-ips}

**IP-Warming ist erforderlich.** Wenn Sie IPs nicht ordnungsgemäß aufwärmen und das Muster Ihrer E-Mails Verdacht erregt, könnte Ihre E-Mail-Zustellgeschwindigkeit erheblich gedrosselt oder verlangsamt werden. Ihre Domain oder IP könnte auch von den ISPs blockiert werden, was dazu führen kann, dass Ihre E-Mails direkt im Spam-Ordner des Posteingangs Ihrer Nutzer:innen landen. Daher ist es wichtig, Ihre IPs ordnungsgemäß aufzuwärmen.

ISPs drosseln die E-Mail-Zustellung, wenn Spam-Verdacht aufkommt, um ihre Nutzer:innen zu schützen. Wenn Sie beispielsweise an 100.000 Nutzer:innen senden, könnte der ISP die E-Mail in der ersten Stunde nur an 5.000 dieser Nutzer:innen zustellen. Dann überwacht der ISP Engagement-Metriken wie Öffnungsraten, Klickraten, Abmeldungen und Spam-Berichte. Wenn eine erhebliche Anzahl von Spam-Berichten auftritt, könnte er den Rest dieses Versands in den Spam-Ordner verschieben, anstatt ihn in den Posteingang der Nutzer:innen zuzustellen.

Wenn das Engagement moderat ist, kann er Ihre E-Mails weiterhin drosseln, um mehr Engagement-Daten zu sammeln und mit größerer Sicherheit festzustellen, ob die E-Mail Spam ist oder nicht. Wenn die E-Mail sehr hohe Engagement-Metriken aufweist, kann er die Drosselung dieser E-Mail vollständig einstellen. Diese Daten werden verwendet, um eine E-Mail-Reputation aufzubauen, die letztendlich bestimmt, ob Ihre E-Mails automatisch als Spam gefiltert werden oder nicht.

Wenn Ihre Domain oder IP von einem ISP blockiert wird, enthalten die Nachrichtenprotokolle im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) Informationen darüber, welche Websites Sie besuchen können, um bei diesen ISPs Einspruch einzulegen und von diesen Listen entfernt zu werden.

## IP-Warming-Zeitpläne {#ip-warming-schedules}

Wir empfehlen dringend, sich strikt an einen IP-Warming-Zeitplan zu halten, um die Zustellbarkeit zu unterstützen. Es ist auch wichtig, keine Tage auszulassen, da eine konsistente Skalierung die Zustellmetriken verbessert. Wählen Sie einen Zeitplan basierend auf Ihrer bestehenden E-Mail-Versandhistorie und Ihren Zustellbarkeitsmetriken.

{% alert tip %}
Wenn Sie an einer dedizierten Zustellbarkeitsressource als Teil Ihres Account-Teams interessiert sind, wenden Sie sich an Ihren Braze Account Manager für weitere Informationen.
{% endalert %}

{% tabs local %}
{% tab Konservativ %}

Der konservative Zeitplan ist ein langsamerer, vorsichtigerer Ansatz, der hilft, eine starke Versandreputation von Grund auf aufzubauen. Dies wird empfohlen, wenn Sie neu im E-Mail-Versand sind, von einer geteilten IP migrieren oder Zustellbarkeitsprobleme wie Drosselung oder Blocklisting durch einen Posteingangsanbieter erlebt haben.

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

Der moderate Zeitplan ist ein ausgewogener Ansatz, der das Sendevolumen in einem gleichmäßigen Tempo steigert. Dies wird für die meisten Absender empfohlen, einschließlich derjenigen mit einer gewissen E-Mail-Versandhistorie, die auf eine neue IP umsteigen.

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
Der aggressive Zeitplan ist der schnellste Ansatz und wird nur für Absender mit einer etablierten, positiven Versandhistorie und Zustellbarkeitsmetriken empfohlen, die den Best Practices entsprechen, einschließlich hoher Öffnungsraten, hoher Klickraten und niedriger Bounce-Raten. Die Verwendung dieses Zeitplans ohne eine nachgewiesene Erfolgsbilanz kann Ihrer Absender-Reputation schaden.
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

In den meisten Fällen sollten Sie auf Ihr durchschnittliches tägliches Sendevolumen aufwärmen, nicht auf Ihr Spitzenvolumen. ISPs betrachten hauptsächlich das Sendeverhalten der letzten Wochen, um Ihre Reputation zu bewerten. Wenn Sie also nur alle paar Monate ein Spitzenvolumen erreichen (zum Beispiel 7 Millionen während einer saisonalen Phase), können Sie näher am Versanddatum auf dieses Spitzenvolumen hochfahren. Wenn Sie jedoch alle ein bis zwei Wochen ein Spitzenvolumen erreichen, sollten Sie von Anfang an auf dieses Spitzenvolumen aufwärmen.

Nachdem das IP-Warming abgeschlossen ist und Sie Ihr gewünschtes tägliches Volumen erreicht haben, sollten Sie darauf abzielen, dieses Volumen täglich beizubehalten. Gewisse Schwankungen sind zu erwarten, aber das gewünschte Volumen zu erreichen und dann nur einmal pro Woche einen Massenversand durchzuführen, kann sich negativ auf Ihre Zustellmetriken und Ihre Absender-Reputation auswirken.

{% alert important %}
Die meisten ISPs speichern Reputationsdaten nur für 30 Tage. Wenn Sie einen Monat lang keine Nachrichten senden, müssen Sie den IP-Warming-Prozess wiederholen.
{% endalert %}

### IP-Adressen {#ip-addresses}

Nach drei Monaten ohne Nutzung kann Braze IP-Adressen recyceln und neu zuweisen. Unabhängig von der vorherigen Historie einer IP-Adresse wird ein vollständiges IP-Warming für alle neu zugewiesenen IPs empfohlen, da die meisten ISPs Reputationsdaten nur für 30 Tage speichern. Für die meisten ISPs bedeutet dies, dass eine dreimonatige Abkühlphase die Reputation effektiv zurücksetzt. Wenn Sie weitere Fragen zur Historie einer bestimmten IP-Adresse haben, wenden Sie sich an den [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/).

## So begrenzen Sie Sendungen während des Warmings {#how-to-limit-sends-during-warming}

Das integrierte Feature zur Nutzerbegrenzung dient als nützliches Werkzeug, um Sie beim Aufwärmen Ihrer IP-Adresse zu unterstützen. Nachdem Sie Ihre gewünschten Messaging-Segmente während der Campaign-Erstellung ausgewählt haben, wählen Sie im Schritt [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/channels/email/html_editor/#step-4-build-the-remainder-of-your-campaign-or-canvas) das Dropdown **Erweiterte Optionen**, um Ihre Nutzer:innen zu begrenzen. Während Ihr Warming-Zeitplan fortschreitet, können Sie dieses Limit schrittweise erhöhen, um das Volumen der gesendeten E-Mails zu steigern.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Subdomain-Segmentierung {#subdomain-segmentation}

Viele ISPs und E-Mail-Zugangsanbieter filtern nicht mehr nur nach IP-Adressen-Reputation. Diese Filtertechnologien berücksichtigen jetzt auch die domainbasierte Reputation. Das bedeutet, dass Filter alle mit der Domain des Absenders verknüpften Daten betrachten und nicht nur die IP-Adresse isoliert bewerten. Aus diesem Grund empfehlen wir zusätzlich zum Aufwärmen Ihrer E-Mail-IP, separate Domains oder Subdomains für Marketing-, Transaktions- und Unternehmens-E-Mails zu verwenden.

{% alert important %}
Die Subdomain-Segmentierung ist besonders wichtig für Absender mit hohem Volumen. Diese Absender sollten bei der Einrichtung ihres Kontos mit einer Braze-Vertretung zusammenarbeiten, um sicherzustellen, dass sie diese Praxis einhalten.
{% endalert %}

Wir empfehlen, Ihre Domains so zu segmentieren, dass Unternehmens-E-Mails über Ihre Top-Level-Domain gesendet werden und Marketing- und Transaktions-E-Mails über verschiedene Domains oder Subdomains.

## Best Practices {#best-practices}

Sie können alle Konsequenzen eines fehlenden IP-Warmings vermeiden, indem Sie diese Best Practices befolgen:

### Beginnen Sie mit kleinen E-Mail-Sendevolumen {#start-with-small-sending-volumes-of-email}

Erhöhen Sie die Menge, die Sie täglich senden, so schrittweise wie möglich. Abrupte E-Mail-Campaigns mit hohem Volumen werden von ISPs mit dem größten Misstrauen betrachtet. Daher sollten Sie mit dem Senden kleiner E-Mail-Mengen beginnen und schrittweise auf das Volumen skalieren, das Sie letztendlich senden möchten. Bedenken Sie, dass Sie Ihre IP bei jedem ISP einzeln aufwärmen – ISPs teilen keine Reputationsdaten untereinander. Wenn Sie Ihre Warming-Volumen aufbauen, stellen Sie sicher, dass Sie das Volumen bei keinem einzelnen ISP zu schnell erhöhen. Unabhängig vom Volumen empfehlen wir, Ihre IP sicherheitshalber aufzuwärmen. Siehe [IP-Warming-Zeitpläne](#ip-warming-schedules).

### Verwenden Sie ansprechende Einführungsinhalte {#have-engaging-introductory-content}

Stellen Sie sicher, dass Ihre ersten Inhalte sehr ansprechend sind und die Wahrscheinlichkeit maximieren, dass Nutzer:innen klicken, öffnen und mit Ihrer E-Mail interagieren. Bevorzugen Sie beim IP-Warming immer gut zielgerichtete E-Mails gegenüber wahllosen Massenversendungen.

### Legen Sie eine konsistente Versandfrequenz fest {#set-a-consistent-sending-cadence}

Sobald das IP-Warming abgeschlossen ist, erstellen Sie eine Versandfrequenz und achten Sie darauf, Ihre E-Mails auch über einen Tag oder mehrere Tage zu verteilen. Indem Sie einen möglichst konsistenten Zeitplan erstellen, können Sie ein IP-Cooldown verhindern, das auftreten kann, wenn das Sendevolumen für mehr als ein paar Tage stoppt oder deutlich abnimmt.

Orientieren Sie sich an unserem [IP-Warming-Zeitplan](#ip-warming-schedules), um Ihren Versand über einen längeren Zeitraum zu verteilen, anstatt einen Massenversand zu einem einzelnen bestimmten Zeitpunkt durchzuführen.

### Bereinigen Sie Ihre E-Mail-Listen {#clean-your-email-lists}

Stellen Sie sicher, dass Ihre E-Mail-Liste sauber ist und keine alten oder unverifizierten E-Mails enthält. Es ist ideal sicherzustellen, dass Sie sowohl [CASL- als auch CAN-SPAM-konform]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations/) sind.

### Überwachen Sie Ihre Absender-Reputation {#monitor-your-sender-reputation}

Achten Sie während des IP-Warming-Prozesses darauf, Ihre Absender-Reputation sorgfältig zu überwachen. Diese spezifischen Metriken sind wichtig zu beobachten:
- **Bounce-Raten:** Wenn eine Campaign eine Bounce-Rate von mehr als 3–5 % aufweist, sollten Sie die Sauberkeit Ihrer Liste bewerten, indem Sie den Richtlinien in unserem Artikel [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/) folgen. Zusätzlich sollten Sie die Implementierung einer [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/) in Betracht ziehen, um den Versand an nicht engagierte oder inaktive E-Mail-Adressen einzustellen.
- **Spam-Berichte:** Wenn eine Campaign mit einer Rate von mehr als 0,08 % als Spam gemeldet wird, sollten Sie die Inhalte, die Sie senden, neu bewerten, überprüfen, ob sie an eine interessierte Zielgruppe gerichtet sind, und sicherstellen, dass Ihre E-Mails angemessen formuliert sind, um deren Interesse zu wecken.
- **Öffnungsraten:** Öffnungsraten sind ein nützlicher Indikator für die Posteingangsplatzierung. Wenn Ihre eindeutigen Öffnungsraten über 25 % liegen, erleben Sie wahrscheinlich eine hohe Posteingangsplatzierung, was auf eine positive Absender-Reputation hinweist.

{% alert tip %}
Braze empfiehlt, [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) nicht zum Aufwärmen Ihrer IPs zu verwenden. Da IP-Warming-Campaigns zu den ersten Campaigns gehören, die Sie senden, verfügt Braze nicht über genügend Informationen über Ihre Nutzer:innen, um einen optimalen Sendezeitpunkt zu berechnen. In diesem Fall würden alle Nachrichten mit intelligentem Timing auf die Fallback-Zeit zurückfallen und ohnehin zur gleichen Zeit gesendet werden.
{% endalert %}

{% alert tip %}
Es ist normal, dass E-Mails während des IP-Warmings im Spam-Ordner landen, da Ihre Domain und IP noch keinen positiven Ruf aufgebaut haben. Wenn E-Mails in Ihrem Spam-Ordner landen, muss Ihr E-Mail-Administrator möglicherweise Ihre Braze-Versanddomain und IP zur Allowlist Ihres Unternehmens hinzufügen.
{% endalert %}