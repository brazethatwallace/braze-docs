---
nav_title: Send to Destination
article_title: Send to Destination 
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "This reference article covers the Send to Destination component and how to use it in your Canvases."
tool: Canvas
---

# Send to Destination step

> The Send to Destination step allows you to send users from one Canvas to another. For example, if you have two Canvases that share messaging for promotional offers, you can use Send to Destination to connect these Canvases.

## How it works

![A Send to Destination step to send users to a new Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Your current Canvas with the Send to Destination step is the source. Within the step, you can choose the destination Canvas. The incoming users from the source Canvas must follow the entry rules of the destination Canvas. Let's say you have two Canvases:

- **Source:** Canvas 1, includes a Send to Destination step that sends users to Canvas 2
- **Destination:** Canvas 2, with the entry criteria to enter users who ordered an item

This step allows users from Canvas 1 to be sent to Canvas 2. When users from Canvas 1 enter the Send to Destination step, they are evaluated by the entry rules of Canvas 2 to determine if they're eligible to enter the Canvas. In this case, users who ordered an item can enter Canvas 2 and also continue their journey in Canvas 1. For users who haven't ordered an item, they continue their journey in Canvas 1 only.

## Create a Send to Destination step

### Step 1: Add a step

Drag and drop the **Send to Destination** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Send to Destination**.

### Step 2: Choose your destination

Select the dropdown or enter the Canvas name in the **Destination** field. Then, select **Done**.

![A Send to Destination step set up to send users from the a Canvas named "Feature Adoption" to "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Step 3: Preview your destination

You can select **Preview destination** to see the journey for users who meet the entry criteria for the destination Canvas.

After setting up this Canvas step, you can [preview the user path]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) to see if a user proceeds to the next step in the current Canvas and if they also proceed to the destination Canvas.

## Frequently asked questions

### Can I set the destination to a draft Canvas?

Yes. The destination Canvas can have a draft or idle status.

### Are context variables preserved?

Yes. The [context]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) of the source Canvas is always passed to the destination Canvas.
