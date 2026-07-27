---
nav_title: Das Dashboard
article_title: Das Braze-Dashboard
page_order: 1
page_type: reference
description: "Das Braze-Dashboard ist Ihr zentraler Workspace zum Erstellen, Verwalten und Analysieren von Customer-Engagement. Es vereint Messaging-Tools, Zielgruppen-Insights, Segmentierung und Realtime-Performance-Daten an einem Ort."

---

# Das Braze-Dashboard {#the-braze-dashboard}

> Das Braze-Dashboard ist Ihr zentraler Workspace zum Erstellen, Verwalten und Analysieren von Customer-Engagement. Greifen Sie darauf zu unter [dashboard.braze.com](https://dashboard.braze.com/) oder [dashboard.braze.eu](https://dashboard.braze.eu/).

Nutzen Sie das Braze-Dashboard, um Campaigns zu planen, Nachrichten zu starten und zu verwalten, Zielgruppen-Insights zu erkunden, die Segmentierung anzupassen und Realtime-Performance- und Engagement-Metriken über eine einzige Schnittstelle zu überprüfen.

## Dashboard-Übersicht {#dashboard-overview}

Wenn Sie sich anmelden, bietet das Dashboard eine zentrale Ansicht Ihrer Engagement-Tools und Daten:

- **Startseite:** Zeigt Ihre [zuletzt bearbeiteten Inhalte](#pick-up-where-you-left-off) und wichtige Performance-Metriken auf einen Blick
- **Linke Navigation:** Organisiert Tools nach Funktion (Messaging, Zielgruppe, Analytics, Einstellungen)
- **Globaler Header:** Bietet schnellen Zugriff auf Suche, Support, Spracheinstellungen, Benachrichtigungen und Ihr Konto

Ihr Dashboard-Erlebnis ist nach [Workspaces]({{site.baseurl}}/user_guide/get_started/workspaces) organisiert, die Ihnen helfen, Inhalte für verschiedene Marken, Regionen oder Teams zu verwalten. Sie können jederzeit über die Seitennavigation [zwischen Workspaces wechseln](#workspace-switcher).

## Auf Ihr Dashboard zugreifen {#access-your-dashboard}

Um loszulegen, [melden Sie sich bei Ihrem Braze-Konto an]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Ihr Zugriff auf Seiten innerhalb des Dashboards und die Berechtigung, bestimmte Aktionen auszuführen, basieren auf Ihren zugewiesenen [Nutzer:innen-Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions). Wenn Sie Hilfe bei Ihren Berechtigungen benötigen, wenden Sie sich an Ihre Braze-Administrator:innen.

## In Braze navigieren {#navigate-braze}

Die Braze-Navigation ist so konzipiert, dass Sie effizient auf Features und Inhalte über verschiedene Geräte zugreifen können. Es gibt zwei Navigationsebenen im Braze-Dashboard: den globalen Header und die Seitennavigation.

Der globale Header ist fast immer oben auf dem Bildschirm sichtbar. Er bietet schnellen Zugriff auf wichtige Tools und Einstellungen, darunter:

- [Suche](#search-your-dashboard)
- Support- und Community-Links
- [Dashboard-Sprache]({{site.baseurl}}/user_guide/administer/personal/language_settings)
- Benachrichtigungen
- Kontoeinstellungen
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)

### Die Seitennavigation verwenden {#use-the-side-navigation}

Das vertikale Menü auf der linken Seite organisiert Braze-Tools nach Funktion und hält Ihre meistgenutzten Elemente in Reichweite. Wählen Sie einen Hauptmenüpunkt aus, um seine Optionen in einem gestapelten vertikalen Layout anzuzeigen.

![Workspace-Umschalter im Braze-Dashboard]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Workspace-Umschalter {#workspace-switcher}

Der Workspace-Umschalter befindet sich oben in der Seitennavigation und ermöglicht es Ihnen, zwischen verschiedenen Workspaces in Ihrer Braze-Instanz zu wechseln. Der aktive Workspace ist hervorgehoben.

[Workspaces]({{site.baseurl}}/user_guide/get_started/workspaces) helfen dabei, Inhalte nach Marke, Region, Produktlinie oder Team zu organisieren. Jeder Workspace umfasst eigene Daten, Campaigns und Einstellungen. Ihr Zugriff kann zwischen Workspaces variieren. Beispielsweise könnten Sie in einem Workspace Bearbeitungszugriff und in einem anderen nur schreibgeschützten Zugriff haben.

Um den Workspace zu wechseln, wählen Sie das Workspace-Dropdown oben in der Seitennavigation und wählen Sie den gewünschten Workspace aus. Sie können auch [bevorzugte Workspaces hinzufügen](#favorite-workspaces), um schneller auf die am häufigsten genutzten zuzugreifen.

#### Seitennavigation minimieren {#minimize-the-side-navigation}

Um visuelle Unordnung zu reduzieren, insbesondere bei Aufgaben wie dem Entwerfen eines Canvas, können Sie das Seitennavigations-Panel minimieren. Klicken Sie auf **Menü minimieren**, um es einzuklappen. Auch im minimierten Zustand können Sie über jedes Symbol hovern, um Tooltips mit den Menüpunktnamen anzuzeigen. So können Sie schnell zwischen Tools wechseln und gleichzeitig Ihren Workspace übersichtlich halten.

![Symbole zum Minimieren und Maximieren des Menüs]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Responsive Navigation {#responsive-navigation}

Die Navigation passt sich nahtlos an verschiedene Bildschirmgrößen an. Auf kleineren Bildschirmen wird die Seitennavigation automatisch eingeklappt. Drücken Sie <i class="fa-solid fa-bars" aria-label="Navigationsmenü öffnen"></i>, um das Menü bei Bedarf zu öffnen.

![Auf kleineren Bildschirmen wird die Seitennavigation automatisch eingeklappt. Durch Tippen auf das Menüsymbol werden die Navigationsoptionen geöffnet.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Ihr Dashboard durchsuchen {#search-your-dashboard}

Die globale Suchleiste im Header ist der schnellste Weg, um Inhalte in Ihrem Braze-Dashboard zu finden. Wählen Sie sie aus, um die Suchoberfläche zu öffnen und direkt zu dem zu springen, was Sie benötigen.

![Globale Suche geöffnet ohne eingegebene Suchbegriffe, mit Anzeige der zuletzt geöffneten Seiten.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Ihre zuletzt geöffneten Inhalte erscheinen unterhalb der Suchleiste. Dazu gehören alle Campaigns, Canvases, Templates oder Seiten, mit denen Sie kürzlich interagiert haben – so können Sie leicht zu Ihrer Arbeit zurückkehren.

### Wonach können Sie suchen? {#what-can-you-search-for}

Sie können nach den folgenden Elementen und Aktionen suchen:

- Campaign-Namen
- Canvas-Namen
- Content Blocks
- Segment-Namen
- E-Mail-Template-Namen
- Seiten innerhalb von Braze (einschließlich Synonyme)

{% alert tip %}
Um nach exaktem Text zu suchen, setzen Sie Ihren Suchbegriff in Anführungszeichen (""). Beispielsweise gibt die Suche nach ["all users"] alle Elemente zurück, die den exakten Ausdruck „all users“ in ihrem Namen enthalten.
{% endalert %}

### Inhaltstyp- und Status-Tags {#content-type-and-status-tags}

Jedes Ergebnis ist mit einem Tag versehen, das den Inhaltstyp angibt – wie Campaign, Canvas oder Segment – sowie den Status (aktiv, archiviert, gestoppt).

### Nach aktiven Inhalten und Entwürfen filtern {#filter-for-active-and-draft-content}

Standardmäßig umfasst die Suche aktive, Entwurfs- und archivierte Elemente. Verwenden Sie den Schalter **Show active and draft only**, um Ihre Ergebnisse einzugrenzen.

![Der Schalter „Show active and draft only“.]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Tastaturkürzel {#keyboard-shortcuts}

Sie können sich mit der Tastatur durch die Suchergebnisse bewegen.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Aktion                           | Tastaturkürzel                                                                |
| -------------------------------- | ----------------------------------------------------------------------------- |
| Suchmenü öffnen                  | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/}  |
| Zwischen Suchergebnissen bewegen | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Ein Suchergebnis auswählen       | <kbd>Enter</kbd>    |
| Suchmenü schließen               | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tastaturkürzel" }

## Produktivitäts-Features {#productivity-features}

Das Braze-Dashboard enthält mehrere Features, die Ihnen helfen, effizienter zu arbeiten und schnell auf die Tools und Inhalte zuzugreifen, die Sie am häufigsten nutzen.

### BrazeAI Operator

BrazeAI Operator™ ist ein KI-gestützter Assistent, der in das Dashboard integriert ist. Nutzen Sie ihn, um Antworten zu erhalten, Einrichtungsschritte durchzugehen, Probleme zu beheben und Ideen zu entwickeln. Öffnen Sie ihn über **BrazeAI Operator™** im globalen Header neben Ihrem Profil. Weitere Informationen finden Sie unter [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator).

### Dort weitermachen, wo Sie aufgehört haben {#pick-up-where-you-left-off}

Auf der **Startseite** zeigt das Dashboard Ihre zuletzt bearbeiteten oder erstellten Campaigns, Canvases und Segments an. So können Sie leicht zu laufenden Arbeiten zurückkehren, ohne suchen zu müssen. Jedes Element enthält Tags, die den Inhaltstyp und Status anzeigen (z. B. Entwurf, aktiv oder gestoppt).

![Ein Canvas-Entwurf, ein aktives Segment und ein Campaign-Entwurf im Abschnitt „Dort weitermachen, wo Sie aufgehört haben“.]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

Weitere Informationen finden Sie unter [Start-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/home#pick-up-where-you-left-off).

### Bevorzugte Workspaces {#favorite-workspaces}

Wenn Sie mit mehreren Workspaces arbeiten, können Sie die am häufigsten genutzten als Favoriten markieren. Bevorzugte Workspaces erscheinen oben im Workspace-Umschalter für schnelleren Zugriff.

So fügen Sie bevorzugte Workspaces hinzu:

1. [Greifen Sie auf Ihre Profileinstellungen zu](#access-your-profile-settings).
2. Suchen Sie im Abschnitt **Kontoprofil** das Feld **Bevorzugte Workspaces**.
3. Wählen Sie die Workspaces aus, die Sie als Favoriten markieren möchten.

### Auf Ihre Profileinstellungen zugreifen {#access-your-profile-settings}

So verwalten Sie Ihre Kontoeinstellungen, Benachrichtigungspräferenzen und persönlichen Informationen:

1. Wählen Sie Ihr Profilsymbol im globalen Header aus.
2. Wählen Sie **Konto verwalten**, um auf Ihre Profilseite zuzugreifen.

Von Ihrer Profilseite aus können Sie Ihre E-Mail-Einstellungen aktualisieren, die Zwei-Faktor-Authentifizierung konfigurieren, Ihre API-Schlüssel einsehen und andere Kontodetails verwalten.

## Barrierefreiheit im Dashboard {#accessibility-in-the-dashboard}

Das Braze-Dashboard verwendet Markenfarben, die den WCAG-AA-Standards für Farbkontrast entsprechen. Dies unterstützt ein inklusives Erlebnis für alle Nutzer:innen und entspricht den Best Practices für Barrierefreiheit.

## Feedback teilen {#sharing-feedback}

Möchten Sie uns Ihre Meinung mitteilen? Sie können Feedback zu Navigation, Barrierefreiheit, Benutzerfreundlichkeit, visuellem Design und mehr teilen. Öffnen Sie das **Support**-Menü im globalen Header und wählen Sie **Share feedback**. Wir prüfen jedes Feedback, um Ihr Braze-Erlebnis zu verbessern.

## Verwandte Ressourcen {#related-resources}

### Administrative Aufgaben {#administrative-tasks}

- [Workspaces erstellen und verwalten]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)
- [Braze-Nutzer:innen verwalten]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)
- [Nutzer:innen-Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)
- [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)

### Wichtige Aufgaben und nächste Schritte {#key-tasks-and-next-steps}

- **Campaigns erstellen**: [Eine Campaign erstellen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- **Journeys erstellen**: [Einen Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- **Zielgruppen definieren**: [Ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)
- **Performance überprüfen**: [Analytics-Übersicht]({{site.baseurl}}/user_guide/analytics/dashboards/home)
- **Einstellungen konfigurieren**: [App-Einstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings)