# Instructions
Overview

Create a narrative visualization implemented as an interactive web page, using your knowledge of visual communication and narrative structure, along with your skills at D3 programming in JavaScript. The narrative visualization should be implemented on a publicly visible website, such as github.io. See https://pages.github.com/  for instructions on how to use github to host a website. You will turn in this project by submitting the URL to the narrative visualization for grading, along with an essay describing how the interactive web page contains the elements of a narrative visualization and satisfies the requirements of this assignment.

The narrative visualization should follow one of the three effective narrative visualization structures:

1. a martini glass, where the message is delivered without allowing user exploration until the end,

1. an interactive slideshow, where user exploration is allowed at some or all of the steps of the story, or

1. a drill down story. which presents an overview and allows the user to explore different storylines from there.

You must use the D3 library to construct your pages. You cannot use Tableau Stories, Vega, Vega-Lite, Ellipses or any other high-level tool designed for data visualization to implement your narrative visualization. The only other library allowed for this assignment is d3-annotation. No other library besides d3 (any version) and d3-annotation will be allowed on this assignment.

The narrative visualization should be built with scenes, annotations, parameters, and triggers.

The scenes should follow a template for visual consistency and follow an order to best convey the message. One way to implement different scenes is to make each a separate web page. Another way is to use d3.select(id).html = "" to clear the contents of a container element (e.g. an SVG element) and then repopulate that element using .append().

The annotations should follow a template for visual consistency from scene to scene. These annotations should also highlight and reinforce specific data items or trends that make the important points for the desired messaging of the narrative visualization. The lessons on d3 popups can be helpful on how to to make and place annotations, but as an annotation, they should appear as part of the scene and not have to wait for a mouseover event.

The parameters are the state variables of your narrative visualization. Your narrative visualization should use these parameters to control the construction of scenes. These parameters will be key variables in your JavaScript code, as well as parameters to key functions used to set up each scene.

The triggers connect user interface actions to changes in parameters that change the state of the narrative visualization. These triggers can be event listeners (callback functions) that change parameter values and then update the display to reflect the result of the event.

This assignment can be successfully completed using as few as three scenes. Those three scenes can simply highlight different details or different data from the same chart. That chart can also be one of the charts we have previously used as an example (e.g. the scatterplot of 2017 automobile data). You can use any dataset you would like, or one of the datasets we have used previously. Free-form user interaction can be as simple as tooltip popups that allow the user to see more information on data items. Just be sure to indicate when a user can access these tooltips, and make sure this free-form user interaction fits properly into the narrative visualization structure.

Due to the end of the semester, this assignment has a hard deadline of 11:59pm CDT Sunday, July 31st, 2022.

## Review Criteria

An essay will be required and will be submitted along with the URL of the narrative visualization. This essay is an important piece of the assignment as it is used for you to communicate your understanding of the concepts of narrative visualization and how they apply to the one you created.

The essay should contain the following sections.

## Messaging. 

What is the message you are trying to communicate with the narrative visualization?

## Narrative Structure. 

Which structure was your narrative visualization designed to follow (martini glass, interactive slide show or drop-down story)? How does your narrative visualization follow that structure? (All of these structures can include the opportunity to "drill-down" and explore. The difference is where that opportunity happens in the structure.)

## Visual Structure. 

What visual structure is used for each scene? How does it ensure the viewer can understand the data and navigate the scene? How does it highlight to urge the viewer to focus on the important parts of the data in each scene? How does it help the viewer transition to other scenes, to understand how the data connects to the data in other scenes?

## Scenes. 

What are the scenes of your narrative visualization?  How are the scenes ordered, and why

## Annotations. 

What template was followed for the annotations, and why that template? How are the annotations used to support the messaging? Do the annotations change within a single scene, and if so, how and why

## Parameters. 

What are the parameters of the narrative visualization? What are the states of the narrative visualization? How are the parameters used to define the state and each scene?

## Triggers. 

