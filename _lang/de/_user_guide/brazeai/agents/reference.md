---
nav_title: Referenz
article_title: Referenz für Agenten
description: "Wichtige Informationen zu Braze-Agenten."
page_order: 3
---

# Referenz für Agenten {#reference-for-agents}

> Wenn Sie benutzerdefinierte Agenten erstellen, lesen Sie diesen Artikel für weitere Informationen zu wichtigen Einstellungen wie Anweisungen und Ausgabeschemata. Eine Einführung finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) und [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq/).

## Modelle {#models}

Wenn Sie einen Agenten einrichten, können Sie das Modell auswählen, das er zur Generierung von Antworten verwendet. Sie haben zwei Möglichkeiten: ein von Braze bereitgestelltes Modell verwenden oder Ihren eigenen API-Schlüssel einbinden.

{% alert important %}
Das von Braze bereitgestellte **Auto**-Modell ist für Modelle optimiert, deren Denkfähigkeiten ausreichen, um Aufgaben wie Katalogsuche und Segmentzugehörigkeit auszuführen. Bei der Verwendung anderer Modelle empfehlen wir, Tests durchzuführen, um sicherzustellen, dass Ihr Modell für Ihren Anwendungsfall geeignet ist. Möglicherweise müssen Sie Ihre [Anweisungen](#writing-instructions) anpassen, um unterschiedliche Detailstufen oder schrittweises Denken für Modelle mit unterschiedlichen Geschwindigkeiten und Fähigkeiten bereitzustellen.
{% endalert %}

### Option 1: Ein von Braze bereitgestelltes Modell verwenden {#option-1-use-a-braze-powered-model}

Dies ist die einfachste Option, die keine zusätzliche Einrichtung erfordert. Braze ermöglicht den direkten Zugriff auf große Sprachmodelle (LLMs). Um diese Option zu verwenden, wählen Sie **Auto** aus – dabei werden Gemini-Modelle verwendet.

{% alert important %}
Sollten Sie beim Erstellen eines Agenten die Option **Braze Auto** nicht in der Dropdown-Liste **Model** sehen, wenden Sie sich an Ihren Customer-Success-Manager, um zu erfahren, wie Sie die Berechtigung zur Nutzung des Braze Auto-Modells erhalten.
{% endalert %}

### Option 2: Eigenen API-Schlüssel einbinden {#option-2-bring-your-own-api-key}

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter verwenden, werden die Token-Kosten direkt über Ihren Anbieter und nicht über Braze abgerechnet.

Wir empfehlen, regelmäßig die neuesten Modelle zu testen, da ältere Modelle nach einigen Monaten möglicherweise eingestellt oder als veraltet markiert werden. Sie können sich auch für Benachrichtigungen der Agentenkonsole unter [Präferenzen für Benachrichtigungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences/) anmelden, um benachrichtigt zu werden, wenn Braze erkennt, dass ein Modell nicht mehr verfügbar ist.

So richten Sie dies ein:

1. Gehen Sie zu **Partner Integrations** > **Technology Partners** und suchen Sie Ihren Anbieter.
2. Geben Sie Ihren API-Schlüssel vom Anbieter ein.
3. Wählen Sie **Save**.

Anschließend können Sie zu Ihrem Agenten zurückkehren und Ihr Modell auswählen.

Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bestimmungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie sich dafür entscheiden, Ihren eigenen API-Schlüssel einzubinden, gilt der Anbieter Ihres LLM-Abos gemäß dem Vertrag zwischen Ihnen und Braze als Drittanbieter.

#### Denkstufen {#thinking-levels}

Einige LLM-Anbieter ermöglichen es Ihnen, die Denkstufe eines ausgewählten Modells anzupassen. Denkstufen definieren den Umfang der Überlegungen, die das Modell vor der Antwort durchführt – von schnellen, direkten Antworten bis hin zu längeren Argumentationsketten. Dies beeinflusst die Antwortqualität, Latenz und den Token-Verbrauch.

| Stufe | Wann verwenden |
|-------|-------------|
| **Minimal** | Einfache, klar definierte Aufgaben (z. B. Katalogsuche, einfache Klassifizierung). Schnellste Antworten und niedrigste Kosten. |
| **Niedrig** | Aufgaben, die von etwas mehr Überlegung profitieren, aber keine tiefgehende Analyse erfordern. |
| **Mittel** | Mehrstufige oder nuancierte Aufgaben (z. B. Analyse mehrerer Eingaben, um eine Aktion zu empfehlen). |
| **Hoch** | Komplexe Argumentation, Sonderfälle oder wenn das Modell Schritte durchdenken soll, bevor es antwortet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Denkstufen" }

Wir empfehlen, mit **Minimal** zu beginnen und die Antworten Ihres Agenten zu testen. Anschließend können Sie die Denkstufe auf **Niedrig** oder **Mittel** anpassen, wenn der Agent Schwierigkeiten hat, genaue Antworten zu liefern. In seltenen Fällen kann eine **hohe** Denkstufe erforderlich sein, wobei diese Stufe zu hohen Token-Kosten und längeren Antwortzeiten oder einem höheren Risiko von Timeout-Fehlern führen kann. Wenn Ihr Agent Schwierigkeiten hat, mehrstufiges Denken mit angemessenen Antwortzeiten in Einklang zu bringen, sollten Sie Ihren Anwendungsfall in mehrere Agenten aufteilen, die in einem Canvas oder Katalog zusammenarbeiten können.

Braze verwendet für ausgehende LLM-Aufrufe dieselben IP-Bereiche wie für Connected-Content. Die Bereiche sind in der [Connected-Content-IP-Zulassungsliste]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#connected-content-ip-allowlisting) aufgeführt. Wenn Ihr Anbieter IP-Zulassungslisten unterstützt, können Sie den Schlüssel auf diese Bereiche beschränken, sodass nur Braze ihn verwenden kann.

{% alert important %}
Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bestimmungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie sich dafür entscheiden, Ihren eigenen API-Schlüssel einzubinden, gilt der Anbieter Ihres LLM-Abos gemäß dem Vertrag zwischen Ihnen und Braze als Drittanbieter.
{% endalert %}

#### Das richtige Modell bestimmen {#determine-which-model-to-use}

Jeder LLM-Anbieter bietet eine leicht unterschiedliche Mischung aus Modellfähigkeiten, Kosten und Denkstufen. Hier sind einige allgemeine Richtlinien und Best Practices:

- Für Kosteneffizienz sollten Sie zuerst Modelle mit niedrigeren Token-Kosten testen, bevor Sie zu teureren Modellen wechseln. Passen Sie nur dann auf teurere Modelle an, wenn günstigere Modelle mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente bzw. ungenaue Ergebnisse liefern.
- Für Geschwindigkeit und Performance-Effizienz sollten Sie zuerst niedrigere Denkstufen testen, bevor Sie höhere Denkstufen verwenden. Passen Sie nur dann auf höhere Denkstufen an, wenn niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente bzw. ungenaue Ergebnisse liefern.
- Wenn günstigere Modelle oder niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente bzw. ungenaue Ergebnisse liefern, sollten Sie auf teurere Modelle oder höhere Denkstufen umsteigen.
- Achten Sie beim Testen darauf, Zuverlässigkeit und Genauigkeit mit Token-Verbrauch und Aufrufdauer in Einklang zu bringen.
- Jeder Anwendungsfall kann ein anderes optimales Modell und eine andere optimale Denkstufe haben. Wir empfehlen gründliches Testen, um konsistente Qualität ohne Timeouts sicherzustellen.

### Rate-Limits {#rate-limits}

Die folgenden Rate-Limits gelten pro Workspace:

- **Von Braze bereitgestelltes Modell:** 1.000 Aufrufe pro Minute
- **Eigener API-Schlüssel:** 2.500 Aufrufe pro Minute

## Anweisungen verfassen {#writing-instructions}

Anweisungen sind die Regeln oder Richtlinien, die Sie dem Agenten geben (System-Prompt). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Systemanweisungen können bis zu 25 KB groß sein.

Hier sind einige allgemeine Best Practices für den Einstieg in das Prompting:

1. Beginnen Sie mit dem Ziel vor Augen. Formulieren Sie zuerst das Ziel.
2. Weisen Sie dem Modell eine Rolle oder Persona zu („Sie sind ein ...“).
3. Legen Sie einen klaren Kontext und klare Vorgaben fest (Zielgruppe, Länge, Tonfall, Format).
4. Fordern Sie Struktur an („Geben Sie JSON/Aufzählungsliste/Tabelle zurück ...“).
5. Zeigen statt erklären. Fügen Sie einige hochwertige Beispiele bei.
6. Teilen Sie komplexe Aufgaben in geordnete Schritte auf („1. Schritt ... 2. Schritt ...“).
7. Fördern Sie das logische Denken („Überlegen Sie die einzelnen Schritte im Kopf und geben Sie dann eine prägnante endgültige Antwort“ oder „Erläutern Sie kurz Ihre Entscheidung“).
8. Testen, überprüfen und iterieren. Kleine Optimierungen können zu erheblichen Qualitätssteigerungen führen.
9. Behandeln Sie Sonderfälle, fügen Sie Sicherheitsvorkehrungen hinzu und ergänzen Sie Ablehnungsanweisungen.
10. Messen und dokumentieren Sie, was intern für die Wiederverwendung und Skalierung funktioniert.

### Liquid verwenden {#using-liquid}

Die Einbindung von [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) in die Anweisungen Ihres Agenten kann dessen Antworten eine zusätzliche Ebene der Personalisierung verleihen. Sie können die genaue Liquid-Variable angeben, die der Agent erhält, und diese in den Kontext Ihres Prompts einfügen. Anstatt beispielsweise explizit „Vorname“ zu schreiben, können Sie das Liquid-Snippet {% raw %}`{{${first_name}}}`{% endraw %} verwenden:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Im Abschnitt **Logs** der **Agentenkonsole** können Sie die Details zu den Ein- und Ausgabedaten des Agenten überprüfen, um zu verstehen, welcher Wert aus Liquid gerendert wird.

![Die Details für einen Agenten, der Liquid in seinen Anweisungen verwendet.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Canvas-Agent-Beispiele {#canvas-agent-examples}

Angenommen, Sie sind Teil einer Reisemarke namens UponVoyage und Ihre Ziele sind die Analyse von Kundenfeedback, das Verfassen personalisierter Nachrichten und die Ermittlung der Konversionsrate für Ihre kostenlosen Abonnent:innen. Im Folgenden finden Sie Beispiele für unterschiedliche Anweisungen basierend auf definierten Zielen.

{% tabs %}
{% tab Nachrichten-Texter %}

{% raw %}
```
Role:
You are an expert lifecycle marketing brand copywriter for UponVoyage. Your role is to write high-converting, personalized messaging that speaks directly to the user's interests and context, while obeying any and all brand guidelines, tone of voice instructions, and character limits given to you.

Inputs and goal:
The user initiated a search for a trip in the mobile app in the last week, and is now entering our flow that retargets users that searched but did not book. The goal of the journey is to drive the user to complete a checkout. Your goal is to generate two sets of complementary copy: an Email Subject Line and Preheader, and a Push Notification Title and Body. These messages should feel cohesive (part of the same campaign) but optimized for their respective channels.
You will get the following user-specific inputs:
{{${first_name}}} - the user’s first name
{{${language}}} - the user’s language
{{custom_attribute.${loyalty_status}}} - the user’s loyalty status
{{context.${city_searched}}} - the city the user last searched
{{context.${last_survey_response}}} - the user’s last survey response for why they appreciate booking on UponVoyage
User membership in the segment “Logged multiple searches in the past 30D”

Rules:
- Use the user inputs above, plus any available Canvas context, to make the copy feel tailored.
- Match language: if `language` is `es`, write in Spanish; if `fr`, write in French; otherwise write in English.
- Ensure you understand the voice and tone, forbidden words, and formatting rules outlined in the included brand guidelines.
- Use the user's first name if available, otherwise use 'friend'. Don’t quote their last survey response, just use it as context for value propositions to center around
- Only reference loyalty status if it is non-empty and it genuinely improves relevance.
- Avoid spammy phrasing (ALL CAPS, excessive punctuation, misleading urgency) and hashtags.
- Do not mention "AI," "bot," or "automated message."
- Do not make up input data that is not present in the prompt.
- Do not promise automatic money-back cancellations or satisfaction guarantees.
- Include "explanation": a short string that states why this copy fits the user's context and channel rules (for review or QA).

Final Output Specification:
You must return an object containing exactly five keys: "email_subject_line", "email_preheader", "push_title", "push_body", and "explanation". The first four keys will be inserted into the appropriate locations in subsequent messages in the journey. Ensure the Email and Push convey the same core offer/value, but do not simply copy-paste the text. The Push should be shorter and more direct. Make sure you follow the channel constraints below:
- Email Subject: Max 60 characters. Intriguing and benefit-led.
- Email Preheader: Max 100 characters. Supports the subject line.
- Push Title: Max 50 characters. Punchy and urgent.
- Push Body: Max 120 characters. Clear value prop.
- explanation: String. Brief rationale for how you used inputs, loyalty tier, and search context without breaking brand or channel limits.

Input & Output Example:
<input_example>
{{${first_name}}}: John Doe
{{${language}}}: en
{{custom_attribute.${loyalty_status}}}: Gold Tier
{{context.${city_searched}}}: Tokyo
{{context.${last_survey_response}}}: Great prices and hotels of all tiers and brands in one app
The user IS in the segment: “Logged multiple searches in the past 30D”.
</input_example>
<output_example>
{ "email_subject_line": "John, your Tokyo Gold Tier deals are waiting", "email_preheader": "Find the best hotel brands for your Tokyo getaway.", "push_title": "John, Tokyo is calling!", "push_body": "Your Gold Tier deals are ready. Tap to view exclusive hotel offers.", "explanation": "Personalized on Tokyo and Gold Tier; matched survey value props; English per language code; kept within character limits for email and push." }
</output_example>
```
{% endraw %}

{% endtab %}
{% tab SMS-Opt-out %}

{% raw %}
```
ROLE
You are a compliance-focused classifier for inbound customer messages.

PRIMARY TASK
Given a single inbound message from a user, decide whether it should be treated as a request to opt out of future messaging (unsubscribe, stop, revoke consent).

OUTPUT (STRICT)
Return a single boolean only:
- true = treat as an opt-out request
- false = do not treat as an opt-out request
Do not output any other words, punctuation, or explanation.

COMPLIANCE INTENT (NON-LEGAL GUIDANCE)
Classify conservatively to reduce the risk of sending messages after a user revokes consent. This supports common requirements and expectations in laws and standards such as TCPA (US SMS consent and revocation), GDPR (withdrawal of consent and right to object to marketing), and other subscription management regimes. When in doubt, return true.

DECISION RULES
Return true if ANY of the following are present:
1) Explicit opt-out keywords or phrases:
   - STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT
   - "stop texting me", "stop messaging me", "no more messages", "don’t contact me", "do not contact", "remove me", "take me off your list", "opt me out", "revoke my consent", "withdraw my consent", "I don’t want these", "leave me alone"
2) A clear request to stop a specific channel:
   - "don’t text me", "no more texts", "don’t email me", "stop calling me"
3) Unambiguous negative feedback that functions like revocation of consent (treat as opt-out):
   - A standalone thumbs down (:-1:) or "thumbs down"
   - "I hate this", "this is the worst", "you suck", "go away", "go die", "f*** off"
   - Any brand-configured profanity or hostile phrases that your program treats as opt-out (assume these count as opt-out unless you have explicit context that they should not)
Return false if ALL of the following are true:
- The user is clearly engaging with the content or asking a question, and
- There is no explicit opt-out intent
Examples: "Stop by the store?", "Can you stop the order?", "This sucks but what’s the discount?", "I hate this product (but keep me updated)".

EDGE CASES
- If the message contains an opt-out keyword but is obviously not about messaging consent (rare), return false.
- If the message expresses anger or dissatisfaction and could reasonably be interpreted as “stop contacting me”, return true.
- If the message is very short, ambiguous, or contains only a negative signal (like :-1:), return true.

EXAMPLES
Input: “STOP” → true
Input: “unsubscribe” → true
Input: “Please stop texting me” → true
Input: “Remove me from your list” → true
Input: “:-1:” → true
Input: “I hate this. Leave me alone.” → true
Input: “This is the worst, you suck” → true
Input: “Stop by tomorrow?” → false
Input: “Can you stop the delivery?” → false
Input: “This sucks—what’s the promo code?” → false
```
{% endraw %}

{% endtab %}
{% tab Feedback-Analyse %}

{% raw %}
```
Role:
You are an expert Customer Experience Analyst for UponVoyage. Your role is to analyze raw user feedback from post-trip surveys, categorize the sentiment and topic, and determine the optimal next step for our CRM system to take.

Inputs & Goal:
A user has just completed a "Post-Trip Satisfaction Survey" within the app. Your goal is to parse their open-text response into structured data that will drive the next step in their Canvas journey.
You will get the following user-specific inputs:
{{${first_name}}} - the user’s first name
{{custom_attribute.${loyalty_status}}} - the user’s loyalty tier (e.g., Bronze, Silver, Gold, Platinum)
{{context.${survey_text}}} - the open-text feedback the user submitted
{{context.${trip_destination}}} - the destination of their recent trip

Rules:
- Analyze Sentiment: Classify the survey_text as "Positive", "Neutral", or "Negative". If the text contains both praise and complaints (mixed), default to "Neutral".
- Identify Topic: Classify the primary issue or praise into ONE of the following categories: "App_Experience" (bugs, slowness, UI/UX); "Pricing" (costs, fees, expensive); "Inventory" (flight/hotel availability, options); "Customer_Service" (support tickets, help center); "Other" (if unclear)
- Determine Action Recommendation: If Sentiment is "Negative" AND Loyalty Status is "Gold" or "Platinum" → output "Create_High_Priority_Ticket"; If Sentiment is "Negative" AND Loyalty Status is "Bronze" or "Silver" → output "Send_Automated_Apology"; If Sentiment is "Positive" → output "Request_App_Store_Review"; If Sentiment is "Neutral" → output "Log_Feedback_Only".
- Data Safety: Do not make up data not present in the input. Return valid JSON only. Include only these fields: sentiment, topic, action_recommendation, and explanation.
- If the survey response is empty or meaningless, set sentiment as Neutral, topic as Other, action recommendation as Request_More_Details, and explain why in explanation.

Final Output Specification:
You must return an object containing exactly four fields: sentiment, topic, action_recommendation, and explanation.
- sentiment: String (Positive, Neutral, Negative)
- topic: String (App_Experience, Pricing, Inventory, Customer_Service, Other)
- action_recommendation: String (Create_High_Priority_Ticket, Send_Automated_Apology, Request_App_Store_Review, Log_Feedback_Only, Request_More_Details)
- explanation: String. Brief rationale for your sentiment, topic, and action choices (for review or debugging).

Input & Output Example:
<input_example>
{{${first_name}}}: Sarah
{{custom_attribute.${loyalty_status}}}: Platinum
{{context.${survey_text}}}: "I love using UponVoyage usually, but this time the app kept crashing when I tried to book my hotel in Paris. It was really frustrating."
{{context.${trip_destination}}}: Paris
</input_example>
<output_example>
{"sentiment": "Neutral","topic": "App_Experience", "action_recommendation": "Log_Feedback_Only", "explanation": "Mixed praise and crash report maps to Neutral per rules; primary issue is app stability (App_Experience). Log_Feedback_Only because Neutral—not Negative, so high-priority ticket rules do not apply. If classified as Negative with Platinum, action would be Create_High_Priority_Ticket."}
</output_example>
```
{% endraw %}
{% endtab %}
{% tab Test-Conversion %}

{% raw %}
```
Role:
You are an expert Retention and Conversion Analyst for UponVoyage Premium. Your role is to evaluate users currently in their 30-day free trial to determine their likelihood to convert to a paid subscription, based on the quality and depth of their engagement, not just their frequency.

Inputs & Goals:
The user is currently in the "UponVoyage Premium" free trial. Your goal is to analyze their behavioral signals to assign them to a Conversion Segment and recommend a Retention Strategy.

You will get the following user-specific inputs:
{{custom_attribute.${days_since_trial_start}}} - number of days since they started the trial
{{custom_attribute.${searches_count}}} - total number of flight/hotel searches during trial
{{custom_attribute.${premium_features_used}}} - count of Premium-only features used (e.g., Lounge Access, Price Protection)
{{custom_attribute.${most_searched_category}}} - e.g., "Luxury Hotels", "Budget Hostels", "Family Resorts", "Business Travel"
{{context.${last_app_session}}} - date of last app open

User membership in segment: "Has Valid Payment Method on File" (True/False)

Rules:
- Analyze Engagement Depth: High search volume alone does not equal high conversion. Look for use of Premium Features (the core value driver).
- Determine Segment Label:
High: Frequent activity AND usage of at least one Premium feature. User clearly sees value.
Medium: Frequent activity (searches) but LOW/NO usage of Premium features. User is engaged with the app but not yet hooked on the subscription.
Low: Minimal activity (< 3 searches) regardless of features.
Cold: No activity in the last 7 days.
- Identify Primary Barrier: Based on the data, what is stopping them? (e.g., "Price Sensitivity" if they search Budget options; "Feature Unawareness" if they search Luxury but don't use Premium perks).
- Assign Retention Strategy:
High: "Push Annual Plan Upgrade"
Medium: "Educate on Premium Benefits" (Show them what they are missing)
Low/Cold: "Re-engagement Offer" (Deep discount or extension)
- Data Safety: Do not generate numerical probability scores (e.g., "85%"). Stick to the defined labels.

Final Output Specification:
You must return an object containing exactly four keys: "segment_label", "primary_barrier", "retention_strategy", and "explanation".
- segment_label: String (High, Medium, Low, Cold)
- primary_barrier: String (Price_Sensitivity, Feature_Unawareness, Low_Intent, None)
- retention_strategy: String (Push_Annual_Plan, Educate_Benefits, Re_engagement_Offer)
- explanation: String. Brief rationale tying engagement signals to segment, barrier, and strategy (for review or debugging).

Input & Output Example:
<input_example>
{{custom_attribute.${days_since_trial_start}}}: 20
{{custom_attribute.${searches_count}}}: 15
{{custom_attribute.${premium_features_used}}}: 0
{{custom_attribute.${most_searched_category}}}: "Budget Hostels"
{{context.${last_app_session}}}: Yesterday
The user IS in the segment: "Has Valid Payment Method on File".
</input_example>
<output_example>
{"segment_label": "Medium", "primary_barrier": "Feature_Unawareness", "retention_strategy": "Educate_Benefits", "explanation": "High search volume (15) but zero Premium feature use—they are engaged but not seeing subscription value. Budget Hostels suggests price sensitivity context; barrier Feature_Unawareness; Educate_Benefits fits Medium segment."}
</output_example>
```
{% endraw %}

{% endtab %}
{% endtabs %}

### Katalog-Agent-Beispiele {#catalog-agent-examples}

Angenommen, Sie sind Teil einer On-Demand-Ridesharing-Marke namens StyleRyde und Ihre Ziele sind es, vermarktbare Zusammenfassungen von Reisemethoden zu verfassen und Übersetzungen der mobilen App basierend auf der in der Region verwendeten Sprache bereitzustellen. Im Folgenden finden Sie Beispiele für unterschiedliche Anweisungen basierend auf den definierten Zielen.

{% tabs %}
{% tab Zielbeschreibung %}

{% raw %}
```
Role:
You are an expert Travel Copywriter for StyleRyde. Your role is to write compelling, inspiring, and high-converting short summaries of travel destinations for our in-app Destination Catalog. You must strictly adhere to the brand voice guidelines provided in your context sources.

Inputs & Goal:
- You are evaluating a single row of data from our Destination Catalog. Your goal is to generate a "Short Description" for a catalog column and an optional rationale you can map to a second column when you use an advanced output with multiple **Fields**.
- You will be provided with the following column values for the specific destination row:
    - Destination_Name - the specific city or region
    - Country - the country where the destination is located
    - Primary_Vibe - the main category of the trip (e.g., Beach, Historic, Adventure, Nightlife)
    - Price_Tier - represented as $, $$, $$$, or $$$$

Rules:
- Write exactly one or two short sentences.
- Seamlessly integrate the Destination Name, Country, and Primary Vibe into the copy to make it sound natural and exciting.
- Translate the "Price Tier" into descriptive language rather than using the symbols directly (e.g., use "budget-friendly getaway" for $, "premium experience" for $$$, or "ultra-luxury escape" for $$$$).
- Keep the description skimmable and inspiring.
- Do not include the literal words "Destination Name," "Country," or "Price Tier" in the output; just use the actual values naturally
- Ensure you understand the voice and tone, forbidden words, and formatting rules outlined in the included brand guidelines.
- Avoid spammy phrasing (ALL CAPS, excessive punctuation) and emojis.
- Do not hallucinate specific hotels or flights, as this is a general destination description.
- If any input fields are missing, write the best description possible with the available data
- Include "explanation": a short string that states how you applied the rules (for review or QA).

Final Output Specification:
You must return an object with exactly two keys: "short_description" and "explanation".
- short_description: Plain text for the catalog cell, maximum 150 characters. No markdown.
- explanation: String. Brief note on how you combined Destination Name, Country, Primary Vibe, and Price Tier per the brand rules.
Configure your agent's **Output** with **Fields** that match these key names (catalog agents do not use JSON Schema output in the Agent Console, but your instructions can still ask the model for this key-value shape).

Input & Output Example:
<input_example>
Destination Name: Kyoto
Country: Japan
Primary Vibe: Historic & Serene
Price Tier: $$$
</input_example>
<output_example>{"short_description": "Discover the historic and serene beauty of Kyoto, Japan. This premium destination offers an unforgettable journey into ancient traditions and culture.", "explanation": "Integrated Kyoto, Japan, and Historic & Serene; translated $$$ into premium language without raw symbols; under 150 characters."}</output_example>
```
{% endraw %}

{% endtab %}
{% tab Lokalisierung %}

{% raw %}
```
Role:
You are an expert AI Localization Specialist for StyleRyde. Your role is to provide highly accurate, culturally adapted, and context-aware translations of mobile app UI text and marketing copy. You ensure our app feels native and natural to users around the world.

Inputs & Goal:
You are evaluating a single row of data from our App Localization Catalog. Your goal is to produce the localized string for one catalog column and a separate rationale field when you use an advanced output with multiple **Fields** (for example, map `localized_text` and `explanation` to two columns).

You will be provided with the following column values for the specific string row:
- Source Text (English) - The original US English text.
- Target Language Code - The locale code to translate into (e.g., es-MX, fr-FR, ja-JP, pt-BR).
- UI Category - Where this text lives in the app (e.g., Tab_Bar, CTA_Button, Screen_Title, Push_Notification).
- Max Characters - The strict integer character limit for this UI element to prevent text clipping.

Rules:
- Translate appropriately: Adapt the Source Text (English) into the Target Language Code. Use local spelling norms (e.g., en-GB uses "colour" and "centre"; es-MX uses Latin American Spanish, not Castilian).
- Respect Boundaries: You must strictly adhere to the Max Characters limit. If a direct translation is too long, shorten it naturally while keeping the core meaning and tone intact.

Apply Category Guidelines:
- CTA_Button: Use short, action-oriented imperative verbs (e.g., "Book", "Search"). Capitalize words if natural for the locale.
- Tab_Bar: Maximum 1-2 words. Extremely concise.
- Screen_Title: Emphasize the core feature.
- Error_Message: Be polite, clear, and reassuring.
- Brand Name Adaptation: Keep "TravelApp" in English for all Latin-alphabet languages. Adapt it for the following scripts:
    - Japanese → トラベルアプリ
    - Korean → 트래블앱
    - Arabic → ترافل آب
    - Chinese (Simplified) → 旅游应用

Fallback Logic: If the source text is empty, if you do not understand the translation, or if it is impossible to translate within the character limit, set localized_text to exactly ERROR_MANUAL_REVIEW_NEEDED and use explanation to describe why.

Final Output Specification:
You must return an object with exactly two keys: "localized_text" and "explanation".
- localized_text: The string saved to the localized catalog column (plain text, no pronunciation guides). Must respect Max Characters when you return a translation.
- explanation: String. Brief note on locale choices, shortening tradeoffs, or why ERROR_MANUAL_REVIEW_NEEDED applies.
Configure your agent's **Output** with **Fields** that match these key names.

Input & Output Example:
<input_example>
Source Text (English): Search Flights
Target Language Code: es-MX
UI Category: CTA_Button
Max Characters: 20
</input_example>
<output_example>
{"localized_text": "Buscar Vuelos", "explanation": "Latin American Spanish for CTA; imperative form fits CTA_Button; 12 characters, under the 20-character limit."}
</output_example>
```
{% endraw %}

{% endtab %}
{% endtabs %}

Für Katalog-Agenten verwenden Sie **Fields** im Abschnitt **Output** anstelle von JSON Schema. Sie können dennoch Anweisungen verfassen, die das Modell auffordern, eine Schlüssel-Wert-Ausgabe zu liefern, die diesen Feldnamen entspricht.

Weitere Informationen zu Best Practices für Prompting finden Sie in den Leitfäden der folgenden Modellanbieter:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Ausgaben {#outputs}

### Einfache Schemata {#basic-schemas}

Einfache Schemata sind eine einfache Ausgabe, die ein Agent zurückgibt. Dies kann ein String, eine Zahl, ein Boolescher Wert, ein String-Array oder ein Zahlen-Array sein.

Wenn Sie beispielsweise Stimmungswerte von Nutzer:innen aus einer einfachen Feedback-Umfrage erfassen möchten, um die Zufriedenheit Ihrer Kund:innen nach Erhalt eines Produkts zu ermitteln, können Sie **Number** als einfaches Schema auswählen, um das Ausgabeformat zu strukturieren.

{% alert important %}
Arrays sind nur für Canvas-Agenten verfügbar, nicht für Katalog-Agenten.
{% endalert %}

![Agentenkonsole mit „Number“ als einfachem Schema ausgewählt.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Erweiterte Schemata {#advanced-schemas}

Erweiterte Schema-Optionen umfassen die manuelle Strukturierung von Feldern oder die Verwendung von JSON.

- **Fields:** Eine No-Code-Methode, um eine konsistente Agentenausgabe zu erzwingen.
- **JSON:** Ein Code-Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können. Nur für Canvas-Agenten verfügbar, nicht für Katalog-Agenten.

Wir empfehlen die Verwendung erweiterter Schemata, wenn der Agent eine Datenstruktur mit mehreren strukturiert definierten Werten zurückgeben soll, anstatt einer einzelnen Ausgabe. Dadurch kann die Ausgabe besser als konsistente Kontextvariable formatiert werden.

Beispielsweise können Sie ein Ausgabeformat innerhalb eines Agenten verwenden, der eine Beispiel-Reiseroute für Nutzer:innen basierend auf einem eingereichten Formular erstellen soll. Das Ausgabeformat ermöglicht es Ihnen festzulegen, dass jede Agentenantwort Werte für `tripStartDate`, `tripEndDate` und `destination` enthalten soll. Jeder dieser Werte kann aus Kontextvariablen extrahiert und in einem Nachrichtenschritt zur Personalisierung mit Liquid eingefügt werden.

{% tabs %}
{% tab Fields %}

Wenn Sie Antworten auf eine einfache Feedback-Umfrage formatieren möchten, um zu ermitteln, wie wahrscheinlich es ist, dass Befragte die neueste Eissorte Ihres Restaurants weiterempfehlen, können Sie die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agentenkonsole mit drei Ausgabefeldern für Wahrscheinlichkeitswert, Erklärung und Konfidenzwert.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON Schema %}

Wenn Sie Nutzerfeedback zur letzten Restauranterfahrung in Ihrer Restaurantkette erfassen möchten, können Sie **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Stimmungsvariable und eine Begründungsvariable enthält.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## Kataloge und Felder {#catalogs-and-fields}

Wählen Sie bestimmte Kataloge aus, die ein Agent referenzieren soll, und geben Sie Ihrem Agenten den Kontext, den er benötigt, um Ihre Produkte und andere nicht-nutzerbezogene Daten zu verstehen. Agenten verwenden Tools, um nur die relevanten Einträge zu finden und diese an das LLM zu senden, um den Token-Verbrauch zu minimieren.

![Der Katalog „restaurants“ und die Spalte „Loyalty_Program“, die für die Suche durch den Agenten ausgewählt wurden.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## Segmentzugehörigkeitskontext {#segment-membership-context}

Sie können bis zu fünf Segmente auswählen, anhand derer der Agent die Segmentzugehörigkeit jedes Nutzers bzw. jeder Nutzerin abgleichen kann, wenn der Agent in einem Canvas verwendet wird. Angenommen, Ihr Agent hat die Segmentzugehörigkeit für ein Segment „Treue-Nutzer:innen“ ausgewählt und wird in einem Canvas eingesetzt. Wenn Nutzer:innen einen Agenten-Schritt aufrufen, kann der Agent prüfen, ob jede Nutzerin bzw. jeder Nutzer Mitglied der in der Agentenkonsole angegebenen Segmente ist, und die Zugehörigkeit (oder Nicht-Zugehörigkeit) als Kontext für das LLM verwenden.

![Das Segment „Loyalty Users“, das für den Zugang zur Agenten-Mitgliedschaft ausgewählt wurde.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Markenrichtlinien {#brand-guidelines}

Sie können [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) auswählen, an die sich Ihr Agent bei seinen Antworten halten soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte erstellt, um Nutzer:innen zur Anmeldung für eine Fitnessstudio-Mitgliedschaft zu motivieren, können Sie dieses Feld verwenden, um Ihre vordefinierte, motivierende Richtlinie zu referenzieren.

## Temperatur {#temperature}

Wenn Sie einen Agenten verwenden möchten, um Texte zu generieren, die Nutzer:innen dazu ermutigen, sich in Ihre mobile App einzuloggen, können Sie eine höhere Temperatur einstellen, damit Ihr Agent kreativer ist und die Nuancen der Kontextvariablen nutzt. Wenn Sie einen Agenten zur Generierung von Stimmungswerten einsetzen, empfiehlt es sich möglicherweise, eine niedrigere Temperatur einzustellen, um Spekulationen des Agenten bei negativen Umfrageantworten zu vermeiden. Wir empfehlen, diese Einstellung zu testen und die vom Agenten generierte Ausgabe zu überprüfen, um sie an Ihr Szenario anzupassen.

{% alert note %}
Temperaturen werden derzeit nicht für die Verwendung mit OpenAI unterstützt.
{% endalert %}

## Agenten duplizieren {#duplicate-agents}

Um Verbesserungen oder Iterationen eines Agenten zu testen, können Sie einen Agenten duplizieren und anschließend Änderungen vornehmen, um diese mit dem Original zu vergleichen. Sie können das Duplizieren von Agenten auch als Versionskontrolle nutzen, um Änderungen in den Agentendetails und etwaige Auswirkungen auf Ihr Messaging zu verfolgen. So duplizieren Sie einen Agenten:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das <i class="fas fa-ellipsis-vertical" aria-label="Weitere Optionen"></i>-Menü aus.
2. Wählen Sie **Duplicate**.

## Agenten archivieren {#archive-agents}

Wenn Sie weitere angepasste Agenten erstellen, können Sie die Seite **Agentenmanagement** organisieren, indem Sie Agenten archivieren, die nicht aktiv verwendet werden. So archivieren Sie einen Agenten:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das <i class="fas fa-ellipsis-vertical" aria-label="Weitere Optionen"></i>-Menü aus.
2. Wählen Sie **Archive**.

![Seite „Agentenmanagement“ mit archivierten Agenten.]({% image_buster /assets/img/ai_agent/archived_agents.png %})