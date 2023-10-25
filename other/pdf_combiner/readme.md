Idea based on book Automate the Boring Stuff with Python and [this tutorial](https://www.youtube.com/watch?v=JRCJ6RtE3xU&list=WL&index=2&t=0s)

### What does this script do:
Sort by name every pdf file in script location, then open them and merge into one single file (with excluded
first page or without). After this send a email with merged file as a attachment. There is an option to only
merge your pdf files without sending result via email

### How to use it:
1. Make sure, you have all dependencies requirements by this script - you can use requirements.txt file,
but that assume you to use conda. 

2. Make sure you have some pdf files to merge in script location

3. In order to send email you need to have 3 things: 
    -> a gmail account (script works only for gmail)
    
    -> a app pasword for your gmail account (you can set it here: [gmail_without_two_factor_auth](https://myaccount.google.com/lesssecureapps), 
    [gmail_with_two_factor_account](https://accounts.google.com/signin/v2/sl/pwd?service=accountsettings&passive=1209600&osid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&followup=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&rart=ANgoxccI9H-DbwSUF7DOdykknsxzM-61Z2b0-WLQ_Bq_NnTiCz_bC2E6pxV6J7S3gf-6C_Lb5ZfqqiV-QHgvjG-_FWzFIrPY9Q&authuser=0&csig=AF-SEnaqKwlmQ-jgofhD%3A1573511705&flowName=GlifWebSignIn&flowEntry=ServiceLogin)
    
    -> set your EMAIL_ADDRESS and EMAIL_PASSWORD (in this case: your app password for gmail) 
    as env variables (script check env variable EMAIL_ADDRESS and EMAIL_PASSWORD) 
    an example [tutorial](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)
    , look for 'Persisting Environment Variables for a User' paragraph )
    
4. Fill msg.txt (content of this file will be message of your email. By default it is filled up by some
generic template)

5. Run a script - program can take 3 arguments - receivers, subject (both of your email) and exclude_first_page. 
All 3 arguments are optional - however if you don't pass receivers and subject email will not be sent
(also you must not pass only receivers or only subject)

    ```
    python main.py 'first_reciever@email.com, second_reciever@email.com, etc', 'subject of your email', exclude_first_page
    python main.py 'email@email.com', subject 
    python main.py exclude_first_page 
    python main.py
   ```

