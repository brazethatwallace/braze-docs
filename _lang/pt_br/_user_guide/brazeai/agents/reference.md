---
nav_title: Referência
article_title: Referência para agentes
description: "Detalhes de referência sobre os Agentes da Braze."
page_order: 3
---

# Referência para agentes {#reference-for-agents}

> Ao criar agentes personalizados, consulte este artigo para mais informações sobre configurações importantes, como instruções e esquemas de saída. Para uma introdução, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) e [Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/agents/faq/).

## Modelos {#models}

Quando você configura um agente, pode escolher o modelo que ele usa para gerar respostas. Você tem duas opções: usar um modelo fornecido pela Braze ou trazer sua própria chave de API.

{% alert important %}
O modelo **Auto** fornecido pela Braze é otimizado para modelos cujas capacidades de raciocínio são suficientes para realizar tarefas como busca em catálogo e associação a Segments. Ao usar outros modelos, recomendamos testar para confirmar se o modelo funciona bem para o seu caso de uso. Pode ser necessário ajustar suas [instruções](#writing-instructions) para fornecer diferentes níveis de detalhe ou raciocínio passo a passo para modelos com diferentes velocidades e capacidades.
{% endalert %}

### Opção 1: Use um modelo fornecido pela Braze {#option-1-use-a-braze-powered-model}

Esta é a opção mais simples, sem configuração extra necessária. A Braze fornece acesso a grandes modelos de linguagem (LLMs) diretamente. Para usar esta opção, selecione **Auto**, que utiliza modelos Gemini.

{% alert important %}
Se você não vê **Braze Auto** como opção no menu suspenso **Model** ao criar um agente, entre em contato com seu gerente de sucesso do cliente para saber como se tornar elegível para usar o modelo Braze Auto.
{% endalert %}

### Opção 2: Traga sua própria chave de API {#option-2-bring-your-own-api-key}

Com esta opção, você pode conectar sua conta da Braze com provedores como OpenAI, Anthropic ou Google Gemini. Se você trouxer sua própria chave de API de um provedor de LLM, os custos de token são cobrados diretamente pelo seu provedor, não pela Braze.

Recomendamos testar rotineiramente os modelos mais recentes, pois modelos legados podem ser descontinuados ou depreciados após alguns meses. Você também pode se inscrever para receber notificações do Console do agente em [Preferências de notificação]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences/) para ser alertado quando a Braze detectar que um modelo não está mais disponível.

Para configurar isso:

1. Acesse **Integrações de parceiros** > **Parceiros de tecnologia** e encontre seu provedor.
2. Insira sua chave de API do provedor.
3. Selecione **Salvar**.

Em seguida, você pode voltar ao seu agente e selecionar o modelo.

Quando você usa um LLM fornecido pela Braze, os provedores desse modelo atuarão como Subprocessadores da Braze, sujeitos aos termos do Aditivo de Processamento de Dados (DPA) entre você e a Braze. Se você optar por trazer sua própria chave de API, o provedor da sua assinatura de LLM é considerado um Provedor Terceiro sob o contrato entre você e a Braze.

#### Níveis de raciocínio {#thinking-levels}

Alguns provedores de LLM podem permitir que você ajuste o nível de raciocínio de um modelo selecionado. Os níveis de raciocínio definem a amplitude de pensamento que o modelo usa antes de responder — desde respostas rápidas e diretas até cadeias mais longas de raciocínio. Isso afeta a qualidade da resposta, a latência e o uso de tokens.

| Nível | Quando usar |
|-------|-------------|
| **Mínimo** | Tarefas simples e bem definidas (como busca em catálogo, classificação direta). Respostas mais rápidas e menor custo. |
| **Baixo** | Tarefas que se beneficiam de um pouco mais de raciocínio, mas não precisam de análise profunda. |
| **Médio** | Tarefas com múltiplas etapas ou nuances (como analisar várias entradas para recomendar uma ação). |
| **Alto** | Raciocínio complexo, casos extremos ou quando você precisa que o modelo trabalhe as etapas antes de responder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Níveis de raciocínio" }

Recomendamos começar com **Mínimo** e testar as respostas do seu agente. Depois, você pode ajustar o nível de raciocínio para **Baixo** ou **Médio** se perceber que o agente está tendo dificuldade em fornecer respostas precisas. Em casos raros, um nível de raciocínio **Alto** pode ser necessário, embora usar esse nível possa resultar em altos custos de token e tempos de resposta mais longos ou maior risco de erros de timeout. Se seu agente está tendo dificuldade em equilibrar raciocínio com múltiplas etapas e tempos de resposta razoáveis, considere dividir seu caso de uso em mais de um agente que possam trabalhar juntos em um Canvas ou catálogo.

