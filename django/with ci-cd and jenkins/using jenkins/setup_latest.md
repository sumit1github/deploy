# Pre-Installation steps

> gather the public ip, domain name and put it on `jenkins file in root directory`

> ssl : get two ssl file with name bundle.cer & hv_ssl.key. Store them inside  `cicd > hard_build > ssl`

> envs : edit `.env.template`  in root folder.

> jenkins file : Finalize a pipeline name, same project name you are going use at the time of creating the `jenkins pipeline` and `jenkins file in root directory.` Do same for database and other.


# Blind Command

> first connect to instance and start running the commnds if a pink screen comes, just press enter
>> sudo nano initial.sh
* copy all contents of initial.sh from local and paste in server.
>> pwd
* copy the path
>> chmod +x <copied>/initial.sh

>> ./initial.sh
* it will install python, postgres, nginx ,jenkins, virtual env


# login into the jenkins dashboard
      
> publicip:8080   open it to browser
      
> it will show the location of your password

* go to terminal 
    >> sudo nano copied_location

    >>sudo nano /var/lib/jenkins/secrets/initialAdminPassword
    * copy the password and login
    * create an user
          
# Open jenkins Dashboard
> click on install suggested plugins

> go to manage plugin > search for bitbucket > select the plugin name bitbucket(only select `bitbucket`)      

### Add jenkins user to sudo group
>> sudo visudo
* search for `root ALL=(ALL:ALL) ALL`
* paste this line  --> `jenkins ALL=(ALL) NOPASSWD: ALL` <-- after above line.


### create a bitbucket token authenticated repo url
> create app-password in bitbucket repo

> `bit-bucket has stopped the username and password authentication. You need a app password.`
        
> Go to bitbucket repo > settings (bottom-left) > access_token > create > check the `write` permission for all

> Copy the url starting with `git clone https://`

> store the url in notepad


### Create a new pipeline
> login > create a job > enter project name > select pipeline > next

> go to  `Dashboard > hvproject > Configuration > pipeline > Definition` select `Pipeline script from SCM`
* `scm` : select git
* `Repositories`: paste the bitbucket url from the notepad
* `Branches` to build : select bitbucket branch_name, from where it pull the code.

> click on build and wait.

> open the public url. Your project is running.
    * make sure you comment out correct code block in nginx_template.conf




# Enable the auto deploy web-hook

### Deal with `403 no valid crumb`
> webhook trigger

> webhook is a link to the jenkins url, when it will be hitted by bitbucket after push the code. The build will start automatically in jenkins.
      
> note : First to prevent `403 no valid crumb` inside the webhook. we need to disable the jenkins CSRF.
            
> go to `Dashboard > Manage Jenkins > Script Console`

>> hudson.security.csrf.GlobalCrumbIssuerConfiguration.

>> DISABLE_CSRF_PROTECTION = true

* output : true
            
* now go to the webhook.txt


### trigger builds remotely enable

> go to Dashboard > Manage Jenkins > Security

> Jenkins' own user database (uncheck Allow users to sign up)

> Authorization: Logged-in users can do anything

> it will appear


### create a jenkins job token

> Dashboard > hvproject > Configuration > General

> inside Build Triggers we have to check ***Trigger builds remotely (e.g., from scripts).

> it will ask token, you can pust anything. Same should be used in webhook.

> initially it will not visible, we have to enable it.



### webhook should looks like

> to create webhook, go to remo setting and webhook

> paste the below link and check all the read operations  

> http://{userame}:{password}@{jenkins url and port}/job/{pipeline}/build?token={token}

> paste the url in bitbucket repo > settings > webhook

> chek on `merge`








# Jenkins Troubleshooting

### create your own user 

>activate security using jenkins own user-database

>DO NOT activate matrix-based security yet.(*******************)

>Save!

>go to "manage jenkins" -> "manage users" (now it should be visible)

>create a user. use only lowercase letters for the username otherwise you will get problems on restart of jenkins.


>now go back to "manage jenkins" -> global security

>activate matrix-based security

>enter the name of your new user and give him all permissions using the button at the end of the row.

>Save

>now you should be able to login.
        
        
 