What are the triggers that connect user actions to changes of state in the narrative visualization? What affordances are provided to the user to communicate to them what options are available to them in the narrative visualization?

## Update from CampusWire

Dear Students,

The grading reference for the narrative visualization project in included at the end of this post.

This is a conclusive list of points, and the graders will only pay attention to these items. No extra-credit for elegance, having more scenes than enough, etc. will be applied to your grade. This list will not be modified.

The points here add up to 36.

The itemized questions are framed as clearly as possible.

To avoid any any confusion, we will not clarify any of the items further neither on Campuswire nor during office hours. While answering a certain question may assure a group of students, it may confuse/worry many other students. Furthermore, we cannot keep the whole class in suspense and constantly checking for new guidelines here and there. To be fair to all students, we won't provide any new information.
If you have any doubts on whether your answer satisfies a particular item, then you should modify your answer until you have no further doubts about receiving the point. Before grading, we cannot confirm whether your answer satisfies a certain item.
The grading will only consider what you delivered, and not what you intended.

If your project is a martini glass but you don't mention it clearly in your essay, then you will lose points no matter how basic or visible it may seem. Graders will only look for the answers in the relevant parts; having answers out of their appropriate places will not count during grading.
Be precise, and answer all the questions clearly and to-the-point. Place yourself in the shoes of the grader. If locating the answer to a particular item doesn't seem easy, or if the answer is buried under too much irrelevant information, then you will likely lose the points for that item. Help the graders give you the points you deserve, and make their life easier by pointing them to what they'll be looking for.

While this is not necessary, it may be a good idea to (a) keep the grading reference structure in mind when writing your essays, and (b) append the following checklist with pointers to each specific item's answer to the end of your essay. This is mainly to help the grader find your specific answers if they had difficulty looking them up.

Sincerely, Ehsan

# The Grading Reference

**A. What is the URL of your narrative visualization?**

[1 point] Does the URL connect to a functioning web page?

**B. Upload a PDF file essay describing your narrative visualization as required by the assignment instructions.**

[5 points] Does the essay state what messaging was intended by the narrative visualization?

**C. Narrative Structure**

[2 points] Does the essay indicate which structure the narrative visualization was designed to follow (martini glass, interactive slide show or drop-down story)?

[3 points] Does the narrative visualization follow that structure?

**D. Visual Structure**

[2 points] Does the essay indicate what visual structure is used for each scene?

[1 point] Does the essay indicate how the visual structure ensures the viewer can understand the data?

[1 point] Does the essay indicate how highlighting is used to get the viewer to focus on the important parts of the data in each scene?

[1 point] Does the essay indicate how the visual structure helps the viewer transition to other scenes, to understand how the data connects to the data in other scenes?

**E. Scenes and Visual Ordering**

[2 points] Does the essay identify the scenes of the narrative visualization?

[1 point] Does the essay discuss ordering (e.g. the order of elements in a chart or the ordering of scenes)?

[2 point] Do the charts used as scenes effectively present the data?

**F. Annotations**

[2 points] Does the essay discuss annotations?

[1 point] Does the essay discuss a template for the annotations?

[2 points] Are the annotations in the narrative visualization effective and consistent?

**G. Parameters and States**

[1 point] Does the essay identify the parameters of the narrative visualization?

[1 point] Does the essay identify the states of the narrative visualization?

[1 point] Does the essay indicate how are the parameters are used to define the state and each scene?

[1 point] Does the narrative visualization use parameters to control its state?

[1 point] Does the narrative visualization use parameters to control each scene?

**H. Triggers**

[2 points] Does the essay indicate the triggers that connect user actions to changes of state in the narrative visualization?

[1 point] Does the essay indicate what affordances are provided to the user to communicate to them what options are available to them in the narrative visualization?

[1 point] Does the narrative visualization implement and respond to user events properly?

[1 point] Does the narrative visualization make any effort at all to communicate what options are available to the user?
