# Project4 - BookBlog

![]() screenshot from am I responsive

This project is created as part of Code Institute's Software Development course.
[BookBlog's](https://bkblog-fdb72a8c4df9.herokuapp.com/) layout and code is mainly based on Code Institute's Walk-through project ["I Think Therefore I Blog"](https://github.com/Code-Institute-Solutions/blog/tree/main). BookBlog has no commercial value or intention.
Aim of this project is to create a blog where Site Users can share book reviews, or create articles for the bookblog, comment on the reviews/books/blog posts. All of the articles, reviews, comments and suggestions need to be approved by BookBlog's Admin.
Bookblogs theme: books and experiences related to energy work, ascension, natural methods to work on wellbeing, heureka moments, serendipity, beautiful changes in life and similar.

Deployed site: [BookBlog](https://bkblog-fdb72a8c4df9.herokuapp.com/)

Github: [link to github](https://github.com/BarbyKelly/blog)

# Content
- [UX Design](#ux-design)
- [User Stories](#user-stories)
- [Features](#features)
- [Structure](#structure)
- [Testing & Validation](#testing--validation)
- [Deployment](#deployment)
- [References & Credits](#references--credits)
- [Acknowledgements](#acknowledgements)



# UX Design

## User Stories

### Admin can:

- Create BookBlog content
- Manage BookBlog content
- Add, edit and delete their own comments
- Approve comments
- Edit and Delete any comments by any Site User
- Add resources
- Edit and delete resources
- Mark Collaboration Requests as "read"


#### Future Features for Admin:

- Comments by Site Users can only be edited by Site Users, and deleted by Admin if needed

### Site User can:

- View a paginated list of posts, and choose which one to read
- Sign up for an account
- Login
- Add comments
- Modify or delete their own comments
- Create drafts

#### Future Features for Site Users:

- Sign up for Newsletter
- Create posts together with other Site Users
- Comments limited to max 500 characters
- System blocking unsuitable/rude/inappropriate words
- Create blog content

### Visitor may:

- View a paginated list of posts, and choose which one to read
- Click on Home, About, Resources, Register, Login
- Opt to Sign up for an account
- Fill on Collaborator Form

#### Future Features for Visitors:

- Sign up for Newsletter

[Back to the overview](#content)


### Documenting & Testing

[Back to the overview](#content)


### Deployments

- Ensure env.py is set up properly
- Check gitignore
- Set DEBUG=False in settings.py
- Login to Heroku
- Click on settings in the Menu
- Click on Reveal Config Vars
- Check if these look ok
- Click on Deploy in the main menu
- Scroll down to the end and click on Deploy Branch
- Once Heroku has finished deploying your app, "View app" appears at the bottom of the page
- Click on "View app"

[Back to the overview](#content)


## Wireframes

- Wireframes created with [Balsamiq](https://balsamiq.com/wireframes/)

### Homepage

![wireframe home page](docs/readmeimages/wireframehome.png)

### Comment as a Logged in User

![wireframe comment option](docs/readmeimages/wireframecomment.png)

### About page

![wireframe comment option](docs/readmeimages/wireframecomment.png)

### Resources page

![wireframe resources page](docs/readmeimages/wireframeresources.png)

### Signup page

![wireframe sign up page](docs/readmeimages/wireframesignup.png)

### Login page

![wireframe login page](docs/readmeimages/wireframelogin.png)

[Back to the overview](#content)


## Fonts


## Colors

- Color contrast for large text checked on [Coolors website](https://coolors.co/contrast-checker/6f90f4-ffffff)
- Color contrast check for brand, checked on [Coolors](https://coolors.co/contrast-checker/35353b-ffffff)

## Media

[Back to the overview](#content)


# Features

## Common Features
- **Navigation Menu**
    - Home
    - About
    - Resources
    - Sign up
    - Login

- **Footer**
    - Copyright
    - Social Media links

## Homepage Features
- Three different articles are displayed, with author's name, suitable image, excerpt, and date and time of the article
- Page visitor can see if they are logged in or not, top right corner
- Below the articles, there's a button 'next', which brings site visitor to the next page of articles


## Website Error Pages

## Future Features


[Back to the overview](#content)

# Testing & Validation

## Bugs

- Resources app displayed only one resource at a time. With tutor's guidance to add for loop, all of the resources were displayed.

- Images for blog articles showed up on the Home page as expected. Once site user clicked on the article, placeholder image was displayed instead.

### Known Bugs


### Forking the repository

- Go to [Github](https://github.com/)
- If you want to fork one of your own repos, then DO NOT login under your own name, as fork option is not available

![How fork looks when logged in](docs/readmeimages/notpossibletofork.png)

- Search Github or Google for the repo that you would like to fork
- Open the repo you want to fork
- On the same line as the Repo's name, on the right, click on the arrow beside the Fork
- Click on: + Create a new fork

![Create a new fork](docs/readmeimages/createanewfork.png)

- Choose a name for the repo
- Add description if you desire
- Choose if you want to Copy the main branch only
- Click on: "Create fork"

![Create fork](docs/readmeimages/createfork.png)

- [Spoon-Knife Github repo](https://github.com/octocat/Spoon-Knife) was used to demonstrate how to fork


### Creating the repository

- Code Institute's [template](https://github.com/Code-Institute-Org/ci-full-template) was used to set up this project.
- After clicking on the above template link, click on the green button: "Use this template"
- From there choose: "Create a new repository"
- Fill in "Repository name" with your desired name for the project
- Leave the project Public like the default setting (for Code Institute projects)
- Click on the green button "Create repository"

[Back to the overview](#content)


# References & Credits

- BookBlog's code is highly based on Code Institute's Walk-through project ["I Think Therefore I Blog"](https://github.com/Code-Institute-Solutions/blog/tree/main)

- General ReadMe template derived from: [findMEreadME](https://github.com/brodsa/findMEreadME/blob/main/README.md#content)

- Developer got inspiration for her ReadMe User Stories layout from her Facilitator Laura's Project 4: [The Happy Reader](https://github.com/LauraMayock/The-happy-reader/blob/main/README.md)

- Wireframes created with [Balsamiq](https://balsamiq.com/wireframes/)

- Developer read this article to remember how to get links to open in a new tab. Article by Jessica Wilkins: [How to Open a Link in a New Tab](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/#:~:text=You%20can%20use%20the%20target,opening%20anchor%20tag%20like%20this.)
 
- How to add favicon: [W3 Schools](https://www.w3schools.com/html/html_favicon.asp)


## Images

- Inna Segal's book cover image from: [Paper Plus](https://www.paperplus.co.nz/shop/books/non-fiction/mind-body-spirit/general/the-secret-language-of-your-body)

- Double rainbow: taken by the developer

- Flowers drawing by developer's 10 year old daughter Aoife, made in school

- Penguin drawing by developer's 6 year old daughter Ciara, made in school

- Beach: taken by the developer, Fenit, Co. Kerry, Ireland

- Default image clouds taken by the developer, Co. Kerry, Ireland

- Images converted with [Simple Image Resizer](https://www.simpleimageresizer.com/resize-image-to-500-kb)

[Back to the overview](#content)

# Acknowledgements

- Developer is grateful for any guidance and support provided by her family and friends, mentor, facilitator, tutors, Slack members, and Django project related content creators  
[Back to the overview](#content)