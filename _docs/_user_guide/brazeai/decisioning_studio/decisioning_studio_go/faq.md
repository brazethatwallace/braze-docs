---
nav_title: FAQ
article_title: Decisioning Studio Go FAQ
page_order: 8
page_type: FAQ
description: "This page provides answers to frequently asked questions about Decisioning Studio Go."
---

# Frequently asked questions

## General

### What is Decisioning Studio Go?

Decisioning Studio Go is an AI decisioning agent built into the Braze dashboard. You curate a menu of options—creative variants, send timing, days of the week—and the agent picks the right combination for each individual user, optimizing for clicks. It delivers one-to-one personalization without requiring a data scientist or a custom integration. The first release supports email; additional channels follow in separate betas, with each channel handled by its own agent.

### How is this different from A/B testing?

A/B testing finds the variant that performs best on average across an entire audience or within a segment, and rolls that one variant out to everyone in that group. Decisioning Studio Go picks the best variant for each individual user, based on what that user has engaged with before. Different users can receive different variants on the same send. Instead of rolling out one winning variant to a group, Decisioning Studio Go personalizes content at the individual level.

### How is this different from Decisioning Studio Pro?

Go is the self-serve tier. It's the right starting point for marketers who want one-to-one email personalization without a heavy implementation lift. It optimizes for clicks and works with options you configure directly inside Braze. 

Pro is the full-service tier. It optimizes for any business metric, connects to any first-party data source, supports multiple channels, and comes with dedicated support from the Braze AI Decisioning Services team.

### What kind of AI is this? Is it generative?

No. The agent that decides what to send each user is a decisioning agent, not a generative one. It doesn't write content for you. You provide the options, and the agent learns which option works best for each individual user.

Decisioning Studio Go is built on reinforcement learning. The agent treats each send as an opportunity to learn: it tries combinations of the options you've approved, observes whether each user engages, and updates its understanding of what works for whom. Over time, it becomes increasingly accurate at matching each individual user with the option from your menu most likely to drive a click.

## Audiences and control groups

### What's the difference between the Decisioning Studio group and the random control group?

The Decisioning Studio group receives AI-optimized email content; the agent picks the best variant for each user. The random control group receives random combinations of the same options, with no optimization. Both groups respect the constraints you've configured (for example, if you've said not to repeat a subject line within 15 days, that rule applies to the random control as well). Comparing the two groups gives you a clean measure of the agent's lift.

### Is the random control a holdout group of users who receive no email?

No. Random control users still receive emails. They receive randomly selected combinations of the options you configured, sent on randomly selected days within your schedule. This lets you compare "AI-personalized" against "the same content, sent randomly" rather than against "no email at all."

### Why is the random control required?

Two reasons. First, it gives you ongoing, real-time measurement of how much the agent is outperforming a random baseline. Second, the agent uses the random control's behavior as part of its learning signal. The minimum random control size is 5%—that's the floor required for the agent to learn reliably and for performance measurement to be meaningful.

### Can I use a segment that's already used in another Canvas or campaign?

You can, but it's strongly discouraged and a warning appears. When the same users receive messages from Decisioning Studio Go and from other Canvases or campaigns at the same time, the other messages affect engagement in ways the agent can't account for. The cleanest setup is a segment dedicated to the agent.

## Configuration

### What can I personalize?

Within each base creative, you can mark the subject line, the CTA, and an image as personalization points using Liquid tags. The agent then chooses among the variants you provide for each component, per user. You can also have multiple base creatives; the agent picks which base creative to use as well.

### Can I use content blocks for the personalized components?

No. Content blocks don't work as creative-component substitution points at this time. Place your personalized subject line, CTA, and image directly in the email body rather than inside a content block.

### Can I use image-based templates with no clickable elements?

Image-based templates are supported, but they limit what the agent can optimize. If the entire email is one image, the agent can still decide which image to send, but it can't optimize subject line, CTA, or layout within the email. You get more lift from HTML-based templates with multiple personalization points.

### Can I change the conversion event?

For the self-serve tier, the supported conversion event is clicks. In Decisioning Studio Pro, you can optimize for any custom business metric.

### How does send frequency work?

You select a single frequency, such as three sends per week. The agent doesn't decide between frequencies. Within that frequency, it chooses which days (from the days you allowed) and which times (within your quiet hours, in the user's local time zone) to send.

### How do frequency caps work?

During setup, you can apply your workspace's frequency capping rules to the agent and choose whether the agent's sends count toward each user's global frequency cap. Your customer success manager or solutions consultant can help you decide the right approach for your program based on how frequency caps are configured in your workspace.

### Can the agent send across multiple channels?

Each agent is single-channel, and the current supported channel is email. You can run multiple agents in parallel for different programs, but each agent handles one channel.

## Testing and launch

### How do I test before going live?

Use the native test send feature in the Braze Composer. Test sends show specific variant combinations that you select—they're for proofing the email itself, not for predicting what the agent would actually send to a real user. The dynamic preview in the composer also lets you see how different variant combinations render.

### What happens right after I launch?

The agent enters a training period. Emails go out from day one without a waiting period, but performance can fluctuate while the agent explores combinations. Reporting indicates when the agent is still training versus when it has moved into active personalization, so you always know what stage it's in.

### Can I edit the agent after launch?

Yes. Audience, schedule, creatives, and constraints can all be updated post-launch. You must promote changes before they take effect.

### What if I update content options after launch?

You can add, remove, or change variants the same way you set them up originally. Changes need to be promoted before they take effect. Adding a new variant doesn't reset the agent's training on existing variants.

## Reporting and results

### Does Decisioning Studio Go reporting match what I see in my email analytics elsewhere in Braze?

The numbers may differ. Decisioning Studio applies more aggressive click filtering than the standard email reports, so totals can be lower. The relative comparison between the Decisioning Studio group and the random control is consistent within Decisioning Studio reporting, as click filtering is applied to each group equally.

### What metrics does the agent optimize for?

Unique daily clicks per user. The agent's goal is to maximize the number of distinct users who click, not raw click volume.

### Can I see which combinations are performing best?

Yes. Reporting includes the distribution of individual elements—such as subject lines, CTAs, and images—that the agent sends.

### Who's accountable for the content the agent sends?

You are. The agent only sends content that you've added as a variant. The agent decides the combination for each user, but every individual element comes from the variants you provided.

## Support

### Where do I get help with my agent?

Reach out to your Braze customer success manager or solutions consultant for help with configuration, performance review, or program design.
