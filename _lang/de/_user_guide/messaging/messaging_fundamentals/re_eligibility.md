---
nav_title: Erneute Berechtigung
article_title: Erneute Berechtigung
page_order: 10
page_type: reference
description: "Dieser Referenzartikel definiert die erneute Berechtigung für Campaigns und Canvases."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Erneute Berechtigung für Campaigns und Canvas {#re-eligibility-for-campaigns-and-canvas}

> Wenn Sie eine wiederkehrende oder getriggerte Campaign oder ein Canvas planen, haben Sie die Möglichkeit, Nutzer:innen erneut dafür zu berechtigen. Erneute Berechtigung bedeutet, dass Nutzer:innen die Campaign oder das Canvas basierend auf dem Trigger mehrfach betreten können.

## Funktionsweise {#how-it-works}

Standardmäßig sendet Braze eine Nachricht nur einmal an eine:n Nutzer:in, selbst wenn diese:r sich mehrfach erneut qualifiziert, da die erneute Berechtigung separat aktiviert werden muss. Nach der Aktivierung dürfen qualifizierte Mitglieder erneut Nachrichten erhalten, nachdem sie die erste Instanz der Campaign oder des Canvas erhalten haben. Sie können den Zeitrahmen festlegen, nach dem Nutzer:innen letztendlich erneut berechtigt werden.

## Erneute Berechtigung aktivieren {#turning-on-re-eligibility}

{% tabs local %}
{% tab campaign %}
Um die erneute Berechtigung für eine Campaign zu aktivieren, wählen Sie das Kontrollkästchen **Allow users to become re-eligible to receive campaign** im Abschnitt **Delivery Controls** aus. Die maximale Zeit für die erneute Berechtigung einer Campaign beträgt 720 Tage.

Bei getriggerten Campaigns mit aktivierter erneuter Berechtigung qualifizieren sich Nutzer:innen, die [die Campaign-Nachricht nicht tatsächlich erhalten haben]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#why-did-a-user-not-receive-my-triggered-campaign) (obwohl sie das Trigger-Ereignis ausgelöst haben), automatisch für die Nachricht beim nächsten Mal, wenn sie das Trigger-Ereignis auslösen. Dies liegt daran, dass die erneute Berechtigung auf dem Nachrichtenempfang basiert und nicht auf dem Campaign-Eintritt. Indem Sie Nutzer:innen für eine getriggerte Campaign erneut berechtigen, ermöglichen Sie ihnen, die Nachricht tatsächlich zu erhalten (und nicht nur zu triggern) – und zwar mehr als einmal.

{% alert note %}
„Empfang“ umfasst die Attribution über gemeinsame Kanalkennungen: Wenn eine Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die dieselbe E-Mail-Adresse oder Telefonnummer teilen. Daher kann eine:r Nutzer:in, der/die die Nachricht nie direkt erhalten hat, als empfangen markiert werden und möglicherweise nicht erneut berechtigt werden.
{% endalert %}

Wenn Sie außerdem versuchen, eine Nachricht sofort mit einer erneuten Berechtigung von null Minuten zu senden, wird Braze immer versuchen, sie sofort zu planen – unabhängig davon, wie eine:r Nutzer:in frühere Versionen der Campaign oder des Canvas erhalten hat.

### Erneute Berechtigung bei API-getriggerten Campaigns {#re-eligibility-with-api-triggered-campaigns}

Die Anzahl der Male, die eine:r Nutzer:in eine API-getriggerte Campaign erhält, kann mithilfe der Einstellungen für die erneute Berechtigung begrenzt werden. Das bedeutet, dass die/der Nutzer:in die Campaign nur einmal oder einmal innerhalb eines bestimmten Zeitfensters erhält, unabhängig davon, wie oft der API-Trigger ausgelöst wird.

Nehmen wir zum Beispiel an, Sie verwenden eine API-getriggerte Campaign, um Nutzer:innen eine Campaign über einen kürzlich angesehenen Artikel zu senden. In diesem Fall können Sie die Campaign auf maximal eine Nachricht pro Tag begrenzen, unabhängig davon, wie viele Artikel angesehen wurden, während der API-Trigger für jeden Artikel ausgelöst wird. Wenn Ihre API-getriggerte Campaign hingegen transaktionsbezogen ist, sollten Sie sicherstellen, dass die/der Nutzer:in die Campaign jedes Mal erhält, wenn die Transaktion durchgeführt wird, indem Sie die Verzögerung auf null Minuten setzen.
{% endtab %}

{% tab canvas %}

Um die erneute Berechtigung für ein Canvas zu aktivieren, wählen Sie **Allow users to re-enter this Canvas** im Abschnitt **Entry Controls** aus. Sie können wählen, ob Nutzer:innen nach der maximalen Dauer des Canvas oder nach einem bestimmten Zeitfenster erneut eintreten dürfen.

Die erneute Berechtigung für Canvas-Varianten ist an den Canvas-Eintritt gebunden und nicht an den Nachrichtenempfang. Nutzer:innen, die ein Canvas betreten und keine Nachrichten erhalten, können das Canvas nicht erneut betreten, es sei denn, die erneute Berechtigung ist aktiviert.

Beachten Sie, dass eine:r Nutzer:in das Canvas nicht erst verlassen muss, bevor er/sie erneut eintritt, wenn die erneute Berechtigung auf null Sekunden eingestellt ist. Das bedeutet, dass eine:r Nutzer:in dasselbe Canvas erneut betreten kann. Ein weiteres Beispiel: Wenn die Canvas-Dauer auf 7 Tage und der Zeitraum für die erneute Berechtigung auf 3 Tage eingestellt ist, kann eine:r Nutzer:in das Canvas erneut betreten, bevor die erste Journey abgeschlossen ist.

Sie können zusätzliche Filter hinzufügen, um zu verhindern, dass Nutzer:innen denselben Schritt oder dieselbe Nachricht mehrfach erhalten. Wenn eine:r Nutzer:in jedoch ein Canvas zum zweiten Mal betritt, sind die zuvor beim ersten Durchlauf erhaltenen Schritte für die/den Nutzer:in nicht sichtbar. Das bedeutet, dass die/der Nutzer:in möglicherweise dieselbe Nachricht erneut erhält. Um dies zu verhindern, können Sie das Canvas so konfigurieren, dass ein erneuter Eintritt verhindert wird, oder die erneute Berechtigung auf die maximale Dauer des Canvas einstellen.

Sie können auch einen [Nutzeraktualisierungs-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) verwenden, damit die/der Nutzer:in, die/der den Schritt erhält, dies als angepasstes Attribut protokolliert. Dieses kann dann verwendet werden, um Nutzer:innen herauszufiltern, die den Schritt während ihrer Canvas-Journey bereits erhalten haben.

### Beispiel {#example}

Nehmen wir zum Beispiel an, eine:r Nutzer:in ohne E-Mail-Adresse betritt ein täglich wiederkehrendes Canvas, das einen Schritt in der Nutzer-Journey enthält. Dieser Schritt enthält nur eine E-Mail-Nachricht, sodass die/der Nutzer:in kein Engagement erhält. Diese:r Nutzer:in kann das Canvas nicht erneut betreten, es sei denn, die erneute Berechtigung ist für das Canvas aktiviert.

Wenn Sie ein aktives wiederkehrendes oder getriggertes Canvas ohne erneute Berechtigung haben und möchten, dass Nutzer:innen das Canvas erneut betreten, bis sie eine Nachricht daraus erhalten, können Sie in Betracht ziehen, Nutzer:innen für den erneuten Eintritt zu berechtigen, indem Sie einen Filter zu den Eintrittskriterien hinzufügen, der Kund:innen ausschließt, die bereits eine Nachricht aus dem Canvas erhalten haben.

Wenn die erneute Berechtigung für ein Canvas auf einen kürzeren Zeitraum als die Dauer des Canvas eingestellt ist, können Nutzer:innen das Canvas möglicherweise mehr als einmal betreten. Dies kann zu irreführendem Verhalten bei Canvases führen, die In-App-Nachrichten mit besonders langen Verzögerungen verwenden. Da mehrere Canvas-In-App-Nachrichten durch denselben Sitzungsstart getriggert werden können, könnte die/der Nutzer:in die Erfahrung machen, dieselbe Nachricht wiederholt zu erhalten, wenn eine bestimmte Komponente schneller gerendert wird als andere.
{% endtab %}
{% endtabs %}

## Berechnung der Verzögerung für die erneute Berechtigung {#re-eligibility-delay-calculations}

Die erneute Berechtigung für Campaigns und Canvases wird in Sekunden berechnet, nicht in Kalendertagen. Das bedeutet, dass ein Tag als 24 Stunden (oder 86.400 Sekunden) ab dem Zeitpunkt gezählt wird, an dem eine:r Nutzer:in die Nachricht erhält, und nicht ab Mitternacht des nächsten Kalendertages. Ebenso zählt ein Monat als genau 2.592.000 Sekunden, was ungefähr 30 Tagen entspricht.

### Beispiel

Betrachten Sie das folgende Szenario:

* Eine Campaign ist so eingestellt, dass sie monatlich am 15. gesendet wird, mit einer erneuten Berechtigung von 30 Tagen.
* Zwischen dem 15. Februar und dem 15. März liegen weniger als 30 Tage.

Das bedeutet, dass Nutzer:innen, die die Campaign am 15. Februar erhalten haben, für den Versand am 15. März nicht berechtigt sind. (Eine:r Nutzer:in kann aufgrund gemeinsamer Kanalkennungen als „erhalten“ markiert werden – zum Beispiel, wenn sie/er eine E-Mail-Adresse oder Telefonnummer mit jemandem teilt, der die Nachricht erhalten, geöffnet oder angeklickt hat.) Wenn die Campaign so eingestellt ist, dass sie täglich um 8:00 Uhr mit einer erneuten Berechtigung von 1 Tag gesendet wird, und es eine Latenz beim Senden der Nachricht gibt, sind Nutzer:innen, die die Campaign um 8:30 Uhr erhalten haben, am folgenden Tag um 8:00 Uhr noch nicht erneut berechtigt.

## Erneute Berechtigung für Content Cards {#re-eligibility-for-content-cards}

Wenn die erneute Berechtigung für Content-Card-Kampagnen oder Canvas-Schritte aktiviert ist, kann eine:r Nutzer:in eine weitere Card erhalten, während eine frühere Card derselben Campaign noch in ihrem/seinem Feed vorhanden ist, was wie doppelte Cards aussehen kann. Um Duplikate zu reduzieren, deaktivieren Sie die erneute Berechtigung oder verlängern Sie das Zeitfenster für die erneute Berechtigung, sodass die erste Card [aus dem Feed abläuft]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#the-30-day-expiration-and-re-eligibility), bevor die/der Nutzer:in sich für einen weiteren Versand qualifiziert.

Im Gegensatz zu anderen Kanälen (wie Push und E-Mail), bei denen die erneute Berechtigung ab dem Zeitstempel der Nachrichtenzustellung berechnet wird, basiert die erneute Berechtigung für Content Cards auf dem Impressions-Zeitstempel – also dem Zeitpunkt, an dem die/der Nutzer:in die Card tatsächlich ansieht. Das bedeutet: Wenn zwischen der Zustellung einer Card und dem Zeitpunkt, an dem die/der Nutzer:in die Sitzung öffnet, um sie anzusehen, eine Zeitverzögerung besteht, wird sie/er möglicherweise nicht wie erwartet erneut berechtigt.

Wenn beispielsweise eine tägliche Content-Card-Campaign ein Zeitfenster für die erneute Berechtigung von 24 Stunden hat und eine:r Nutzer:in eine Card mehrere Stunden nach der Zustellung ansieht, erhält sie/er möglicherweise die Card des nächsten Tages nicht, da seit der Impression noch keine 24 Stunden vergangen sind. Um dies zu berücksichtigen, sollten Sie das Zeitfenster für die erneute Berechtigung bei wiederkehrenden Content-Card-Campaigns etwas verkürzen.

## Erneute Berechtigung für Banner {#re-eligibility-for-banners}

Wenn die erneute Berechtigung für Banner-Campaigns aktiviert ist, können Nutzer:innen, die ein Banner schließen, nach einem konfigurierbaren Abklingzeitraum ab dem Schließen erneut berechtigt werden. Wenn die erneute Berechtigung nicht aktiviert ist, bleiben Nutzer:innen, die das Banner geschlossen haben, nicht berechtigt. Informationen zur Konfiguration der erneuten Berechtigung finden Sie unter [Erneute Berechtigung konfigurieren]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Beachten Sie, dass Canvas-Banner-Schritte stattdessen die Canvas-Wiedereintrittseinstellungen verwenden.

## Multivariates Testen {#multivariate-testing}

Für multivariates Testen bestimmt Braze die erneute Berechtigung für Varianten bei allen Campaigns, getriggerten In-App-Nachrichten und Canvases anhand der folgenden Regeln:

- Wenn die Variantenprozentsätze nicht geändert werden, tritt jede:r Nutzer:in bei jeder erneuten Berechtigung immer in dieselbe Variante einer Campaign, einer getriggerten In-App-Nachricht oder eines Canvas-Eintritts ein.
- Wenn die Variantenprozentsätze geändert werden, können Nutzer:innen anderen Varianten zugewiesen werden.
- Kontrollgruppen bleiben konsistent, wenn der Variantenprozentsatz unverändert bleibt. Keine Nutzer:innen, die zuvor Nachrichten erhalten haben, werden jemals bei einem späteren Versand in die Kontrollgruppe aufgenommen, und keine:r Nutzer:in in der Kontrollgruppe wird jemals eine Nachricht erhalten.