# Testing

## Contents 
   - [Automated Testing](#automated-testing)
      * [HTML validation](#w3c-markup-validator)
      * [CSS validation](#w3c-css-validator)
      * [Pep8 validation](#pep8-validation)
      * [Lighthouse testing](#lighthouse-testing-in-devtools)
      * [Responsive](\static\responsive\responsivepa.png)
   - [Testing User Stories](#testing-user-stories)
   

## Automated Testing

The W3C Markup Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no syntax errors in the project.

-   ## [W3C Markup Validator](https://validator.w3.org/) 

      ![htmlvalidator](https://user-images.githubusercontent.com/76841050/165843136-7548c13a-8de2-488a-b05a-20ceeebb5562.png)

-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    
    
      ![cssvalidator](https://user-images.githubusercontent.com/76841050/165842862-ac21ed73-e2e9-4a85-9718-e15c9830df44.png)


-   ## [Pep8 validation](http://pep8online.com/) 
    
    ### Initial/final testing
  
    - views.py 

      ![pep8validation](https://user-images.githubusercontent.com/76841050/165843345-22f14619-d804-48bf-b779-873711b6ec15.png)

    
-   ## [Lighthouse testing in devtools](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 
       
  
     + Home.html (see report [here](app\static\tests\LHhome.png))

       ![LHhome](https://user-images.githubusercontent.com/76841050/163257658-7e378204-899a-46e2-ba90-5c2e3616fac8.png)

     + Login.html(see report [here](app\static\tests\Lhlogin.png))

       ![Lhlogin](https://user-images.githubusercontent.com/76841050/163257661-3010e65f-e6bf-4f9e-99f8-20846ac2c8e8.png)
     
     + Logout.html(see report [here](app\static\tests\LHlogout.png)

       ![LHlogout](https://user-images.githubusercontent.com/76841050/163257624-edc81ac2-b956-4a9c-ad18-46cb389382f3.png)

      
    
## Testing User Stories 

   - #### First Time Visitor 

      1. As a first time visitor, I want to easily understand the main purpose of the site.<br>
        The search bar is located in the center of the page, right below the logo. There is also a menu located in the top right corner.  
         * About us.
         ![about us](https://user-images.githubusercontent.com/76841050/165845791-ac5b15b1-a536-43af-acdf-c4e9cdd03830.png)
         * Service.
         ![services](https://user-images.githubusercontent.com/76841050/165845925-d4aa8d5d-8a83-4495-9d17-2bd1ccf90f26.png)
         * Contact.
         ![contact](https://user-images.githubusercontent.com/76841050/165846009-3fd4a94b-b35f-4d84-97d9-f778225674c4.png)
         
         
      2. As a first time visitor, I want to be able to intuitively use the site.<br>
         I have put social links, contact number and other useful links in the footer.

         ![footermenu](https://user-images.githubusercontent.com/76841050/166121363-c6cf7e74-3d43-4597-aa91-c3ce633dc01a.png)


      3. As a first time visitor, I expect to see an objective, visually simple site.<br>
         I have used the green and white color for the entire<br> Didn't want any gaps in the site or a broken link.

         
      4. As a first time visitor, I expect an accessible site.<br>
         
               
         * Already a member, use the login function.<br>
         ![login](https://user-images.githubusercontent.com/76841050/165846104-cc5ff28f-2daf-4d22-881f-d4d2d3013c4d.png)
         * A simple way to  become a member by signing up.<br>
         ![signup](https://user-images.githubusercontent.com/76841050/165846179-3e7b192f-6082-4d78-85ec-857da0ddf28c.pn)
         * Already logged in, you can logout anytime.<br>
         ![appointment](https://user-images.githubusercontent.com/76841050/165846244-bcdb2462-b1b6-449f-8234-8fbb6d07fde2.png)
         

      6. As a first time visitor, I want to easily search the movies.<br>
         
         
         * The search bar is at the top or center of the home page, the user can use it to search for movie titles, actors, and actresses.<br>
         ![searchmovie]()
         * After clicking on the review button, user will be able to leave the review.<br>
         ![thanksforreview]()
         * Review function 
         ![updatingreview]()
         * No delete function needed, update your review.<br>