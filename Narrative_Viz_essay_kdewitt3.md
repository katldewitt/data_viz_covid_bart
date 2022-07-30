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
1. [Conclusion](#conclusion)
1. [Grading Reference](#grading-reference)

## Introduction

For my narrative visualization, I created a story about public transit ridership in the California Bay Area as influenced by the pandemic using D3 in Javascript. Based on the information I have learned in CS416, I designed a narrative that allows me to communicate my point while also giving the user the freedom to explore the data.

Please note that the [grading reference section](#grading-reference) is a tool that will assist you with grading my responses. For ease, I will link back to the appropriate section of my essay; highlight chunks of code; or include screenshots of the visualization.

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

> What visual structure is used for each scene? How does it ensure the viewer can understand the data and navigate the scene? How does it highlight to urge the viewer to focus on the important parts of the data in each scene? How does it help the viewer transition to other scenes, to understand how the data 
connects to the data in other scenes?

I utilized the same axis structure throughout the visual narrative. While this may make some data more compressed (see Santa Clara, which has only 2 BART stations), it allows the viewer to stay oriented to the scale of the decrease in ridership. Additionally, I utilized gentle transitions of the points to ensure that the viewer did not get disoriented when switching data points between scenes.

![Scene 0 Screenshot](scene1_screenshot.png)

For example, switching between the overview scene (above) to the scene showing the pandemic (below), I use the same axes, same colors, and keep a faint outline of the line graph for San Francisco. In the below screenshot, I draw the viewer's attention to the data points in focus through annotations, removing other counties, and changing the title.

![Scene 2 Screenshot](scene2_screenshot.png)

> [Click here to go back to the table of contents.](#table-of-contents)

## Scenes

> What are the scenes of your narrative visualization?  How are the scenes ordered, and why?

TODO: Screenshots.

## Annotations

> What template was followed for the annotations, and why that template? How are the annotations used to support the messaging? Do the annotations change within a single scene, and if so, how and why

I used the `d3-annotations` package and standardized my template for annotations. Below is an example template from scene 1, where I discuss the dip in ridership found in Feb 2019.

```
{
    note: {
      label: "Slight dip in ridership",
      title: "Feb 2019"
    },
    color: ["blue"],
    x: x(new Date("2/1/2019")),
    y: y(8000000),
    dy: 25,
    dx: 10
}
```

In creating the annotation template, I used the principles of data visualization to communicate my message. I used a consistent color scheme (blue for general notes and red for the start of the COVID era to highlight this time point). The consistent color scheme ensures that the user does not become disoriented. Where possible, I had the annotation not cross the line graph of ridership. Additionally, I used the title field as the date (or x value) and the label as the reason this point is highlighted. In order to place the annotations where I wanted, I manually adjusted x, y, dy, and dx.

In on top of the template, I used callouts in 3 specific locations to communicate my message. The first was in scene 0 to emphasize the drop in ridership in March 2020. The second was in scene 1 to provide explanation to the ridership decrease in the November and December; since the explanation applied to two months, it was appropriate to use a callout. Finally, in scene 4, I have an annotation with a callout about return to office for the early months of 2022.

As mentioned above, in scene 0, I have one annotation that appears after a 3 second delay. This change in annotation within a scene is meant to allow the user to first review the graph as a whole then have their attention drawn to the area I want them to focus on.


> [Click here to go back to the table of contents.](#table-of-contents)

## Parameters

> What are the parameters of the narrative visualization? What are the states of the narrative visualization? How are the parameters used to define the state and each scene?

I used the parameters `scene`, `county`, and `year` to control the narrative visualization. Scene worked as a state machine, which drove the values of `county` and `year` for scenes 1-4. In scene 5, I revealed a dropdown box for the user to select the `county` and `year` of interest.

!TODO: more writing here

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

## Grading Reference

The goal of this section is to check all the boxes to make your life (i.e. the grader) easier. Please feel free to use the below table of contents.

**Grading Table of Contents**

<ol type="A">
  <li>URL</li>
  <li>PDF Essay</li>
  <li>Narrative Structure</li>
  <li>Visual Structure</li>
  <li>Scenes and visual Ordering</li>
  <li>Annotations</li>
  <li>Parameters and State</li>
  <li>Triggers</li>
</ol>


### **A. What is the URL of your narrative visualization?**

> [1 point] Does the URL connect to a functioning web page?

Yes. TODO: add link.

### **B. Upload a PDF file essay describing your narrative visualization as required by the assignment instructions.**

> [5 points] Does the essay state what messaging was intended by the narrative visualization?

Yes, see [my section on Messaging above](#messaging).

### **C. Narrative Structure**

> [2 points] Does the essay indicate which structure the narrative visualization was designed to follow (martini glass, interactive slide show or drop-down story)?

> [3 points] Does the narrative visualization follow that structure?

### **D. Visual Structure**

> [2 points] Does the essay indicate what visual structure is used for each scene?

> [1 point] Does the essay indicate how the visual structure ensures the viewer can understand the data?

> [1 point] Does the essay indicate how highlighting is used to get the viewer to focus on the important parts of the data in each scene?

> [1 point] Does the essay indicate how the visual structure helps the viewer transition to other scenes, to understand how the data connects to the data in other scenes?

### **E. Scenes and Visual Ordering**

> [2 points] Does the essay identify the scenes of the narrative visualization?

> [1 point] Does the essay discuss ordering (e.g. the order of elements in a chart or the ordering of scenes)?

> [2 point] Do the charts used as scenes effectively present the data?

### **F. Annotations**

> [2 points] Does the essay discuss annotations?

> [1 point] Does the essay discuss a template for the annotations?

> [2 points] Are the annotations in the narrative visualization effective and consistent?

### **G. Parameters and States**

> [1 point] Does the essay identify the parameters of the narrative visualization?

> [1 point] Does the essay identify the states of the narrative visualization?

> [1 point] Does the essay indicate how are the parameters are used to define the state and each scene?

> [1 point] Does the narrative visualization use parameters to control its state?

> [1 point] Does the narrative visualization use parameters to control each scene?

### **H. Triggers**

> [2 points] Does the essay indicate the triggers that connect user actions to changes of state in the narrative visualization?

> [1 point] Does the essay indicate what affordances are provided to the user to communicate to them what options are available to them in the narrative visualization?

> [1 point] Does the narrative visualization implement and respond to user events properly?

> [1 point] Does the narrative visualization make any effort at all to communicate what options are available to the user?

### TODO LIST

Nice to haves:

1. Tooltip
2. brushing
