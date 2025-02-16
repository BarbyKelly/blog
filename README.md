# Project4 - BookBlog

This project is created as part of Code Institute's Software Development course.
[BookBlog's](https://bkblog-fdb72a8c4df9.herokuapp.com/) layout and code is based on Code Institute's Walk-through project
["I Think Therefore I Blog"](https://github.com/Code-Institute-Solutions/blog/tree/main). BookBlog has no commercial intention.
Aim of this project was to create a blog where Site Users can share book reviews, or create articles for the bookblog, comment on the reviews/books/blog posts. All of the articles, reviews, comments and suggestions need to be approved by BookBlog's Admin.
Bookblogs theme: books and experiences related to energy work, ascension, natural methods to work on wellbeing, heureka moments, serendipity, beautiful changes in life and similar.
At the time of submission deadline, on developer's screen there seems to be only an option to add posts via Django page. 

Deployed site: [BookBlog](https://bkblog-fdb72a8c4df9.herokuapp.com/)

Github: [link to github](https://github.com/BarbyKelly/blog)

![Am I Responsive image](docs/readmeimages/amiresponsive.png)


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

- Comments by Site Users can only be edited by Site Users, and deleted by Admin if needed, no editing option for Admin, except for their own comments

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
- Comments visible only to Signed In users
- Sign Out form has an option to "Go Back" with a button, instead of just clicking on a different NavLink, if don't want to Sign Out

### Visitor may:

- View a paginated list of posts, and choose which one to read
- Click on Home, About, Resources, Register, Login
- Opt to Sign up for an account
- Fill on Collaborator Form

#### Future Features for Visitors:

- Sign up for Newsletter

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


## Colors

- Color contrast for large text checked on [Coolors website](https://coolors.co/contrast-checker/6f90f4-ffffff)
- Color contrast check for brand, checked on [Coolors](https://coolors.co/contrast-checker/35353b-ffffff)


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


## Resources Features
- Various links are available for Visitor
- Visitor can click on links to open YouTube videos
- Only Admin can add and edit Resources


## Future Features

- Site Users can add posts once they log in
- Admin can add posts not just only via Django
- Add an option to like the comment or post with a heart favicon
- Resources page displaying "Suggestion" form, for visitors to be able to fill it
- Image/video of waves on top of Resources page
- Resources are displaying their default image/website, not just the link/text
- Admin would notify User, if their Comment has been deleted due to inappropriate details, wording or images
- Admin won't have an option to edit other User's post
- Admin can notify User if there's spelling error, inappropriate details, in their comment, before deleting it
- Resources to be replaced with links that open without ads
- Resources not displayed if 'Draft' or 'Unapproved' or 'Not yet approved'
- Sign Up form to have asterisk for required fields: Username, Password, Password(again)
- When Sign Up is successful, and Home page opens, pop up on the screen to say "Successfully signed up, and signed in as ...",
  instead of "Successfully signed in as..."

[Back to the overview](#content)

# Testing & Validation

- Testing and Validation can be accessed here: [TESTING.md](../TESTING.md)

# List of Tests, Validations
- [Lighthouse Reports](Lighthouse Reports)
- [HTML Validator](HTML Validator)
- [CSS Validator](CSS Validator)
- [JS Validator](JS Validator)
- [NavBar, NavLinks, NavButtons](NavBar, NavLinks, NavButtons)
- [About Page, Collaboration Form](About Page, Collaboration Form)
- [Blog Posts, Comments, Edit and Delete Options, Approving of Comments](Blog Posts, Comments, Edit and Delete Options, Approving of Comments)
- [Social media links in Footer](Social media links in Footer)
- [ReadMe links](ReadMe links)


## Lighthouse Reports

  validated with Google developer tools

- ![Lighthouse Home](docs/readmeimages/lighthousetest.png)

- 

-

-

-



  


## HTML Validator

- ![HTML Validator](docs/readmeimages/htmlcheck.png) 

  validated with: [W3C Markaup Validation](https://validator.w3.org/)


## CSS Validator

- ![CSS Validator](docs/readmeimages/cssvalidator.png) 

  validated with: [W3C Markup Validation](https://validator.w3.org/)


## JS Validator

- ![JS Validator](docs/readmeimages/jsvalidator.png)

  validated with: [codebeautify](https://codebeautify.org/jsvalidate)


## NavBar, NavLinks, NavButtons 

| Tested Item | Expected Outcome                                      | Outcome     |
| ----------- | ----------------------------------------------------- | ----------- |
| Home        | Clickable,                                            | as expected |
| NavLink     | Opens Home page,                                      | as expected |
|             | Or refreshes it if user is already on Home page,      | as expected |
|             | Color of Home NavLink darkens once it's selected,     | as expected |
|             | Opens in the current tab                              | as expected |         
|             |                                                       |             |
| About       | Clickable,                                            | as expected |
| NavLink     | Opens About page,                                     | as expected |
|             | Or refreshes it if user is already on About page,     | as expected |
|             | Color of About NavLink darkens once it's selected,    | as expected |
|             | Opens in the current tab                              | as expected | 
|             |                                                       |             |
| Resources   | Clickable,                                            | as expected |
| NavLink     | Opens Resources page,                                 | as expected |
|             | Or refreshes it if user is already on Resources page, | as expected |
|             | Color of Resources NavLink darkens once it's selected,| as expected |
|             | Opens in the current tab                              | as expected | 
|             |                                                       |             |
| Sign In     | Clickable,                                            | as expected |
| NavLink     | Visible only when user is not Signed In,              | as expected |
|             | Opens up a Sign In form,                              | as expected |
|             | which shows an option to Sign Up if no account,       | as expected | 
|             | Color of Sign In NavLink darkens once it's selected,  | as expected |
|             | Once logged in, Sign Out replaces Sign In on NavBar,  | as expected |
|             | Message appears "Successfully signed in as (username)"| as expected |
|             | Signed in as (username) appears on the right side,    | as expected |
|             | And is visible on all Pages while user is signed in,  | as expected |
|             | Sign Up option is visible if not signed in            | as expected |
|             |                                                       |             |
| Sign Out    | Sign Out is visible only when user is Signed In,      | as expected |
| NavLink     | Color of Sign Out NavLink darkens once it's selected, | as expected |
|             | Opens in the current tab,                             | as expected | 
|             | Sign Out form Opens with an option to Sign Out,       | as expected |
|             | Or refreshes the Sign Out page if user already on Sign| as expected |
|             | Out page,                                             |             |
|             | Sign Out option remains on the page,                  | as expected |
|             | for the user until Sign Out button is clicked,        |             |
|             | after which message pops up: "You have signed out.",  | as expected |
|             | And Sign In option appears instead of Sign Out,       | as expected |
|             | And now on the right side can see "Not signed in",    | as expected |
|             | And Sign Up option is now available in NavBar         | as expected |
|             |                                                       |             |
| Logo        | Clickable,                                            | as expected |
|             | Opens Home page,                                      | as expected |
|             | Or refreshes Home page if user is already on Home page| as expected |
|             | Opens in the current tab                              | as expected | 
|             |                                                       |             |
| NEXT >>     | Visible only on Home page (accessed via               | as expected |
|             | Home page or Logo),                                   |             |
|             | Clickable,                                            | as expected |
|             | Available to user when signed in,                     | as expected |
|             | And when not signed in,                               | as expected |
|             | On the next page << PREV NavButton appears instead    | as expected |
|             |                                                       |             |
| << PREV     | Visible only on Home page after NEXT >> is clicked,   | as expected |
|             | And the user can see the next page,                   |             |
|             | Clickable,                                            | as expected |
|             | Available to user when signed in,                     | as expected |
|             | And when not signed in,                               | as expected |
|             | << PREV is replaced by NEXT >> on the first Home page | as expected |
|             |                                                       |             |
| NavBar Text | Not Clickable,                                        | as expected |
|             | sharing beautiful moments remains the same,           | as expected |
|             | Visible in top right corner on all pages              | as expected |


## Blog Posts, Comments, Edit and Delete Options, Approving of Comments

| Tested Item | Expected Outcome                                      | Outcome         |
| ----------- | ----------------------------------------------------- | --------------  |
| Blog Post   | Clickable Blog Post title,                            | as expected     |
|             | Opens in a new tab,                                   | as expected     |
|             | Title, author, time of creation are visible,          | as expected     |
|             | Blog Posts text is visible and clear,                 | as expected     |
|             | Full Image of the blog post is visible                | not as expected |
|             | beside the title, on different screen sizes,          |                 |
|             | Image of the blog post is visible on different        | not as expected |
|             | screen sizes,                                         |                 |
|             |                                                       |                 |
| Comment     | Clickable,                                            | as expected     |


## About Page, Collaboration Form

| Tested Item | Expected Outcome                                                  | Outcome     |
| ----------- | ----------------------------------------------------------------- | ----------- |
| About       | About page opens when About is clicked on in the NavBar,          | as expected |
| Page        | Page available when Signed in or not Signed in,                   | as expected |
|             | Admin can access via NavBar and via Django.                       | as expected |
|             |                                                                   |             |
|             | NavLink About in the NavBar darkens to show user is on About page,| as expected |
|             | NavText remains in the top right corner,                          | as expected |
|             | Top right corner, below NavText, user can see if Signed in        | as expected |
|             | or signed out                                                     | as expected |
|             |                                                                   |             |
| Image       | Default image is displayed on the left side or                    | as expected |
|             | above the text (if smaller screen size),                          | as expected |
|             | only Developer can add/edit/change/delete Images on About page,   | as expected |
|             |                                                                   |             |
| Text        | Developer's view on what this website/project is about,           | as expected |
|             | disclaimer Collaboration Forms won't be replied to,               | as expected |
|             | only Developer can add/edit/delete About page text,               | as expected |
|             | date and time of the update of the text are on the right,         | as expected |
|             | below the text about the website                                  | as expected |
|             |                                                                   |             |
| Form        | Collaboration Form is part of About page,                         | as expected |
|             | located below text about the website,                             | as expected |
|             | Visitor might need to scroll to see the form,                     | as expected |
|             | Form is accessable when Signed in,                                | as expected |
|             | and when not Signed in.                                           | as expected |
|             |                                                                   |             |
| Name        | Name field is part of the Collaboration form,                     | as expected |
| field       | Visitor can type in Name* field,                                  | as expected |
|             | Name field is mandatory if visitor wants to submit form,          | as expected |
|             | Name field is marked with an asterisk to show it's mandatory,     | as expected |
|             | pop up appears if trying to submit without name:                  | as expected |
|             | "Please fill in this field",                                      | as expected |
|             |                                                                   |             |
| Email       | Email field is part of the Collaboration form,                    | as expected |
| field       | Visitor can type in Email* field,                                 | as expected |
|             | Email field is mandatory if want to submit form,                  | as expected |
|             | Email field is marked with an asterisk to show it's mandatory,    | as expected |
|             | pop up appears if trying to submit without email:                 | as expected |
|             | "Please fill in this field",                                      | as expected |
|             | pop up appears if no text before '@' in the email:                | as expected |
|             | "Please enter a part followed by '@'. '@...' is incomplete"       | as expected |
|             | pop up appears when no '@' in the email:                          | as expected |
|             | "Please include an '@' in the email...",                          | as expected |
|             | pop up appears if no text after '@' in the email:                 | as expected |
|             | "Please enter a part following '@'. '...@' is incomplete"         | as expected |
|             |                                                                   |             |
| Message     | Message field is part of the Collaboration Form,                  | as expected |
| field       | Visitor can type in Message* field,                               | as expected |
|             | Message field is mandatory if want to submit form,                | as expected |
|             | Message fiels is marked with an asterisk, to show it's mandatory  | as expected |
|             | pop up appears if trying to submit without message:               | as expected |
|             | "Please fill in this field"                                       | as expected |
|             |                                                                   |             |
| Submit Here | 'Submit Here' button is accessible below the Collaboration Form.  | as expected |
| button      | Visitor can click on 'Submit Here' button.                        | as expected |
|             | If Name, Email and Message fields have text in them,              |             |
|             | and Email matches all required aspects                            | as expected |
|             | then Collaboration Form is submitted once 'Submit Here' is clicked| as expected |
|             | and pop up appears:                                               | as expected |
|             | "Collaboration Form received. Reviewed within 48 hours."          | as expected |
|             | If form is not filled as requested,                               |             |
|             | pop up would appear, after visitor clicks on 'Submit Here',       | as expected |
|             | informing visitor to adjust the field,                            |             |
|             | that is not filled as required                                    | as expected |

## Resources page

| Tested Item | Expected Outcome                                      | Outcome     |
| ----------- | ----------------------------------------------------- | ----------- |
|             | Logo, NavLinks, NavText displayed on top of the page, | as expected |
|             | Signed in or Not Signed in displayed on the right     | as expected |
|             | Resources NavLink is darkened,                        | as expected |
|             | to show visitor which page they are on                |             |
|             |                                                       |             |
|             | Titles of various links are displayed on the page.    | as expected |
|             | Links to each Resource are displayed,                 | as expected |
|             | links are clickable.                                  | as expected |
|             | On the click, selected link opens in a new tab,       | as expected |
|             | in YouTube,                                           | as expected |
|             | Resources page remains open in a previous tab,        | as expected |
|             | If visitor has YouTube subcsription,                  | as expected |
|             | link content starts on YouTube after link is clicked, | as expected |
|             | if visitor has no YouTube subscription,               | as expected |
|             | random ad chosen by YouTube may play first,           | as expected |
|             | which is out of Developer's expertise                 | as expected |
|             |                                                       |             |
|             | Note on the right below links,                        | as expected |
|             | stating Resources added by Site's admin               | as expected |


## Sign Up page

| Tested Item | Expected Outcome                                                 | Outcome     |
| ----------- | ---------------------------------------------------------------- | ----------- |
| Sign Up     | Logo, NavBar, NavLinks, NavText displayed,                       | as expected |
| page        | or NavLinks and NavText in the Side Menu,                        | as expected |
|             | if smaller screen                                                | as expected |
|             | On the right,                                                    | as expected |
|             | below Side Menu or NavText,                                      | as expected |
|             | 'Not signed in' is displayed.                                    | as expected |
|             |                                                                  |             |
|             | Below Sign Up Title, text Welcomes users,                        | as expected |
|             | gives an option to 'Sign In' if user already has an account,     | as expected |
|             | with a clickable 'Sign In' link.                                 | as expected |
|             |                                                                  |             |
| Sign Up     | Sign Up form is displayed,                                       | as expected |
| Form        | with Username, Email, Password, Password(again) fields,          | as expected |
|             | and grayed out field names where Visitor can type.               | as expected |
|             |                                                                  |             |
| Username    | Visitor can type in what Username they would like.               | as expected |
|             | Username is required, even though there's no asterisk            | as expected |
|             | highlighting that Username is required.                          | as expected |
|             | When cursor is on Username field,                                | as expected |
|             | 'Please fill in this field' appears below the field.             | as expected |
|             | Letters, Numbers and certain special characters are allowed.     | as expected |
|             | If different special characters are entered,                     | as expected |
|             | Notice appears above Username field:                             | as expected |
|             | 'Enter a valid username. This value may contain only letters,    | as expected |
|             | numbers, and @/./+/-/_ characters.'                              |             |
|             |                                                                  |             |
|             | If Username is entered and 'Sign Up' clicked,                    | as expected |
|             | without filling in Password fields,                              | as expected |
|             | "Please fill in this field" pops up below Password field.        | as expected |
|             |                                                                  |             |
|             | If nothing is entered in Username field,                         | as expected |
|             | and user clicks on 'Sign Up' button,                             | as expected |
|             | pop up appears near Username field: "Please fill in this field." | as expected |
|             |                                                                  |             |
|             | When User has tried a few Usernames to sign up with,             | as expected |
|             | these Usernames show up as options, when cursor is in Username   | as expected |
|             | field,                                                           |             |
|             | and User has an option to choose one of them,                    | as expected |
|             | by moving cursor to the selected one,                            | as expected |
|             | and clicking on it,                                              | as expected |
|             | and selected Username then appears in Username field.            | as expected |
|             | If this Username is already not taken by someone else,           | as expected |
|             | User can sign up with that Username.                             | as expected |
|             | If this Username is already taken by someone else,               | as expected |
|             | and new User clicks on 'Sign Up' button, with that Username      | as expected |
|             | displayed on their Username field,                               | as expected |
|             | message will show above Username:                                | as expected |
|             | "A user with that username already exists."                      | as expected |
|             | User can try to sign up with a different Username then.          | as expected |
|             |                                                                  |             |
|             |                                                                  |             |
| Email       | Email field is optional,                                         | as expected |
| (optional)  | User can type in their email,                                    | as expected |
|             | or leave it blank.                                               | as expected |
|             | If Visitor chooses to fill in email:                             | as expected |
|             | pop up appears if no text before '@' in the email:               | as expected |
|             | "Please enter a part followed by '@'. '@...' is incomplete"      | as expected |
|             | pop up appears when no '@' in the email:                         | as expected |
|             | "Please include an '@' in the email...",                         | as expected |
|             | pop up appears if no text after '@' in the email:                | as expected |
|             | "Please enter a part following '@'. '...@' is incomplete".       | as expected |
|             | Suggestions for email are displayed below the Email field,       | as expected |
|             | while adjusting email to match the requirements,                 | as expected |
|             | even before clicking on 'Sign Up'                                | as expected |
|             |                                                                  |             |
| Password    | Password field is required,                                      | as expected |
|             | even though there's no asterisk                                  | as expected |
|             | highlighting that Password is required.                          | as expected |
|             | User can type in what password they would like,                  | as expected |
|             | all typed password characters, are masked as black dots,         | as expected |
|             | for sercurity.                                                   | as expected |
|             |                                                                  |             |
|             | Below Password field, guidelines for Password are listed.        | as expected |
|             | If Password entered doesn't match Password guidelines,           | as expected |
|             | and user clicks on 'Sign Up' button,                             | as expected |
|             | User is notified of Password not matching guidelines,            | as expected |
|             | and one or more guidelines are shown above the Password field,   | as expected |
|             | Highlighting issues with Users chosen Password,                  | as expected |
|             | even if password macthes some of the guidelines:                 | as expected |
|             |                                                                  |             |
|             | If Password is too short, message above Password field states:   | as expected |
|             | 'This password is too short. It must contain at least            | as expected |
|             | 8 characters.'                                                   |             |
|             |                                                                  |             |
|             | If Password is too common, message above Password field states:  | as expected |
|             | 'This password is too common.'                                   | as expected |
|             |                                                                  |             |
|             | If Password is long enough, yet too similar to the username,     | as expected |
|             | message above Password field states:                             | as expected |
|             | 'This password is too similar to the username.'                  | as expected |
|             |                                                                  |             |
|             | If Password field is left blank,                                 | as expected |
|             | and user clicks on 'Sign Up' button,                             | as expected |
|             | pop up appears near Password field: "Please fill in this field." | as expected |
|             |                                                                  |             |
|             | If Password is only numbers,                                     | as expected |
|             | message above Password field states:                             | as expected |
|             | 'This password is too common.'                                   | as expected |
|             | 'This password is entirely numeric.'                             | as expected |
|             |                                                                  |             |
| Password    | If User does not fill in the Password(again) field,              | as expected |
| (again)     | pop up appears below Password(again) field,                      | as expected |
|             | 'Please fill in this field.'                                     | as expected |
|             |                                                                  |             |
|             | User has an option to correct the Username, Email, Password      | as expected |
|             | and Password(again) mutliple times to try to 'Sign Up'           | as expected |
|             | If Username, Password, Password(again) and Email(if chosen)      | as expected |
|             | are entered as required, and user clicks on 'Sign Up' button,    | as expected |
|             | Home page opens,                                                 | as expected |
|             | "Successfully signed in as ...." is shown below NavBar,          | as expected |
|             | or below logo and Side Menu (on a smaller screen),               | as expected |
|             | "Signed in as ..." is displayed on the rightside below pop-up,   | as expected |
|             | NavBar shows 'Sign Out' instead of 'Sign Up' and 'Sign In'.      | as expected |
|             | and user is now allowed to comment on any published posts.       | as expected |



## Sign In page

| Tested Item | Expected Outcome                                                 | Outcome     |
| ----------- | ---------------------------------------------------------------- | ----------- |
| Sign In     | Logo, NavBar, NavLinks, NavText displayed,                       | as expected |
| page        | or NavLinks and NavText in the Side Menu,                        | as expected |
|             | if smaller screen                                                | as expected |
|             | On the right,                                                    | as expected |
|             | below Side Menu or NavText,                                      | as expected |
|             | 'Not signed in' is displayed.                                    | as expected |
|             |                                                                  |             |
|             | Below Sign In Title, text welcomes users back,                   | as expected |
|             | mentions that comments can be made only when Signed In,          | as expected |
|             | and gives New Users an option to Sign Up.                        | as expected |
|             | Sign Up link is clickable,                                       | as expected |
|             | and brings New users to Sign Up form.                            | as expected |
|             |                                                                  |             |
| Sign In     | Sign In form is displayed,                                       | as expected |
| Form        | Username field is displayed,                                     |             |
|             | with grayed out 'Username' in the box.                           | as expected |
|             |                                                                  |             |
| Username    | User can type in their Username,                                 | as expected |
|             | or choose their Username from the options shown,                 | as expected |
|             | after clicking in Username box,                                  | as expected |
|             | if user has previously opted for 'Remember Me:'                  | as expected |
|             |                                                                  |             |
|             | If incorrect Username is entered,                                | as expected |
|             | and user clicks on 'Sign In' button:                             | as expected |
|             | "The username and/or password you specified are not correct."    | as expected |
|             | appears above 'Username' field                                   | as expected |
|             |                                                                  |             |
|             | If nothing is entered in Username field,                         | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | pop up appears near Username field: "Please fill in this field." | as expected |
|             |                                                                  |             |
| Password    | Password field is displayed,                                     | as expected |
|             | User can type in their password,                                 | as expected |
|             | all characters typed, are masked as black dots.                  | as expected |
|             |                                                                  |             |
|             | If incorrect password is entered,                                | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | "The username and/or password you specified are not correct."    | as expected |
|             | appears above 'Username field',                                  | as expected |
|             | User has an option to correct the password and try again.        | as expected |
|             |                                                                  |             |
|             | If password field is left blank,                                 | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | pop up appears near Password field: "Please fill in this field." | as expected |
|             |                                                                  |             |
|             | User has an option to click in checkbox beside 'Remember Me:'    | as expected |
|             | Check appears in the checkbox if user clicks on it.              | as expected |
|             | 'Sign In' button is available below 'Remember Me:'               | as expected |
|             |                                                                  |             |
|             | If correct Username and correct Password are entered,            | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | Home page opens,                                                 | as expected |
|             | "Successfully signed in as ...." pops up below NavBar,           | as expected |
|             | or below logo and Side Menu (on a smaller screen),               | as expected |
|             | "Signed in as ..." is displayed on the rightside below pop-up,   | as expected |
|             | NavBar shows 'Sign Out' instead of 'Sign Up' and 'Sign In'.      | as expected |
|             | and user is now allowed to comment on any published posts.       | as expected |


## Social media links in Footer

| Icon clicked | Expected Outcome                 | Outcome
| ------------ | -------------------------------- | ----------- |
| Facebook     | facebook.com opens in a new tab  | as expected |    
| Twitter/X    | x.com opens in a new tab         | as expected |
| Instagram    | instagram.com opens in a new tab | as expected |
| YouTube      | youtube.com opens in a new tab   | as expected |


## ReadMe links 




## Bugs

- Resources app displayed only one resource at a time. With tutor's guidance to add for loop, all of the resources were displayed (for original version of this project)

- Images on Home page, on Next page, too big.

- Collaboration Form confirmation mentioned Collaboration Request. Developer changed 'request' for 'form' in about>views.py, to match the wording of the form and confirmation:

Before:

![Collaboration Request](readmerequestreceived.png)

After:

![Collaboration Form](readmeformreceived.png)




### Images post_detail.html
- Images for bookblog articles showed up as expected on the Home page, matching the subject of the Title.

![Correct images](docs/readmeimages/correctimages.png)

- When developer clicked on any post, the new page displayed the placeholder image instead of the unique image selected for each post.

![Placeholder image](docs/readmeimages/placeholderimage.png)

- Developer had inspected the page before:

[Previous image](docs/readmeimages/previousinspection.png)

- This time the developer clicked on the image part of the page instead:

[New inspection](docs/readmeimages/newinspection.png)

- The developer finally saw the right area, where image details were
- The developer then compared codes of the images between home page and the new tab:

[Correct code](docs/readmeimages/correctimagecode.png)

[Placeholder code](docs/readmeimages/placeholder.png)

- By matching post_detail.html image code with the home page one, the correct images started to display in the new tab as well:

[Correct image displayed](docs/readmeimages/correctimagedisplayed.png)

### am I Responsive

- am I responsive test showed white screens instead of the website: [Blank am I responsive](docs/readmeimages/amiresponsiveblank.png)
  Thanks to Kera's post on Slack, developer found out that she needed to install [an extension](https://chromewebstore.google.com/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe?pli=1), so that Heroku site could be tested for responsiveness. Sorted! Am I responsive image displayed at the start of the ReadMe.


### Known Bugs

- Resources and About showing up in Django as Resourcess and Abouts
- On Django, Collaboration requests needs to be replaced with Collaboration Form 
- Collaboration form to be made smaller to fit on the screen better
- When post is open for further reading, the image of the post is not displaying fully, on developer's screen size
- Resources is missing an image/video on top of the page
- Resources are displayed only as text or link, instead of an image of the page
- js validation showed one error, not fixed
- Spelling check was not done for the website, yet
- Sign up boxes could be shown in a nicer way, at the moment they are not lined up evenly
- Alert messages, pop ups are showing up in the color of the walk-through, instead of developer's chosen color
- Admin and Site Users are not able to create posts when logged in. Admin can create posts from Django
- Not all of the python files have been checked with [CI Python Linter](https://pep8ci.herokuapp.com/)
- When filling Sign Up form, and existing Username is chosen, Visitor is not informed straigt away that this Username is already taken, instead, cursor moves to Password  field (as email is optional). Yet when user clicks on Sign Up button, while existing Username is on Username field, and passwords not matching that Username, User is notified above Username field: "A User with that username already exists".
  It would be beneficial and time saving for users for system to recognise this Username is already taken, and inform the Visitor to choose a different Username.
- There are errors showing in some of the python files, checked by developer:

![Python error](docs/readmeimages/indentationpython.png)

- Error pages not added

- In Django, when Resource is marked as a Draft, it still shows up on the Website, just at the bottom of the page, separated from Published ones,
  and still clickable, usable:

![Resource Draft](draftresource.png)

![Resource Draft Available on the Website](resourcesdraftvisibleclickable.png)

Developer unapproved the Resource, by unchecking checkbox beside 'Approved', and Draft/Unapproved Resource was still displayed on the page, and clickable:

![Resource Draft, Unapproved](resourcedraftnotapproved.png)

As the video was marked as Draft, and Unapproved for testing purposes only, Developer kept the video in the Resources, as it fits the theme of the Website,
and marked this bug fix in Future Features


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

- BookBlog's code is based on following Code Institute's Walk-through project ["I Think Therefore I Blog"](https://github.com/Code-Institute-Solutions/blog/tree/main) . 
  The developer has credited Walk-through mainly on top of html files, 
  due to enourmous number of other files, which are all coded like Walk-through project.

- General ReadMe template derived from: [findMEreadME](https://github.com/brodsa/findMEreadME/blob/main/README.md#content)

- Developer got inspiration for her ReadMe User Stories layout from her Facilitator Laura's Project 4: [The Happy Reader](https://github.com/LauraMayock/The-happy-reader/blob/main/README.md)

- Responsiveness test/image created with: [am I responsive](https://ui.dev/amiresponsive)

- Wireframes created with [Balsamiq](https://balsamiq.com/wireframes/)

- Developer read this article to remember how to get links to open in a new tab. Article by Jessica Wilkins: [How to Open a Link in a New Tab](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/#:~:text=You%20can%20use%20the%20target,opening%20anchor%20tag%20like%20this.)
 
- How to add favicon: [W3 Schools](https://www.w3schools.com/html/html_favicon.asp)

- Thanks to tutor Oisin's guidelines, Developer learned from [this ReadMe](https://github.com/Dimitris112/rum-away-testp4/blob/main/TESTING.md)
  how to add an extra file to document testing, and how to format testing tables

- Developer used [ABC Webpage Spell-Check](https://chromewebstore.google.com/detail/webpage-spell-check/mgdhaoimpabdhmacaclbbjddhngchjik) to check spelling, found this suggestion on Slack, from Kera


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

- Developer is grateful for any guidance and support provided by her family and friends, mentor, facilitator, tutors, Slack members, and  
  online content creators.

- Due to circumstances and time constraint, the project is not fully finished as required:
  - missing ERD
  - personalised model, Suggest, is not displaying on the website (only available on Django)
  - Resources app is supposed to have a wave image/video on top of the page
  - all of the resources links should be displaying their own images/websites
  - not enough testing done
  - there are probably bugs that the developer has not found yet

[Back to the overview](#content)