A Braze usa os mesmos intervalos de IP para chamadas de LLM de saída que para Conteúdo conectado. Os intervalos estão listados na [lista de permissão de IP de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#connected-content-ip-allowlisting). Se seu provedor suporta lista de permissão de IP, você pode restringir a chave a esses intervalos para que apenas a Braze possa usá-la.

{% alert important %}
Quando você usa um LLM fornecido pela Braze, os provedores desse modelo atuarão como Subprocessadores da Braze, sujeitos aos termos do Aditivo de Processamento de Dados (DPA) entre você e a Braze. Se você optar por trazer sua própria chave de API, o provedor da sua assinatura de LLM é considerado um Provedor Terceiro sob o contrato entre você e a Braze.
{% endalert %}

#### Determinar qual modelo usar {#determine-which-model-to-use}

Cada provedor de LLM tem uma combinação ligeiramente diferente de capacidades de modelo, custos e níveis de raciocínio. Aqui estão algumas diretrizes gerais e melhores práticas:

- Para eficiência de custo, priorize testar modelos com menor custo de token antes dos modelos com custo mais alto. Ajuste para modelos de custo mais alto somente se os modelos de menor custo estiverem tendo dificuldade com o caso de uso ou gerando saídas inconsistentes ou imprecisas.
- Para eficiência de velocidade e desempenho, priorize testar níveis de raciocínio mais baixos antes dos mais altos. Ajuste para níveis de raciocínio mais altos somente se os níveis mais baixos estiverem tendo dificuldade com o caso de uso ou gerando saídas inconsistentes ou imprecisas.
- Se modelos de menor custo ou níveis de raciocínio mais baixos estiverem tendo dificuldade com o caso de uso ou gerando saídas inconsistentes ou imprecisas, considere ajustar para modelos de custo mais alto ou níveis de raciocínio mais altos.
- Durante os testes, certifique-se de equilibrar a confiabilidade e a precisão com o uso de tokens e a duração da invocação.
- Cada caso de uso pode ter um modelo e nível de raciocínio ideais diferentes. Recomendamos testar minuciosamente para verificar a qualidade consistente sem timeouts.

### Limites de taxa {#rate-limits}

Os seguintes limites de taxa se aplicam por espaço de trabalho:

- **Modelo fornecido pela Braze:** 1.000 invocações por minuto
- **Trazendo sua própria chave de API:** 2.500 invocações por minuto

## Escrevendo instruções {#writing-instructions}

Instruções são as regras ou diretrizes que você dá ao agente (prompt do sistema). Elas definem como o agente deve se comportar cada vez que é executado. As instruções do sistema podem ter até 25 KB.

Aqui estão algumas melhores práticas gerais para você começar a criar prompts:

1. Comece com o fim em mente. Declare o objetivo primeiro.
2. Dê ao modelo um papel ou persona ("Você é um ...").
3. Defina contexto e restrições claros (público, comprimento, tom, formato).
4. Peça por estrutura ("Retorne JSON/lista com marcadores/tabela...").
5. Mostre, não conte. Inclua alguns exemplos de alta qualidade.
6. Divida tarefas complexas em etapas ordenadas ("Etapa 1... Etapa 2...").
7. Incentive o raciocínio ("Pense nas etapas internamente, depois forneça uma resposta final concisa," ou "explique brevemente sua decisão").
8. Pilote, inspecione e itere. Pequenos ajustes podem levar a grandes ganhos de qualidade.
9. Lide com os casos extremos, adicione barreiras de proteção e instruções de recusa.
10. Meça e documente o que funciona internamente para reutilização e escalabilidade.

### Usando Liquid {#using-liquid}

Incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) nas instruções do seu agente pode adicionar uma camada extra de personalização na resposta. Você pode especificar a variável Liquid exata que o agente recebe e incluí-la no contexto do seu prompt. Por exemplo, em vez de escrever explicitamente "nome", você pode usar o trecho Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Na seção **Logs** do **Console do agente**, você pode revisar os detalhes da entrada e saída do agente para entender qual valor é renderizado a partir do Liquid.

