---
nav_title: Funktionen
article_title: Was Sie mit Operator tun können
page_order: 1
page_type: reference
toc_headers: h2
description: "Dieser Referenzartikel behandelt, was BrazeAI Operator™ im gesamten Dashboard leisten kann – einschließlich der Erstellung von Campaigns, Canvases, Segmenten, Berichten, Dashboards und Agents, der Generierung von Texten, Nachrichten, Liquid und Bildern, der Datentransformation, der Überprüfung der Inhaltsqualität und der Informationssuche."
---

# Was Sie mit Operator tun können {#operator-capabilities}

> [BrazeAI<sup>TM</sup> Operator]({{site.baseurl}}/user_guide/brazeai/operator) ist ein KI-Assistent, der in das Braze-Dashboard integriert ist. Er beantwortet Fragen, verfasst Nachrichten und agiert auf unterstützten Seiten – beschreiben Sie in natürlicher Sprache, was Sie möchten, und Operator erledigt es im Kontext.

Da Operator Ihren Workspace versteht – angepasste Attribute, Connected-Content, die Seite, an der Sie arbeiten, und alle Markenrichtlinien, die Sie als Kontext hinzufügen – ist die Ausgabe kontextbewusster als das, was eigenständige Assistenten liefern können. Wenn Operator eine Änderung an einer Campaign, einem Canvas, einem Segment oder einem anderen Objekt vorschlägt, zeigt es die Änderung als visuellen Diff in einer [Aktionskarte]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) an, die Sie überprüfen und genehmigen, bevor etwas gespeichert wird.

Sie können das Gespräch mit Folgefragen fortsetzen. Operator merkt sich frühere Nachrichten, bis Sie Ihren Chatverlauf löschen.

## Voraussetzungen {#prerequisites}

Der Operator verfügt über dieselben Berechtigungen wie Sie, sodass bestimmte Aktionen die entsprechende Berechtigung für die jeweilige Oberfläche erfordern. Zum Beispiel erfordert das Generieren eines Bildes die Berechtigung *Medienbibliothek-Assets bearbeiten*. Wenn Sie keinen Einstiegspunkt sehen, überprüfen Sie Ihre Berechtigungen bei Ihrem Admin. Weitere Informationen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## Im Dashboard navigieren {#navigate-the-dashboard}

Operator ist nicht darauf beschränkt, nur auf der Seite zu agieren, die Sie gerade betrachten. Wenn ein Prompt einen anderen Bereich des Dashboards erfordert, identifiziert Operator das Ziel, schlägt die Navigation vor und bringt Sie dorthin, bevor die Arbeit fortgesetzt wird.

Das bedeutet, dass Operator mehrstufige Aufgaben aus einem einzigen Prompt heraus verketten kann. Wenn Sie Operator beispielsweise von der Startseite aus bitten, Ihre Drag-and-Drop-Editor-Einstellungen an Ihre Markenrichtlinien anzupassen, navigiert Operator Sie zu den relevanten E-Mail-Einstellungen und hilft Ihnen von dort aus weiter. Beschreiben Sie das gewünschte Ergebnis in einfacher Sprache, und Operator kann Sie zu den relevanten Einstellungen oder dem entsprechenden Feature führen, um mit der Arbeit zu beginnen.

Standardmäßig bittet Operator Sie, eine vorgeschlagene Navigation zu genehmigen, bevor Sie auf eine neue Seite weitergeleitet werden – genauso wie bei anderen vorgeschlagenen Aktionen. Um Operator ohne Ihre Genehmigung navigieren zu lassen, aktivieren Sie [Aktionen automatisch genehmigen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions).

## Was Operator erstellen kann {#what-operator-can-create}

Über die Generierung von Texten und Liquid hinaus kann Operator Ihnen beim Erstellen verschiedener anderer Objekte im gesamten Dashboard helfen, einschließlich, aber nicht beschränkt auf:

