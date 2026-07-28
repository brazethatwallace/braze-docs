---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "Learn how to set up and integrate BrazeAI Decisioning Studio<sup>TM</sup> Go into Braze."
---

# BrazeAI Decisioning Studio™ Go

> Learn how to set up and integrate BrazeAI Decisioning Studio™ Go into Braze.

## About Decisioning Studio Go

Decisioning Studio Go is an AI decisioning agent for recurring email programs. Instead of choosing one winning subject line, send time, or image for an entire audience, the agent selects the best combination for each recipient based on their past engagement.

You define the variants the agent can choose from—such as subject lines, CTAs, images, send days, and send times. For each user in your segment, the agent picks the option most likely to drive engagement, within the constraints and schedule you configure.

This differs from campaign-level A/B testing or [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), which optimize a single variant for the whole audience. Decisioning Studio Go personalizes at the individual level across every send in the program.

### How it works

The agent splits a Braze segment into two groups: a Decisioning Studio group that receives AI-optimized email content, and a random control group (minimum 5%) that receives random combinations of the same options. The random control gives you an ongoing, like-for-like measurement of the agent's lift; you can always see how the personalized experience performs against the same content sent without personalization.

For each user in the Decisioning Studio group, the agent chooses across the options you provided: which creative to send (including the specific subject line, CTA, and image within it), and when to send it (day of the week and time of day, respecting quiet hours and the user's local time zone). [Set up your Decisioning Studio Go agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup/) covers each of these in detail.

As users engage—or don't—the agent learns. Reporting indicates when the agent is still in its training period versus when it is actively personalizing, so you always know what stage the agent is in.

### What you configure

| Configuration | Description |
|---|---|
| **Audience** | A single Braze segment as the entry audience. The agent automatically splits the segment between the decisioning group and the random control group. |
| **Schedule** | Send frequency (for example, a single selection three times per week), allowed days of the week, quiet hours in the user's local time zone, and agent-level frequency capping rule adherence. |
| **Creatives** | One or more base creatives built in the Braze composer. Within each base creative, you can mark a subject line, CTA, and image as personalization points using Liquid tags, then provide a list of variants for each. The agent decides which base creative and variant to use for each recipient. |
| **Constraints** | Limits that prevent the agent from sending the same base creative or the same subject line to a user more than once within a window you define. |
| **Review and launch** | A final validation screen surfaces any warnings to attend to before you launch. The agent moves from **Draft** to **Live** and begins sending. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Go configuration" }

### When to use Decisioning Studio Go

The strongest fit is recurring email programs with stable audiences and clickable content, such as always-on calendars (rewards, content drops, lifecycle nudges), evergreen programs (winbacks, re-engagement), and multi-email promotions. These give the agent enough volume and variety to learn meaningfully.

See [Examples for Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples/) for detailed fit guidance by program type.

### Where Decisioning Studio Go sits in the Decisioning Studio suite

Decisioning Studio Go is the entry tier of BrazeAI Decisioning Studio. It's designed for marketers who want one-to-one email personalization without the setup overhead of a full Decisioning Studio Pro implementation.

Decisioning Studio Pro adds: 
- Optimization for any business metric (not just clicks)
- Connection to any first-party data source
- Multi-channel decisioning
- Extended orchestration patterns
- Dedicated support from the Braze AI Decisioning Services team

## Next steps

- [Set up your Decisioning Studio Go agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup/) and configure audience, schedule, creatives, and constraints
- [Review examples for Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples/) to confirm your program is a good fit
- See the [FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq/) for common questions
