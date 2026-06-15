---
nav_title: Campaign QA Agent
article_title: Campaign QA Agent
permalink: /campaign_qa_agent/
description: "This reference article covers Campaign QA Agents, including how these agents work and best practices."
hidden: true
---

# Campaign QA Agent

> Campaign QA Agents are AI-powered helpers that run automated checks on your campaign configuration. These agents act as a final safeguard, validating your setup against brand guidelines, organizational conventions, and technical requirements before you launch.

By using Campaign QA Agents, you can reduce manual oversight and ensure every message sent from the Braze platform is accurate, compliant, and launch-ready.

{% alert important %}
Campaign QA Agents for Agent Console are currently in beta. Contact your Braze account manager if you're interested in participating in this beta.
{% endalert %}

## How it works

When you create a Campaign QA Agent, you define specific rules, grouped into “rulesets”, that the agent uses to evaluate a campaign. You can choose from pre-built rulesets covering common marketing needs or create custom rules specific to your team.

When configured, you can test the agent in the Preview pane against any existing campaign in your workspace. The agent provides a detailed report, categorizing its findings into Pass, Warning, or Fail.

## Create a Campaign QA Agent

### Step 1: Choose the agent type

To create your agent, go to **Agent Console** > **Agent Management**. Select **Create agent** and choose **Campaign QA** from the dropdown menu.

### Step 2: Set up details

Next, set up the details for your agent:

1. Enter a name and description to help your team understand its purpose.
2. (optional) Add tags to filter your agent.
3. Choose the model for your agent to use. This powers the agent's reasoning.

![A Campaign QA Agent "Campaign QA for copy" that will check the quality of the campaign message, using the Braze Auto model.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Step 3: Configure instructions and rules

In the **Instructions** tab, define the rules that the agent checks. You can add up to 10 rulesets per agent, and up to 20 rules per ruleset.

1. Select **Add ruleset** to see a list of the following categories:

- **Campaign setup:** Validates naming conventions, tags, and conversion tracking.
Audience and targeting: Checks segments, exclusions, and audience size.
- **Content and copy:** Evaluates text quality, character limits, and message completeness.
- **Links and tracking:** Verifies URLs, CTAs, deep links, and UTM parameters.
- **Personalization and dynamic content:** Checks Liquid logic and fallback values.
- **Compliance and deliverability:** Ensures legal requirements and sending safeguards are met.
- **Generate with Operator:** If you aren't sure how to phrase a rule, select Generate with Operator to have our AI assistant help you draft specific logic based on your requirements.
- **Custom rules:** Select Create custom ruleset to define unique checks that don’t fit cleanly into any of the pre-configured categories.

![Six rules set up for the Content and copy category.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Step 4: Test your agent

Before deploying your agent, use the **Preview** pane to simulate a response and confirm the logic is working as expected.

1. Choose an existing campaign from the dropdown menu to use as a test case.
2. Choose to test all rulesets or a specific one.
3. Select the **Simulate response** button.

Next, review the results. The agent evaluates the campaign and displays the results in the following categories:

- **Pass:** These rules were met successfully. For example, the agent might confirm that your naming conventions match expected patterns.
- **Warning:** These are non-critical issues that may require attention. For example, if you are testing an email ruleset against a Webhook campaign, the agent may issue a warning that sender names do not apply.
- **Fail:** These are critical issues that should be fixed before launch. Examples include scheduled dates that are in the past or missing required organizational tags.

## Use Campaign QA Agents

After you have configured a Campaign QA Agent, you can use it to audit any campaign during the final review process. This ensures that your campaign meets all requirements before it is sent to your users.

### Run an audit

To run an automated check, go to the **Review Summary** step of your campaign creation workflow.

1. Go to the **QA Agent** section and select your desired agent from the dropdown menu.
3. Select **Run QA Agent**.

If you make changes to your campaign after running an initial check, you can select **Re-run QA Agent** to refresh the results.

### Review audit results

After the evaluation is complete, the agent provides a summary of its findings categorized into these tabs: **Pass**, **Fail**, and **Warning**.
 
The **Fail** tab lists rules that were not met. For each failure, the agent provides the:

- **Rule:** The specific criteria being checked, such as "Spelling & Grammar Check".
- **Reasoning:** A detailed explanation of why the check failed. For example, the agent might identify that "personalized" was used instead of the Australian English spelling "personalised".
- **Direct corrections:** Specific text or configuration changes suggested by the agent to fix the issue.

The **Pass** tab lists all rules that your campaign successfully followed. This confirms that checks like **Offensive Language Detection** or **Naming Convention Validation** have been cleared.

The **Warning** tab lists non-critical issues that may require attention. For example, if you're testing an email ruleset against a webhook campaign, the agent may issue a warning that sender names do not apply.

### Resolve or ignore issues

For every identified failure or warning, you can decide how to proceed before launching. Select **Resolve** next to an issue, then select from the following options:

- **I fixed the issue:** Select this after you have updated your campaign configuration or copy based on the agent's feedback.
- **Ignore this issue:** Select this to make an exception to the rule. This is useful for intentional deviations or edge cases where the agent's suggestion may not apply.

After all critical issues are resolved or ignored, you can proceed to launch your campaign.

## Best practices

- **Start with templates:** Use the pre-built rulesets for campaign setup and links and tracking first, as these cover the most common manual errors and ensure the agent has the right context to check for.
- **Be specific:** When writing custom rules, provide clear examples of what "correct" looks like. For instance, instead of writing "Check the naming convention," try "Ensure the campaign name starts with the current year (for example, 2026_)."
- **Iterate often:** As your brand guidelines or internal processes change, update your Campaign QA Agent rulesets to keep your automated checks relevant.
