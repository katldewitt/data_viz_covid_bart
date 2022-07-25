# BART Ridership Narrative Visualization

**NetId**: Kdewitt3

**Student Name**: Kathryn DeWitt

**Course**: CS416 Data Visualization

## Table of Contents

1. [Introduction](#introduction)
1. [Messaging](#messaging)
1. [Narrative Structure](#narrative-structure)
1. [Visual Structure](#visual-structure)
1. [Scenes](#scenes)
1. [Annotations](#annotations)
1. [Parameters](#parameters)
1. [Triggers](#triggers)
1. [Conclusions](#conclusion)

## Introduction

For my narrative visualization, I created a story about public transit ridership in the California Bay Area as influenced by the pandemic using D3 in Javascript. Based on the information I have learned in CS416, I designed a narrative that allows me to communicate my point while also giving the user the freedom to explore the data.

> [Click here to go back to the table of contents.](#table-of-contents)

## Messaging

> What is the message you are trying to communicate with the narrative visualization?

The message I am trying to communicate with the narrative visualization is that Bay Area Rapid Transit (BART) ridership has decreased significantly due to the pandemic and has not rebounded. The user can explore this trend by county and station. This is the main finding I found when putting together [a Tableau dashboard for a previous assignment in this class](https://public.tableau.com/views/COVIDsImpactonBARTRidership/FinalDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link).

> [Click here to go back to the table of contents.](#table-of-contents)

## Narrative Structure

> Which structure was your narrative visualization designed to follow (martini glass, interactive slide show or drop-down story)? How does your narrative visualization follow that structure? (All of these structures can include the opportunity to "drill-down" and explore. The difference is where that opportunity happens in the structure.)

When designing my narrative, I decided to follow a Martini Glass structure to walk the viewer through San Francisco's ridership data. San Francisco had the highest ridership prior to the pandemic, which makes the drop in 2020 especially stark. Additionally, for those living outside of the Bay Area, San Francisco is a familiar city name. The user first goes through an overview of the data, followed by a presentation showing how BART ridership changed in each calendar year. At scene number 5, the user is free to explore on their own using the drop downs for `year` and `county`. I found the Martini Glass structure particularly useful to communicate my message as the paths the user can explore are similar to those of San Francisco.

> [Click here to go back to the table of contents.](#table-of-contents)

## Visual Structure

> What visual structure is used for each scene? How does it ensure the viewer can understand the data and navigate the scene? How does it highlight to urge the viewer to focus on the important parts of the data in each scene? How does it help the viewer transition to other scenes, to understand how the data connects to the data in other scenes?

I utilized the same axis structure throughout the visual narrative. While this may make some data more compressed (see Santa Clara, which has only 2 BART stations), it allows the viewer to stay oriented to the scale of the decrease in ridership. Additionally, I utilized gentle transitions of the points to ensure that the viewer did not get disoriented when switching data points between scenes.

- would like a train to transition to other scenes...

> [Click here to go back to the table of contents.](#table-of-contents)

## Scenes

> What are the scenes of your narrative visualization?  How are the scenes ordered, and why?

TODO: Screenshots.

## Annotations

> What template was followed for the annotations, and why that template? How are the annotations used to support the messaging? Do the annotations change within a single scene, and if so, how and why

- TODO: template definition?
- Annotation: text describing scene

> [Click here to go back to the table of contents.](#table-of-contents)

## Parameters

> What are the parameters of the narrative visualization? What are the states of the narrative visualization? How are the parameters used to define the state and each scene?

I used the parameters `scene`, `county`, and `year` to control the narrative visualization. Scene worked as a state machine (TODO: is this language right?), which drove the values of `county` and `year` for scenes 1-4. In scene 5, I revealed a dropdown box for the user to select the `county` and `year` of interest.

> [Click here to go back to the table of contents.](#table-of-contents)

## Triggers

> What are the triggers that connect user actions to changes of state in the narrative visualization? What affordances are provided to the user to communicate to them what options are available to them in the narrative visualization?

- affordance lets user know how to interact w/ them
- need data pt/city name in tool tip
- need ability to highlight county

TODO: affordances/highlight dp

The most basic triggers I utilized to change state are dropdowns and buttons in scene 5, user directed exploration. I used `click`ing on a button to reset to all counties. In selecting `scene`, `county`, and `year`, I used a drop down that utilized an event listener that checked for `change`s.  

> [Click here to go back to the table of contents.](#table-of-contents)

## Conclusion

> [Click here to go back to the table of contents.](#table-of-contents)

### TODO LIST

Must haves:

1. Title for chart
2. Annotations
3. Scene # -> State
4. Triggers between scenes.

Nice to haves:

1. Get data in a line graph separated by county
2. brushing