![Detalhes de um agente que tem Liquid em suas instruções.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Exemplos de agentes em Canvas {#canvas-agent-examples}

Vamos supor que você faz parte de uma marca de viagens, UponVoyage, e seus objetivos são analisar o feedback dos clientes, escrever mensagens personalizadas e determinar a taxa de conversão para seus assinantes gratuitos. Aqui estão exemplos de diferentes instruções com base em objetivos definidos.

{% tabs %}
{% tab Redator de mensagens %}

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
{% tab Descadastramento por SMS %}

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
{% tab Análise de feedback %}

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
{% tab Conversão de trial %}

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

### Exemplos de agentes de catálogo {#catalog-agent-examples}

Vamos supor que você faz parte de uma marca de transporte por aplicativo, StyleRyde, e seus objetivos são escrever resumos atrativos de métodos de viagem e fornecer traduções do app móvel com base no idioma usado na região. Aqui estão exemplos de diferentes instruções com base nos objetivos definidos.

{% tabs %}
{% tab Descrição de destino %}

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
{% tab Localização %}

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

Para agentes de catálogo, use **Campos** na seção **Saída** em vez de JSON Schema. Você ainda pode escrever instruções que peçam ao modelo uma saída em formato chave-valor correspondente aos nomes desses campos.

Para saber mais sobre as melhores práticas de prompting, consulte os guias dos seguintes provedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Saídas {#outputs}

### Esquemas básicos {#basic-schemas}

Esquemas básicos são uma saída simples que um agente retorna. Pode ser uma string, um número, um booleano, um array de strings ou um array de números.

Por exemplo, se você quiser coletar pontuações de sentimento dos usuários a partir de uma pesquisa de feedback simples para determinar o nível de satisfação dos seus clientes após receberem um produto, você pode selecionar **Number** como esquema básico para estruturar o formato de saída.

{% alert important %}
Arrays estão disponíveis apenas para agentes de Canvas, não para agentes de catálogo.
{% endalert %}

![Console do agente com número selecionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Esquemas avançados {#advanced-schemas}

As opções de esquema avançado incluem estruturar campos manualmente ou usar JSON.

- **Campos:** Uma forma sem código de definir uma saída de agente que você pode usar de forma consistente.
- **JSON:** Uma abordagem com código para criar um formato de saída preciso, onde você pode aninhar variáveis e objetos dentro do esquema JSON. Disponível apenas para agentes de Canvas, não para agentes de catálogo.

Recomendamos usar esquemas avançados quando você quiser que o agente retorne uma estrutura de dados com múltiplos valores definidos de forma estruturada, em vez de uma saída de valor único. Isso permite que a saída seja melhor formatada como uma variável de contexto consistente.

Por exemplo, você pode usar um formato de saída dentro de um agente destinado a criar um itinerário de viagem de exemplo para um usuário com base em um formulário que ele enviou. O formato de saída permite que você defina que toda resposta do agente deve retornar com valores para `tripStartDate`, `tripEndDate` e `destination`. Cada um desses valores pode ser extraído de variáveis de contexto e inserido em uma etapa de Mensagem para personalização usando Liquid.

{% tabs %}
{% tab Campos %}

Se você quiser formatar respostas de uma pesquisa de feedback simples para determinar a probabilidade de os respondentes recomendarem o novo sabor de sorvete do seu restaurante, você pode configurar os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **likelihood_score** | Número |
| **explanation** | String |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquemas avançados" }

![Console do agente mostrando três campos de saída para pontuação de probabilidade, explicação e pontuação de confiança.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab Esquema JSON %}

Se você quiser coletar feedback dos usuários sobre a experiência gastronômica mais recente na sua rede de restaurantes, você pode selecionar **JSON Schema** como formato de saída e inserir o seguinte JSON para retornar um objeto de dados que inclui uma variável de sentimento e uma variável de raciocínio.

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

## Catálogos e campos {#catalogs-and-fields}

Escolha catálogos específicos para um agente referenciar e forneça ao seu agente o contexto necessário para entender seus produtos e outros dados não relacionados ao usuário quando relevante. Os agentes usam ferramentas para encontrar apenas os itens relevantes e enviá-los ao LLM para minimizar o uso de tokens.

![O catálogo "restaurants" e a coluna "Loyalty_Program" selecionados para o agente pesquisar.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## Contexto de associação a Segments {#segment-membership-context}

Você pode selecionar até cinco Segments para o agente verificar a associação de cada usuário quando o agente é usado em um Canvas. Vamos supor que seu agente tenha a associação a Segments selecionada para um Segment "Loyalty Users", e o agente é usado em um Canvas. Quando os usuários entram em uma etapa do agente, o agente pode verificar se cada usuário é membro de cada Segment que você especificou no Console do agente e usar a associação (ou não associação) de cada usuário como contexto para o LLM.

![O Segment "Loyalty Users" selecionado para acesso de associação do agente.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Diretrizes da marca {#brand-guidelines}

Você pode selecionar [diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) para o seu agente seguir em suas respostas. Por exemplo, se você quiser que seu agente gere textos de SMS para incentivar os usuários a se inscreverem em uma academia, você pode usar este campo para referenciar sua diretriz motivacional predefinida.

## Histórico de interação específico do usuário {#user-history}

Os dados de interação de um usuário incluem aberturas, cliques e dados de conversão recentes de Campaigns e Canvas. Por exemplo, você pode incluir esse contexto para um agente referenciar quando ele é avaliado em um Canvas. O histórico de interação específico do usuário também pode ajudar a influenciar um agente quando sua função é escrever textos de mensagens personalizadas.

## Duplicar agentes {#duplicate-agents}

Para testar melhorias ou iterações de um agente, você pode duplicar um agente e aplicar alterações para comparar com o original. Você também pode tratar a duplicação de agentes como controle de versão para rastrear variações nos detalhes do agente e quaisquer impactos no seu envio de mensagens. Para duplicar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Duplicar**.

## Arquivar agentes {#archive-agents}

À medida que você cria mais agentes personalizados, pode organizar a página **Gerenciamento de agentes** arquivando agentes que não estão sendo usados ativamente. Para arquivar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Arquivar**.

![Página de Gerenciamento de agentes com agentes arquivados.]({% image_buster /assets/img/ai_agent/archived_agents.png %})