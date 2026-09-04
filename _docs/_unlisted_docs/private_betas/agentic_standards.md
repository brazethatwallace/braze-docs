---
nav_title: Agentic Standards
article_title: Agentic Standards
permalink: /campaign_qa_agent/
description: "This reference article covers Agentic Standards, including how Campaign Standards work and best practices."
hidden: true
---

# Agentic Standards

> Agentic Standards are rules and rulesets to enforce enterprise policies and guardrails on campaigns in Braze. They are followed by Operator during the build and edit process. These standards can be agentically evaluated before a campaign launches to act as a final safeguard to validate against brand guidelines, organizational conventions, and technical requirements before you launch.

Agentic Standards reduce manual oversight so every message Braze sends is accurate, compliant, and launch-ready.

{% alert important %}
Agentic Standards for Agent Console are currently in beta. Contact your Braze account manager if you're interested in participating in this beta.
{% endalert %}

## How it works

When you create a Campaign Standard, you define specific rules, grouped into "rulesets", that Operator follows and evaluates before you launch a campaign. You can choose from pre-built rulesets covering common marketing needs or create custom rules specific to your team.

When configured, you can test the Campaign Standard in the **Evaluation preview** pane against any existing campaign in your workspace. The agentic evaluation provides a detailed report with categories of its findings.

## Create a Campaign Standard

### Step 1: Choose the standard type

To create your standard, go to **Agent Console** > **Agentic Standards**. Select **Create Agentic Standard** and choose **Campaign Standards** from the dropdown menu.

### Step 2: Set up details

Next, set up the details for your standard:

1. Enter a name and description to help your team understand its purpose.
2. (Optional) Add tags to filter your standard.
3. Choose the evaluation model for your standard to use. This powers the agentic evaluation of a standard.

![A Campaign Standard "Abandoned Cart Campaign Standards" that defines the rules and rulesets for Abandoned Cart Campaigns in Braze.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Step 3: Configure campaign rules

In the **Campaign Rules** step, define the rules that should be enforced as part of this standard. You can add up to 10 rulesets per standard, and up to 20 rules per ruleset.

Select **Add ruleset** to see a list of the following categories:

- **Campaign setup:** Validates naming conventions, tags, and conversion tracking.
- **Audience and targeting:** Checks segments, exclusions, and audience size.
- **Content and copy:** Defines requirements for text quality, character limits, and message completeness.
- **Links and tracking:** Verifies URLs, CTAs, deep links, and UTM parameters.
- **Personalization and dynamic content:** Defines checks for Liquid logic and fallback values.
- **Compliance and deliverability:** Defines requirements for legal obligations and sending safeguards.
- **Custom rules:** Select **Create custom ruleset** to define unique requirements that don't fit cleanly into any of the pre-configured categories.

If you aren't sure how to phrase a rule, select **Generate with Operator** to have Operator help you draft specific logic based on your requirements.

![Four rules set up for the Audience and targeting category.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Step 4: Test your standard

Before using your standard for campaigns in Braze, use the **Evaluation preview** pane to simulate an agentic evaluation.

1. Choose an existing campaign from the dropdown menu to use as a test case.
2. Choose to test all rulesets or a specific one.
3. Select the **Simulate response** button.

Next, review the results. The evaluation runs against the campaign and displays results in the following categories:

- **Pass:** These rules were met successfully. For example, the evaluation can confirm that your naming conventions match expected patterns.
- **Warning:** These are non-critical issues that may require attention. For example, if you are testing an email ruleset against a webhook campaign, the agentic evaluation may issue a warning that sender names do not apply.
- **Fail:** These are critical issues that should be fixed before launch. Examples include scheduled dates that are in the past or missing required organizational tags.

## Use Agentic Standards

After you have configured a Campaign Standard, you can use it to evaluate any campaign during the final review process. This confirms your campaign meets all requirements before it is sent to your users.

### Run an evaluation

To run an automated evaluation, go to the **Review Summary** step of your campaign creation workflow.

1. Go to the **Agentic Standards** section and select your desired standard from the dropdown menu.
2. Select **Run evaluation**.

If you make changes to your campaign after running an initial evaluation, select **Re-run evaluation** to refresh the results.

### Review evaluation results

After the evaluation is complete, a summary shows the findings in these categories: **Pass**, **Fail**, and **Warning**.
 
The **Fail** tab lists rules that were not met. For each failure, the standard provides the:

- **Rule:** The specific criteria being checked, such as "Spelling & Grammar Check".
- **Reason:** An explanation of why the check failed. For example, the evaluation might identify that "personalized" was used instead of the Australian English spelling "personalised".

The **Pass** tab lists all rules that your campaign successfully followed. This confirms that checks like **Offensive Language Detection** or **Naming Convention Validation** have been cleared.

The **Warning** tab lists non-critical issues that may require attention. For example, if you're testing an email ruleset against a webhook campaign, the evaluation of the standard may yield a warning that sender names do not apply. 

### Resolve or ignore issues

For every identified failure or warning, you can decide how to proceed before launching. Select **Resolve** next to an issue, then select from the following options:

- **Mark as fixed:** Select this after you have updated your campaign configuration or copy based on the evaluation suggestion.
- **Ignore this issue:** Select this to skip the issue for this run only. This is useful for intentional deviations or edge cases where the evaluation suggestion may not apply.
- **Ask BrazeAI Operator:** Select this to fix the issue using Operator.

After all critical issues are resolved or ignored, you can proceed to launch your campaign.

## Best practices

- **Start with templates:** Use the pre-built rulesets for campaign setup and links and tracking first, as these cover the most common manual errors and give the agentic evaluation the right context.
- **Be specific:** When writing custom rules, provide clear examples of what "correct" looks like. For example, instead of writing "Check the naming convention," try "The campaign name starts with the current year (for example, 2026_)."
- **Iterate often:** As your brand guidelines or internal processes change, update your Campaign Standard rulesets to keep your automated checks relevant.
