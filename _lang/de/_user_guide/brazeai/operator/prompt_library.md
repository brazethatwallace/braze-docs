---
nav_title: Prompt-Bibliothek
article_title: Prompt-Bibliothek für BrazeAI Operator
page_order: 4
page_type: reference
description: "Durchsuchen Sie Beispiel-Prompts für BrazeAI Operator, organisiert nach dem, was Sie erreichen möchten."
---

# Prompt-Bibliothek für BrazeAI Operator {#prompt-library-for-brazeai-operator}

> Durchsuchen Sie eine kuratierte Sammlung von Beispiel-Prompts für den Operator, zusammengestellt von Braze-Expert:innen. Wählen Sie ein Ziel aus, um relevante Prompts zu finden. Weitere Informationen finden Sie unter [Seitenabhängigen Kontext nutzen]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context).


<div class="prompt-library-tabs">
{% sdktabs local %}
{% sdktab Datenanalyse %}

{% include copy_block.html content="Fassen Sie die wichtigsten Trends für MAU, DAU und neue Nutzer:innen in diesem Zeitraum zusammen und nennen Sie die nächsten Schritte." available="Home page" %}

{% include copy_block.html content="Zeigen Sie die MAU-, DAU- und Neue-Nutzer:innen-Trends der letzten 90 Tage – wo sind die größten Einbrüche und Spitzen?" available="Home page" %}

{% include copy_block.html content="Schlüsseln Sie die Sitzungen nach App auf (falls verfügbar) und heben Sie hervor, welche App diesen Monat das meiste Wachstum antreibt." available="Home page" %}

{% include copy_block.html content="Geben Sie mir einen 5-Punkte-Gesundheitscheck unseres Engagement-Programms für die letzten 30 Tage mit den größten Chancen." available="Home page" %}

{% include copy_block.html content="Welche aktiven Canvases haben im FY26 Q1 die meisten zugeordneten Conversions und den meisten Umsatz erzielt (7-Tage-Attribution)?" available="Canvas" %}

{% include copy_block.html content="Fassen Sie diesen Campaign-Digest in 5 Punkten zusammen: größte Erfolge, größte Probleme und was sich im Vergleich zum vorherigen Zeitraum geändert hat." available="Campaigns" %}

{% endsdktab %}
{% sdktab Strategie und Optimierung %}

{% include copy_block.html content="Welche 3 Möglichkeiten gibt es, diese App-Nutzungs-Insights zu nutzen, um einen Re-Engagement-Canvas für Nutzer:innen mit Churn-Risiko zu gestalten?" available="Home page" %}

{% include copy_block.html content="Was bedeutet unsere x%-Kundenbindung, und welche 3 Möglichkeiten gibt es, sie mit Lifecycle-Messaging zu verbessern?" available="Home page" %}

{% include copy_block.html content="Welche 3 Möglichkeiten gibt es, unsere aktiven Lifecycle-Canvases zu optimieren, um die Aktivierung zu steigern und Churn zu reduzieren?" available="Canvas" %}

{% include copy_block.html content="Welche 3 Möglichkeiten gibt es, unsere Onboarding-Canvases umzustrukturieren, um Abbrüche zu reduzieren und die Aktivierung zu verbessern?" available="Canvas" %}

{% include copy_block.html content="Zeigen Sie meine inaktiven Canvases und fassen Sie zusammen, was sie zuletzt gesendet haben und wann Nutzer:innen zuletzt eingetreten sind (letzte 90 Tage)." available="Canvas" %}

{% include copy_block.html content="Wie können wir das Segment [Ihr Segmentname] nutzen, um eine Re-Engagement-Journey aufzubauen und Churn zu reduzieren?" available="Segments" %}

{% include copy_block.html content="Wie sollten wir Frequency-Capping-Segmenterweiterungen (E-Mail/SMS/48 h) strukturieren, um Über-Messaging zu reduzieren, ohne Conversions zu beeinträchtigen?" available="Segment Extensions" %}

{% include copy_block.html content="Welche 3 wirkungsvollen Berichte sollten wir hier erstellen, um die wöchentliche Campaign- und Canvas-Performance zu überwachen und Probleme frühzeitig zu erkennen?" available="Report Builder" %}

{% endsdktab %}
{% sdktab Messaging-Performance %}

{% include copy_block.html content="Zeigen Sie die wichtigsten Engagement-Metriken dieser Campaign (Öffnungs-/Klickraten) für die letzten 30 Tage und die vorherigen 30 Tage." available="Individual campaign" %}

{% include copy_block.html content="Wie viel zugeordneten Umsatz und wie viele Conversions hat diese Campaign in den letzten 90 Tagen erzielt (7-Tage-Fenster)?" available="Individual campaign" %}

{% include copy_block.html content="Vergleichen Sie die Konversionsrate dieser Campaign mit unseren anderen In-App-Campaigns in diesem Quartal bis heute." available="Individual campaign" %}

