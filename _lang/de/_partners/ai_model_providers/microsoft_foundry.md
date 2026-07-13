---
nav_title: Microsoft Foundry
article_title: Microsoft Foundry
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Microsoft Foundry, mit der Sie in Foundry verwaltete KI-Modelle mit Braze verbinden können, um sie mit benutzerdefinierten KI-Agenten zu verwenden."
alias: /partners/microsoft_foundry/
page_type: partner
search_tag: Partner

---

# Microsoft Foundry

> [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) ist ein einheitliches Azure-Platform-as-a-Service-Angebot für Enterprise-KI-Betrieb, Modellentwicklung und Anwendungsentwicklung.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Microsoft Foundry integration' %}

## Über die Integration {#about-the-integration}

Die Integration von Braze und Microsoft Foundry ermöglicht es Ihnen, generative KI-Modelle, die in Microsoft Foundry verwaltet werden, beim Erstellen benutzerdefinierter KI-Agenten zu verwenden. Die Integration unterstützt derzeit zwei Modelle: gpt-5.4-mini und gpt-5.4-nano. Mit dieser Integration können Ihre Agenten personalisierte Texte generieren, Realtime-Entscheidungen treffen oder Katalogfelder mithilfe von Foundry-verwalteten Modellen aktualisieren.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| Ein Azure-Konto mit einem aktiven Abo | Wenden Sie sich an Ihre:n Administrator:in oder lesen Sie die [Azure-Kontooptionen](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account). |
| Microsoft Foundry-Instanz | Eine Microsoft Foundry-Instanz zum Erstellen eines Projekts. |
| Microsoft Foundry-Projekt | Ein Projekt innerhalb Ihrer Foundry-Instanz, das die bereitgestellten Modelle enthält. |
| Bereitgestellte Modelle | Mindestens eines der unterstützten Modelle, das innerhalb des Foundry-Projekts bereitgestellt wurde. |
| Braze-Instanz | Sie finden Ihre Braze-Instanz auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints) oder bei Ihrer/Ihrem Braze-Onboarding-Manager:in. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Unterstützte Modelle in Foundry bereitstellen {#deploy-supported-models-in-foundry}

Die Braze-Integration mit Microsoft Foundry unterstützt zwei Modelle: gpt-5.4-mini und gpt-5.4-nano. Beide müssen in einem Foundry-Projekt innerhalb der Foundry-Instanz bereitgestellt werden, die Sie integrieren.

Um das Foundry-Projekt zu erstellen und die Modelle bereitzustellen, folgen Sie der [Microsoft Foundry-Dokumentation](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal):

1. Melden Sie sich über Ihr Azure-Portal bei Microsoft Foundry an.
2. Erstellen Sie in Microsoft Foundry ein Projekt, das die Modelle enthält, die Sie mit Braze integrieren möchten.
3. Entscheiden Sie, ob Sie gpt-5.4-mini, gpt-5.4-nano oder beide verwenden möchten.
4. Stellen Sie jedes gewünschte Modell mithilfe der Microsoft Foundry-Dokumentation bereit. Ändern Sie nicht den Standard-Bereitstellungsnamen, da die Integration für dieses Modell sonst möglicherweise nicht funktioniert.

## Integration

So verbinden Sie Ihre Foundry-Instanz mit Braze:

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie **Microsoft Foundry**.
2. Geben Sie Ihren **Microsoft Foundry-API-Schlüssel** ein.
3. Geben Sie den **Namen Ihrer Microsoft Foundry-Instanz** ein. Dies ist die Subdomain vor `.services.ai.azure.com`.
4. Wählen Sie **Speichern**.

Nach dem Speichern zeigt Braze einen Verbindungsstatus mit Datum und Uhrzeit der Verbindung an. Sie können Foundry-Modelle auswählen, wenn Sie in der Agentenkonsole [einen benutzerdefinierten Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

{% alert important %}
Um gpt-5.4-mini oder gpt-5.4-nano zu verwenden, müssen Sie jedes Modell in Ihrem Foundry-Projekt bereitstellen, ohne den Standard-Bereitstellungsnamen zu ändern.
{% endalert %}

Um zu bestätigen, dass die Integration funktioniert, gehen Sie zur Agentenkonsole und erstellen Sie einen Testagenten mit einem Ihrer bereitgestellten Modelle. Geben Sie eine einfache Anweisung ein, z. B. „Erzähl mir einen Witz“, und führen Sie einen Testaufruf durch, um zu überprüfen, ob das Modell wie erwartet antwortet.

Um die Integration zu entfernen, wählen Sie **Trennen** auf der Seite **Microsoft Foundry-Integration**.

Kontaktieren Sie den [Azure-Support](https://azure.microsoft.com/en-us/support/options/) bei Problemen oder Fragen zu Ihrer Integration.