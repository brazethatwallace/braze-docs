---
nav_title: JustAI
article_title: JustAI
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und JustAI, einer KI-basierten SaaS-Unternehmensplattform, die personalisierte Versionen bestehender Campaigns erstellt und Betreffzeilen, kreative Inhalte und HTML-E-Mail-Layouts im Laufe der Zeit optimiert."
alias: ["/partners/just_ai/", "/partners/just_words/"]
page_type: partner
---

# JustAI-Integrationsleitfaden {#justai-integration-guide}

> [JustAI](https://www.getjust.ai/) hyper-personalisiert Messaging in großem Umfang über Lifecycle-Marketing-Kanäle und ermöglicht es Ihnen, dynamisch Hunderte von Varianten zu testen und leistungsschwache Inhalte automatisch zu aktualisieren.

Wenn Sie JustAI mit Braze [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) verwenden, um Ihre bestehenden Braze-Campaigns und Canvases zu personalisieren, nutzt JustAI Braze-Currents, um die Inhalte dynamisch zu optimieren – so müssen Sie es nicht selbst tun.

## Welche Vorteile bietet die Integration? {#what-are-the-benefits}

Nach Abschluss Ihrer Integration können Sie die JustAI-Plattform nutzen, um:

- Realtime-Experimentergebnisse einzusehen
- Texte dynamisch zu bearbeiten
- Performance-Insights anzuzeigen

{% alert note %}
Fragen? Kontaktieren Sie JustAI über ihre [Buchungsseite](https://www.getjust.ai/book-demo) oder über den gemeinsamen Slack-Kanal.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| JustAI-Konto | Ein [JustAI](https://www.getjust.ai/)-Konto ist erforderlich, um diese Partnerschaft zu nutzen. Wenn Sie kein JustAI-Konto haben, [vereinbaren Sie ein 30-minütiges Onboarding-Gespräch](https://www.getjust.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## JustAI mit Braze integrieren {#integrating-justai-with-braze}

### 1. Schritt: Ein JustAI-Template erstellen {#step-1-create-a-justai-template}

1. Gehen Sie zu Ihrer JustAI-Konsole und [erstellen Sie ein neues Template](https://console.getjust.ai/new).
2. Wählen Sie eine leicht zu merkende ID, die nur Buchstaben, Zahlen und Unterstriche enthält.
3. Füllen Sie die grundlegenden Campaign-Details aus.
4. Verwenden Sie KI, um personalisierte Varianten zu generieren.

![Die JustAI-Template-Erstellungsplattform.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### 2. Schritt: Einen JustAI-API-Schlüssel erstellen {#step-2-create-a-justai-api-key}

1. Gehen Sie zu **Org Settings** > **API Keys** > **Generate API Key**.
2. Kopieren Sie den API-Schlüssel und speichern Sie ihn an einem sicheren Ort.

![Das JustAI-API-Schlüssel-Formular.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### 3. Schritt: JustAI in Ihren Braze-Inhalten verwenden {#step-3-use-justai-in-your-braze-content}

JustAI funktioniert mit Canvases und Campaigns über Connected-Content. Wenn Sie ein Canvas erstellen, sollte jeder E-Mail-Schritt einem eindeutigen JustAI-Template entsprechen.

#### Schritt 3.1: Ihren A/B-Test einrichten {#step-31-set-up-your-ab-test}

{% tabs %}
{% tab Canvas %}

1. Wählen Sie in einem Canvas **Variante hinzufügen** > **Variante hinzufügen**, bis Sie die gewünschte Anzahl an Varianten haben, und fügen Sie jeder Variante Schritte hinzu (z. B. einen E-Mail-Nachrichtenschritt).
2. Teilen Sie den Zielgruppen-Traffic nach Wunsch auf. Wenn Sie beispielsweise zwei Varianten haben, könnten Sie jeder 50 % zuweisen. Oder Sie könnten zwei Varianten mit jeweils 40 % und eine Kontrollgruppe mit 20 % haben. Weitere Informationen zu A/B-Tests für Canvases finden Sie unter [Ein Canvas erstellen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. Fügen Sie in den Editoren der Nachrichtenschritte, die Sie mit Connected-Content verwenden möchten, das Connected-Content-Snippet aus der JustAI-Konsole ein, wie z. B. das folgende Snippet.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Braze-A/B-Test-Canvas-Einrichtung.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. Erstellen Sie im Schritt **Compose Messages** Ihrer Campaign zwei Varianten.
2. Gehen Sie im Schritt **Target Audience** zum Abschnitt **A/B Testing** und passen Sie die Prozentsätze der Nutzer:innen an, die jede Ihrer Varianten (und Ihre optionale Kontrollgruppe) erhalten sollen. Sie können Ihren Test weiter anpassen, indem Sie eine Optimierungsoption auswählen. Weitere Informationen zu A/B-Tests für Campaigns finden Sie unter [Multivariate und A/B-Tests erstellen]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. Fügen Sie im Nachrichten-Editor das Connected-Content-Snippet aus der JustAI-Konsole ein. Das folgende Liquid-Snippet zeigt ein Beispiel dafür.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Schritt 3.2: Personalisierung mit angepassten Attributen hinzufügen (optional) {#step-32-add-personalization-with-custom-attributes-optional}

Um Ihre Nachrichten mit angepassten Attributen (wie `industry`) zu personalisieren, verwenden Sie das folgende Liquid-Format:

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Beachten Sie, dass das angepasste Attribut `industry` durch {% raw %}`&attrs.industry={{ custom_attribute.industry }}`{% endraw %} angegeben wird.

![Braze-Liquid-Logik in einem HTML-Nachrichten-Editor.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### 4. Schritt: E-Mail-Vorschau anzeigen {#step-4-preview-the-email}

Stellen Sie sicher, dass Sie die E-Mail in Braze in der Vorschau anzeigen, um zu bestätigen, dass der personalisierte Inhalt korrekt dargestellt wird.

![Braze-Nachrichtenvorschau für eine JustAI-E-Mail.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### 5. Schritt: Braze-Currents einrichten {#step-5-set-up-braze-currents}

Braze-Currents ermöglicht Performance-Tracking und Optimierung im Laufe der Zeit.

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Wählen Sie **Create New Test Current** und dann **Test Amazon S3 Data Export**.

![Dropdown „Create New Test Current“ mit der Option „Test Amazon S3 Data Export“.]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3. Geben Sie die S3-Zugangs-ID, den AWS-Secret-Access-Key, den Bucket-Namen und den Ordner ein, die Ihnen von JustAI während des Onboardings bereitgestellt wurden.

![Abschnitt „Zugangsdaten“ für den AWS-Secret-Access-Key.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4. Wählen Sie die zu trackenden Ereignisse aus, wie z. B. Sends, Öffnungen, Klicks, Abmeldungen, Conversions und andere.

![Abschnitt „Message Engagement Events“ mit auswählbaren Ereignissen.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5. Starten Sie den Braze-Current.

Das war's! Jetzt können Sie JustAI mit Braze Connected-Content verwenden.