- Campaigns
- Canvases
- Content Blocks
- Angepasste Agents
- Angepasste Attribute und angepasste Events
- Dashboards
- Bilder
- Nachrichten und Nachrichten-Templates (siehe [Nachrichten generieren](#generate-messages) und [Nachrichten-Templates erstellen](#create-message-templates))
- Prognosen
- Berichte
- Segmente
- Segmenterweiterungen

{% alert note %}
Die Funktionen von Operator im gesamten Dashboard werden regelmäßig erweitert. **Fragen Sie Operator direkt** nach der aktuellsten Antwort darauf, was es leisten kann.
{% endalert %}

## Campaigns und Zielgruppen {#campaigns-and-audiences}

Operator kann Ihnen helfen, von einer Idee zu einer entworfenen Campaign oder Zielgruppe zu gelangen und beide zu verfeinern, sobald sie existieren. Alle Änderungen, die Operator an einer Campaign oder einem Segment vorschlägt, erscheinen als Aktionskarte, die Sie überprüfen, bevor sie gespeichert werden.

Um zu beginnen, suchen Sie nach der Option **Mit Operator erstellen**, wenn Sie eine Campaign oder ein Segment erstellen.

![Die Menüs „Campaign erstellen“ und „Segment erstellen“, die jeweils die Option „Mit Operator erstellen“ anzeigen.]({% image_buster /assets/img/operator/operator_create_with_operator.png %}){:style="max-width:90%"}

- **Campaigns erstellen und bearbeiten:** Wenn Sie eine Campaign starten, kann Operator Ihnen helfen, sie End-to-End aus einem einzigen Briefing in natürlicher Sprache zu entwerfen. Dies umfasst Zielgruppe, Inhalt und Zustellungseinstellungen. Sie können Operator auch bitten, Ihnen beim Bearbeiten einer bestehenden Campaign zu helfen, z. B. beim Anpassen des Targetings oder beim Aktualisieren des Nachrichteninhalts.
- **Vom Briefing zur Campaign:** Beschreiben Sie ein vollständiges Campaign-Briefing, und Operator hilft Ihnen, einen Entwurf zu erstellen, der Text, Bilder, Personalisierung, Targeting und Empfehlungen für den Sendezeitpunkt enthält. Überprüfen Sie den Entwurf im Campaign-Editor und verfeinern Sie ihn mit Folgeprompts, bevor Sie ihn starten.
- **Segmente erstellen und bearbeiten:** Wenn Sie ein Segment starten, beschreiben Sie die gewünschte Zielgruppe, und Operator hilft Ihnen, die Filterlogik aufzubauen – einschließlich Attributbedingungen, Event-Verlauf und Katalogabfragen. Operator kann Ihnen auch helfen, die Filter eines bestehenden Segments zu bearbeiten, wenn sich Ihre Targeting-Strategie ändert.
- **Segmenterweiterungen erstellen:** Operator kann Ihnen helfen, eine SQL-definierte [Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension) zu erstellen, indem es die Abfrage schreibt, die sie definiert. Beschreiben Sie die gewünschte Zielgruppenlogik, und Operator entwirft die Abfrage, die Sie überprüfen, bevor Sie sie speichern. Sie können Operator auch über die Übersicht der Segmenterweiterungen um Hilfe bitten. Weitere Informationen zu Operator und SQL finden Sie unter [SQL-Abfragen schreiben](#write-sql-queries).
- **Nutzer:innen importieren und verwalten:** Auf unterstützten Zielgruppenseiten kann Operator Ihnen helfen, [Nutzer:innen zu importieren]({{site.baseurl}}/user_guide/audience/manage_audience/import_users), [Nutzer:innen zu löschen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) und [doppelte Profile zusammenzuführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users). Überprüfen Sie jede vorgeschlagene Aktion, bevor sie gespeichert wird.

## Canvases {#canvases}

Operator kann Ihnen helfen, von einer Journey-Idee zu einem entworfenen [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) zu gelangen und ein bestehendes Canvas zu verfeinern. Alle Änderungen, die Operator vorschlägt, erscheinen als Aktionskarte, die Sie überprüfen, bevor sie gespeichert werden.

Beschreiben Sie die Journey in natürlicher Sprache. Operator erstellt einen Entwurf, der Eintrittskriterien, Schritte, Verzögerungen und Nachrichten enthalten kann. Sie können Operator auch bitten, ein bestehendes Canvas zu bearbeiten, z. B. einen Schritt hinzuzufügen oder Nachrichteninhalte zu aktualisieren. Überprüfen Sie den Entwurf im Canvas-Builder und verfeinern Sie ihn mit Folgeanweisungen, bevor Sie ihn starten.

Bitten Sie Operator beispielsweise, eine Warenkorb-Abbruch-Journey zu erstellen, die eine Stunde nach dem Warenkorb-Abbruch wartet, eine E-Mail-Erinnerung sendet und dann nach 24 Stunden einen Push sendet, wenn die Nutzer:innen noch nicht gekauft haben.

Sie können dies von jeder Dashboard-Seite aus starten. Wenn Sie sich noch nicht in Canvas befinden, [navigiert](#navigate-the-dashboard) Operator dorthin, um die Anfrage abzuschließen.

## Agents {#agents}

![Das Menü „Agent erstellen“, das die Option „Angepasster Agent“ und von Operator erstellte Agent-Templates zeigt.]({% image_buster /assets/img/operator/operator_create_agent.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

Operator kann Ihnen helfen, Agents in der [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents) zu erstellen und zu verfeinern. Alle Änderungen, die Operator an einem Agent vorschlägt, erscheinen als Aktionskarte, die Sie überprüfen, bevor sie gespeichert werden.

- **Einen Agent von Grund auf erstellen:** Operator hat Zugriff auf jedes Feld in der Agent Console, sodass Sie den gewünschten Agent beschreiben können und Operator Ihnen bei der Konfiguration hilft. Dies umfasst Anweisungen, Ausgabeeinstellungen und andere Agent-Felder.
- **Von einem Template starten:** Die Agent Console bietet eine Option **Agent mit Operator erstellen**, die einen vorgeschriebenen Prompt für einen gängigen Anwendungsfall lädt, z. B. Texterstellung, Sentimentanalyse, Journey-Routing oder Kataloganreicherung. Wählen Sie eine Kategorie, und Operator hilft Ihnen, einen Agent zu entwerfen, den Sie verfeinern können. Die vollständige Liste der Templates finden Sie unter [Mit Operator erstellte Agent-Templates]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).
- **Einen bestehenden Agent verfeinern:** Wenn Sie einen Agent bearbeiten, wählen Sie **Mit Operator generieren** oder **Mit Operator verfeinern** neben dem Anweisungsfeld des Agents, um Operators Hilfe beim Schreiben oder Überarbeiten des Agent-Prompts und der Ausgabeeinstellungen zu erhalten. Wenn der Agent bereits eine Markenrichtlinie hat, hängt Operator diese als Kontext an.

## Inhalt und Kreatives {#content-and-creative}

Operator kann den Inhalt Ihrer Nachrichten generieren und überprüfen – einschließlich Text, Nachrichten-HTML, Liquid und Bilder – und alle Markenrichtlinien anwenden, die Sie als Kontext hinzufügen. Sie können Operator auch über die Template-Bibliothek und Übersichtsseiten um Hilfe bitten. So können Sie beispielsweise [E-Mail-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates) oder Content Blocks über deren Listenseiten erstellen oder aktualisieren, Arbeit im [Content-Kalender]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/campaign_calendar) planen, [Farbprofil-Templates für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) erstellen oder [Banner-Platzierungen]({{site.baseurl}}/developer_guide/banners/placements) konfigurieren.

### Markenrichtlinien anwenden {#apply-brand-guidelines}

Fügen Sie [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) als Kontext im Operator-Chat-Panel hinzu, damit generierte Texte, Templates und Bilder zur Stimme, zum Ton und zum Stil Ihrer Marke passen.

### Texte generieren {#generate-copy}

Sie können Operator nutzen, um von überall aus Texte zu brainstormen oder zu generieren, aber das beste Erlebnis erhalten Sie, wenn Sie es direkt im Nachrichten-Editor verwenden, wo es Sie bei der Nachricht, die Sie erstellen, unterstützen kann. Beschreiben Sie Ihr Produkt oder Ihre Campaign, und Operator liefert Texte, die Sie überprüfen und einfügen können.

Operator verbessert den eigenständigen Copywriter auf mehrere Arten:

- Es wendet alle [Markenrichtlinien](#apply-brand-guidelines) an, die Sie als Kontext hinzufügen.
- Es nutzt [seitenbezogenen Kontext]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), sodass Sie den Kanal oder die Nachricht, an der Sie arbeiten, nicht erneut beschreiben müssen. Da es seitenbezogen ist, können Sie es auch verwenden, um eine bestehende Nachricht zu bearbeiten oder zu verfeinern, anstatt eine von Grund auf neu zu generieren.
- Es kann Ihre [angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) und Events nachschlagen, sodass Sie es bitten können, Textempfehlungen mit echtem Liquid zu personalisieren.
- Sie können das Gespräch fortsetzen und iterieren. Fragen Sie zum Beispiel nach einem anderen Ton, einer kürzeren Version oder einer Übersetzung.

#### Tonalität {#generate-copy-tones}

Die Tonalität des generierten Textes wird durch Ihren Prompt bestimmt. Beschreiben Sie den gewünschten Stil, und Operator passt seine Ausgabe entsprechend an. Fragen Sie zum Beispiel nach formell, locker, dringend oder auffällig. Sie können die Tonalität auch in Folgeprompts verfeinern, zum Beispiel nach einer entspannteren oder ausgefeilteren Version fragen. Wenn Sie Markenrichtlinien als Kontext hinzufügen, wendet Operator diese an, damit Texte konsistent mit der Stimme Ihrer Marke bleiben.

### Nachrichten generieren {#generate-messages}

Operator kann ein vollständiges Nachrichtendesign für jeden Kanal oder Editor mit einem HTML-Modus generieren, einschließlich, aber nicht beschränkt auf:

- E-Mail
- SMS/MMS/RCS
- In-App-Nachricht
- Content-Card
- Banner
- Push
- Webhook

Drag-and-Drop-Editoren unterstützen keine direkte Designgenerierung, obwohl Operator Ihnen weiterhin bei Texten oder anderen Inhalten helfen kann, die Sie manuell hinzufügen. Beschreiben Sie die gewünschte Nachricht in natürlicher Sprache, überprüfen Sie die Ausgabe und fügen Sie sie in Ihren Editor ein. Setzen Sie das Gespräch fort, um das Ergebnis zu verfeinern. Sie können zum Beispiel nach einem anderen Layout, kürzerem Text oder aktualisierten Button-Styles fragen, bevor Sie das HTML in den Editor einfügen.

Die besten Ergebnisse erzielen Sie, wenn Sie Operator in dem Editor verwenden, in dem Sie gerade arbeiten, da es dort [seitenbezogenen Kontext]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context) für den Kanal und den Nachrichtentyp hat. Wenn Sie Markenrichtlinien als Kontext hinzufügen, wendet Operator diese auf die generierte Nachricht an.

### Content Blocks erstellen {#create-content-blocks}

Operator kann Ihnen helfen, [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) zu erstellen – die wiederverwendbaren Inhaltsbausteine, die Sie in Nachrichten einfügen. Beschreiben Sie den gewünschten Block, und Operator entwirft seinen Inhalt, den Sie überprüfen, bevor Sie ihn speichern. Da Content Blocks geteilt werden, aktualisiert eine Änderung jede Nachricht, die darauf verweist.

Operator erstellt Content Blocks einzeln im Dashboard. Um Content Blocks in großen Mengen zu erstellen, verwenden Sie den Endpunkt [Content-Block erstellen]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) mit einem API-Schlüssel, der die Berechtigung `content_blocks.create` hat.

### Nachrichten-Templates erstellen {#create-message-templates}

Operator kann Ihnen helfen, wiederverwendbare [Nachrichten-Templates]({{site.baseurl}}/user_guide/messaging/templates) zu erstellen, die Sie in Campaigns verwenden können. Beschreiben Sie das gewünschte Template, und Operator entwirft es, damit Sie es überprüfen, bevor Sie es speichern. Sie können von überall in Braze starten. Die Generierung eines Templates funktioniert ähnlich wie die Generierung einer Nachricht – siehe [Nachrichten generieren](#generate-messages) für die unterstützten Kanäle und Editoren.

### Liquid generieren {#generate-liquid}

Operator ist mit der [Liquid-Syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) sehr leistungsfähig. Es kann komplexe Liquid-Logik generieren, die auf den Daten in Ihrem Workspace basiert – einschließlich der Suche nach Attribut-, Event- und [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs)-Daten, um Beispielwerte zu finden. Es kann auch das vorhandene Liquid in Ihren Campaigns überprüfen und erklären.

Wie bei der Texterstellung können Sie Operator von überall aus bitten, Liquid zu generieren, und es funktioniert über alle Kanäle und Nachrichten-Editoren hinweg. Die besten Ergebnisse erzielen Sie innerhalb eines Nachrichten-Editors, wo Operator den vollständigen Kontext der Nachricht hat, die Sie erstellen.

{% details Best Practices für Liquid-Prompts %}

#### Kontext geben {#generate-liquid-give-context}

Kontext hilft Operator, das Gesamtbild Ihres Projekts zu verstehen. Es ist hilfreich, Kontext wie den folgenden einzubeziehen:

- Ihren Unternehmensnamen und Ihre Branche
- Eine Campaign, an der Sie arbeiten, wie Black Friday oder Feiertagsverkäufe
- Ihr Ziel, wie die Steigerung Ihrer Click-through-Rate
- Bestimmte angepasste Attribute, die Sie in Ihre Nachricht aufnehmen möchten

Das Einbeziehen von Kontext in Ihren Prompt hilft Operator, seine Antworten besser auf Ihre Bedürfnisse abzustimmen. Sie können auch Details aus Ihrer Campaign, Ihrem Nachrichten-Briefing oder Ihrem Brainstorming-Dokument einfügen, um Operator auf den neuesten Stand zu bringen.

#### Spezifisch sein {#generate-liquid-be-specific}

Operator kann Rückfragen stellen, aber die Angabe von Details im Voraus kann schneller zu präziseren Ergebnissen führen. Erwägen Sie, Details wie die folgenden einzubeziehen:

- Bekannte Präferenzen oder Anforderungen für die Nachricht
- Anweisungen zum Umgang mit Situationen, wie fehlende Antworten von Empfänger:innen oder Fallback-Nachrichtenoptionen
- Genaue oder ähnliche Werte für die angepassten Attribute, die Sie verwenden möchten, die Operator helfen, genauere Logik zu generieren und zu testen
- Wenn Sie nach Liquid fragen, das Connected-Content verwendet, die Dokumentation für den API-Endpunkt, eine Beispiel-API-Antwort oder beides

#### Kreativ werden {#generate-liquid-get-creative}

Probieren Sie verschiedene Prompts aus, um zu sehen, wie Operator Ihr Messaging verbessern kann. Experimentieren Sie mit verschiedenen Prompts und Ideen, da Kreativität zu ansprechenderen Ergebnissen führen kann.

{% enddetails %}

### Bilder generieren {#generate-images}

Operator generiert Bilder mit [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), einem KI-System von OpenAI und einem Drittanbieter von Braze. Damit können Sie realistische Bilder und Kunst aus einer Beschreibung in natürlicher Sprache erstellen.

Wählen Sie in der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) im Panel **Upload Assets** die Option **Generate with Operator** aus. Beschreiben Sie das gewünschte Bild, und Operator generiert es und speichert es direkt in Ihrer Medienbibliothek.

#### Prompt-Tipps {#generate-images-prompt-tips}

- Beschreiben Sie das Motiv, den Stil, die Stimmung und die Farben konkret. Je mehr Details Sie angeben, desto besser das Ergebnis. Das Hochladen eines Referenzbildes wird nicht unterstützt.
- Wenn Sie [Markenrichtlinien](#apply-brand-guidelines) als Kontext in Ihrem Operator-Prompt anwenden, wendet Operator diese direkt auf das generierte Bild an, sodass das Ergebnis den visuellen Stil Ihrer Marke widerspiegelt.
- Bildgenerierungen werden zusammen mit anderen Operator-Aktionen auf das unternehmensweite tägliche Operator-Nutzungslimit angerechnet. Weitere Informationen finden Sie unter [Einschränkungen](#limitations).

### Inhaltsqualität überprüfen {#review-content-quality}

Wählen Sie auf dem **Test**-Tab für SMS, Android-Push, iOS-Push und traditionelle In-App-Nachrichten **Review with Operator** aus, um Ihre Inhalte vor dem Senden zu überprüfen. Standardmäßig prüft Operator Ihre Campaign auf Rechtschreib- und Grammatikfehler, markenfremden oder unangemessenen Ton, anstößige Sprache sowie fehlerhaften Code, Testinhalte oder nicht gerendertes Liquid und empfiehlt, wie gefundene Probleme behoben werden können. Sie können Operator auch direkt in Ihrem Prompt bitten, die Überprüfung Ihrer Inhalte anzupassen.

Über die Standardüberprüfung hinaus können Sie Operator auf bestimmte Prüfungen ausrichten. Erwägen Sie, es auf Folgendes prüfen zu lassen:

- **Rechtschreibung und Grammatik:** Prüfung auf Rechtschreib- und Grammatikfehler und Vorschlag von Korrekturen, die die Genauigkeit Ihrer Inhalte verbessern.
- **Tonalität:** Bewertung, ob die Tonalität zu Ihrem beabsichtigten Kommunikationsstil passt, und Markierung von allem, was missverstanden werden könnte.
- **Anstößige Sprache:** Suche nach potenziell anstößiger oder unangemessener Sprache, damit Sie diese überarbeiten und Ihr Messaging respektvoll halten können.
- **Unbeabsichtigte Inhalte:** Erkennung von fehlerhaftem Code, Markup oder Testnachrichten, die unbeabsichtigt hinzugefügt wurden, einschließlich Liquid, das für eine:n Testnutzer:in nicht gerendert wurde.
- **Andere Sprachen:** Überprüfung von Inhalten in einer anderen Sprache. Die Unterstützung für nicht-englische Inhalte kann variieren, daher überprüfen Sie die Ergebnisse sorgfältig.

#### Best Practices {#review-content-quality-best-practices}

Beachten Sie Folgendes, um die Inhaltsüberprüfung optimal zu nutzen:

- **Lesen Sie Ihre Nachricht Korrektur:** Obwohl die Inhaltsüberprüfung helfen kann, Fehler zu identifizieren, ist es weiterhin wichtig, Ihre Inhalte manuell Korrektur zu lesen. Nutzen Sie die KI-generierten Vorschläge als hilfreiche Orientierung, aber verlassen Sie sich auf Ihr eigenes Urteil, um die Genauigkeit sicherzustellen.
- **Verstehen Sie die Tonalitätsanalyse:** Die Ergebnisse der Tonalitätsanalyse sind subjektiv und basieren auf dem Verständnis des KI-Modells. Obwohl sie nützliche Insights liefern können, berücksichtigen Sie Ihre beabsichtigte Tonalität und den Gesprächskontext, um angemessene Anpassungen vorzunehmen.
- **Überprüfen Sie markierte anstößige Sprache:** Die Erkennung anstößiger Sprache ist darauf ausgelegt, robust zu sein, kann aber gelegentlich falsch-positive Ergebnisse liefern. Überprüfen Sie markierte Abschnitte sorgfältig und nehmen Sie bei Bedarf entsprechende Änderungen vor.

## Datenautomatisierung und -suche {#data-automation-and-lookup}

Operator kann als Referenz für Ihre Workspace-Daten und die Braze-Dokumentation dienen, SQL schreiben, wenn Sie diese Daten direkt abfragen müssen, und den Code generieren, der eingehende Daten – wie eine Webhook-Payload – in ein Format transformiert, das Braze verwenden kann.

### Was Operator nachschlagen kann {#what-operator-can-look-up}

Operator kann Folgendes referenzieren, um Fragen zu beantworten oder die generierten Inhalte zu fundieren, einschließlich, aber nicht beschränkt auf:

- Braze-Dokumentation
- [Segmente]({{site.baseurl}}/user_guide/audience/segments)
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) und [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs)-Daten
- Bestehende [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns)- und [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)-Konfigurationen, wie Targeting- und Zustellungseinstellungen
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Aktionscodes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)
- [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)-Antworten
- [Agents]({{site.baseurl}}/user_guide/brazeai/agents)

Fragen Sie Operator direkt, wenn Sie nicht sicher sind, ob es eine bestimmte Information nachschlagen kann.


### Performance-Daten analysieren {#analyze-performance-data}

Stellen Sie Operator Fragen in natürlicher Sprache zur Performance Ihrer Campaigns und Canvases, und es liefert Charts, Vergleiche und kurze Insights auf Basis Ihrer Workspace-Daten. Im Gegensatz zu den seitenabhängigen Features von Operator, die Kontext von der aktuellen Seite benötigen, beantwortet „Analyze“ Fragen von überall im Dashboard. Weitere Informationen finden Sie unter [Operator Analyze]({{site.baseurl}}/user_guide/brazeai/operator/analyze).

### Berichte und Dashboards erstellen {#build-reports-and-dashboards}

Operator kann Ihnen helfen, [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder)-Berichte und [Dashboard-Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)-Dashboards auf Basis einer Beschreibung in natürlicher Sprache zu erstellen. Beschreiben Sie die gewünschten Metriken, Kanäle und den Zeitraum, und Operator entwirft den Bericht oder das Dashboard, das Sie überprüfen, bevor Sie es speichern.

Fragen Sie zum Beispiel: „Erstelle mir einen Bericht, der das SMS-Engagement meines Workspace der letzten 30 Tage zeigt.“

### Prognosen erstellen {#create-predictions}

Operator kann Ihnen helfen, [Predictive-Abwanderung]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn)-Prognosen und [KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai) anzuzeigen und zu erstellen. Beschreiben Sie das gewünschte Ergebnis, und Operator schlägt die Prognose oder Empfehlung vor, die Sie überprüfen können.

### SQL-Anfragen schreiben {#write-sql-queries}

Operator kann Ihnen helfen, SQL für [Segmenterweiterungen](#campaigns-and-audiences) und für [Abfrage-Templates]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) im Query Builder zu schreiben. Beschreiben Sie die gewünschte Abfrage in natürlicher Sprache, und Operator generiert SQL, das Sie überprüfen, bevor Sie es ausführen.

### Datentransformationscode generieren {#generate-data-transformation-code}

Wählen Sie im [Datentransformations]({{site.baseurl}}/user_guide/data/unification/data_transformation)-Editor **Insert Code** aus, um Transformationscode zu generieren, der eine eingehende Webhook-Payload in gültige Braze-API-Anfragen umwandelt. Schritt-für-Schritt-Anleitungen zum Erstellen einer Transformation finden Sie unter [Transformation erstellen]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

## Workspace-Einstellungen {#workspace-settings}

Operator kann Einstellungen auf mehreren Workspace-Konfigurationsseiten überprüfen und aktualisieren. Beschreiben Sie die gewünschte Änderung, und Operator schlägt sie als Aktionskarte vor, die Sie überprüfen, bevor sie gespeichert wird. Unterstützte Einstellungsseiten umfassen unter anderem:

- [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- [Push-Einstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings)
- [Messaging-Rate-Limits]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)
- [Genehmigungsworkflows]({{site.baseurl}}/user_guide/messaging/governance/approvals), einschließlich [Messaging-Regeln]({{site.baseurl}}/user_guide/messaging/governance/approvals/messaging_rules) und Always-on-Genehmigung
- [APIs und Bezeichner]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers), einschließlich [andere Bezeichner]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers#other-identifiers), API-Limits und [API-Nutzungsbenachrichtigungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts)
- [Kontaktinformationen in den Admin-Einstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/contact_information)
- [Sicherheitseinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings) und [SCIM-Bereitstellung]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning)
- [Rollen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role) und [Berechtigungssets]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set)
- [Export-Protokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/exports_log)
- Nachrichtenpriorisierungskategorien

{% alert note %}
Die Abdeckung von Einstellungsseiten durch Operator wird regelmäßig erweitert. **Fragen Sie Operator direkt**, um die aktuellste Auskunft darüber zu erhalten, was konfiguriert werden kann.
{% endalert %}

## Einschränkungen {#limitations}

{% alert note %}
Die Abdeckung von Operator ändert sich häufig. Wenn Sie nicht sicher sind, ob ein bestimmter Bildschirm oder Workflow unterstützt wird, fragen Sie Operator direkt.
{% endalert %}

Die Dashboard-Unterstützung von Operator ist umfassend, hat aber Grenzen.

- **Canvases:** Operator kann [Canvases erstellen und bearbeiten](#canvases) – im aktuellen Canvas-Editor. Der [ursprüngliche Canvas-Editor]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), das Starten eines Canvas von der Template-Auswahlseite oder die Verwendung von **Vorschau als Nutzer:in** beim Erstellen von Canvases werden nicht unterstützt. Operator kann dennoch die Konfiguration eines bestehenden Canvas referenzieren – wie Targeting- und Zustellungseinstellungen –, um Fragen zu beantworten und seine Ausgabe zu fundieren.
- **Campaign-Duplizierung:** Operator kann keine bestehende Campaign aus der Campaign-Listenansicht duplizieren. Um eine ähnliche Campaign zu erstellen, bitten Sie Operator, eine neue von Grund auf zu erstellen, oder duplizieren Sie die Campaign manuell über das Menü **Weitere Aktionen** in der Listenansicht.
- **Drag-and-Drop-Editoren:** Operator kann kein Nachrichtendesign direkt in einem Drag-and-Drop-Editor generieren oder einfügen, wie z. B. in den Editoren für [E-Mail]({{site.baseurl}}/user_guide/channels/email/drag_and_drop), [Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner) und [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop). Wechseln Sie zum entsprechenden HTML-Editor, um Operator zu verwenden, oder bitten Sie Operator, Inhalte wie Texte zu generieren, die Sie manuell einfügen können. Siehe [Nachrichten generieren](#generate-messages) für unterstützte Kanäle und Editoren.
- **Bildschirmsichtbarkeit:** Operator nutzt seitenbezogenen Kontext, um zu verstehen, was Sie betrachten, einschließlich Inhalten in unterstützten Vorschauen und Editoren. Wenn ein Teil einer Seite außerhalb dessen liegt, was Operator lesen kann, teilt es Ihnen dies mit, anstatt zu raten, sodass Sie wissen, dass Sie diesen Inhalt selbst beschreiben müssen.
- **Nutzungslimits:** Operator hat ein unternehmensweites tägliches Nutzungslimit, das alle 24 Stunden zurückgesetzt wird. Alle Operator-Aktionen werden auf dieses Limit angerechnet, und der Verbrauch skaliert mit dem Umfang dessen, was Operator lesen und erzeugen muss. Fragen stellen, Informationen nachschlagen und [ein Support-Ticket erstellen]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets) verbrauchen weniger. Das Erstellen oder Bearbeiten von Objekten wie Campaigns und Segmenten verbraucht mehr. [Bildgenerierungen](#generate-images) werden ebenfalls auf dieses Limit angerechnet. Wenn das Limit erreicht ist, erscheint die Meldung „Tägliches Limit erreicht“ und Operator verarbeitet keine weiteren Anfragen, bis das Limit zurückgesetzt wird. Schritte zur Fehlerbehebung finden Sie unter [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting).

## Frühere Assistenten {#legacy-assistants}

Vor Operator waren mehrere KI-Features als eigenständige Assistenten verfügbar: der KI Copywriter, der KI Liquid Assistant, der KI Image Generator, der KI SQL Generator, der Data Transformations KI Copilot und die Inhaltsüberprüfung. Alle ihre Einstiegspunkte bleiben erhalten und leiten zu Operator weiter, sodass Ihre bestehenden Workflows nicht beeinträchtigt werden. Was diese heute leisten, erfahren Sie unter [Inhalt und Kreatives](#content-and-creative) und [Datenautomatisierung und -suche](#data-automation-and-lookup).

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Datenschutz und Sicherheit {#data-privacy-and-security}

Operator integriert sich mit OpenAI, um Ausgaben zu generieren. Weitere Informationen darüber, welche Daten Braze an OpenAI sendet, wie diese Daten verwendet werden und Ihre Rechte an geistigem Eigentum finden Sie unter [Wie Daten mit OpenAI verwendet werden]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security).

## Nächste Schritte {#next-steps}

- [Erste Schritte mit Operator]({{site.baseurl}}/user_guide/brazeai/operator): Zugriff auf und Nutzung von Operator
- [Prompt-Bibliothek]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): Fertige Beispiel-Prompts durchstöbern
- [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Vorgeschlagene Änderungen von Operator überprüfen und genehmigen
- [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Häufige Probleme und Lösungen nachschlagen