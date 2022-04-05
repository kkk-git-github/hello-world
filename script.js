first_signup_button = document.getElementsByClassName("sign-up-ad");
first_signup_button.addEventListener(
  'click', function() {
    console.log("An user pressed \'first_signup_button\'");
  }
)

second_signup_button = document.getElementsByClassName("signup-button");
second_signup_button.addEventListener(
  'click', function() {
    console.log("An user pressed \'second_signup_button\'");
  }
)