{% include copy_block.html content="Zeigen Sie die Top 10 der aktiven Campaigns nach Engagement-Rate in den letzten 30 Tagen (nach Kanal)." available="Campaigns, Individual campaign" %}

{% include copy_block.html content="Welche Kanäle haben bei Campaigns, die auf „C&L Newsletter Clickers“ vs. „Openers but not Clickers“ abzielen, in den letzten 30 Tagen am besten abgeschnitten?" available="Segments" %}

{% include copy_block.html content="Wie viel zugeordneten Umsatz und wie viele Conversions haben Campaigns für Nutzer:innen generiert, die durch unsere Caps in den letzten 30 Tagen ausgeschlossen wurden (7-Tage-Fenster)?" available="Segment Extensions" %}

{% include copy_block.html content="Vergleichen Sie unsere E-Mail-Öffnungsrate und Click-through-Rate mit Branchen-Benchmarks für die letzten 30 Tage." available="Email Performance" %}

{% include copy_block.html content="Welche E-Mail-Campaigns hatten die niedrigste CTR (bei hohen Öffnungen) in den letzten 30 Tagen?" available="Email Performance" %}

{% endsdktab %}
{% sdktab Personalisierung und Liquid %}

{% include copy_block.html content="Was ist Liquid, und wie kann es mir helfen, die Personalisierung meiner Marketing-Campaigns in Braze zu verbessern?" %}

{% include copy_block.html content="Welche Arten von Daten kann ich in Liquid verwenden, um meine Marketing-Nachrichten zu personalisieren, z. B. demografische Informationen oder vergangene Käufe?" %}

{% include copy_block.html content="Können Sie mir einige Beispiele geben, wie Liquid in Marketing-Campaigns eingesetzt wird, um Engagement und Konversionsraten zu steigern?" %}

{% include copy_block.html content="Was sind gängige Anwendungsfälle für Liquid in Textnachrichten für Sommeraktionen, z. B. Warenkorb-Abbruch-Erinnerungen oder personalisierte Aktionen?" %}

{% include copy_block.html content="Fügen Sie dieser Nachricht einen Countdown hinzu, der die verbleibende Zeit bis zum Flug der Nutzer:innen anzeigt." available="Message composer" %}

{% include copy_block.html content="Personalisieren Sie diese Nachricht mit dem Vornamen der Nutzer:innen, mit einem Fallback, falls er fehlt." available="Message composer" %}

{% include copy_block.html content="Verbessern Sie dieses Liquid, damit es leichter lesbar ist." available="Message composer" %}

{% include copy_block.html content="Erstellen Sie eine Nachricht, die unterschiedliche Inhalte basierend auf dem Treuestatus meiner Kund:innen anzeigt. Falls wir den Treuestatus nicht kennen, senden Sie eine Fallback-Nachricht." available="Message composer" %}

{% include copy_block.html content="Schreiben Sie eine dynamische Nachricht, die das Lieblingsprodukt und das letzte Kaufdatum der Nutzer:innen enthält. Falls kein letzter Kauf vorliegt, brechen Sie die Nachricht ab." available="Message composer" %}

{% include copy_block.html content="Schreiben Sie mir Liquid, um jemanden zum Klicken meiner Nachricht zu animieren, das einen Countdown mit der verbleibenden Zeit enthält. Falls das Angebot abgelaufen ist, brechen Sie die Nachricht ab." available="Message composer" %}

{% include copy_block.html content="Helfen Sie mir, eine Nachricht zu schreiben, die Nutzer:innen ermutigt, zurückzukommen und zur Kasse zu gehen, wenn sie noch Artikel im Warenkorb haben." available="Message composer" %}

{% include copy_block.html content="Schreiben Sie Liquid, um eine Nachricht basierend auf dem Land der Kund:innen zu personalisieren. Ich möchte den Ländernamen in die Nachricht einfügen. Falls wir keines von beiden haben, schlagen Sie vor, auf einen Link zu klicken, um das Profil zu aktualisieren." available="Message composer" %}

{% include copy_block.html content="Wie kann ich eine Willkommensnachricht mit dem Vornamen der Nutzer:innen personalisieren und unterschiedliche Texte basierend auf dem Geschlecht schreiben?" available="Message composer" %}

{% include copy_block.html content="Schreiben Sie Liquid, um verschiedene Nachrichten basierend auf einem angepassten Attribut „CUSTOM_ATTRIBUTE_NAME“ und dessen Wert anzuzeigen. Es gibt sechs verschiedene Optionen, die ich senden könnte. Falls kein Wert für das angepasste Attribut vorhanden ist, möchte ich eine Platzhalter-Nachricht senden." available="Message composer" %}

{% endsdktab %}
{% sdktab Inhaltserstellung %}

