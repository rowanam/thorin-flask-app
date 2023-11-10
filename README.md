# Thorin & Company Flask App

## Workspace Set Up

Install Flask

- Run command: pip3 install Flask

## Deployment to Heroku

Two ways were tried with this project, one of which (using the Heroku CLI) will be described here. (The other method is deploying from GitHub, which is more straightforward.)

### Install the Heroku toolbelt (Heroku CLI) and log in

Check if Heroku is installed by running `heroku --version`

- If not, run `npm install -g heroku`

Log in by running `heroku login -i` and supplying email and password

- If MFA is set up, you may need to log in with API Key instead of password. This can be found in your Heroku Account Settings

Check that log in worked by running `heroku apps`, which will output a list your Heroku apps

### Create and deploy Heroku app

Create a Heroku app

- Go to [Heroku dashboard](https://dashboard.heroku.com/apps)
- Create a new app and give it a unique name

Connect Git remote

- In IDE terminal, run `git remote add <remote name> <remote git url>`
  - Remote name - choose a name for the remote branch
  - Remote git url - can be found in the settings tab of the Heroku app
  - Example: `git remote add heroku https://git.heroku.com/<APP-NAME>.git`
- Make sure all code is commited and pushed (`git push -u heroku main`)

Add requirements.txt

- To store the necessary Python dependencies, and also let Heroku know what the app language is
- Run `pip3 freeze --local > requirements.txt`
- (File 'requirements.txt' should appear in explorer)
- Commit and push this change (`git push -u heroku main`)

Add Procfile

- To tell Heroku how to run the app
- Run `echo web: python run.py > Procfile`
- (File 'Procfile' should appear in explorer)
- Commit and push this change (`git push -u heroku main`)

App should now work when opened from Heroku

## Attributions

Site theme - [Clean Blog theme](https://github.com/StartBootstrap/startbootstrap-clean-blog) from [Start Bootstrap](https://startbootstrap.com/)

Thorin and company header background image - by Art-Calavera at [deviantart](https://www.deviantart.com/art-calavera/art/The-Hobbit-Thorin-and-Company-341472935)

About page text and images - [Lord of the Rings Wiki | Fandom](https://lotr.fandom.com/wiki/Thorin_and_Company)

## CI Template Instructions

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
