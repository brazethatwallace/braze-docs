---
nav_title: Use case
article_title: Use case: Decisioning Studio
description: "This example shows how a fictional brand uses Braze AI item recommendations to deliver personalized content and product suggestions across key customer moments."
page_type: tutorial
---

# Use case: Win back lapsed customers with a revenue-focused decisioning agent

> This example shows how a fictional brand uses BrazeAI Decisioning Studio™ and a decisioning agent to route each customer toward an optimal decision from the action bank, personalize messaging for win-back, and optimize for revenue. It ties together agent design, audience and experiments, orchestration through Braze, and post-launch learning.

Let’s say Poppy is a CRM manager at Kitchenerie, a fictional online retailer brand specializing in kitchenware. 

Many customers only browse seasonal collections once or twice before navigating away. Past win-back programs used fixed journeys and manual A/B splits, which were helpful for testing copy, but not for learning which combination of offer, channel, cadence, and timing maximizes purchase revenue for each customer. Leadership’s priority is clear: bring back as many lapsed buyers as possible and lift revenue without breaking guardrails on discounts or frequency. 

This walkthrough describes how Poppy:

- Targets lapsed or at-risk customers as the agent’s audience while structuring experiment groups for a fair comparison
- Allows the agent to choose the best-fit allowed actions from a rich action bank so messaging stays personalized at scale
- Sets up orchestration so decisions flow into Braze as the customer engagement platform
- Launches the agent and closes the loop with feedback so the agent keeps learning what drives win-back revenue

## Step 1: Define success metrics and “who” the agent targets

Poppy confirms the success metric the agent should maximize: revenue from repurchases among customers who’ve stopped buying. 

She defines who enters the program: a Braze segment of lapsed purchasers or high-value dormants. This segment is shared with the AI Decisioning Services team, and together, they set treatment groups, such as Decisioning Studio (AI-optimized recommendations) and Random Control (randomized options as a baseline). This way, the lift in win-backs and revenue is measurable, not anecdotal.

## Step 2: Build the action bank and constraints

Poppy maps the dimensions that matter for win-back strategies: 

- Offer: Free shipping, percentage off, or item bundle
- Channel: Email, push, or SMS
- Send time or cadence
- Creative: Small illustrations or utility-focused copy

For each dimension, she lists concrete options in the action bank—the only actions the agent may take (everything else stays off-limits by design). 

She adds constraints: maximum discount rates, inventory exclusions, frequency limits, and geographic rules so personalization never violates finance or brand policy. The agent then experiments across allowed combinations to discover what works for each customer while optimizing the chosen success metric.

## Step 3: Prepare data and connect orchestration to Braze

Following [Prepare your data and Connect data sources], Poppy ensures rich first-party signals (including purchase history, category affinity, browse behavior, and engagement) feed the agent so each decision is grounded in real behavior. 

For orchestration, she uses the native Braze path: Decisioning Studio decides what to send and when; Braze delivers it. She plans base templates (API-triggered campaigns) per channel with dynamic fields for offers and creative, and sets re-eligibility so tests can run repeatedly as the agent learns.

## Step 4: Launch, monitor, and optimize for revenue

After configuration review with AI Decisioning Services, Poppy launches the agent. 

The agent begins recommending actions per user, orchestrating sends through Braze, and ingesting feedback (conversions, engagement, activations) to improve over time, often streamlined when integrated with Braze. 

She monitors performance against the success metric, learning progress, and which dimensions drive lift for which segments, then refines options or constraints with the team as rules or inventory change.

By pairing a revenue-first success metric with a decisioning agent that continuously tests allowed actions, Kitchenerie moves from static win-back blasts to 1:1 decisions that adapt per customer, aiming to win back more customers and grow revenue while staying within the business rules Poppy defined.