{% include copy_block.html content="Schreiben Sie eine kurze, aufmerksamkeitsstarke Push-Benachrichtigung, die unseren Sommerschlussverkauf ankündigt." available="Message composer" %}

{% include copy_block.html content="Schreiben Sie diese Betreffzeile in einem lockereren Ton um." available="Message composer" %}

{% include copy_block.html content="Übersetzen Sie diesen Text ins Spanische." available="Message composer" %}

{% include copy_block.html content="Erstellen Sie ein Banner, das unseren Sommerschlussverkauf mit einer Überschrift, einer kurzen Beschreibung und einem „Jetzt shoppen“-Button bewirbt." available="Banner HTML editor" %}

{% include copy_block.html content="Verwenden Sie ein zweispaltiges Layout mit einem Produktbild in der ersten Spalte und der Überschrift, Beschreibung und dem „Jetzt shoppen“-Button gestapelt in der zweiten Spalte." available="Banner HTML editor" %}

{% include copy_block.html content="Machen Sie den Schließen-Button kleiner und positionieren Sie ihn als Eck-Schließen-Steuerelement." available="Banner HTML editor" %}

{% include copy_block.html content="Generieren Sie ein helles, sommerliches Banner-Bild einer Strandszene für einen E-Mail-Header." available="Media library" %}

{% include copy_block.html content="Erstellen Sie einen minimalistischen Produkthintergrund in unseren Markenfarben." available="Media library" %}

{% include copy_block.html content="Überprüfen Sie diese Push-Benachrichtigung auf Rechtschreibung, Grammatik und Ton und markieren Sie nicht gerendertes Liquid oder übrig gebliebene Testinhalte, bevor ich sie sende." available="Message composer" %}

{% endsdktab %}
{% sdktab Datentransformation %}

{% include copy_block.html content="Schreiben Sie Transformationscode, der diesen Umfrage-Webhook einem angepassten Event im Profil der Nutzer:innen zuordnet." available="Data Transformation" %}

{% include copy_block.html content="Aktualisieren Sie diese Transformation, um Nutzer:innen anhand der E-Mail-Adresse statt der externen ID zu identifizieren." available="Data Transformation" %}

{% endsdktab %}
{% sdktab Zielgruppenverwaltung %}

{% include copy_block.html content="Erstellen Sie ein Segment von Nutzer:innen, die in den letzten 30 Tagen einen Kauf getätigt, aber die App in den letzten 7 Tagen nicht geöffnet haben." available="Segments" %}

{% include copy_block.html content="Welche unserer aktiven Segmente wurden zuletzt bearbeitet, und welche sehen nach Duplikaten aus, die wir konsolidieren sollten?" available="Segments" %}

{% include copy_block.html content='Was bedeutet hier „Complex audience“, und wie kann ich diese Campaigns vereinfachen, ohne das Targeting zu verlieren?' available="Campaigns" %}

{% include copy_block.html content="Welche 3 Möglichkeiten gibt es, „Complex audience“ in diesen Campaigns zu reduzieren, ohne die Targeting-Genauigkeit zu verlieren?" available="Campaigns" %}

{% endsdktab %}
{% sdktab Onboarding %}

{% include copy_block.html content="Welche 5 Stellen in Braze sollte ich basierend auf diesem Dashboard zuerst besuchen, um unser Setup zu verstehen (Daten, Kanäle, Versand und Targeting)?" available="Home page" %}

{% include copy_block.html content="Ich fühle mich überfordert und möchte mit der Agent Console loslegen, weiß aber nicht wie. Was könnte ich basierend auf meinen aktuell laufenden Campaigns tun?" available="Campaigns" %}

{% include copy_block.html content="Was kann ich auf der Seite „Knowledge Sources“ tun, und wie richte ich am schnellsten meine erste Quelle ein?" available="Agent Console" %}

{% endsdktab %}
{% sdktab Wartung und Kosteneinsparungen %}

{% include copy_block.html content="Zeigen Sie mir die 5 inaktiven aktiven Campaigns und empfehlen Sie, welche pausiert, aktualisiert oder archiviert werden sollten." available="Campaigns" %}

{% include copy_block.html content="Welche Segmenterweiterungen sind aktiv, wurden aber kürzlich nicht verarbeitet, und können sie sicher archiviert werden, um freie Plätze zu schaffen?" available="Segment Extensions" %}

{% include copy_block.html content="Wie können wir die Nutzung von Query-Builder-Credits reduzieren, ohne die Berichtsabdeckung zu verlieren? Schlagen Sie 3 Taktiken vor." available="Query Builder" %}

{% include copy_block.html content="Welche gespeicherten Abfragen wurden seit 90 Tagen nicht ausgeführt – können Sie mir helfen, Kandidaten zum Archivieren zu identifizieren?" available="Query Builder" %}

{% endsdktab %}
{% endsdktabs %}
</div>